# System Report: LLM Infrastructure Scan - EvaBot

**Scan timestamp:** 2026-09-09T05:09:55.514727+00:00  
**Server:** EvaBot Agent VM (europe-west3-a, 100.66.98.4)  
**Active GCP account:** `evabot.online@gmail.com`  
**Active GCP project:** `evabot-agent-server`  

## 1. Google Cloud Platform

| Project ID | Name | Project Number | Billing | Services |
|---|---|---|---|---|
| gen-lang-client-0091776451 | Default Gemini Project | 853103212819 | disabled | 0 enabled |
| evabot-agent-server | evabot-agent-server | 873069440066 | enabled | 0 enabled |

## 2. Local Backend (http://127.0.0.1:8000)

**Total models in catalog:** 56  
**Endpoint:** `/api/models`

| ID | Provider | Tier | Context | Output |
|---|---|---|---|---|
| gemini-3.8-flash | Google DeepMind | Free Quota + Paid | 1048576 | 8192 |
| gemini-3.1-pro | Google DeepMind | Free Quota + Paid | 2097152 | 8192 |
| gemini-3.1-flash | Google DeepMind | Free Quota + Paid | 1048576 | 8192 |
| gemini-2.5-flash | Google DeepMind | Free Quota + Paid | 1048576 | 8192 |
| gemini-2.5-pro | Google DeepMind | Free Quota + Paid | 2097152 | 8192 |
| gemini-2.0-flash | Google DeepMind | Free Quota + Paid | 1048576 | 8192 |
| gemini-2.0-flash-lite | Google DeepMind | Free Quota + Paid | 1048576 | 8192 |
| gemini-2.0-flash-thinking-exp | Google DeepMind | Free Quota + Paid | 1048576 | 8192 |
| gemini-1.5-pro | Google DeepMind | Free Quota + Paid | 2097152 | 8192 |
| gemini-1.5-flash | Google DeepMind | Free Quota + Paid | 1048576 | 8192 |
| gemini-1.5-flash-8b | Google DeepMind | Free Quota + Paid | 1048576 | 8192 |
| gemma-2-27b-it | Google DeepMind | Open Weights | 8192 | 4096 |
| gemma-2-9b-it | Google DeepMind | Open Weights | 8192 | 4096 |
| gemma-2-2b-it | Google DeepMind | Open Weights | 8192 | 4096 |
| codegemma-7b-it | Google DeepMind | Open Weights | 8192 | 4096 |
| codegemma-2b | Google DeepMind | Open Weights | 8192 | 2048 |
| recurrentgemma-2b-it | Google DeepMind | Open Weights | 8192 | 4096 |
| text-embedding-004 | Google DeepMind | Free Quota + Paid | 2048 | 768 |
| deepseek/deepseek-r1:free | OpenRouter | 100% Free Community | 64000 | 8192 |
| meta-llama/llama-3.3-70b-instruct:free | OpenRouter | 100% Free Community | 128000 | 4096 |
| meta-llama/llama-3.3-70b:free | OpenRouter | 100% Free Community | 128000 | 4096 |
| google/gemini-2.0-flash-exp:free | OpenRouter | 100% Free Community | 1048576 | 8192 |
| qwen/qwen-2.5-coder-32b-instruct:free | OpenRouter | 100% Free Community | 128000 | 8192 |
| mistralai/mistral-7b-instruct:free | OpenRouter | 100% Free Community | 32768 | 4096 |
| google/gemini-2.0-pro-exp-02-05:free | OpenRouter | 100% Free Community | 2097152 | 8192 |
| microsoft/phi-3-medium-128k-instruct:free | OpenRouter | 100% Free Community | 128000 | 4096 |
| anthropic/claude-3.7-sonnet | OpenRouter | OpenRouter Paid | 200000 | 8192 |
| anthropic/claude-3.5-sonnet | OpenRouter | OpenRouter Paid | 200000 | 8192 |
| anthropic/claude-3.5-haiku | OpenRouter | OpenRouter Paid | 200000 | 8192 |
| openai/o3-mini | OpenRouter | OpenRouter Paid | 200000 | 100000 |
| openai/o1 | OpenRouter | OpenRouter Paid | 200000 | 100000 |
| openai/gpt-4o | OpenRouter | OpenRouter Paid | 128000 | 16384 |
| openai/gpt-4o-mini | OpenRouter | OpenRouter Paid | 128000 | 16384 |
| deepseek/deepseek-r1 | OpenRouter | OpenRouter Paid | 64000 | 8192 |
| qwen/qwen-2.5-coder-32b-instruct | OpenRouter | OpenRouter Paid | 128000 | 8192 |
| meta-llama/llama-3.1-405b-instruct | OpenRouter | OpenRouter Paid | 128000 | 4096 |
| mistralai/codestral-2501 | OpenRouter | OpenRouter Paid | 256000 | 8192 |
| x-ai/grok-2-1212 | OpenRouter | OpenRouter Paid | 131072 | 4096 |
| cohere/command-r-plus-08-2024 | OpenRouter | OpenRouter Paid | 128000 | 4096 |
| openrouter/deepseek-chat | OpenRouter | OpenRouter Paid | 64000 | 8192 |
| claude-3-7-sonnet | Anthropic | Vertex AI Enterprise | 200000 | 8192 |
| claude-3-5-sonnet | Anthropic | Vertex AI Enterprise | 200000 | 8192 |
| claude-3-5-haiku | Anthropic | Vertex AI Enterprise | 200000 | 8192 |
| llama-3.3-70b-instruct | Meta | Vertex AI Enterprise | 128000 | 4096 |
| llama-3.2-90b-vision-instruct | Meta | Vertex AI Enterprise | 128000 | 4096 |
| llama-3.1-405b-instruct | Meta | Vertex AI Enterprise | 128000 | 4096 |
| mistral-large-2411 | Mistral AI | Vertex AI Enterprise | 128000 | 4096 |
| codestral-2501 | Mistral AI | Vertex AI Enterprise | 256000 | 4096 |
| deepseek-r1 | DeepSeek | Open Weights | 64000 | 8192 |
| jamba-1.5-large | AI21 Labs | Vertex AI Enterprise | 256000 | 4096 |
| command-r-plus | Cohere | Vertex AI Enterprise | 128000 | 4096 |
| omniroute/gemini-2.5-pro | OmniRoute | OmniRoute Daemon | 2097152 | 8192 |
| omniroute/deepseek-r1 | OmniRoute | OmniRoute Daemon | 64000 | 8192 |
| omniroute/claude-3.5-sonnet | OmniRoute | OmniRoute Daemon | 200000 | 8192 |
| opencode/go-coder-32b | OpenCode AI | OpenCode Platform | 64000 | 8192 |
| opencode/go-fast | OpenCode AI | OpenCode Platform | 32768 | 4096 |

