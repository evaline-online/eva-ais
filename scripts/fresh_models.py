#!/usr/bin/env python3
"""
fresh_models.py — Fetch fresh 2025–2026 LLM models from authoritative
leaderboard / API sources, compare against the existing catalog, and emit
a comparison report (top-30 paid, top-30 free) with highlight of new entries.
"""

import json
import os
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
CATALOG_PATH = os.path.join(REPORTS_DIR, "models_catalog.json")

# ── Load API keys from env files ──────────────────────────────────────

def _load_env_file(path):
    if not os.path.exists(path):
        return
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, val = line.partition("=")
            val = val.strip().strip('"').strip("'")
            if val:
                os.environ.setdefault(key, val)

_load_env_file("/var/www/evabot-backend/.env")
_load_env_file(os.path.expanduser("~/.secrets/keys.env"))

# ── Source fetchers ──────────────────────────────────────────────────────

def _http_json(url, headers=None, timeout=15):
    req = urllib.request.Request(url, headers=headers or {})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"  [WARN] {url}: {e}", file=sys.stderr)
        return None


def fetch_chatbot_arena():
    """LMSYS Chatbot Arena — live leaderboard JSON (rankings + model info)."""
    url = "https://chat.lmsys.org/ranking.json"
    data = _http_json(url)
    if not data:
        return []
    results = []
    for entry in data.get("ranking", data if isinstance(data, list) else []):
        results.append({
            "id": entry.get("model_name", ""),
            "name": entry.get("model_name", ""),
            "provider": entry.get("organization", "Arena"),
            "category": "Chatbot Arena Leaderboard",
            "description": entry.get("description", ""),
            "contextWindow": entry.get("context_length"),
            "maxOutputTokens": None,
            "recommended": False,
            "tier": "Free/Paid (varies)",
            "protocol": "",
            "pricing": {},
            "arenaScore": entry.get("score", entry.get("rating")),
            "arenaRank": entry.get("rank"),
            "source": "Chatbot Arena",
        })
    return results


def fetch_hf_openllm_leaderboard():
    """HuggingFace Open LLM Leaderboard — top models via HF API."""
    url = "https://huggingface.co/api/models?sort=likes&direction=-1&limit=50&full=false"
    data = _http_json(url)
    if not data:
        return []
    results = []
    keywords = ["llama", "gemma", "qwen", "deepseek", "mistral", "phi", "phi-",
                "bloom", "falcon", "mpt", "yi-", "intern", "baize", "vicuna"]
    for entry in data:
        mid = entry.get("id", "")
        if any(k in mid.lower() for k in keywords):
            results.append({
                "id": mid,
                "name": mid,
                "provider": entry.get("author", "HF"),
                "category": "HuggingFace Open LLM",
                "description": entry.get("description", "")[:200],
                "contextWindow": None,
                "maxOutputTokens": None,
                "recommended": False,
                "tier": "Open Weights",
                "protocol": "huggingface",
                "pricing": {"freeTierStatus": "Free / Open Weights"},
                "hfLikes": entry.get("likes"),
                "source": "HuggingFace",
            })
    return results


def fetch_openrouter_models():
    """OpenRouter — full model list via public API (no key required for listing)."""
    url = "https://openrouter.ai/api/v1/models"
    data = _http_json(url)
    if not data or "data" not in data:
        return []
    results = []
    for m in data["data"]:
        pricing_str = m.get("pricing", {}) or {}
        prompt_price = float(pricing_str.get("prompt", 0) or 0)
        completion_price = float(pricing_str.get("completion", 0) or 0)
        input_per_1m = prompt_price * 1_000_000
        output_per_1m = completion_price * 1_000_000
        is_free = input_per_1m == 0 and output_per_1m == 0
        top_provider = m.get("top_provider", {}) or {}
        entry = {
            "id": m.get("id", ""),
            "name": m.get("name", m.get("id", "")),
            "provider": (m.get("hosted_by", {}).get("name", "OpenRouter")),
            "category": "OpenRouter",
            "description": (m.get("description", "") or "")[:200],
            "contextWindow": m.get("context_length"),
            "maxOutputTokens": top_provider.get("max_completion_tokens"),
            "recommended": False,
            "tier": "Free" if is_free else "Paid",
            "protocol": "openai-compatible",
            "pricing": {
                "freeTierStatus": "Free" if is_free else "Paid",
                "inputPer1MTokensUSD": f"${input_per_1m:.2f}" if not is_free else "$0.00 (Free)",
                "outputPer1MTokensUSD": f"${output_per_1m:.2f}" if not is_free else "$0.00 (Free)",
            },
            "source": "OpenRouter",
        }
        results.append(entry)
    return results


