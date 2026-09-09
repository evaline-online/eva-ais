# Free LLM API Aggregators & Trackers

Websites and tools that aggregate, track, and provide free access to LLM models across multiple providers.

## 1. FreeLLMAPI

| Field | Value |
|---|---|
| Website | https://freellmapi.co |
| GitHub | https://github.com/tashfeenahmed/freellmapi |
| Models | 605 across 34 providers |
| Free Tokens | 7.4B/month (tracked in live catalog) |
| Router | OpenAI-compatible, self-hosted, open-source |
| Cost | Free router · $19/year premium |
| Card Required | No |

**Strongest free models right now:**

| Model | Provider | Context | Free Limit |
|---|---|---|---|
| `minimaxai/minimax-m3` | NVIDIA NIM | 197K | 40 rpm |
| `kimi-k2.7-code` | NavyAI | 262K | 20 rpm |
| `gemini-3.6-flash` | Google AI Studio | 1M | 10 rpm, 20 rpd |
| `kimi-k3` | NavyAI | 262K | 20 rpm |
| `moonshotai/Kimi-K3` | HuggingFace Router | 262K | $0.10/mo credit |
| `gemini-3.5-flash` | Google AI Studio | 1M | 10 rpm, 20 rpd |
| `Qwen/Qwen3-Coder-Next` | HuggingFace Router | 262K | ~1-3M |
| `moonshotai/Kimi-K2.6` | HuggingFace Router | 262K | ~1-3M |
| `nvidia/nemotron-3-ultra-550b-a55b` | NVIDIA NIM | 1M | 40 rpm |
| `Qwen/Qwen3-Coder-480B-A35B-Instruct` | HuggingFace Router | 262K | $0.10/mo credit |
| `zai-org/GLM-5.2` | HuggingFace Router | 200K | $0.10/mo credit |
| `grok-4.5` | NavyAI | 1M | 20 rpm |
| `deepseek-v4-flash-free` | OpenCode Zen | 131K | 20 rpm, 200 rpd |
| `gpt-5.4` | NavyAI | 1.1M | 20 rpm |

**Free providers aggregated:** BazaarLink, Cloudflare Workers AI, HuggingFace Router, ModelScope, NavyAI, OpenCode Zen, NVIDIA NIM

## 2. Free LLM API Hub

| Field | Value |
|---|---|
| Website | https://freellmapihub.com |
| Description | Continuously-verified, machine-readable dataset of free LLM APIs |
| Coverage | 25+ providers, 331+ free models |
| Updates | Daily from live sources |
| Card Required | No (for permanent free tiers) |
| GitHub | Based on `chadcms/free-llm-api-resources` |

## 3. Token Gratis (tokengratis.id)

| Field | Value |
|---|---|
| Website | https://tokengratis.id |
| Description | Indonesian aggregator of free LLM APIs |
| Coverage | 25 providers, 323 models |
| Features | Searchable directory, fallback chains, rate limit tracking |
| Sources | freellm.net, mnfst/awesome-free-llm-apis, models.dev, openrouter.ai |

## 4. LLM7.io (llm7.io)

| Field | Value |
|---|---|
| Type | API gateway with free tier |
| Anonymous Access | Yes (no key needed for turbo models) |
| Token Limit | Free token from token.llm7.io raises limits |
| Models | 7 free models |

## 5. Free Way (GoDiao/Free-Way)

| Field | Value |
|---|---|
| GitHub | github.com/GoDiao/Free-Way |
| Description | Free Claude Code, Codex, OpenCode, Cline via 14+ free LLM providers |
| Compatibility | OpenAI & Anthropic compatible |
| Features | Single gateway, fallback chains |

## 6. Free-LLM Atlas (happyyboxx/free-llm-atlas)

| Field | Value |
|---|---|
| GitHub | github.com/happyyboxx/free-llm-atlas |
| Description | 46+ free LLM API platforms with automated probing |
| Features | Structured data, gateway configs |

## 7. Other Notable Trackers

| Site | Focus | Update Frequency |
|---|---|---|
| **Kilo Code Leaderboard** | Coding model rankings | Real-time |
| **BenchLM.ai** | Pricing trends | Monthly |
| **PricePerToken.com** | Pricing comparison | Daily |
| **LLMReference** | Model specs & pricing | Weekly |
| **free-llm-api-watch** (GitHub) | Free tier tracker | Daily commits |
| **nejib1/Free-LLM** | Directory of free APIs | Daily sync |

## Free Model Families (by availability)

From FreeLLMAPI's 2026 state report, the most-available free model families:

| Model Family | Free Providers | Notes |
|---|---|---|
| **Llama** | 12 providers | Meta Llama 4, 3.1, 3.2 series |
| **Qwen** | 10 providers | Qwen 3.6, 3.7, 3.8, 3.5 series |
| **Gemma** | 10 providers | Gemma 2, 3, 4 series |
| **GPT-OSS** | 8 providers | OpenAI open-source, 120B/20B |
| **Nemotron** | 8 providers | NVIDIA, free via NIM & OpenRouter |
| **Mistral** | 7 providers | Mistral Small, Mixtral variants |
| **DeepSeek** | 6 providers | V3, R1, V4 Flash/Pro |
| **GLM** | 6 providers | Z.ai GLM 5.x, 4.x series |
| **Kimi** | 4 providers | Moonshot K2, K3, K2.7-Code |
| **MiniMax** | 3 providers | M2, M2.5, M3 series |

## Notes

- **FreeLLMAPI** and **Free-LLM Atlas** are the most comprehensive aggregators
- **Free-LLM API Watch** (GitHub) provides machine-readable JSON tracking
- Most free tiers are rate-limited (by RPM/RPD) rather than credit-based
- Kilo Code's free models update within 60 seconds via their live catalog
