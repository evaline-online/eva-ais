# Gemini 3.6 Flash (Free via Google AI Studio)

| Field | Value |
|---|---|
| **ID** | `gemini-3.6-flash` |
| **Provider** | Google DeepMind |
| **Category** | Google Gemini (3.x Series) |
| **Tier** | Free Quota + Paid |
| **Free Tier** | 10 RPM, 20 RPD |
| **Context Window** | 1,000,000 tokens |
| **Max Output Tokens** | 8,192+ |
| **Capabilities** | Tools, Vision |

## Description

Gemini 3.6 Flash is a high-efficiency model from Google for coding, agentic workflows, and web/app development. Designed to produce polished outputs with fewer unnecessary edits.

## Coding Strengths

Fast code generation, agentic workflow support, reduced over-engineering in outputs.

## Test Status

- **Status:** ✅ Working (via gen-lang key)
- **HTTP:** 200 OK
- **Response time:** ~2.3s

## Pricing

- **Free:** 10 RPM / 20 RPD (Google AI Studio free tier)
- **Paid:** $0.08/1M input · $0.32/1M output (USD)

## Configuration

```env
MODEL_ID=gemini-3.6-flash
PROVIDER=Google DeepMind
PROTOCOL=google-genai
```