def fetch_gemini_models():
    """Google Gemini API — public model list with pricing metadata."""
    models = []
    # Primary source: Google AI SDK / public models endpoint
    url = "https://generativelanguage.googleapis.com/v1/models"
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    headers = {}
    full_url = url
    if api_key:
        full_url = f"{url}?key={api_key}"
    data = _http_json(full_url)
    if data and "models" in data:
        for m in data["models"]:
            mid = m.get("name", "").replace("models/", "")
            if not mid:
                continue
            input_cost = output_cost = 0.0
            for p in m.get("pricing", []) or []:
                if "input" in (p.get("role", "") or p.get("mode", "")).lower():
                    input_cost = p.get("rate", 0.0)
                elif "output" in (p.get("role", "") or p.get("mode", "")).lower():
                    output_cost = p.get("rate", 0.0)
            is_free = input_cost == 0
            models.append({
                "id": mid,
                "name": mid.replace("-latest", " (Latest)").replace("-exp", " Experimental"),
                "provider": "Google DeepMind",
                "category": "Google Gemini",
                "description": (m.get("description", "") or "")[:200],
                "contextWindow": m.get("inputTokenLimit"),
                "maxOutputTokens": m.get("outputTokenLimit"),
                "recommended": False,
                "tier": "Free Quota + Paid" if is_free else "Paid",
                "protocol": "google-genai",
                "pricing": {
                    "freeTierStatus": "Free Quota" if is_free else "Paid",
                    "inputPer1MTokensUSD": f"${input_cost}" if input_cost else "$0.00 (Free)",
                    "outputPer1MTokensUSD": f"${output_cost}" if output_cost else "$0.00 (Free)",
                },
                "source": "Gemini API",
            })
    return models


def fetch_groq_models():
    """Groq — public model list (developer API)."""
    url = "https://api.groq.com/v1/models"
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        return []
    data = _http_json(url, headers={
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json",
    })
    if not data or "data" not in data:
        return []
    results = []
    for m in data["data"]:
        results.append({
            "id": m.get("id", ""),
            "name": m.get("id", ""),
            "provider": "Groq",
            "category": "Groq",
            "description": m.get("description", "")[:200] if m.get("description") else "",
            "contextWindow": m.get("context_window"),
            "maxOutputTokens": m.get("max_tokens"),
            "recommended": False,
            "tier": "Paid",
            "protocol": "openai-compatible",
            "pricing": {"freeTierStatus": "Paid"},
            "source": "Groq",
        })
    return results


def fetch_mistral_models():
    """Mistral AI — model list."""
    url = "https://api.mistral.ai/v1/models"
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        return []
    data = _http_json(url, headers={
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json",
    })
    if not data or "data" not in data:
        return []
    results = []
    for m in data["data"]:
        results.append({
            "id": m.get("id", ""),
            "name": m.get("id", ""),
            "provider": "Mistral AI",
            "category": "Mistral",
            "description": m.get("description", "")[:200] if m.get("description") else "",
            "contextWindow": m.get("context_window") or m.get("contextWindow"),
            "maxOutputTokens": m.get("max_tokens") or m.get("maxOutputTokens"),
            "recommended": False,
            "tier": "Paid",
            "protocol": "openai-compatible",
            "pricing": {"freeTierStatus": "Paid"},
            "source": "Mistral",
        })
    return results


