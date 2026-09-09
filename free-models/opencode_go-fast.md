# OpenCode Go Fast (Low-Latency)

| Field | Value |
|---|---|
| **ID** | `opencode/go-fast` |
| **Provider** | OpenCode AI |
| **Category** | OpenCode Go Platforms |
| **Tier** | OpenCode Platform |
| **Source** | local-backend |
| **Recommended** | No |
| **Context Window** | 32,768 tokens |
| **Max Output Tokens** | 4,096 tokens |
| **Free Tier Status** | 100% Free Quota Available |
| **Free Tier Details** | OpenCode Developer Community Quota ($0.00 / €0.00) |
| **Pricing (USD)** | Input: $0.00 (Dev Tier) / $0.08 (Prod) | Output: $0.00 (Dev Tier) / $0.24 (Prod) |
| **Pricing (EUR)** | Input: €0.00 (Dev Tier) / €0.07 (Prod) | Output: €0.00 (Dev Tier) / €0.22 (Prod) |

## Coding Strengths

Fast auto-complete, short snippet transformations, and inline suggestions.

## Configuration

```env
MODEL_ID=opencode/go-fast
PROVIDER=OpenCode AI
```

## Test Status

- **Status:** FAILED
- **Reason:** `OPENCODE_API_KEY` not configured; backend returns "All connection attempts failed"
- **Free tier:** Dev Tier ($0.00) — requires OpenCode API key to activate
