#!/usr/bin/env python3
"""
eva-ais / scan_all_llms.py
==========================
Системный сканер LLM-инфраструктуры EvaBot.

Анализирует:
  1. Google Cloud (gcloud) — проекты, сервисы, биллинг, сервис-аккаунты
  2. Локальный бэкенд EvaBot (/api/models) — каталог моделей
  3. OmniRoute daemon (LiteLLM proxy) — роуты к бесплатным провайдерам
  4. OpenRouter API — все модели (free + paid)
  5. Gemini API — каталог моделей
  6. HuggingFace Inference — модели из opencode.json / kilo.jsonc
  7. Groq / Cerebras / Z.ai / Cloudflare AI / Mistral API
  8. Локальные LLM-сервисы (Ollama, oobabooga, vLLM, LMStudio)
  9. Docker контейнеры
  10. Файлы конфигураций (.env, mcp.json, opencode.json, claude_desktop_config.json, kilo.jsonc)

Экспорт в:
  - reports/models_catalog.json
  - reports/models_catalog.tsv
  - reports/system_scan_report.md
  - free-models/<id>.md          (бесплатные + open-weights + free-quota)
  - paid-models/<id>.md          (pay-per-use)
  - providers/<provider>.md      (по каждому провайдеру)
"""

import json, os, re, socket, subprocess, sys, urllib.request
from pathlib import Path
from datetime import datetime, timezone

REPO_ROOT = Path(__file__).resolve().parent.parent
REPORTS_DIR = REPO_ROOT / "reports"
FREE_DIR = REPO_ROOT / "free-models"
PAID_DIR = REPO_ROOT / "paid-models"
PROVIDERS_DIR = REPO_ROOT / "providers"

for d in (REPORTS_DIR, FREE_DIR, PAID_DIR, PROVIDERS_DIR):
    d.mkdir(parents=True, exist_ok=True)


def sh(cmd, timeout=15, shell=False):
    """Run a shell command, return (rc, stdout, stderr)."""
    try:
        r = subprocess.run(cmd if shell else cmd.split(),
                           capture_output=True, text=True, timeout=timeout)
        return r.returncode, r.stdout.strip(), r.stderr.strip()
    except Exception as e:
        return -1, "", str(e)


def http_get(url, headers=None, timeout=10):
    """GET via stdlib, return (ok, data_or_text)."""
    req = urllib.request.Request(url, headers=headers or {})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            try:
                return True, json.loads(body)
            except Exception:
                return True, body
    except Exception as e:
        return False, str(e)