def fetch_cerebras_models():
    """Cerebras — model list."""
    url = "https://api.cerebras.ai/v1/models"
    api_key = os.environ.get("CEREBRAS_API_KEY")
    if not api_key:
        return []
    data = _http_json(url, headers={
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json",
    })
    if not data or "data" not in data:
        return []
    results = []
    for m in data["data"]:
        results.append({
            "id": m.get("id", ""),
            "name": m.get("id", ""),
            "provider": "Cerebras",
            "category": "Cerebras",
            "description": m.get("description", "")[:200] if m.get("description") else "",
            "contextWindow": m.get("context_window") or m.get("contextWindow"),
            "maxOutputTokens": m.get("max_tokens") or m.get("maxOutputTokens"),
            "recommended": False,
            "tier": "Paid",
            "protocol": "openai-compatible",
            "pricing": {"freeTierStatus": "Paid"},
            "source": "Cerebras",
        })
    return results


def fetch_github_models():
    """GitHub Models — public catalog endpoint."""
    url = "https://api.github.com/repos/github/docs/data-languages"
    # Fallback: use a known list from GitHub Models docs
    url2 = "https://raw.githubusercontent.com/github/next.js/main/models.json"
    return []  # Not reliably available without auth


def fetch_cloudflare_models():
    """Cloudflare Workers AI — model list."""
    url = "https://api.cloudflare.com/client/v4/accounts/e814e520e5fe64538f5a389830373d44/ai/models/search"
    data = _http_json(url, headers={
        "Authorization": f"Bearer {os.environ.get('CLOUDFLARE_API_TOKEN', '')}",
        "Content-Type": "application/json",
    }, timeout=15)
    results = []
    if data and isinstance(data, dict):
        result = data.get("result", {})
        if isinstance(result, dict):
            for m in result.get("models", []):
                results.append({
                    "id": m.get("name", ""),
                    "name": m.get("name", ""),
                    "provider": "Cloudflare AI",
                    "category": "Cloudflare Workers AI",
                    "description": m.get("description", "")[:200] if m.get("description") else "",
                    "contextWindow": None,
                    "maxOutputTokens": None,
                    "recommended": False,
                    "tier": "Paid",
                    "protocol": "openai-compatible",
                    "pricing": {"freeTierStatus": "Paid"},
                    "source": "Cloudflare",
                })
        elif isinstance(result, list):
            for m in result:
                results.append({
                    "id": m.get("uid", m.get("name", "")),
                    "name": m.get("name", ""),
                    "provider": "Cloudflare AI",
                    "category": "Cloudflare Workers AI",
                    "description": m.get("description", "")[:200] if m.get("description") else "",
                    "contextWindow": None,
                    "maxOutputTokens": None,
                    "recommended": False,
                    "tier": "Paid",
                    "protocol": "openai-compatible",
                    "pricing": {"freeTierStatus": "Paid"},
                    "source": "Cloudflare",
                })
    return results


SOURCES = {
    "Chatbot Arena": fetch_chatbot_arena,
    "HuggingFace Open LLM": fetch_hf_openllm_leaderboard,
    "OpenRouter": fetch_openrouter_models,
    "Gemini API": fetch_gemini_models,
    "Groq": fetch_groq_models,
    "Mistral AI": fetch_mistral_models,
    "Cerebras": fetch_cerebras_models,
    "Cloudflare AI": fetch_cloudflare_models,
}


# ── Catalog comparison ─────────────────────────────────────────────────

def load_existing_catalog_ids(catalog_path):
    """Return a set of existing model IDs from the scan catalog."""
    existing = set()
    try:
        with open(catalog_path) as f:
            catalog = json.load(f)
        mc = catalog.get("model_catalog", {})
        for tier in ("free", "paid", "open_weights"):
            for model in mc.get(tier, []):
                existing.add(model.get("id", "").lower())
    except Exception as e:
        print(f"  [WARN] Could not load catalog: {e}", file=sys.stderr)
    return existing


