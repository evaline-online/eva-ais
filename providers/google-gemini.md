# Google Gemini / Vertex AI

Google DeepMind LLM API and Vertex AI platform models, accessed via the evabot-agent-server project.

## Configuration

| Field | Value |
|---|---|
| API Endpoint | `https://generativelanguage.googleapis.com/v1beta` |
| Env Var | `GEMINI_API_KEY` |
| Config File | `/var/www/evabot-backend/.env` |
| Project | `evabot-agent-server` |
| Billing | enabled |

## Free / Free-Quota Models (from local catalog)

| ID | Context Window | Max Output |
|---|---|---|
| gemini-3.8-flash | 1048576 | 8192 |
| gemini-3.1-pro | 2097152 | 8192 |
| gemini-3.1-flash | 1048576 | 8192 |
| gemini-2.5-flash | 1048576 | 8192 |
| gemini-2.5-pro | 2097152 | 8192 |
| gemini-2.0-flash | 1048576 | 8192 |
| gemini-2.0-flash-lite | 1048576 | 8192 |
| gemini-2.0-flash-thinking-exp | 1048576 | 8192 |
| gemini-1.5-pro | 2097152 | 8192 |
| gemini-1.5-flash | 1048576 | 8192 |
| gemini-1.5-flash-8b | 1048576 | 8192 |
| text-embedding-004 | 2048 | 768 |

## Open-Weights Models

| ID | Context Window | Max Output |
|---|---|---|
| gemma-2-27b-it | 8192 | 4096 |
| gemma-2-9b-it | 8192 | 4096 |
| gemma-2-2b-it | 8192 | 4096 |
| codegemma-7b-it | 8192 | 4096 |
| codegemma-2b | 8192 | 2048 |
| recurrentgemma-2b-it | 8192 | 4096 |
| deepseek-r1 | 64000 | 8192 |
