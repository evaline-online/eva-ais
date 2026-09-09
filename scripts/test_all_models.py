#!/usr/bin/env python3
"""
eva-ais / test_all_models.py
============================
Тестер всех LLM-моделей в системе EvaBot.

Для каждой модели отправляет минимальный тестовый промпт и определяет:
  - working  — модель отвечает корректно
  - failed   — модель возвращает ошибку (с указанием кода и сообщения)
  - timeout  — модель не отвечает в течение 10 секунд
  - unavailable — модель недоступна / отключена / помечена deprecated

Результаты экспортируются в:
  - reports/model_test_results.tsv   (машиночитаемый TSV)
  - reports/model_test_report.md     (читаемый markdown)
  - reports/model_test_results.json  (полный JSON)
"""

import json, os, re, sys, time, urllib.request, urllib.error, ssl
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

REPO_ROOT = Path(__file__).resolve().parent.parent
REPORTS_DIR = REPO_ROOT / "reports"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

# Disable SSL for some endpoints
SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode = ssl.CERT_NONE

TEST_PROMPT = "Hello, reply with exactly: OK"
TEST_TIMEOUT = 8  # seconds per model


def load_env(path="/var/www/evabot-backend/.env"):
    env = {}
    if os.path.isfile(path):
        for line in open(path, encoding="utf-8", errors="replace"):
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k] = v
    return env


ENV = load_env()
GEMINI_KEY = ENV.get("GEMINI_API_KEY", "")
OPENROUTER_KEY = ENV.get("OPENROUTER_API_KEY", "")
OMNIROUTE_KEY = ENV.get("OMNIROUTE_API_KEY", "omniroute-token")

# SSL context that doesn't verify (for internal endpoints)
ssl_ctx = ssl.create_default_context()
ssl_ctx.check_hostname = False
ssl_ctx.verify_mode = ssl.CERT_NONE


def make_request(url, method="GET", headers=None, data=None, timeout=TEST_TIMEOUT):
    """Make HTTP request, return (ok, response_text_or_error)."""
    req = urllib.request.Request(url, method=method, headers=headers or {})
    if data is not None:
        req.data = json.dumps(data).encode("utf-8")
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            return True, body, resp.status
    except urllib.error.HTTPError as e:
        try:
            err_body = e.read().decode("utf-8", errors="replace")
        except Exception:
            err_body = ""
        return False, err_body[:500], e.code
    except urllib.error.URLError as e:
        return False, str(e.reason), 0
    except Exception as e:
        return False, str(e)[:500], 0


def test_gemini_model(model_id):
    """Test a Gemini API model."""
    # Remove 'models/' prefix if present
    mid = model_id.replace("models/", "")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{mid}:generateContent?key={GEMINI_KEY}"
    payload = {"contents": [{"parts": [{"text": TEST_PROMPT}]}]}
    ok, resp, code = make_request(url, method="POST", data=payload, timeout=TEST_TIMEOUT)
    if ok:
        try:
            data = json.loads(resp)
            if "candidates" in data:
                return "working", code, "OK"
            elif "error" in data:
                msg = data["error"].get("message", str(data["error"]))
                return "failed", code, msg[:200]
            else:
                return "unknown", code, resp[:200]
        except json.JSONDecodeError:
            return "unknown", code, resp[:200]
    else:
        if "deprecated" in resp.lower() or "not available" in resp.lower() or "high demand" in resp.lower():
            return "unavailable", code, resp[:200]
        return "failed", code, resp[:200]


def test_openrouter_model(model_id):
    """Test an OpenRouter model."""
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {"Authorization": f"Bearer {OPENROUTER_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": model_id,
        "messages": [{"role": "user", "content": TEST_PROMPT}],
        "max_tokens": 16,
    }
    ok, resp, code = make_request(url, method="POST", headers=headers, data=payload, timeout=TEST_TIMEOUT)
    if ok:
        try:
            data = json.loads(resp)
            if "choices" in data:
                content = data["choices"][0].get("message", {}).get("content", "")
                if "OK" in content or "ok" in content:
                    return "working", code, content[:100].strip()
                return "working", code, content[:100].strip()
            elif "error" in data:
                msg = data["error"].get("message", data["error"].get("type", str(data["error"])))
                return "failed", code, msg[:200]
            else:
                return "unknown", code, resp[:200]
        except json.JSONDecodeError:
            return "unknown", code, resp[:200]
    else:
        if "not found" in resp.lower() or "does not exist" in resp.lower():
            return "unavailable", code, resp[:200]
        if "rate limit" in resp.lower() or "429" in resp:
            return "failed", code, "Rate limited"
        return "failed", code, resp[:200]