## 3. OmniRoute daemon (LiteLLM proxy)

**Endpoint:** http://127.0.0.1:20128/v1  
**Routes:** 35

| ID |
|---|
| omni/gemini-3.5-flash |
| omni/gemini-3.6-flash |
| omni/gemini-3.7-flash |
| omni/gemini-3.8-flash |
| omni/gemini-3.1-pro |
| omni/cf-gpt-oss-120b |
| omni/cf-gpt-oss-20b |
| omni/cf-llama-3.3-70b |
| omni/cf-gemma-4-26b |
| omni/cf-nemotron-3-120b |
| omni/cf-llama-4-scout |
| omni/cf-qwen2.5-coder-32b |
| omni/cf-mistral-small-3.1 |
| omni/groq-gpt-oss-120b |
| omni/groq-gpt-oss-20b |
| omni/groq-compound |
| omni/groq-compound-mini |
| omni/groq-qwen3.8-27b |
| omni/groq-qwen3.6-27b |
| omni/zai-glm-5.3-flash |
| omni/zai-glm-4.5-air |
| omni/or-nemotron-3.5-lightning |
| omni/or-nemotron-3-ultra-550b |
| omni/or-nemotron-3-super-120b |
| omni/or-nemotron-3-nano-omni |
| omni/or-gemma-4-31b |
| omni/or-gemma-4-26b |
| omni/or-ling-3.0-flash-sante |
| omni/or-ling-3.0-flash-fin |
| omni/or-laguna-s-2.1 |
| omni/or-laguna-xs-2.1 |
| omni/or-north-mini-code |
| omni/or-dots-3-note |
| omni/or-lfm-2.5 |
| omni/mistral-codestral |