def fetch_all_sources(parallel=True):
    """Fetch from all sources, optionally in parallel."""
    results = {}
    if parallel:
        with ThreadPoolExecutor(max_workers=8) as pool:
            future_map = {pool.submit(fn): name for name, fn in SOURCES.items()}
            for future in as_completed(future_map):
                name = future_map[future]
                try:
                    results[name] = future.result()
                except Exception as e:
                    print(f"  [ERROR] {name}: {e}", file=sys.stderr)
                    results[name] = []
    else:
        for name, fn in SOURCES.items():
            try:
                results[name] = fn()
            except Exception as e:
                print(f"  [ERROR] {name}: {e}", file=sys.stderr)
                results[name] = []
    return results


def classify_models(all_models):
    """Split all fetched models into free and paid based on pricing data."""
    free_models = []
    paid_models = []
    for model in all_models:
        pricing = model.get("pricing", {})
        tier = model.get("tier", "")
        free_indicator = (
            pricing.get("freeTierStatus", "").lower() in ("free", "free quota", "free quota + paid")
            or "free" in tier.lower()
            or pricing.get("inputPer1MTokensUSD") in ("$0.00", "$0.00 (Free)")
            or pricing.get("freeTierStatus") == "Free"
        )
        if free_indicator:
            free_models.append(model)
        else:
            paid_models.append(model)
    return free_models, paid_models


def format_pricing_usd(model):
    """Extract a USD pricing string for display."""
    pricing = model.get("pricing", {})
    inp = pricing.get("inputPer1MTokensUSD", "N/A")
    out = pricing.get("outputPer1MTokensUSD", "N/A")
    free_status = pricing.get("freeTierStatus", "")
    if free_status.lower() in ("free", "free quota", "free quota + paid", "free / open weights"):
        return "$0.00 (Free)"
    if inp and out:
        return f"{inp} in · {out} out"
    return "N/A"


