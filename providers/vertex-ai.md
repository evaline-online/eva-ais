# Vertex AI (Enterprise)

Google Cloud Vertex AI serving Anthropic Claude, Meta Llama, Mistral, Cohere, and DeepSeek models.

## Configuration

| Field | Value |
|---|---|
| API Endpoint | `https://us-central1-aiplatform.googleapis.com` |
| Env Var | `—` |
| Config File | `/var/www/evabot-backend/.env` |
| Project | `evabot-agent-server` |
| Billing | enabled |

## Paid Models (from local catalog)

| ID | Provider | Context Window | Input USD | Output USD |
|---|---|---|---|---|
| claude-3-7-sonnet | Anthropic | 200000 | $3.00 | $15.00 |
| claude-3-5-sonnet | Anthropic | 200000 | $3.00 | $15.00 |
| claude-3-5-haiku | Anthropic | 200000 | $0.80 | $4.00 |
| llama-3.3-70b-instruct | Meta | 128000 | $0.70 | $0.90 |
| llama-3.2-90b-vision-instruct | Meta | 128000 | $0.90 | $1.20 |
| llama-3.1-405b-instruct | Meta | 128000 | $3.50 | $3.50 |
| mistral-large-2411 | Mistral AI | 128000 | $2.00 | $6.00 |
| codestral-2501 | Mistral AI | 256000 | $0.30 | $0.90 |
| jamba-1.5-large | AI21 Labs | 256000 | $2.00 | $8.00 |
| command-r-plus | Cohere | 128000 | $2.50 | $10.00 |