## 4. OpenRouter API

**Total models:** 431  
**Free:** 21  
**Paid:** 410

### Free models

| ID | Context | Input $ | Output $ |
|---|---|---|---|
| nex-agi/nex-n2.5-mini:free | 262144 | 0 | 0 |
| nex-agi/nex-n2.5-pro:free | 262144 | 0 | 0 |
| inclusionai/ling-3.0-flash-sante:free | 262144 | 0 | 0 |
| inclusionai/ling-3.0-flash-fin:free | 262144 | 0 | 0 |
| dots-studio/dots-3-note-preview:free | 512000 | 0 | 0 |
| liquid/lfm-2.5-2.6b:free | 65536 | 0 | 0 |
| nvidia/nemotron-3.5-lightning:free | 1000000 | 0 | 0 |
| thinkingmachines/inkling-small:free | 1048576 | 0 | 0 |
| poolside/laguna-s-2.1:free | 262144 | 0 | 0 |
| thinkingmachines/inkling:free | 1048576 | 0 | 0 |
| poolside/laguna-xs-2.1:free | 262144 | 0 | 0 |
| cohere/north-mini-code:free | 256000 | 0 | 0 |
| nvidia/nemotron-3.5-content-safety:free | 128000 | 0 | 0 |
| nvidia/nemotron-3-ultra-550b-a55b:free | 1000000 | 0 | 0 |
| nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free | 256000 | 0 | 0 |
| google/gemma-4-26b-a4b-it:free | 262144 | 0 | 0 |
| google/gemma-4-31b-it:free | 262144 | 0 | 0 |
| google/lyria-3-pro-preview | 1048576 | 0 | 0 |
| google/lyria-3-clip-preview | 1048576 | 0 | 0 |
| nvidia/nemotron-3-super-120b-a12b:free | 262144 | 0 | 0 |
| openrouter/free | 200000 | 0 | 0 |

### Paid models (first 20)

| ID | Context | Input $ | Output $ |
|---|---|---|---|
| inception/mercury-2.5 | 260000 | 0.00000004 | 0.00000015 |
| openai/gpt-6-astra | 1050000 | 0.00001 | 0.00005 |
| openai/gpt-6-astra:batch | 1050000 | 0.000005 | 0.000025 |
| openai/gpt-6-astra-pro | 1050000 | 0.00001 | 0.00005 |
| openai/gpt-6-astra-pro:batch | 1050000 | 0.000005 | 0.000025 |
| qwen/qwen3.8-max-0902 | 1000000 | 0.000002 | 0.000006 |
| meta/muse-spark-1.3-contributor | 1048576 | 0.0000001 | 0.0000002 |
| meta/muse-spark-1.3 | 1048576 | 0.00000125 | 0.00000425 |
| google/gemini-3.8-flash | 1048576 | 0.00000075 | 0.00000375 |
| google/gemini-3.8-flash:batch | 1048576 | 0.000000375 | 0.000001875 |
| anthropic/claude-fable-5.1 | 1000000 | 0.00001 | 0.00005 |
| anthropic/claude-fable-5.1:batch | 1000000 | 0.000005 | 0.000025 |
| ibm-granite/granite-4.2-8b | 131072 | 0.00000006 | 0.00000025 |
| tencent/hy4-preview | 1048576 | 0.000000834 | 0.000002501 |
| inclusionai/ling-3.0-flash-fin | 262144 | 0.00000006 | 0.00000018 |
| ~z-ai/glm-flash-latest | 1310720 | 0.000000075 | 0.00000025 |
| qwen/qwen3.8-flash | 1000000 | 0.00000015 | 0.00000047 |
| z-ai/glm-5.3-flash | 1310720 | 0.000000075 | 0.00000025 |
| z-ai/glm-5.3-flash:batch | 1048576 | 0.000000075 | 0.00000025 |
| meta/muse-spark-1.2-contributor | 1048576 | 0.0000001 | 0.0000002 |