def test_omniroute_model(model_id):
    """Test an OmniRoute model."""
    url = "http://127.0.0.1:20128/v1/chat/completions"
    headers = {"Authorization": f"Bearer {OMNIROUTE_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": model_id,
        "messages": [{"role": "user", "content": TEST_PROMPT}],
        "max_tokens": 16,
    }
    ok, resp, code = make_request(url, method="POST", headers=headers, data=payload, timeout=TEST_TIMEOUT)
    if ok:
        try:
            data = json.loads(resp)
            if "choices" in data:
                content = data["choices"][0].get("message", {}).get("content", "")
                return "working", code, content[:100].strip()
            elif "error" in data:
                msg = data["error"].get("message", str(data["error"]))
                return "failed", code, msg[:200]
            else:
                return "unknown", code, resp[:200]
        except json.JSONDecodeError:
            return "unknown", code, resp[:200]
    else:
        if "not found" in resp.lower() or "does not exist" in resp.lower():
            return "unavailable", code, resp[:200]
        return "failed", code, resp[:200]


def get_models_to_test():
    """Collect all models to test from various sources."""
    models = []

    # 1. Local backend models
    ok, data, _ = make_request("http://127.0.0.1:8000/api/models")
    if ok:
        try:
            mdata = json.loads(data)
            for m in mdata.get("models", []):
                mid = m.get("id", "")
                provider = m.get("provider", "")
                tier = m.get("tier", "")
                models.append({
                    "id": mid,
                    "provider": provider,
                    "tier": tier,
                    "source": "local-backend",
                    "test_type": "gemini" if provider == "Google DeepMind" and "OMNI" not in mid else
                                 "openrouter" if provider == "OpenRouter" else
                                 "omniroute" if provider == "OmniRoute" else
                                 "vertexai" if provider in ("Anthropic", "Meta", "Mistral AI", "AI21 Labs", "Cohere") else
                                 "openrouter",
                    "is_free": "free" in str(tier).lower() or "open weights" in str(tier).lower(),
                })
        except json.JSONDecodeError:
            pass

    # 2. OmniRoute routes
    ok, data, _ = make_request("http://127.0.0.1:20128/v1/models",
                               headers={"Authorization": f"Bearer {OMNIROUTE_KEY}"})
    if ok:
        try:
            mdata = json.loads(data)
            for m in mdata.get("data", []):
                mid = m.get("id", "")
                models.append({
                    "id": mid,
                    "provider": "OmniRoute",
                    "tier": "OmniRoute Daemon (via routing)",
                    "source": "omniroute-daemon",
                    "test_type": "omniroute",
                    "is_free": True,
                })
        except json.JSONDecodeError:
            pass

    # 3. OpenRouter free models (from API)
    ok, data, _ = make_request("https://openrouter.ai/api/v1/models",
                               headers={"Authorization": f"Bearer {OPENROUTER_KEY}"})
    if ok:
        try:
            mdata = json.loads(data)
            for m in mdata.get("data", []):
                mid = m.get("id", "")
                pricing = m.get("pricing", {})
                is_free = pricing.get("prompt", "") == "0"
                # Only add free models or models not already in our list
                existing_ids = [x["id"] for x in models]
                if mid not in existing_ids:
                    models.append({
                        "id": mid,
                        "provider": "OpenRouter",
                        "tier": "Free Community" if is_free else "OpenRouter Paid",
                        "source": "openrouter-api",
                        "test_type": "openrouter" if not is_free else "openrouter",
                        "is_free": is_free,
                    })
        except json.JSONDecodeError:
            pass

    # 4. Gemini API models (gen-lang key)
    if GEMINI_KEY:
        ok, data, _ = make_request(f"https://generativelanguage.googleapis.com/v1beta/models?key={GEMINI_KEY}")
        if ok:
            try:
                mdata = json.loads(data)
                for m in mdata.get("models", []):
                    mid = m.get("name", "").replace("models/", "")
                    existing_ids = [x["id"] for x in models]
                    if mid not in existing_ids:
                        models.append({
                            "id": mid,
                            "provider": "Google DeepMind (gen-lang)",
                            "tier": "Gemini API",
                            "source": "gemini-api-gen-lang",
                            "test_type": "gemini",
                            "is_free": True,  # gen-lang has free quota
                        })
            except json.JSONDecodeError:
                pass

    # Deduplicate by id (keep first occurrence)
    seen = set()
    unique = []
    for m in models:
        key = (m["id"], m["test_type"])
        if key not in seen:
            seen.add(key)
            unique.append(m)

    return unique


