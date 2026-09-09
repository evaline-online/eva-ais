# Cloudflare Workers AI

Cloudflare Workers AI provides serverless inference at the edge with a generous free tier.

## Configuration

| Field | Value |
|---|---|
| API Endpoint | `https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1` |
| Env Var | `CLOUDFLARE_API_TOKEN` |
| Config File | `/home/evabot/.config/kilo/kilo.jsonc` |
| Account ID | `e814e520e5fe64538f5a389830373d44` |
| Billing | Free Tier: 10K neurons/day ($0.00) · Paid: $0.02–$0.05/1K tokens |
| Status | **65 models available** |

## Free Tier

Cloudflare offers **10,000 neurons/day** free (no credit card required). Approximate token budgets per model size:

| Model Size | Est. Daily Free Tokens |
|---|---|
| 3B params | ~3,000–5,000 |
| 7B params | ~1,500–2,000 |
| 20B params | ~300–500 |
| 30B+ params | ~100–300 |

## Available Models (65)

| # | Model ID | Size | Type | Notes |
|---|---|---|---|---|
| 1 | `@cf/openai/gpt-oss-120b` | 120B | Text | Free tier |
| 2 | `@cf/baai/bge-m3` | — | Embedding | Embedding model |
| 3 | `@cf/huggingface/distilbert-sst-2-int8` | 67M | Classification | Sentiment |
| 4 | `@cf/google/gemma-2b-it-lora` | 2B | Text | LoRA finetune |
| 5 | `@cf/black-forest-labs/flux-2-klein-9b` | 9B | Image | Text-to-image |
| 6 | `@cf/meta/llama-3.2-3b-instruct` | 3B | Text | Free tier |
| 7 | `@cf/meta/llama-guard-3-8b` | 8B | Classification | Safety guard |
| 8 | `@cf/qwen/qwen3-embedding-0.6b` | 600M | Embedding | Embedding |
| 9 | `@cf/myshell-ai/melotts` | — | Audio | Text-to-speech |
| 10 | `@cf/mistral/mistral-7b-instruct-v0.2-lora` | 7B | Text | LoRA finetune |
| 11 | `@cf/deepgram/aura-2-es` | — | Audio | Speech |
| 12 | `@cf/moonshotai/kimi-k2.7-code` | 14B | Code | Coding optimized |
| 13 | `@cf/openai/whisper` | — | Audio | Speech-to-text |
| 14 | `@cf/zai-org/glm-5.3` | — | Text | Z.ai GLM |
| 15 | `@cf/pfnet/plamo-embedding-1b` | 1B | Embedding | Embedding |
| 16 | `@cf/llava-hf/llava-1.5-7b-hf` | 7B | Vision | Multimodal |
| 17 | `@cf/deepseek-ai/deepseek-r1-distill-qwen-32b` | 32B | Text | DeepSeek distilled |
| 18 | `@cf/runwayml/stable-diffusion-v1-5-inpainting` | — | Image | Inpainting |
| 19 | `@cf/deepgram/flux` | — | Image | Text-to-image |
| ... | + 46 more models | — | — | See full list |

## Notes

- Free tier: 10,000 neurons/day (≈ $0.00 value, limited daily)
- Paid: $0.02–$0.05 per 1K neurons (scales with model size)
- Edge inference: runs at Cloudflare's global edge network
- No models currently marked as permanently `$0.00/1M` (unlike OpenRouter free models)

## Links

- Docs: https://developers.cloudflare.com/workers-ai/
- Playground: https://playground.kilocode.ai (via Kilo Code)