... and 390 more paid models

## 5. Gemini API (gen-lang project)

**Total models:** 50

| Name | Display | Input Tokens | Output Tokens |
|---|---|---|---|
| models/gemini-2.5-flash | Gemini 2.5 Flash | 1048576 | 65536 |
| models/gemini-2.5-pro | Gemini 2.5 Pro | 1048576 | 65536 |
| models/gemini-2.5-flash-preview-tts | Gemini 2.5 Flash Preview TTS | 8192 | 16384 |
| models/gemini-2.5-pro-preview-tts | Gemini 2.5 Pro Preview TTS | 8192 | 16384 |
| models/gemma-4-26b-a4b-it | Gemma 4 26B A4B IT | 262144 | 32768 |
| models/gemma-4-31b-it | Gemma 4 31B IT | 262144 | 32768 |
| models/gemini-flash-latest | Gemini Flash Latest | 1048576 | 65536 |
| models/gemini-flash-lite-latest | Gemini Flash-Lite Latest | 1048576 | 65536 |
| models/gemini-pro-latest | Gemini Pro Latest | 1048576 | 65536 |
| models/gemini-2.5-flash-lite | Gemini 2.5 Flash-Lite | 1048576 | 65536 |
| models/gemini-2.5-flash-image | Nano Banana | 32768 | 32768 |
| models/gemini-3-flash-preview | Gemini 3 Flash Preview | 1048576 | 65536 |
| models/gemini-3.1-pro-preview | Gemini 3.1 Pro Preview | 1048576 | 65536 |
| models/gemini-3.1-pro-preview-customtools | Gemini 3.1 Pro Preview Custom Tools | 1048576 | 65536 |
| models/gemini-3.1-flash-lite-preview | Gemini 3.1 Flash Lite Preview | 1048576 | 65536 |
| models/gemini-3.1-flash-lite | Gemini 3.1 Flash Lite | 1048576 | 65536 |
| models/gemini-3-pro-image-preview | Nano Banana Pro | 131072 | 32768 |
| models/gemini-3-pro-image | Nano Banana Pro | 131072 | 32768 |
| models/nano-banana-pro-preview | Nano Banana Pro | 131072 | 32768 |
| models/gemini-3.1-flash-image-preview | Nano Banana 2 | 65536 | 65536 |
| models/gemini-3.1-flash-image | Nano Banana 2 | 65536 | 65536 |
| models/gemini-3.1-flash-lite-image | Nano Banana 2 Lite | 65536 | 65536 |
| models/gemini-3.5-flash | Gemini 3.5 Flash | 1048576 | 65536 |
| models/gemini-3.5-flash-lite | Gemini 3.5 Flash Lite | 1048576 | 65536 |
| models/gemini-omni-flash-preview | Gemini Omni Flash Preview | 131072 | 65536 |
| models/gemini-omni-1.1-flash | Gemini Omni 1.1 Flash | 131072 | 65536 |
| models/gemini-3.5-transcribe | Gemini 3.5 Transcribe | 98304 | 32768 |
| models/gemini-3.6-flash | Gemini 3.6 Flash | 1048576 | 65536 |
| models/gemini-3.7-flash | Gemini 3.7 Flash | 1048576 | 65536 |
| models/gemini-3.8-flash | Gemini 3.8 Flash | 1048576 | 65536 |
| models/lyria-3-clip-preview | Lyria 3 Clip Preview | 1048576 | 65536 |
| models/lyria-3-pro-preview | Lyria 3 Pro Preview | 1048576 | 65536 |
| models/lyria-3.5 | Lyria 3.5 | 1048576 | 65536 |
| models/gemini-3.1-flash-tts-preview | Gemini 3.1 Flash TTS Preview | 8192 | 16384 |
| models/gemini-robotics-er-2-preview | Gemini Robotics-ER 2 Preview | 131072 | 65536 |
| models/gemini-2.5-computer-use-preview-10-2025 | Gemini 2.5 Computer Use Preview 10-2025 | 131072 | 65536 |
| models/antigravity-preview-05-2026 | Antigravity Agent Preview | 131072 | 65536 |
| models/deep-research-max-preview-04-2026 | Deep Research Max Preview (Apr-21-2026) | 131072 | 65536 |
| models/deep-research-preview-04-2026 | Deep Research Preview (Apr-21-2026) | 131072 | 65536 |
| models/deep-research-pro-preview-12-2025 | Deep Research Pro Preview (Dec-12-2025) | 131072 | 65536 |
| models/gemini-embedding-001 | Gemini Embedding 001 | 2048 | 1 |
| models/gemini-embedding-2-preview | Gemini Embedding 2 Preview | 8192 | 1 |
| models/gemini-embedding-2 | Gemini Embedding 2 | 8192 | 1 |
| models/aqa | Model that performs Attributed Question Answering. | 7168 | 1024 |
| models/veo-3.1-generate-preview | Veo 3.1 | 480 | 8192 |
| models/veo-3.1-fast-generate-preview | Veo 3.1 fast | 480 | 8192 |
| models/veo-3.1-lite-generate-preview | Veo 3.1 lite | 480 | 8192 |
| models/gemini-3.5-transcribe-live | Gemini 3.5 Transcribe Live | 131072 | 65536 |
| models/gemini-2.5-flash-native-audio-latest | Gemini 2.5 Flash Native Audio Latest | 131072 | 8192 |
| models/gemini-2.5-flash-native-audio-preview-09-2025 | Gemini 2.5 Flash Native Audio Preview 09-2025 | 131072 | 8192 |