def test_model(model_entry):
    """Test a single model, return result dict."""
    mid = model_entry["id"]
    test_type = model_entry.get("test_type", "openrouter")
    start = time.time()
    status, code, detail = "error", 0, ""

    try:
        if test_type == "gemini":
            status, code, detail = test_gemini_model(mid)
        elif test_type == "openrouter":
            status, code, detail = test_openrouter_model(mid)
        elif test_type == "omniroute":
            status, code, detail = test_omniroute_model(mid)
        else:
            status, code, detail = test_openrouter_model(mid)
    except Exception as e:
        status, code, detail = "error", 0, str(e)[:200]

    elapsed = round(time.time() - start, 2)

    return {
        "id": mid,
        "provider": model_entry.get("provider", ""),
        "tier": model_entry.get("tier", ""),
        "source": model_entry.get("source", ""),
        "test_type": test_type,
        "is_free": model_entry.get("is_free", False),
        "status": status,
        "http_code": code,
        "detail": detail,
        "response_time_s": elapsed,
    }


def main():
    print("\U0001F50D Сбор всех моделей для тестирования...")
    models = get_models_to_test()
    print(f"  Найдено {len(models)} моделей для тестирования")
    print()

    # Split free and paid
    free_models = [m for m in models if m.get("is_free")]
    paid_models = [m for m in models if not m.get("is_free")]
    print(f"  Бесплатных: {len(free_models)}")
    print(f"  Платных: {len(paid_models)}")
    print()

    # Test all with thread pool
    results = []
    tested = 0
    total = len(models)

    print("🧪 Тестирование моделей (max_workers=10, timeout=8s)...")
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_model = {executor.submit(test_model, m): m for m in models}
        for future in as_completed(future_to_model):
            tested += 1
            model = future_to_model[future]
            try:
                result = future.result(timeout=TEST_TIMEOUT + 5)
            except Exception as e:
                result = {
                    "id": model["id"],
                    "provider": model.get("provider", ""),
                    "tier": model.get("tier", ""),
                    "source": model.get("source", ""),
                    "test_type": model.get("test_type", ""),
                    "is_free": model.get("is_free", False),
                    "status": "timeout",
                    "http_code": 0,
                    "detail": str(e)[:200],
                    "response_time_s": TEST_TIMEOUT + 5,
                }
            results.append(result)
            # Progress
            status_emoji = {"working": "\u2705", "failed": "\u274c", "unavailable": "\U0001F516", "timeout": "\u231F", "error": "\u26A0\uFE0F", "unknown": "\u2754"}.get(result["status"], "\u2754")
            print(f"  [{tested}/{total}] {status_emoji} {result['status']:12s} — {result['id'][:50]}")

    # Sort results
    results.sort(key=lambda x: (x["is_free"], x["provider"], x["id"]))

    # ── Write JSON ──
    json_path = REPORTS_DIR / "model_test_results.json"
    json_path.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\n  → {json_path}")

    # ── Write TSV ──
    tsv_path = REPORTS_DIR / "model_test_results.tsv"
    tsv_lines = ["id\tprovider\ttier\tsource\ttest_type\tis_free\tstatus\thttp_code\tdetail\tresponse_time_s"]
    for r in results:
        tsv_lines.append("\t".join([
            r["id"],
            r["provider"],
            r["tier"],
            r["source"],
            r["test_type"],
            str(r["is_free"]),
            r["status"],
            str(r["http_code"]),
            r["detail"].replace("\t", " ").replace("\n", " ")[:200],
            str(r["response_time_s"]),
        ]))
    tsv_path.write_text("\n".join(tsv_lines), encoding="utf-8")
    print(f"  → {tsv_path}")

    # ── Write Markdown report ──
    md_path = REPORTS_DIR / "model_test_report.md"
    md = []
    md.append("# Отчёт тестирования моделей LLM")
    md.append("")
    md.append(f"**Дата:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}  ")
    md.append(f"**Всего моделей:** {len(results)}")
    md.append("")

    # Summary table
    working = [r for r in results if r["status"] == "working"]
    failed = [r for r in results if r["status"] == "failed"]
    unavailable = [r for r in results if r["status"] == "unavailable"]
    timeout = [r for r in results if r["status"] == "timeout"]
    unknown = [r for r in results if r["status"] == "unknown"]

    md.append("## Сводка")
    md.append("")
    md.append("| Статус | Количество |")
    md.append("|---|---|")
    md.append(f"| ✅ Working | {len(working)} |")
    md.append(f"| ❌ Failed | {len(failed)} |")
    md.append(f"| 🔚 Unavailable | {len(unavailable)} |")
    md.append(f"| ⏳ Timeout | {len(timeout)} |")
    md.append(f"| ❔ Unknown | {len(unknown)} |")
    md.append("")

    # Free working
    free_working = [r for r in working if r["is_free"]]
    free_failed = [r for r in failed if r["is_free"] or r["status"] == "unavailable"]
    md.append("## Бесплатные модели — Working")
    md.append("")
    if free_working:
        md.append("| ID | Provider | Source | Detail |")
        md.append("|---|---|---|---|")
        for r in sorted(free_working, key=lambda x: x["provider"]):
            md.append(f"| {r['id']} | {r['provider']} | {r['source']} | {r['detail'][:80]} |")
    else:
        md.append("Ни одна бесплатная модель не прошла тестирование.")
    md.append("")

    md.append("## Бесплатные модели — Not Working")
    md.append("")
    if free_failed:
        md.append("| ID | Provider | Status | HTTP | Detail |")
        md.append("|---|---|---|---|---|")
        for r in sorted(free_failed, key=lambda x: x["provider"]):
            md.append(f"| {r['id']} | {r['provider']} | {r['status']} | {r['http_code']} | {r['detail'][:150]} |")
    else:
        md.append("Все бесплатные модели работают!")
    md.append("")

    # Paid working
    paid_working = [r for r in working if not r["is_free"]]
    paid_failed = [r for r in failed if not r["is_free"] or r["status"] == "unavailable"]
    md.append("## Платные модели — Working")
    md.append("")
    if paid_working:
        md.append("| ID | Provider | Source | Detail |")
        md.append("|---|---|---|---|")
        for r in sorted(paid_working, key=lambda x: x["provider"]):
            md.append(f"| {r['id']} | {r['provider']} | {r['source']} | {r['detail'][:80]} |")
    else:
        md.append("Ни одна платная модель не прошла тестирование.")
    md.append("")

    md.append("## Платные модели — Not Working")
    md.append("")
    if paid_failed:
        md.append("| ID | Provider | Status | HTTP | Detail |")
        md.append("|---|---|---|---|---|")
        for r in sorted(paid_failed, key=lambda x: x["provider"]):
            md.append(f"| {r['id']} | {r['provider']} | {r['status']} | {r['http_code']} | {r['detail'][:150]} |")
    else:
        md.append("Все платные модели работают!")
    md.append("")

    # Full results by provider
    md.append("## Полные результаты по провайдерам")
    md.append("")
    providers = sorted(set(r["provider"] for r in results))
    for prov in providers:
        prov_results = [r for r in results if r["provider"] == prov]
        w = sum(1 for r in prov_results if r["status"] == "working")
        f = sum(1 for r in prov_results if r["status"] == "failed")
        u = sum(1 for r in prov_results if r["status"] == "unavailable")
        md.append(f"### {prov}")
        md.append("")
        md.append(f"Working: {w} | Failed: {f} | Unavailable: {u} | Total: {len(prov_results)}")
        md.append("")

    md_path.write_text("\n".join(md), encoding="utf-8")
    print(f"  → {md_path}")

    print(f"\n✅ Готово. {len(working)}/{len(results)} моделей работают.")


if __name__ == "__main__":
    main()
