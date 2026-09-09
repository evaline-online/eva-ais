# DeepSeek

DeepSeek is an AI research lab from China offering powerful open-weight models. They provide a **free API tier** with 50 requests/day and $5 API credit for testing.

## Configuration

| Field | Value |
|---|---|
| Website | https://deepseek.com |
| API Endpoint | `https://api.deepseek.com/v1` |
| Env Var | `DEEPSEEK_API_KEY` |
| Config File | `/var/www/evabot-backend/.env` |
| Free Tier | 50 requests/day, 2 RPM, $5 API credit |
| Credit Card | Not required for free tier |
| Models | 4 free models |

## Free Models

| Model | Context | Free Tier | Description |
|---|---|---|---|
| `deepseek-v4-pro` | 1,000K | 20 RPM | Flagship, 1.6T params (49B active MoE) |
| `deepseek-v4-flash` | 1,000K | 20 RPM | Lightweight, 284B params (13B active) |
| `deepseek-v3` | 64K | 50 RPD | Previous flagship, 64K context |
| `deepseek-r1` | 64K | 50 RPD | Reasoning model, strong at math/code |

## DeepSeek Through FreeLLMAPI

FreeLLMAPI (freellmapi.co) routes to DeepSeek models for free through multiple providers:

| Model | Provider | Free Limit |
|---|---|---|
| `deepseek-ai/DeepSeek-V4-Pro` | HuggingFace Router | $0.10/mo credit |
| `deepseek-ai/DeepSeek-V4-Flash` | HuggingFace Router | ~1-3M tokens |
| `deepseek-v4-flash-free` | OpenCode Zen | 20 rpm, 200 rpd |
| `deepseek-v4-pro` | NavyAI | 20 rpm |
| `deepseek-v4-flash` | NavyAI | 20 rpm |
| `deepseek-v3.2` | NavyAI | 20 rpm, 164K context |
| `deepseek-chat` | NavyAI | 20 rpm |
| `deepseek-reasoner` | NavyAI | 20 rpm |
| `@cf/deepseek-ai/deepseek-r1-distill-qwen-32b` | Cloudflare AI | ~3-5M tokens |

## Notes

- DeepSeek V4 models released April 2026 under MIT license
- DeepSeek V4 Pro: 1.6T total params, 49B active (MoE with CSA + HCA)
- DeepSeek V4 Flash: 284B total, 13B active, efficiency-optimized

## Links

- API: https://api.deepseek.com/v1
- Docs: https://platform.deepseek.com/docs
- FreeLLMAPI: https://freellmapi.co
- Models catalog: https://freellmapi.co/models