## 6. HuggingFace Inference (from config files)

**Models in config:** 272

| ID | Source |
|---|---|
| CohereLabs/aya-expanse-32b | /home/evabot/.config/opencode/opencode.json |
| CohereLabs/aya-vision-32b | /home/evabot/.config/opencode/opencode.json |
| CohereLabs/c4ai-command-a-03-2025 | /home/evabot/.config/opencode/opencode.json |
| CohereLabs/c4ai-command-r-08-2024 | /home/evabot/.config/opencode/opencode.json |
| CohereLabs/c4ai-command-r7b-12-2024 | /home/evabot/.config/opencode/opencode.json |
| CohereLabs/c4ai-command-r7b-arabic-02-2025 | /home/evabot/.config/opencode/opencode.json |
| CohereLabs/command-a-reasoning-08-2025 | /home/evabot/.config/opencode/opencode.json |
| CohereLabs/command-a-translate-08-2025 | /home/evabot/.config/opencode/opencode.json |
| CohereLabs/tiny-aya-earth | /home/evabot/.config/opencode/opencode.json |
| CohereLabs/tiny-aya-fire | /home/evabot/.config/opencode/opencode.json |
| CohereLabs/tiny-aya-global | /home/evabot/.config/opencode/opencode.json |
| CohereLabs/tiny-aya-water | /home/evabot/.config/opencode/opencode.json |
| MiniMaxAI/MiniMax-M1-80k | /home/evabot/.config/opencode/opencode.json |
| MiniMaxAI/MiniMax-M2 | /home/evabot/.config/opencode/opencode.json |
| MiniMaxAI/MiniMax-M2.1 | /home/evabot/.config/opencode/opencode.json |
| MiniMaxAI/MiniMax-M2.5 | /home/evabot/.config/opencode/opencode.json |
| MiniMaxAI/MiniMax-M2.7 | /home/evabot/.config/opencode/opencode.json |
| MiniMaxAI/MiniMax-M3 | /home/evabot/.config/opencode/opencode.json |
| NousResearch/Hermes-3-Llama-3.1-70B | /home/evabot/.config/opencode/opencode.json |
| Qwen/Qwen2.5-72B-Instruct | /home/evabot/.config/opencode/opencode.json |
| Qwen/Qwen2.5-Coder-32B-Instruct | /home/evabot/.config/opencode/opencode.json |
| Qwen/Qwen2.5-Coder-3B-Instruct | /home/evabot/.config/opencode/opencode.json |
| Qwen/Qwen2.5-Coder-7B-Instruct | /home/evabot/.config/opencode/opencode.json |
| Qwen/Qwen2.5-VL-72B-Instruct | /home/evabot/.config/opencode/opencode.json |
| Qwen/Qwen3-14B | /home/evabot/.config/opencode/opencode.json |
| Qwen/Qwen3-235B-A22B | /home/evabot/.config/opencode/opencode.json |
| Qwen/Qwen3-235B-A22B-Instruct-2507 | /home/evabot/.config/opencode/opencode.json |
| Qwen/Qwen3-235B-A22B-Thinking-2507 | /home/evabot/.config/opencode/opencode.json |
| Qwen/Qwen3-30B-A3B | /home/evabot/.config/opencode/opencode.json |
| Qwen/Qwen3-32B | /home/evabot/.config/opencode/opencode.json |

