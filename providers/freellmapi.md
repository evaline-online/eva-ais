# FreeLLMAPI

FreeLLMAPI is an open-source, self-hosted LLM API router that provides free access to **605 models across 34 providers**. It aggregates free tiers from multiple providers and routes requests to the available free endpoint.

## Configuration

| Field | Value |
|---|---|
| Website | https://freellmapi.co |
| GitHub | https://github.com/tashfeenahmed/freellmapi |
| Router Endpoint | Local (self-hosted) |
| Env Var | Various (per provider) |
| Free Tier | 7.4B free tokens/month, 605 models |
| Credit Card | Not required for free router |
| Premium | $19/year (live catalog updates) |

## What's Free

FreeLLMAPI aggregates free models from:
- **HuggingFace Router** — free HF Inference Endpoints credits
- **Cloudflare Workers AI** — 10K neurons/day
- **ModelScope** — 100 requests/day
- **NavyAI** — 20 RPM free
- **OpenCode Zen** — 20 RPM, 200 RPD
- **BazaarLink** — 10 RPM, 150 RPD

## Free DeepSeek Models (15)

| Model | Provider | Context | Free Limit |
|---|---|---|---|
| `deepseek-ai/DeepSeek-V4-Pro` | HuggingFace Router | 131K | $0.10/mo credit |
| `deepseek-ai/DeepSeek-V4-Pro` | ModelScope | 131K | 100 rpd |
| `deepseek-ai/DeepSeek-V4-Flash` | HuggingFace Router | 131K | ~1-3M tokens |
| `deepseek-v4-flash-free` | OpenCode Zen | 131K | 20 rpm, 200 rpd |
| `deepseek-v4-pro` | NavyAI | 1,000K | 20 rpm |
| `deepseek-ai/DeepSeek-V4-Flash` | — | 131K | — |
| `deepseek-v4-flash` | NavyAI | 1,000K | 20 rpm |
| `deepseek-v4-flash-venice` | NavyAI | 1,000K | 20 rpm |
| `@cf/deepseek-ai/deepseek-r1-distill-qwen-32b` | Cloudflare AI | 131K | ~3-5M tokens |
| `deepseek-ai/DeepSeek-R1` | HuggingFace Router | 164K | $0.10/mo credit |
| `deepseek-ai/DeepSeek-V3.2` | HuggingFace Router | 164K | $0.10/mo credit |
| `deepseek-v3.2` | NavyAI | 164K | 20 rpm |
| `deepseek-v3.2-venice` | NavyAI | 164K | 20 rpm |
| `deepseek-chat` | NavyAI | 131K | 20 rpm |
| `deepseek-reasoner` | NavyAI | — | 20 rpm |

## Other Free Providers on FreeLLMAPI

Beyond DeepSeek, FreeLLMAPI also provides free access to:
- **MiniMax** (M2, M2.5, M2.7, M3) — free via OpenRouter/HF
- **Qwen** (Qwen3 series) — free via HF Router
- **Gemma** (Gemma 4) — free via OpenRouter/HF
- **GLM** (Z.ai) — free via OpenRouter
- **Nemotron** (NVIDIA) — free via OpenRouter

## Notes

- **7.4 billion free tokens per month** tracked in live catalog
- Router is **free forever** (self-hosted open-source)
- Premium ($19/year) keeps catalog live with new free models/quotas
- Built for personal use only — each provider's ToS applies
- GitHub: https://github.com/tashfeenahmed/freellmapi

## Links

- Homepage: https://freellmapi.co
- Catalog: https://freellmapi.co/models
- GitHub: https://github.com/tashfeenahmed/freellmapi
