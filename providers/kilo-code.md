# Kilo Code

Kilo Code is an open-source AI coding agent (VS Code extension, CLI, and Cloud) that provides **500+ models** with zero markup. It offers **14+ free models** (no credit card required for free tier).

## Configuration

| Field | Value |
|---|---|
| Website | https://kilocode.ai |
| API Endpoint | https://app.kilo.ai |
| Env Var | `KILO_API_KEY` |
| Config File | `/home/evabot/.config/kilo/kilo.jsonc` |
| Project | Kilo Code Platform |
| Billing | Free account (no card) + paid hosted inference |
| Status | **14+ models free** |

## Free Models (14+)

All free models are **$0.00/1M tokens** input and output. No credit card required — just create a free Kilo Cloud account.

| # | Model | Provider | Context | KiloBench | Code Rank |
|---|---|---|---|---|---|
| 1 | `minimax/minimax-m2.7` | MiniMax | — | — | #40 |
| 2 | `dots-studio/dots-3-note-preview` | Dots Studio | — | — | #96 |
| 3 | `minimax/minimax-m3` | MiniMax | 1M | 47.6% | #8 |
| 4 | `inclusionai/ling-3.0-flash` | inclusionAI | — | — | #51 |
| 5 | `poolside/laguna-s-2.1` | Poolside | — | — | #48 |
| 6 | `nvidia/nemotron-3-ultra-550b` | NVIDIA | — | 15.5% | #34 |
| 7 | `nexagi/nex-n2-pro` | Nex AGI | — | — | — |
| 8 | `inclusionai/ring-2.6-1t` | inclusionAI | — | — | — |
| 9 | `tencent/hy3` | Tencent | 1M | 47.6% | — |
| 10 | `inclusionai/ling-2.6-1t` | inclusionAI | — | 28.1% | #60 |
| 11 | `inclusionai/ling-2.6-flash` | inclusionAI | — | — | — |
| 12 | `google/gemma-4-26b-a4b-it` | Google | 256K | — | — |
| 13 | `nvidia/nemotron-3.5-lightning` | NVIDIA | — | — | — |
| 14 | `baidu/cobuddy` | Baidu | — | — | — |

## Paid Models

Kilo Code also offers 500+ paid models at provider cost (no markup):

| Model | Provider | Price (USD/1M) |
|---|---|---|
| `openai/gpt-6-astra` | OpenAI | $10.00 in / $50.00 out |
| `anthropic/claude-fable-5.1` | Anthropic | $10.00 in / $91.41/attempt |
| `google/gemini-3.8-flash` | Google | $0.75 in / $112.27/attempt |
| `x-ai/grok-4.6` | xAI | $0.75 in / $33.83/attempt |
| `deepseek/deepseek-v4-pro` | DeepSeek | $1.60 in / $15.91/attempt |

## Notes

- **No KILO_API_KEY configured** in the current environment — free models cannot be tested locally
- Kilo Code provides a free account tier with $0.00/1M token pricing on selected models
- Models are hosted by Kilo Code (not directly accessible via provider APIs)
- The free model list updates every 60 seconds from the live Kilo catalog

## Links

- Free models: https://kilocode.ai/landing/free-models
- Leaderboard: https://kilocode.ai/leaderboard
- Docs: https://kilocode.ai/docs