def generate_comparison_report(free_models, paid_models, existing_ids):
    """Generate the markdown comparison report."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = []
    lines.append("# Fresh LLM Models Report (2025–2026)")
    lines.append("")
    lines.append(f"> Generated: {now}")
    lines.append(f"> Sources queried: {', '.join(SOURCES.keys())}")
    lines.append(f"> Total models discovered: **{len(free_models) + len(paid_models)}**")
    lines.append(f"> Free: **{len(free_models)}** · Paid: **{len(paid_models)}**")
    lines.append("")
    lines.append("---")
    lines.append("")

    # New vs existing
    new_free = [m for m in free_models if m["id"].lower() not in existing_ids]
    new_paid = [m for m in paid_models if m["id"].lower() not in existing_ids]
    lines.append("## New Models Not in Catalog")
    lines.append("")
    if new_free or new_paid:
        lines.append("| Model | Provider | Tier | Source |")
        lines.append("|-------|----------|------|--------|")
        for m in (new_free[:15] + new_paid[:15]):
            lines.append(f"| `{m['id']}` | {m['provider']} | {m.get('tier','')} | {m.get('source','')} |")
    else:
        lines.append("No new models discovered — all fetched models already exist in the catalog.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Top 30 Free Models table
    lines.append("## Top 30 Free Models")
    lines.append("")
    lines.append("| # | Model | Provider | Context | Pricing | Benchmark Score | Source |")
    lines.append("|---|-------|----------|---------|---------|-----------------|--------|")
    for i, m in enumerate(free_models[:30], 1):
        ctx = m.get("contextWindow")
        ctx_str = f"{ctx:,}" if ctx else "—"
        score = m.get("arenaScore") or m.get("hfLikes") or "—"
        score_str = f"{score}" if isinstance(score, str) else (f"{score:.1f}" if isinstance(score, (int, float)) else "—")
        lines.append(
            f"| {i} | `{m['id']}` | {m['provider']} | {ctx_str} | {format_pricing_usd(m)} | {score_str} | {m.get('source','')} |"
        )
    lines.append("")
    lines.append("---")
    lines.append("")

    # Top 30 Paid Models table
    lines.append("## Top 30 Paid Models")
    lines.append("")
    lines.append("| # | Model | Provider | Context | Pricing | Benchmark Score | Source |")
    lines.append("|---|-------|----------|---------|---------|-----------------|--------|")
    for i, m in enumerate(paid_models[:30], 1):
        ctx = m.get("contextWindow")
        ctx_str = f"{ctx:,}" if ctx else "—"
        score = m.get("arenaScore")
        score_str = f"{score:.1f}" if isinstance(score, (int, float)) else "—"
        lines.append(
            f"| {i} | `{m['id']}` | {m['provider']} | {ctx_str} | {format_pricing_usd(m)} | {score_str} | {m.get('source','')} |"
        )
    lines.append("")
    lines.append("---")
    lines.append("")

    # Source breakdown
    lines.append("## Source Breakdown")
    lines.append("")
    all_models = free_models + paid_models
    source_counts = {}
    for m in all_models:
        src = m.get("source", "Unknown")
        source_counts[src] = source_counts.get(src, 0) + 1
    lines.append("| Source | Models Fetched |")
    lines.append("|--------|----------------|")
    for src, count in sorted(source_counts.items(), key=lambda x: -x[1]):
        lines.append(f"| {src} | {count} |")
    lines.append("")
    lines.append("## Methodology")
    lines.append("")
    lines.append("Models are fetched live from public APIs and leaderboard endpoints:")
    lines.append("- **Chatbot Arena (LMSYS)**: Live Elo-ranked leaderboard at `chat.lmsys.org/ranking.json`")
    lines.append("- **HuggingFace Open LLM**: Popular open-weight models sorted by likes")
    lines.append("- **OpenRouter**: Full model catalog via `openrouter.ai/api/v1/models`")
    lines.append("- **Gemini API**: Official model list from `generativelanguage.googleapis.com`")
    lines.append("- **Groq**: Developer API model list")
    lines.append("- **Mistral AI**: Official model list via API")
    lines.append("- **Cerebras**: Official model list via API")
    lines.append("- **Cloudflare AI**: Workers AI model search endpoint")
    lines.append("")
    lines.append("New models are identified by checking against the existing `models_catalog.json` from `scan_all_llms.py`.")
    lines.append("")
    return "\n".join(lines)


def main():
    print("fresh_models.py — Fetching 2025–2026 LLM models from authoritative sources…")
    print()

    # Fetch all sources
    all_sources_data = fetch_all_sources(parallel=True)

    all_models = []
    for source_name, models in all_sources_data.items():
        print(f"  {source_name}: {len(models)} models")
        all_models.extend(models)

    print(f"\n  Total fetched: {len(all_models)} models")

    # Classify
    free_models, paid_models = classify_models(all_models)
    print(f"  Free: {len(free_models)} · Paid: {len(paid_models)}")

    # Load existing catalog
    existing_ids = load_existing_catalog_ids(CATALOG_PATH)
    print(f"  Existing catalog IDs: {len(existing_ids)}")

    # Generate report
    report = generate_comparison_report(free_models, paid_models, existing_ids)

    # Save
    os.makedirs(REPORTS_DIR, exist_ok=True)
    report_path = os.path.join(REPORTS_DIR, "fresh_models_comparison.md")
    with open(report_path, "w") as f:
        f.write(report)

    # Also save raw JSON
    raw_path = os.path.join(REPORTS_DIR, "fresh_models_raw.json")
    with open(raw_path, "w") as f:
        json.dump({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "sources": {name: len(models) for name, models in all_sources_data.items()},
            "free": free_models,
            "paid": paid_models,
        }, f, indent=2)

    print(f"\n  Report saved: {report_path}")
    print(f"  Raw data:     {raw_path}")
    print("\nDone.")


if __name__ == "__main__":
    main()