... and 242 more

## 7. Other API Providers

| Provider | Env Var | Configured |
|---|---|---|
| Groq | `GROQ_API_KEY` | No |
| Cerebras | `CEREBRAS_API_KEY` | No |
| Z.ai (GLM) | `ZAI_API_KEY` | No |
| Cloudflare Workers AI | `CLOUDFLARE_AI_KEY` | No |
| Mistral AI | `MISTRAL_API_KEY` | No |
| HuggingFace | `HF_TOKEN` | No |
| OpenCode Platform | `OPENCODE_API_KEY` | No |
| OpenRouter | `OPENROUTER_API_KEY` | Yes |
| Google Gemini | `GEMINI_API_KEY` | Yes |
| OmniRoute | `OMNIROUTE_API_KEY` | Yes |

## 8. Local LLM Services

| Port | Service | Status |
|---|---|---|
| 8080 | vLLM / oobabooga | listening |
| 8000 | Local Backend (FastAPI) | listening |
| 3000 | Frontend (Vite/React) | listening |
| 8090 | Backend Proxy | listening |
| 8101 | MCP / Agent service | listening |
| 8137 | Agent service | listening |
| 20128 | OmniRoute Daemon (LiteLLM) | listening |

## 9. Docker Containers

| Names | Image | Status |
|---|---|---|

## 10. Config Files

### `/var/www/evabot-backend/.env`
- Size: 422 bytes
- API keys found:
  - `GEMINI_API_KEY` = `AQ.Ab8RN...***`
  - `OPENROUTER_API_KEY` = `sk-or-v1...***`
  - `OMNIROUTE_API_KEY` = `omnirout...***`

### `/var/www/evabot-backend/.env.example`
- Size: 1474 bytes
- API keys found:
  - `GEMINI_API_KEY` = `# Defaul...***`
  - `OPENROUTER_API_KEY` = `# HTTP s...***`
  - `OMNIROUTE_API_KEY` = `omnirout...***`
  - `OPENCODE_API_KEY` = `# Telegr...***`
  - `TELEGRAM_BOT_TOKEN` = `# TTS ch...***`

### `/home/evabot/.config/opencode/opencode.json`
- Size: 24915 bytes
- No API keys found

### `/home/evabot/.config/Code/User/mcp.json`
- Size: 3982 bytes
- No API keys found

### `/home/evabot/.config/Claude/claude_desktop_config.json`
- Size: 3982 bytes
- No API keys found

### `/home/evabot/.config/kilo/kilo.jsonc`
- Size: 38210 bytes
- No API keys found

## Summary

| Metric | Count |
|---|---|
| Total models in local catalog | 56 |
| Free / Free-Quota models | 24 |
| Open-Weights models | 7 |
| Paid (pay-per-use) models | 25 |
| OpenRouter free models | 21 |
| OpenRouter paid models | 410 |
| Gemini API models (gen-lang) | 50 |
| OmniRoute routes | 35 |
| HuggingFace models in configs | 272 |
| Local LLM services listening | 7 |
| Docker containers | 0 |