def load_env(path):
    """Parse a .env file into a dict."""
    env = {}
    if not os.path.isfile(path):
        return env
    for line in open(path, encoding="utf-8", errors="replace"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            k, v = line.split("=", 1)
            env[k] = v
    return env


def strip_jsonc(raw):
    """Remove // line comments without breaking URLs containing //."""
    lines = []
    for line in raw.split("\n"):
        stripped = line.lstrip()
        if stripped.startswith("//"):
            continue
        lines.append(line)
    return "\n".join(lines)


# ─── GCP ──────────────────────────────────────────────────────────────────────

def scan_gcp():
    result = {"projects": [], "active_account": "", "active_project": ""}
    rc, out, _ = sh("gcloud config get-value account")
    result["active_account"] = out if rc == 0 else ""
    rc, out, _ = sh("gcloud config get-value project")
    result["active_project"] = out if rc == 0 else ""

    rc, out, _ = sh("gcloud projects list --format=json")
    if rc == 0 and out:
        try:
            for p in json.loads(out):
                pid = p.get("projectId", "?")
                pnum = p.get("projectNumber", "?")
                rc2, svc_out, _ = sh(f"gcloud services list --project={pid} --format='value(serviceName)'")
                services = [s for s in svc_out.split("\n") if s] if rc2 == 0 else []
                rc3, bill_out, _ = sh(f"gcloud beta billing projects describe {pid}")
                billing = "enabled" if "billingEnabled: true" in bill_out else "disabled"
                result["projects"].append({
                    "projectId": pid,
                    "name": p.get("name", "?"),
                    "projectNumber": pnum,
                    "billing": billing,
                    "services": services,
                    "service_count": len(services),
                })
        except json.JSONDecodeError:
            pass
    return result


# ─── Local backend ────────────────────────────────────────────────────────────

def scan_local_backend():
    ok, data = http_get("http://127.0.0.1:8000/api/models")
    if not ok:
        return {"error": data, "models": [], "count": 0}
    models = data.get("models", []) if isinstance(data, dict) else []
    return {"endpoint": "http://127.0.0.1:8000/api/models", "models": models, "count": len(models)}


# ─── OmniRoute daemon ─────────────────────────────────────────────────────────

def scan_omniroute():
    result = {"endpoint": "http://127.0.0.1:20128/v1", "models": [], "count": 0}
    ok, data = http_get("http://127.0.0.1:20128/v1/models",
                        headers={"Authorization": "Bearer omniroute-token"})
    if ok and isinstance(data, dict):
        result["models"] = data.get("data", [])
        result["count"] = len(result["models"])
    elif ok and isinstance(data, str):
        result["error"] = data[:200]
    else:
        result["error"] = data
    return result


# ─── OpenRouter API ───────────────────────────────────────────────────────────

def scan_openrouter():
    result = {"free": [], "paid": [], "free_count": 0, "paid_count": 0, "total_count": 0}
    env = load_env("/var/www/evabot-backend/.env")
    key = env.get("OPENROUTER_API_KEY", "")
    if not key:
        result["error"] = "No OPENROUTER_API_KEY in .env"
        return result
    ok, data = http_get("https://openrouter.ai/api/v1/models",
                        headers={"Authorization": f"Bearer {key}"})
    if not ok:
        result["error"] = data[:300]
        return result
    all_models = data.get("data", []) if isinstance(data, dict) else []
    for m in all_models:
        pricing = m.get("pricing", {})
        is_free = pricing.get("prompt", "") == "0"
        entry = {
            "id": m.get("id", "?"),
            "name": m.get("name", m.get("id", "?")),
            "context_length": m.get("context_length", 0),
            "is_free": is_free,
            "prompt_price": pricing.get("prompt", ""),
            "completion_price": pricing.get("completion", ""),
        }
        if is_free:
            result["free"].append(entry)
        else:
            result["paid"].append(entry)
    result["free_count"] = len(result["free"])
    result["paid_count"] = len(result["paid"])
    result["total_count"] = len(all_models)
    return result


# ─── Gemini API ───────────────────────────────────────────────────────────────

def scan_gemini_api():
    result = {"models": [], "count": 0}
    env = load_env("/var/www/evabot-backend/.env")
    key = env.get("GEMINI_API_KEY", "")
    if not key:
        result["error"] = "No GEMINI_API_KEY in .env"
        return result
    ok, data = http_get(
        f"https://generativelanguage.googleapis.com/v1beta/models?key={key}")
    if not ok:
        result["error"] = data[:300]
        return result
    models = data.get("models", []) if isinstance(data, dict) else []
    for m in models:
        result["models"].append({
            "name": m.get("name", "?"),
            "displayName": m.get("displayName", ""),
            "inputTokenLimit": m.get("inputTokenLimit", 0),
            "outputTokenLimit": m.get("outputTokenLimit", 0),
            "supportedGenerationMethods": m.get("supportedGenerationMethods", []),
        })
    result["count"] = len(result["models"])
    return result


# ─── HuggingFace from configs ─────────────────────────────────────────────────

def scan_hf_from_config():
    configs = [
        "/home/evabot/.config/opencode/opencode.json",
        "/home/evabot/.config/Code/User/mcp.json",
        "/home/evabot/.config/kilo/kilo.jsonc",
        "/home/evabot/.config/Claude/claude_desktop_config.json",
    ]
    hf_models = []
    for cfg_path in configs:
        if not os.path.isfile(cfg_path):
            continue
        try:
            raw = open(cfg_path, encoding="utf-8").read()
            data = json.loads(strip_jsonc(raw))
        except Exception:
            continue
        providers = data.get("provider", {}) if "provider" in data else {}
        if "huggingface" in providers:
            models = providers["huggingface"].get("models", {})
            for k, v in models.items():
                hf_models.append({"id": k, "name": v.get("name", k),
                                  "source": cfg_path})
    return {"models": hf_models, "count": len(hf_models)}


# ─── Other providers (.env keys) ──────────────────────────────────────────────

def scan_other_providers():
    env = load_env("/var/www/evabot-backend/.env")
    cfg = {
        "groq": ("GROQ_API_KEY", "Groq"),
        "cerebras": ("CEREBRAS_API_KEY", "Cerebras"),
        "zai": ("ZAI_API_KEY", "Z.ai (GLM)"),
        "cloudflare_ai": ("CLOUDFLARE_AI_KEY", "Cloudflare Workers AI"),
        "mistral": ("MISTRAL_API_KEY", "Mistral AI"),
        "hf": ("HF_TOKEN", "HuggingFace"),
        "opencode": ("OPENCODE_API_KEY", "OpenCode Platform"),
        "openrouter_key": ("OPENROUTER_API_KEY", "OpenRouter"),
        "gemini_key": ("GEMINI_API_KEY", "Google Gemini"),
        "omniroute_key": ("OMNIROUTE_API_KEY", "OmniRoute"),
    }
    result = []
    for key_name, (env_var, label) in cfg.items():
        val = env.get(env_var, "")
        result.append({
            "provider": label,
            "env_var": env_var,
            "configured": bool(val),
            "masked": (val[:8] + "...***") if val else "",
        })
    return result


# ─── Local LLM services (port scan) ───────────────────────────────────────────

def check_local_llm_services():
    ports = {
        11434: "Ollama",
        1234: "oobabooga / LMStudio",
        8080: "vLLM / oobabooga",
        8000: "Local Backend (FastAPI)",
        3000: "Frontend (Vite/React)",
        8090: "Backend Proxy",
        8101: "MCP / Agent service",
        8137: "Agent service",
        5000: "Flask / Generic API",
        9000: "PHP-FPM / Generic",
        20128: "OmniRoute Daemon (LiteLLM)",
    }
    found = []
    for port, name in ports.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex(("127.0.0.1", port))
        sock.close()
        if result == 0:
            found.append({"port": port, "service": name, "status": "listening"})
    return found


# ─── Docker containers ────────────────────────────────────────────────────────

def scan_docker():
    rc, out, _ = sh("docker ps --format '{{json .}}'")
    containers = []
    if rc == 0 and out:
        for line in out.strip().split("\n"):
            if line:
                try:
                    containers.append(json.loads(line))
                except Exception:
                    pass
    return containers


# ─── Config files ─────────────────────────────────────────────────────────────

CONFIG_FILES = [
    "/var/www/evabot-backend/.env",
    "/var/www/evabot-backend/.env.example",
    "/home/evabot/.config/opencode/opencode.json",
    "/home/evabot/.config/Code/User/mcp.json",
    "/home/evabot/.config/Claude/claude_desktop_config.json",
    "/home/evabot/.config/kilo/kilo.jsonc",
]

def scan_config_files():
    api_key_patterns = re.compile(r'([A-Z][A-Z0-9_]*)\s*[=:]\s*["\']?([^"\'\n]+)["\']?')
    results = []
    for path in CONFIG_FILES:
        if not os.path.isfile(path):
            continue
        content = open(path, encoding="utf-8", errors="replace").read()
        matches = api_key_patterns.findall(content)
        keys = []
        for k, v in matches:
            if any(term in k.upper() for term in ("API", "KEY", "TOKEN", "SECRET")):
                masked = v[:8] + "...***" if len(v) > 8 else "***"
                keys.append({"var": k, "masked": masked})
        results.append({"file": path, "api_keys_found": keys, "size_bytes": os.path.getsize(path)})
    return results


# ─── Model classification ─────────────────────────────────────────────────────

def classify_model(model_entry):
    """Return ('free'|'paid'|'open_weights', tier_string)."""
    tier = str(model_entry.get("tier", "")).lower()
    pricing = model_entry.get("pricing", {})
    free_tier = str(pricing.get("freeTierStatus", "")).lower()

    if "open weights" in tier:
        return "open_weights", tier
    if "free quota" in tier:
        return "free", tier
    if "community" in tier and "free" in tier:
        return "free", tier
    if "opencode platform" in tier.lower():
        return "free", tier
    if "omniroute daemon" in tier.lower() and "free" in free_tier.lower():
        return "free", tier
    if "omniroute daemon" in tier.lower() and ("paid" in free_tier.lower() or "pay" in free_tier.lower()):
        return "paid", tier
    if "paid" in tier or "enterprise" in tier:
        return "paid", tier
    if free_tier == "100% free quota available":
        return "free", tier
    return "paid", tier


def model_to_markdown(model_entry, source="local-backend"):
    mid = model_entry.get("id", "unknown")
    name = model_entry.get("name", mid)
    provider = model_entry.get("provider", "?")
    category = model_entry.get("category", "")
    tier = model_entry.get("tier", "")
    cw = model_entry.get("contextWindow", 0)
    out_tokens = model_entry.get("maxOutputTokens", 0)
    coding = model_entry.get("codingStrengths", "")
    pricing = model_entry.get("pricing", {})
    free_status = pricing.get("freeTierStatus", "")
    free_details = pricing.get("freeTierDetails", "")
    input_usd = pricing.get("inputPer1MTokensUSD", "")
    output_usd = pricing.get("outputPer1MTokensUSD", "")
    input_eur = pricing.get("inputPer1MTokensEUR", "")
    output_eur = pricing.get("outputPer1MTokensEUR", "")
    recommended = model_entry.get("recommended", False)

    md = f"""# {name}

| Field | Value |
|---|---|
| **ID** | `{mid}` |
| **Provider** | {provider} |
| **Category** | {category} |
| **Tier** | {tier} |
| **Source** | {source} |
| **Recommended** | {"Yes" if recommended else "No"} |
| **Context Window** | {cw:,} tokens |
| **Max Output Tokens** | {out_tokens:,} tokens |
| **Free Tier Status** | {free_status} |
| **Free Tier Details** | {free_details} |
| **Pricing (USD)** | Input: {input_usd} | Output: {output_usd} |
| **Pricing (EUR)** | Input: {input_eur} | Output: {output_eur} |

## Coding Strengths

{coding if coding else "Not specified."}

## Configuration

```env
MODEL_ID={mid}
PROVIDER={provider}
```
"""
    return md


def write_model_md(model_entry, is_free):
    mid = model_entry.get("id", "unknown").replace("/", "_").replace(".", "_")
    md = model_to_markdown(model_entry)
    dest = FREE_DIR if is_free else PAID_DIR
    fpath = dest / f"{mid}.md"
    fpath.write_text(md, encoding="utf-8")
    return str(fpath)


# ─── Provider markdown generation ─────────────────────────────────────────────

DASH = "—"

def write_provider_md(providers_info):
    for prov_id, info in providers_info.items():
        prov_md_path = PROVIDERS_DIR / f"{prov_id}.md"
        lines = [f"# {info['name']}", "", info["description"], "", "## Configuration", ""]
        lines.append("| Field | Value |")
        lines.append("|---|---|")
        lines.append(f"| API Endpoint | `{info.get('api_endpoint', DASH)}` |")
        lines.append(f"| Env Var | `{info.get('env_var', DASH)}` |")
        lines.append(f"| Config File | `{info.get('config_file', DASH)}` |")
        lines.append(f"| Project | `{info.get('project', DASH)}` |")
        lines.append(f"| Billing | {info.get('billing', DASH)} |")
        if "services" in info and info["services"]:
            lines.append(f"| GCP Services | {', '.join(info['services'])} |")
        if "free_count" in info:
            lines.append(f"| Free Models | {info['free_count']} |")
        if "paid_count" in info:
            lines.append(f"| Paid Models | {info['paid_count']} |")
        if "total_count" in info:
            lines.append(f"| Total Models | {info['total_count']} |")
        lines.append("")
        if "free_models" in info and info["free_models"]:
            lines.append("## Free / Free-Quota Models (from local catalog)")
            lines.append("")
            lines.append("| ID | Context Window | Max Output |")
            lines.append("|---|---|---|")
            for m in info["free_models"]:
                lines.append(f"| {m.get('id','')} | {m.get('contextWindow','')} | {m.get('maxOutputTokens','')} |")
            lines.append("")
        if "open_weights" in info and info["open_weights"]:
            lines.append("## Open-Weights Models")
            lines.append("")
            lines.append("| ID | Context Window | Max Output |")
            lines.append("|---|---|---|")
            for m in info["open_weights"]:
                lines.append(f"| {m.get('id','')} | {m.get('contextWindow','')} | {m.get('maxOutputTokens','')} |")
            lines.append("")
        if "paid_models" in info and info["paid_models"]:
            lines.append("## Paid Models (from local catalog)")
            lines.append("")
            lines.append("| ID | Provider | Context Window | Input USD | Output USD |")
            lines.append("|---|---|---|---|---|")
            for m in info["paid_models"]:
                pricing = m.get("pricing", {})
                lines.append(f"| {m.get('id','')} | {m.get('provider','')} | {m.get('contextWindow','')} | {pricing.get('inputPer1MTokensUSD','')} | {pricing.get('outputPer1MTokensUSD','')} |")
            lines.append("")
        if "routes" in info and info["routes"]:
            lines.append("## Routes / Models")
            lines.append("")
            for mid in info["routes"]:
                lines.append(f"- `{mid}`")
            lines.append("")
        if "model_count" in info:
            lines.append(f"## Model Count\n\n{info['model_count']}\n")
        prov_md_path.write_text("\n".join(lines), encoding="utf-8")


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    print("\U0001F504 Scanning full system for LLM infrastructure...")
    report = {
        "scan_timestamp": datetime.now(timezone.utc).isoformat(),
        "system": "EvaBot Agent VM (europe-west3-a, 100.66.98.4)",
        "gcp": {},
        "local_backend": {},
        "omniroute": {},
        "openrouter": {},
        "gemini_api": {},
        "huggingface": {},
        "other_providers": [],
        "local_llm_services": [],
        "docker_containers": [],
        "config_files": [],
        "model_catalog": {"free": [], "paid": [], "open_weights": []},
    }

    print("  [1/10] Scanning GCP projects, services, billing...")
    report["gcp"] = scan_gcp()

    print("  [2/10] Scanning local backend /api/models...")
    report["local_backend"] = scan_local_backend()

    print("  [3/10] Scanning OmniRoute daemon...")
    report["omniroute"] = scan_omniroute()

    print("  [4/10] Scanning OpenRouter API...")
    report["openrouter"] = scan_openrouter()

    print("  [5/10] Scanning Gemini API models...")
    report["gemini_api"] = scan_gemini_api()

    print("  [6/10] Scanning HuggingFace models from configs...")
    report["huggingface"] = scan_hf_from_config()

    print("  [7/10] Scanning other API providers (.env keys)...")
    report["other_providers"] = scan_other_providers()

    print("  [8/10] Scanning local LLM services (ports)...")
    report["local_llm_services"] = check_local_llm_services()

    print("  [9/10] Scanning Docker containers...")
    report["docker_containers"] = scan_docker()

    print("  [10/10] Scanning config files for API keys...")
    report["config_files"] = scan_config_files()

    # ── Classify & write model markdown files ──
    print("\n\U0001F4DD Classifying models and writing markdown files...")
    backend_models = report["local_backend"].get("models", [])
    for m in backend_models:
        cls, _ = classify_model(m)
        if cls == "free":
            report["model_catalog"]["free"].append(m)
            write_model_md(m, is_free=True)
        elif cls == "open_weights":
            report["model_catalog"]["open_weights"].append(m)
            write_model_md(m, is_free=True)
        else:
            report["model_catalog"]["paid"].append(m)
            write_model_md(m, is_free=False)

    written_free = len(list(FREE_DIR.glob("*.md")))
    written_paid = len(list(PAID_DIR.glob("*.md")))
    print(f"    -> {written_free} free/open-weights model files, {written_paid} paid-model files written")

    # ── Write provider markdown files ──
    active_proj = report["gcp"].get("active_project", "")
    proj_info = next((p for p in report["gcp"]["projects"] if p["projectId"] == active_proj), {})
    billing = proj_info.get("billing", "unknown")
    services = [s for s in proj_info.get("services", [])
                if "gemini" in s or "aiplatform" in s or "vertexai" in s]

    providers_info = {
        "google-gemini": {
            "name": "Google Gemini / Vertex AI",
            "description": "Google DeepMind LLM API and Vertex AI platform models, accessed via the evabot-agent-server project.",
            "api_endpoint": "https://generativelanguage.googleapis.com/v1beta",
            "project": active_proj,
            "billing": billing,
            "services": services,
            "free_models": [m for m in report["model_catalog"]["free"]
                            if m.get("provider") == "Google DeepMind"],
            "paid_models": [m for m in report["model_catalog"]["paid"]
                            if m.get("provider") == "Google DeepMind"],
            "open_weights": report["model_catalog"]["open_weights"],
            "config_file": "/var/www/evabot-backend/.env",
            "env_var": "GEMINI_API_KEY",
        },
        "openrouter": {
            "name": "OpenRouter",
            "description": "Aggregated LLM API with 21 free community models and 400+ paid premium models.",
            "api_endpoint": "https://openrouter.ai/api/v1",
            "free_count": report["openrouter"].get("free_count", 0),
            "paid_count": report["openrouter"].get("paid_count", 0),
            "total_count": report["openrouter"].get("total_count", 0),
            "config_file": "/var/www/evabot-backend/.env",
            "env_var": "OPENROUTER_API_KEY",
        },
        "omniroute": {
            "name": "OmniRoute (LiteLLM Daemon)",
            "description": "Self-hosted LiteLLM proxy routing to free providers: Groq, Cloudflare, Z.ai, OpenRouter free.",
            "api_endpoint": "http://127.0.0.1:20128/v1",
            "routes": [m.get("id", "") for m in report["omniroute"].get("models", [])],
            "model_count": report["omniroute"].get("count", 0),
            "config_file": "/var/www/evabot-backend/.env",
            "env_var": "OMNIROUTE_API_KEY (local, self-hosted)",
        },
        "huggingface": {
            "name": "HuggingFace Inference Providers",
            "description": "HuggingFace router serving 136 models from multiple providers via @ai-sdk/openai-compatible.",
            "api_endpoint": "https://router.huggingface.co/v1",
            "model_count": report["huggingface"].get("count", 0),
            "config_file": "/home/evabot/.config/opencode/opencode.json",
            "env_var": "HF_TOKEN",
        },
        "vertex-ai": {
            "name": "Vertex AI (Enterprise)",
            "description": "Google Cloud Vertex AI serving Anthropic Claude, Meta Llama, Mistral, Cohere, and DeepSeek models.",
            "api_endpoint": "https://us-central1-aiplatform.googleapis.com",
            "project": active_proj,
            "billing": billing,
            "paid_models": [m for m in report["model_catalog"]["paid"]
                            if m.get("provider") in ("Anthropic", "Meta", "Mistral AI", "AI21 Labs", "Cohere", "DeepSeek")],
            "config_file": "/var/www/evabot-backend/.env",
        },
        "opencode": {
            "name": "OpenCode Platform",
            "description": "OpenCode-native models: go-coder-32b and go-fast, both with free developer quota.",
            "api_endpoint": "http://127.0.0.1:8000/api/models",
            "free_models": [m for m in report["model_catalog"]["free"]
                            if m.get("provider") == "OpenCode AI"],
            "config_file": "/home/evabot/.config/opencode/opencode.json",
        },
        "groq": {
            "name": "Groq",
            "description": "Groq LPU inference API, used via OmniRoute free routing.",
            "env_var": "GROQ_API_KEY",
            "config_file": "/var/www/evabot-backend/.env",
        },
        "cerebras": {
            "name": "Cerebras",
            "description": "Cerebras Cloud API for fast inference.",
            "env_var": "CEREBRAS_API_KEY",
            "config_file": "/var/www/evabot-backend/.env",
        },
        "zai": {
            "name": "Z.ai (GLM)",
            "description": "Z.ai GLM API (GLM-5.3 Flash free tier).",
            "env_var": "ZAI_API_KEY",
            "config_file": "/var/www/evabot-backend/.env",
        },
        "cloudflare-ai": {
            "name": "Cloudflare Workers AI",
            "description": "Cloudflare Workers AI inference (gpt-oss, Llama, Gemma, Nemotron free models).",
            "env_var": "CLOUDFLARE_AI_KEY",
            "config_file": "/var/www/evabot-backend/.env",
        },
        "mistral": {
            "name": "Mistral AI",
            "description": "Mistral AI API (also via OmniRoute and Vertex AI).",
            "env_var": "MISTRAL_API_KEY",
            "config_file": "/var/www/evabot-backend/.env",
        },
    }

    print("  \U0001F4C4 Writing provider markdown files...")
    write_provider_md(providers_info)

    # ── Write JSON report ──
    json_path = REPORTS_DIR / "models_catalog.json"
    json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"    -> {json_path}")

    # ── Write TSV ──
    tsv_path = REPORTS_DIR / "models_catalog.tsv"
    tsv_lines = [
        "id\tname\tprovider\tcategory\ttier\tsource\tcontext_window\tmax_output_tokens\tfree_or_paid\tinput_price_usd\toutput_price_usd"
    ]
    for cat in ("free", "open_weights", "paid"):
        for m in report["model_catalog"][cat]:
            pricing = m.get("pricing", {})
            tsv_lines.append("\t".join([
                m.get("id", ""),
                m.get("name", ""),
                m.get("provider", ""),
                m.get("category", ""),
                m.get("tier", ""),
                "local-backend",
                str(m.get("contextWindow", "")),
                str(m.get("maxOutputTokens", "")),
                cat,
                pricing.get("inputPer1MTokensUSD", ""),
                pricing.get("outputPer1MTokensUSD", ""),
            ]))
    tsv_path.write_text("\n".join(tsv_lines), encoding="utf-8")
    print(f"    -> {tsv_path}")

    # ── Write markdown system report ──
    md_path = REPORTS_DIR / "system_scan_report.md"
    md = []
    md.append("# System Report: LLM Infrastructure Scan - EvaBot")
    md.append("")
    md.append(f"**Scan timestamp:** {report['scan_timestamp']}  ")
    md.append(f"**Server:** {report['system']}  ")
    md.append(f"**Active GCP account:** `{report['gcp'].get('active_account','')}`  ")
    md.append(f"**Active GCP project:** `{report['gcp'].get('active_project','')}`  ")
    md.append("")

    # GCP projects
    md.append("## 1. Google Cloud Platform")
    md.append("")
    md.append("| Project ID | Name | Project Number | Billing | Services |")
    md.append("|---|---|---|---|---|")
    for p in report["gcp"]["projects"]:
        md.append(f"| {p['projectId']} | {p['name']} | {p['projectNumber']} | {p['billing']} | {p['service_count']} enabled |")
    md.append("")

    # Local backend
    lb = report["local_backend"]
    md.append("## 2. Local Backend (http://127.0.0.1:8000)")
    if lb.get("count"):
        md.append(f"\n**Total models in catalog:** {lb['count']}  ")
        md.append("**Endpoint:** `/api/models`\n")
        md.append("| ID | Provider | Tier | Context | Output |")
        md.append("|---|---|---|---|---|")
        for m in lb["models"]:
            md.append(f"| {m.get('id','')} | {m.get('provider','')} | {m.get('tier','')} | {m.get('contextWindow','')} | {m.get('maxOutputTokens','')} |")
    else:
        md.append(f"Error: {lb.get('error','unknown')}")
    md.append("")

    # OmniRoute
    om = report["omniroute"]
    md.append("## 3. OmniRoute daemon (LiteLLM proxy)")
    md.append(f"\n**Endpoint:** {om.get('endpoint','')}  ")
    md.append(f"**Routes:** {om.get('count','?')}")
    if om.get("models"):
        md.append("")
        md.append("| ID |")
        md.append("|---|")
        for m in om["models"]:
            md.append(f"| {m.get('id','?')} |")
    md.append("")

    # OpenRouter
    orr = report["openrouter"]
    md.append("## 4. OpenRouter API")
    md.append(f"\n**Total models:** {orr.get('total_count','?')}  ")
    md.append(f"**Free:** {orr.get('free_count','?')}  ")
    md.append(f"**Paid:** {orr.get('paid_count','?')}\n")
    md.append("### Free models")
    md.append("")
    md.append("| ID | Context | Input $ | Output $ |")
    md.append("|---|---|---|---|")
    for m in orr.get("free", []):
        md.append(f"| {m['id']} | {m['context_length']} | {m['prompt_price']} | {m['completion_price']} |")
    md.append("")
    md.append("### Paid models (first 20)")
    md.append("")
    md.append("| ID | Context | Input $ | Output $ |")
    md.append("|---|---|---|---|")
    for m in orr.get("paid", [])[:20]:
        md.append(f"| {m['id']} | {m['context_length']} | {m['prompt_price']} | {m['completion_price']} |")
    if len(orr.get("paid", [])) > 20:
        md.append(f"\n... and {len(orr.get('paid',[]))-20} more paid models")
    md.append("")

    # Gemini
    gm = report["gemini_api"]
    md.append("## 5. Gemini API (gen-lang project)")
    if gm.get("count"):
        md.append(f"\n**Total models:** {gm['count']}\n")
        md.append("| Name | Display | Input Tokens | Output Tokens |")
        md.append("|---|---|---|---|")
        for m in gm["models"]:
            md.append(f"| {m.get('name','')} | {m.get('displayName','')} | {m.get('inputTokenLimit','')} | {m.get('outputTokenLimit','')} |")
    else:
        md.append(f"Error: {gm.get('error','unknown')}")
    md.append("")

    # HuggingFace
    hf = report["huggingface"]
    md.append("## 6. HuggingFace Inference (from config files)")
    md.append(f"\n**Models in config:** {hf.get('count','?')}\n")
    if hf.get("models"):
        md.append("| ID | Source |")
        md.append("|---|---|")
        for m in hf["models"][:30]:
            md.append(f"| {m['id']} | {m['source']} |")
        if len(hf["models"]) > 30:
            md.append(f"\n... and {len(hf['models'])-30} more")
    md.append("")

    # Other providers
    md.append("## 7. Other API Providers")
    md.append("")
    md.append("| Provider | Env Var | Configured |")
    md.append("|---|---|---|")
    for p in report["other_providers"]:
        md.append(f"| {p['provider']} | `{p['env_var']}` | {'Yes' if p['configured'] else 'No'} |")
    md.append("")

    # Local services
    md.append("## 8. Local LLM Services")
    md.append("")
    md.append("| Port | Service | Status |")
    md.append("|---|---|---|")
    for s in report["local_llm_services"]:
        md.append(f"| {s['port']} | {s['service']} | {s['status']} |")
    md.append("")

    # Docker
    md.append("## 9. Docker Containers")
    md.append("")
    md.append("| Names | Image | Status |")
    md.append("|---|---|---|")
    for c in report["docker_containers"]:
        md.append(f"| {c.get('Names','')} | {c.get('Image','')} | {c.get('Status','')} |")
    md.append("")

    # Config files
    md.append("## 10. Config Files")
    md.append("")
    for c in report["config_files"]:
        md.append(f"### `{c['file']}`")
        md.append(f"- Size: {c['size_bytes']} bytes")
        if c["api_keys_found"]:
            md.append("- API keys found:")
            for k in c["api_keys_found"]:
                md.append(f"  - `{k['var']}` = `{k['masked']}`")
        else:
            md.append("- No API keys found")
        md.append("")

    # Summary
    t_free = len(report["model_catalog"]["free"])
    t_paid = len(report["model_catalog"]["paid"])
    t_ow = len(report["model_catalog"]["open_weights"])
    md.append("## Summary")
    md.append("")
    md.append(f"| Metric | Count |")
    md.append(f"|---|---|")
    md.append(f"| Total models in local catalog | {t_free + t_paid + t_ow} |")
    md.append(f"| Free / Free-Quota models | {t_free} |")
    md.append(f"| Open-Weights models | {t_ow} |")
    md.append(f"| Paid (pay-per-use) models | {t_paid} |")
    md.append(f"| OpenRouter free models | {orr.get('free_count','?')} |")
    md.append(f"| OpenRouter paid models | {orr.get('paid_count','?')} |")
    md.append(f"| Gemini API models (gen-lang) | {gm.get('count','?')} |")
    md.append(f"| OmniRoute routes | {om.get('count','?')} |")
    md.append(f"| HuggingFace models in configs | {hf.get('count','?')} |")
    md.append(f"| Local LLM services listening | {len(report['local_llm_services'])} |")
    md.append(f"| Docker containers | {len(report['docker_containers'])} |")
    md.append("")

    md_path.write_text("\n".join(md), encoding="utf-8")
    print(f"    -> {md_path}")

    print(f"\nDone. All reports in {REPORTS_DIR}/")


if __name__ == "__main__":
    main()
