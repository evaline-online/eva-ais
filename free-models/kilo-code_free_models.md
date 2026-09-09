# Kilo Code Free Models

Kilo Code hosts **14+ active free models** on their platform. No credit card or API key required — just create a free account at [app.kilo.ai](https://app.kilo.ai). All pricing is **$0.00/1M tokens** input and output.

## Free Model Catalog

| # | Model | Provider | Context | KiloBench | Code Rank | Notes |
|---|-------|----------|---------|-----------|-----------|-------|
| 1 | **Hy3 (free)** | Tencent | 1M | 47.6% | — | 295B MoE, 21B active, top-tested free model |
| 2 | **MiniMax M2.7 (free)** | MiniMax | — | — | #40 | Newest (Sep 2026), agentic productivity |
| 3 | **Dots3-Note Preview (free)** | Dots Studio | — | — | #96 | 280B MoE, 16B active, lightest Dots 3 |
| 4 | **MiniMax M3 (free)** | MiniMax | 1M | 47.6% | #8 | Multimodal (text/image/video), long-context |
| 5 | **Ling-3.0-flash (free)** | inclusionAI | — | — | #51 | 124B MoE, 5.1B active, token-efficient |
| 6 | **Laguna S 2.1 (free)** | Poolside | — | — | #48 | 118B total, 8B active, 70.2% Terminal-Bench |
| 7 | **Nemotron 3 Ultra (free)** | NVIDIA | — | 15.5% | #34 | 55B active/550B, hybrid Transformer-Mamba |
| 8 | **Nex-N2-Pro (free)** | Nex AGI | — | — | — | 17B active/397B, Qwen3.5 architecture |
| 9 | **Ring-2.6-1T (free)** | inclusionAI | — | — | — | 1T params, 63B active, thinking model |
| 10 | **Hy3 preview (free)** | Tencent | 1M | — | — | Configurable reasoning (low/high/max) |
| 11 | **Ling-2.6-1T (free)** | inclusionAI | — | 28.1% | #60 | 1T params, fast execution, 7.4B active |
| 12 | **Ling-2.6-flash (free)** | inclusionAI | — | — | — | 104B total, 7.4B active |
| 13 | **Gemma 4 26B A4B (free)** | Google DeepMind | 256K | — | — | 3.8B active params per token (MoE) |
| 14 | **Nemotron 3.5 Lightning (free)** | NVIDIA | — | — | — | Speed-optimized, high throughput |
| 15 | **baidu/cobuddy:free** | Baidu | — | — | — | No benchmark data yet |
| 16 | **free** | Kilo | — | — | — | Generic Kilo free route |

## How to Use

1. Install [Kilo Code](https://kilocode.ai) (VS Code extension or CLI)
2. Create a free Kilo Cloud account (no credit card required)
3. Open the model picker and select any model marked **Free**
4. Switch between free, paid, local, and BYOK models anytime

## Pricing

All free models have **$0.00/1M tokens** for both input and output. These are hosted promotions — availability may change when providers change pricing, but the list updates automatically from the live Kilo catalog every 60 seconds.

## Testing Status

**Cannot test locally** — Kilo Code free models require a Kilo Cloud account and authentication token. No `KILO_API_KEY` is configured in the current environment. The models are documented here from the live Kilo leaderboard at [kilocode.ai/leaderboard](https://kilocode.ai/leaderboard).

## Comparison with OpenCode Free Models

| Platform | Free Models | API Key Required | Free Tier |
|---|---|---|---|
| Kilo Code | 14+ | Free account (no card) | $0.00/1M tokens |
| OpenCode | 2 (`go-fast`, `go-coder-32b`) | `OPENCODE_API_KEY` (not configured) | Dev Tier $0.00 |

## Source

- Kilo Code Free Models: https://kilocode.ai/landing/free-models
- Kilo Leaderboard: https://kilocode.ai/leaderboard
