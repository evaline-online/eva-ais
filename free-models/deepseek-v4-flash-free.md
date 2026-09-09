# DeepSeek V4 Flash (Free via FreeLLMAPI / OpenCode Zen)

| Field | Value |
|---|---|
| **ID** | `deepseek-v4-flash` |
| **Provider** | DeepSeek (via FreeLLMAPI / NavyAI) |
| **Category** | DeepSeek V4 Series |
| **Tier** | Free (within provider free allowances) |
| **Free Tier** | 20 RPM (NavyAI) |
| **Context Window** | 1,000,000 tokens |
| **Max Output** | 384,000 tokens |

## Description

DeepSeek V4 Flash is the lightweight efficiency-optimized variant of DeepSeek V4. With 284B total parameters (13B active), it's designed for fast inference and cost-effective coding tasks.

## Coding Strengths

Fast inference, cost-efficient code generation, good for high-volume coding tasks, supports function calling and tools.

## Pricing (Free)

- **NavyAI:** 20 RPM free
- **HuggingFace Router:** $0.10/mo credit for new users
- **OpenCode Zen:** 200 RPD free

## Configuration

```env
MODEL_ID=deepseek-v4-flash
PROVIDER=DeepSeek via FreeLLMAPI
```
