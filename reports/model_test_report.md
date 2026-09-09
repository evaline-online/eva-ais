# Отчёт тестирования моделей LLM

**Дата:** 2026-09-09 06:08:10 UTC  
**Всего моделей:** 562

## Сводка

| Статус | Количество |
|---|---|
| ✅ Working | 27 |
| ❌ Failed | 524 |
| 🔚 Unavailable | 0 |
| ⏳ Timeout | 0 |
| ❔ Unknown | 0 |

## Бесплатные модели — Working

| ID | Provider | Source | Detail |
|---|---|---|---|
| gemini-3.8-flash | Google DeepMind | local-backend | OK |
| gemini-3-flash-preview | Google DeepMind (gen-lang) | gemini-api-gen-lang | OK |
| gemini-3.1-flash-lite | Google DeepMind (gen-lang) | gemini-api-gen-lang | OK |
| gemini-3.1-flash-lite-preview | Google DeepMind (gen-lang) | gemini-api-gen-lang | OK |
| gemini-3.5-flash-lite | Google DeepMind (gen-lang) | gemini-api-gen-lang | OK |
| gemini-3.5-transcribe | Google DeepMind (gen-lang) | gemini-api-gen-lang | OK |
| gemini-3.6-flash | Google DeepMind (gen-lang) | gemini-api-gen-lang | OK |
| gemini-flash-lite-latest | Google DeepMind (gen-lang) | gemini-api-gen-lang | OK |
| gemini-robotics-er-2-preview | Google DeepMind (gen-lang) | gemini-api-gen-lang | OK |
| gemma-4-26b-a4b-it | Google DeepMind (gen-lang) | gemini-api-gen-lang | OK |
| omni/groq-compound | OmniRoute | omniroute-daemon | **Reasoning**

- The original request was: “Hello, reply with exactly: OK”.  
-  |
| omni/groq-compound-mini | OmniRoute | omniroute-daemon | OK |
| omni/groq-gpt-oss-120b | OmniRoute | omniroute-daemon |  |
| omni/groq-gpt-oss-20b | OmniRoute | omniroute-daemon |  |
| omni/groq-qwen3.6-27b | OmniRoute | omniroute-daemon | <think>
Here's a thinking process:

1.  **Analyze User Input:** |
| omni/groq-qwen3.8-27b | OmniRoute | omniroute-daemon | OK |
| omni/mistral-codestral | OmniRoute | omniroute-daemon | OK |
| omni/or-laguna-s-2.1 | OmniRoute | omniroute-daemon | OK |
| omni/or-nemotron-3-nano-omni | OmniRoute | omniroute-daemon | OK |
| omni/or-nemotron-3-super-120b | OmniRoute | omniroute-daemon | User says: "Hello, reply with exactly: OK". So they want the |
| omni/or-nemotron-3.5-lightning | OmniRoute | omniroute-daemon | Here's a thinking process:

1.  **Analyze User Input:** The |
| nex-agi/nex-n2.5-mini:free | OpenRouter | openrouter-api | OK |
| nex-agi/nex-n2.5-pro:free | OpenRouter | openrouter-api | OK |
| nvidia/nemotron-3-super-120b-a12b:free | OpenRouter | openrouter-api | We need to reply exactly with "OK". No extra whitespace or newline? Probably |
| nvidia/nemotron-3.5-lightning:free | OpenRouter | openrouter-api | Here's a thinking process:

1.  **Analyze User Input:** The |
| openrouter/free | OpenRouter | openrouter-api | Here's a thinking process:

1.  **Analyze User Input:** |
| poolside/laguna-s-2.1:free | OpenRouter | openrouter-api | OK |

## Бесплатные модели — Not Working

| ID | Provider | Status | HTTP | Detail |
|---|---|---|---|---|
| deepseek-r1 | DeepSeek | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| codegemma-2b | Google DeepMind | failed | 404 | {
  "error": {
    "code": 404,
    "message": "models/codegemma-2b is not found for API version v1beta, or is not supported for generateContent. Call |
| codegemma-7b-it | Google DeepMind | failed | 404 | {
  "error": {
    "code": 404,
    "message": "models/codegemma-7b-it is not found for API version v1beta, or is not supported for generateContent. C |
| gemini-1.5-flash | Google DeepMind | failed | 404 | {
  "error": {
    "code": 404,
    "message": "models/gemini-1.5-flash is not found for API version v1beta, or is not supported for generateContent.  |
| gemini-1.5-flash-8b | Google DeepMind | failed | 404 | {
  "error": {
    "code": 404,
    "message": "models/gemini-1.5-flash-8b is not found for API version v1beta, or is not supported for generateConten |
| gemini-1.5-pro | Google DeepMind | failed | 404 | {
  "error": {
    "code": 404,
    "message": "models/gemini-1.5-pro is not found for API version v1beta, or is not supported for generateContent. Ca |
| gemini-2.0-flash | Google DeepMind | failed | 404 | {
  "error": {
    "code": 404,
    "message": "This model models/gemini-2.0-flash is no longer available. Please update your code to use models/gemin |
| gemini-2.0-flash-lite | Google DeepMind | failed | 404 | {
  "error": {
    "code": 404,
    "message": "This model models/gemini-2.0-flash-lite is no longer available. Please update your code to use models/ |
| gemini-2.0-flash-thinking-exp | Google DeepMind | failed | 404 | {
  "error": {
    "code": 404,
    "message": "models/gemini-2.0-flash-thinking-exp is not found for API version v1beta, or is not supported for gene |
| gemini-2.5-flash | Google DeepMind | failed | 404 | {
  "error": {
    "code": 404,
    "message": "This model models/gemini-2.5-flash is no longer available to new users. Please update your code to use |
| gemini-2.5-pro | Google DeepMind | failed | 404 | {
  "error": {
    "code": 404,
    "message": "This model models/gemini-2.5-pro is no longer available to new users. Please update your code to use m |
| gemini-3.1-flash | Google DeepMind | failed | 404 | {
  "error": {
    "code": 404,
    "message": "models/gemini-3.1-flash is not found for API version v1beta, or is not supported for generateContent.  |
| gemini-3.1-pro | Google DeepMind | failed | 404 | {
  "error": {
    "code": 404,
    "message": "models/gemini-3.1-pro is not found for API version v1beta, or is not supported for generateContent. Ca |
| gemma-2-27b-it | Google DeepMind | failed | 404 | {
  "error": {
    "code": 404,
    "message": "models/gemma-2-27b-it is not found for API version v1beta, or is not supported for generateContent. Ca |
| gemma-2-2b-it | Google DeepMind | failed | 404 | {
  "error": {
    "code": 404,
    "message": "models/gemma-2-2b-it is not found for API version v1beta, or is not supported for generateContent. Cal |
| gemma-2-9b-it | Google DeepMind | failed | 404 | {
  "error": {
    "code": 404,
    "message": "models/gemma-2-9b-it is not found for API version v1beta, or is not supported for generateContent. Cal |
| recurrentgemma-2b-it | Google DeepMind | failed | 404 | {
  "error": {
    "code": 404,
    "message": "models/recurrentgemma-2b-it is not found for API version v1beta, or is not supported for generateConte |
| text-embedding-004 | Google DeepMind | failed | 404 | {
  "error": {
    "code": 404,
    "message": "models/text-embedding-004 is not found for API version v1beta, or is not supported for generateContent |
| antigravity-preview-05-2026 | Google DeepMind (gen-lang) | failed | 400 | {
  "error": {
    "code": 400,
    "message": "This model only supports Interactions API.",
    "status": "INVALID_ARGUMENT"
  }
}
 |
| aqa | Google DeepMind (gen-lang) | failed | 404 | {
  "error": {
    "code": 404,
    "message": "models/aqa is not found for API version v1beta, or is not supported for generateContent. Call ModelSer |
| deep-research-max-preview-04-2026 | Google DeepMind (gen-lang) | failed | 400 | {
  "error": {
    "code": 400,
    "message": "This model only supports Interactions API.",
    "status": "INVALID_ARGUMENT"
  }
}
 |
| deep-research-preview-04-2026 | Google DeepMind (gen-lang) | failed | 400 | {
  "error": {
    "code": 400,
    "message": "This model only supports Interactions API.",
    "status": "INVALID_ARGUMENT"
  }
}
 |
| deep-research-pro-preview-12-2025 | Google DeepMind (gen-lang) | failed | 400 | {
  "error": {
    "code": 400,
    "message": "This model only supports Interactions API.",
    "status": "INVALID_ARGUMENT"
  }
}
 |
| gemini-2.5-computer-use-preview-10-2025 | Google DeepMind (gen-lang) | failed | 429 | {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on t |
| gemini-2.5-flash-image | Google DeepMind (gen-lang) | failed | 429 | {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on t |
| gemini-2.5-flash-lite | Google DeepMind (gen-lang) | failed | 404 | {
  "error": {
    "code": 404,
    "message": "This model models/gemini-2.5-flash-lite is no longer available to new users. Please update your code t |
| gemini-2.5-flash-native-audio-latest | Google DeepMind (gen-lang) | failed | 400 | {
  "error": {
    "code": 400,
    "message": "models/gemini-2.5-flash-native-audio-latest only supports real-time bidirectional streaming via WebSoc |
| gemini-2.5-flash-native-audio-preview-09-2025 | Google DeepMind (gen-lang) | failed | 400 | {
  "error": {
    "code": 400,
    "message": "models/gemini-2.5-flash-native-audio-preview-09-2025 only supports real-time bidirectional streaming v |
| gemini-2.5-flash-preview-tts | Google DeepMind (gen-lang) | failed | 400 | {
  "error": {
    "code": 400,
    "message": "The requested combination of response modalities (TEXT) is not supported by the model. models/gemini-2 |
| gemini-2.5-pro-preview-tts | Google DeepMind (gen-lang) | failed | 429 | {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on t |
| gemini-3-pro-image | Google DeepMind (gen-lang) | failed | 429 | {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on t |
| gemini-3-pro-image-preview | Google DeepMind (gen-lang) | failed | 429 | {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on t |
| gemini-3.1-flash-image | Google DeepMind (gen-lang) | failed | 429 | {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on t |
| gemini-3.1-flash-image-preview | Google DeepMind (gen-lang) | failed | 429 | {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on t |
| gemini-3.1-flash-lite-image | Google DeepMind (gen-lang) | failed | 429 | {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on t |
| gemini-3.1-flash-tts-preview | Google DeepMind (gen-lang) | failed | 400 | {
  "error": {
    "code": 400,
    "message": "Request contains an invalid argument.",
    "status": "INVALID_ARGUMENT"
  }
}
 |
| gemini-3.1-pro-preview | Google DeepMind (gen-lang) | failed | 429 | {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on t |
| gemini-3.1-pro-preview-customtools | Google DeepMind (gen-lang) | failed | 429 | {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on t |
| gemini-3.5-flash | Google DeepMind (gen-lang) | failed | 0 | The read operation timed out |
| gemini-3.5-transcribe-live | Google DeepMind (gen-lang) | failed | 400 | {
  "error": {
    "code": 400,
    "message": "models/gemini-3.5-transcribe-live only supports real-time bidirectional streaming via WebSocket (bidiG |
| gemini-3.7-flash | Google DeepMind (gen-lang) | failed | 0 | The read operation timed out |
| gemini-embedding-001 | Google DeepMind (gen-lang) | failed | 404 | {
  "error": {
    "code": 404,
    "message": "models/gemini-embedding-001 is not found for API version v1beta, or is not supported for generateConte |
| gemini-embedding-2 | Google DeepMind (gen-lang) | failed | 404 | {
  "error": {
    "code": 404,
    "message": "models/gemini-embedding-2 is not found for API version v1beta, or is not supported for generateContent |
| gemini-embedding-2-preview | Google DeepMind (gen-lang) | failed | 404 | {
  "error": {
    "code": 404,
    "message": "models/gemini-embedding-2-preview is not found for API version v1beta, or is not supported for generat |
| gemini-flash-latest | Google DeepMind (gen-lang) | failed | 429 | {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on t |
| gemini-omni-1.1-flash | Google DeepMind (gen-lang) | failed | 429 | {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on t |
| gemini-omni-flash-preview | Google DeepMind (gen-lang) | failed | 429 | {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on t |
| gemini-pro-latest | Google DeepMind (gen-lang) | failed | 429 | {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on t |
| gemma-4-31b-it | Google DeepMind (gen-lang) | failed | 0 | The read operation timed out |
| lyria-3-clip-preview | Google DeepMind (gen-lang) | failed | 429 | {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on t |
| lyria-3-pro-preview | Google DeepMind (gen-lang) | failed | 429 | {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on t |
| lyria-3.5 | Google DeepMind (gen-lang) | failed | 429 | {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on t |
| nano-banana-pro-preview | Google DeepMind (gen-lang) | failed | 429 | {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on t |
| veo-3.1-fast-generate-preview | Google DeepMind (gen-lang) | failed | 404 | {
  "error": {
    "code": 404,
    "message": "models/veo-3.1-fast-generate-preview is not found for API version v1beta, or is not supported for gene |
| veo-3.1-generate-preview | Google DeepMind (gen-lang) | failed | 404 | {
  "error": {
    "code": 404,
    "message": "models/veo-3.1-generate-preview is not found for API version v1beta, or is not supported for generateC |
| veo-3.1-lite-generate-preview | Google DeepMind (gen-lang) | failed | 404 | {
  "error": {
    "code": 404,
    "message": "models/veo-3.1-lite-generate-preview is not found for API version v1beta, or is not supported for gene |
| omni/cf-gemma-4-26b | OmniRoute | failed | 429 | {"error":{"message":"litellm.RateLimitError: RateLimitError: OpenAIException - Error code: 429 - {'errors': [{'message': \"AiError: AiError: you have  |
| omni/cf-gpt-oss-120b | OmniRoute | failed | 429 | {"error":{"message":"litellm.RateLimitError: RateLimitError: OpenAIException - Error code: 429 - {'errors': [{'message': \"AiError: AiError: you have  |
| omni/cf-gpt-oss-20b | OmniRoute | failed | 429 | {"error":{"message":"litellm.RateLimitError: RateLimitError: OpenAIException - Error code: 429 - {'errors': [{'message': \"AiError: AiError: you have  |
| omni/cf-llama-3.3-70b | OmniRoute | failed | 429 | {"error":{"message":"litellm.RateLimitError: RateLimitError: OpenAIException - Error code: 429 - {'errors': [{'message': \"AiError: AiError: you have  |
| omni/cf-llama-4-scout | OmniRoute | failed | 429 | {"error":{"message":"litellm.RateLimitError: RateLimitError: OpenAIException - Error code: 429 - {'errors': [{'message': \"AiError: AiError: you have  |
| omni/cf-mistral-small-3.1 | OmniRoute | failed | 429 | {"error":{"message":"litellm.RateLimitError: RateLimitError: OpenAIException - Error code: 429 - {'errors': [{'message': \"AiError: AiError: you have  |
| omni/cf-nemotron-3-120b | OmniRoute | failed | 429 | {"error":{"message":"litellm.RateLimitError: RateLimitError: OpenAIException - Error code: 429 - {'errors': [{'message': \"AiError: AiError: you have  |
| omni/cf-qwen2.5-coder-32b | OmniRoute | failed | 429 | {"error":{"message":"litellm.RateLimitError: RateLimitError: OpenAIException - Error code: 429 - {'errors': [{'message': \"AiError: AiError: you have  |
| omni/gemini-3.1-pro | OmniRoute | failed | 429 | {"error":{"message":"litellm.RateLimitError: litellm.RateLimitError: GeminiException - {\n  \"error\": {\n    \"code\": 429,\n    \"message\": \"Your  |
| omni/gemini-3.5-flash | OmniRoute | failed | 429 | {"error":{"message":"litellm.RateLimitError: litellm.RateLimitError: GeminiException - {\n  \"error\": {\n    \"code\": 429,\n    \"message\": \"Your  |
| omni/gemini-3.6-flash | OmniRoute | failed | 429 | {"error":{"message":"litellm.RateLimitError: litellm.RateLimitError: GeminiException - {\n  \"error\": {\n    \"code\": 429,\n    \"message\": \"Your  |
| omni/gemini-3.7-flash | OmniRoute | failed | 429 | {"error":{"message":"litellm.RateLimitError: litellm.RateLimitError: GeminiException - {\n  \"error\": {\n    \"code\": 429,\n    \"message\": \"Your  |
| omni/gemini-3.8-flash | OmniRoute | failed | 429 | {"error":{"message":"litellm.RateLimitError: litellm.RateLimitError: GeminiException - {\n  \"error\": {\n    \"code\": 429,\n    \"message\": \"Your  |
| omni/or-gemma-4-26b | OmniRoute | failed | 429 | {"error":{"message":"litellm.RateLimitError: RateLimitError: OpenrouterException - {\"error\":{\"message\":\"Provider returned error\",\"code\":429,\" |
| omni/or-gemma-4-31b | OmniRoute | failed | 429 | {"error":{"message":"litellm.RateLimitError: RateLimitError: OpenrouterException - {\"error\":{\"message\":\"Provider returned error\",\"code\":429,\" |
| omni/or-laguna-xs-2.1 | OmniRoute | failed | 0 | timed out |
| omni/or-nemotron-3-ultra-550b | OmniRoute | failed | 0 | timed out |
| omni/zai-glm-4.5-air | OmniRoute | failed | 429 | {"error":{"message":"litellm.RateLimitError: RateLimitError: OpenAIException - Insufficient balance or no resource package. Please recharge.No fallbac |
| omni/zai-glm-5.3-flash | OmniRoute | failed | 429 | {"error":{"message":"litellm.RateLimitError: RateLimitError: OpenAIException - Insufficient balance or no resource package. Please recharge.No fallbac |
| deepseek/deepseek-r1:free | OpenRouter | failed | 404 | {"error":{"message":"This model is unavailable for free. The paid version is available now - use this slug instead: deepseek/deepseek-r1","code":404}, |
| google/gemini-2.0-flash-exp:free | OpenRouter | failed | 404 | {"error":{"message":"No endpoints found for google/gemini-2.0-flash-exp:free.","code":404},"user_id":"user_3HLeY7tYu6sZcGHpPdoSE3u7hUg"} |
| google/gemini-2.0-pro-exp-02-05:free | OpenRouter | failed | 400 | {"error":{"message":"google/gemini-2.0-pro-exp-02-05:free is not a valid model ID","code":400},"user_id":"user_3HLeY7tYu6sZcGHpPdoSE3u7hUg"} |
| google/gemma-4-26b-a4b-it:free | OpenRouter | failed | 429 | Rate limited |
| google/gemma-4-31b-it:free | OpenRouter | failed | 429 | Rate limited |
| google/lyria-3-clip-preview | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| google/lyria-3-pro-preview | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| meta-llama/llama-3.3-70b-instruct:free | OpenRouter | failed | 404 | {"error":{"message":"This model is unavailable for free. The paid version is available now - use this slug instead: meta-llama/llama-3.3-70b-instruct" |
| meta-llama/llama-3.3-70b:free | OpenRouter | failed | 400 | {"error":{"message":"meta-llama/llama-3.3-70b:free is not a valid model ID","code":400},"user_id":"user_3HLeY7tYu6sZcGHpPdoSE3u7hUg"} |
| microsoft/phi-3-medium-128k-instruct:free | OpenRouter | failed | 404 | {"error":{"message":"No endpoints found for microsoft/phi-3-medium-128k-instruct:free.","code":404},"user_id":"user_3HLeY7tYu6sZcGHpPdoSE3u7hUg"} |
| mistralai/mistral-7b-instruct:free | OpenRouter | failed | 404 | {"error":{"message":"No endpoints found for mistralai/mistral-7b-instruct:free.","code":404},"user_id":"user_3HLeY7tYu6sZcGHpPdoSE3u7hUg"} |
| nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free | OpenRouter | failed | 200 | Upstream error from Nvidia: ResourceExhausted: Worker local total request limit reached (16/16) |
| nvidia/nemotron-3-ultra-550b-a55b:free | OpenRouter | failed | 0 | The read operation timed out |
| poolside/laguna-xs-2.1:free | OpenRouter | failed | 429 | Rate limited |
| qwen/qwen-2.5-coder-32b-instruct:free | OpenRouter | failed | 404 | {"error":{"message":"This model is unavailable for free. The paid version is available now - use this slug instead: qwen/qwen-2.5-coder-32b-instruct", |
| thinkingmachines/inkling-small:free | OpenRouter | failed | 403 | {"error":{"message":"thinkingmachines/inkling-small:free is only available on agentic harnesses. Try plugging it into a coding agent or productivity a |
| thinkingmachines/inkling:free | OpenRouter | failed | 403 | {"error":{"message":"thinkingmachines/inkling:free is only available on agentic harnesses. Try plugging it into a coding agent or productivity app lis |

## Платные модели — Working

Ни одна платная модель не прошла тестирование.

## Платные модели — Not Working

| ID | Provider | Status | HTTP | Detail |
|---|---|---|---|---|
| jamba-1.5-large | AI21 Labs | failed | 400 | {"error":{"message":"jamba-1.5-large is not a valid model ID","code":400},"user_id":"user_3HLeY7tYu6sZcGHpPdoSE3u7hUg"} |
| claude-3-5-haiku | Anthropic | failed | 404 | {"error":{"message":"No endpoints found for claude-3-5-haiku.","code":404},"user_id":"user_3HLeY7tYu6sZcGHpPdoSE3u7hUg"} |
| claude-3-5-sonnet | Anthropic | failed | 400 | {"error":{"message":"claude-3-5-sonnet is not a valid model ID","code":400},"user_id":"user_3HLeY7tYu6sZcGHpPdoSE3u7hUg"} |
| claude-3-7-sonnet | Anthropic | failed | 400 | {"error":{"message":"claude-3-7-sonnet is not a valid model ID","code":400},"user_id":"user_3HLeY7tYu6sZcGHpPdoSE3u7hUg"} |
| command-r-plus | Cohere | failed | 404 | {"error":{"message":"No endpoints found for command-r-plus.","code":404},"user_id":"user_3HLeY7tYu6sZcGHpPdoSE3u7hUg"} |
| llama-3.1-405b-instruct | Meta | failed | 404 | {"error":{"message":"No endpoints found for llama-3.1-405b-instruct.","code":404},"user_id":"user_3HLeY7tYu6sZcGHpPdoSE3u7hUg"} |
| llama-3.2-90b-vision-instruct | Meta | failed | 404 | {"error":{"message":"No endpoints found for llama-3.2-90b-vision-instruct.","code":404},"user_id":"user_3HLeY7tYu6sZcGHpPdoSE3u7hUg"} |
| llama-3.3-70b-instruct | Meta | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| codestral-2501 | Mistral AI | failed | 404 | {"error":{"message":"No endpoints found for codestral-2501.","code":404},"user_id":"user_3HLeY7tYu6sZcGHpPdoSE3u7hUg"} |
| mistral-large-2411 | Mistral AI | failed | 404 | {"error":{"message":"No endpoints found for mistral-large-2411.","code":404},"user_id":"user_3HLeY7tYu6sZcGHpPdoSE3u7hUg"} |
| omniroute/claude-3.5-sonnet | OmniRoute | failed | 400 | {"error":{"message":"/chat/completions: Invalid model name passed in model=omniroute/claude-3.5-sonnet. Call `/v1/models` to view available models for |
| omniroute/deepseek-r1 | OmniRoute | failed | 400 | {"error":{"message":"/chat/completions: Invalid model name passed in model=omniroute/deepseek-r1. Call `/v1/models` to view available models for your  |
| omniroute/gemini-2.5-pro | OmniRoute | failed | 400 | {"error":{"message":"/chat/completions: Invalid model name passed in model=omniroute/gemini-2.5-pro. Call `/v1/models` to view available models for yo |
| opencode/go-coder-32b | OpenCode AI | failed | 400 | {"error":{"message":"opencode/go-coder-32b is not a valid model ID","code":400},"user_id":"user_3HLeY7tYu6sZcGHpPdoSE3u7hUg"} |
| opencode/go-fast | OpenCode AI | failed | 400 | {"error":{"message":"opencode/go-fast is not a valid model ID","code":400},"user_id":"user_3HLeY7tYu6sZcGHpPdoSE3u7hUg"} |
| aion-labs/aion-2.0 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| aion-labs/aion-3.0 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| aion-labs/aion-3.0-mini | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| aion-labs/aion-rp-llama-3.1-8b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| amazon/nova-2-lite-v1 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| amazon/nova-lite-v1 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| amazon/nova-micro-v1 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| amazon/nova-premier-v1 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| amazon/nova-pro-v1 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| anthracite-org/magnum-v4-72b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| anthropic/claude-3-haiku | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| anthropic/claude-3.5-haiku | OpenRouter | failed | 404 | {"error":{"message":"No endpoints found for anthropic/claude-3.5-haiku.","code":404},"user_id":"user_3HLeY7tYu6sZcGHpPdoSE3u7hUg"} |
| anthropic/claude-3.5-sonnet | OpenRouter | failed | 404 | {"error":{"message":"No endpoints found for anthropic/claude-3.5-sonnet.","code":404},"user_id":"user_3HLeY7tYu6sZcGHpPdoSE3u7hUg"} |
| anthropic/claude-3.7-sonnet | OpenRouter | failed | 404 | {"error":{"message":"No endpoints found for anthropic/claude-3.7-sonnet.","code":404},"user_id":"user_3HLeY7tYu6sZcGHpPdoSE3u7hUg"} |
| anthropic/claude-fable-5 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| anthropic/claude-fable-5.1 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| anthropic/claude-fable-5.1:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| anthropic/claude-fable-5:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| anthropic/claude-haiku-4.5 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| anthropic/claude-haiku-4.5:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| anthropic/claude-opus-4 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| anthropic/claude-opus-4.1 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| anthropic/claude-opus-4.1:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| anthropic/claude-opus-4.5 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| anthropic/claude-opus-4.5:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| anthropic/claude-opus-4.6 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| anthropic/claude-opus-4.6:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| anthropic/claude-opus-4.7 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| anthropic/claude-opus-4.7:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| anthropic/claude-opus-4.8 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| anthropic/claude-opus-4.8:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| anthropic/claude-opus-5 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| anthropic/claude-opus-5:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| anthropic/claude-sonnet-4 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| anthropic/claude-sonnet-4.5 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| anthropic/claude-sonnet-4.5:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| anthropic/claude-sonnet-4.6 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| anthropic/claude-sonnet-4.6:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| anthropic/claude-sonnet-5 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| anthropic/claude-sonnet-5:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| arcee-ai/trinity-large-thinking | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| baidu/ernie-4.5-vl-424b-a47b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| bytedance-seed/seed-1.6 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| bytedance-seed/seed-1.6-flash | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| bytedance-seed/seed-2-1-turbo | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| bytedance-seed/seed-2.0-code | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| bytedance-seed/seed-2.0-lite | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| bytedance-seed/seed-2.0-mini | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| bytedance/ui-tars-1.5-7b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| cognitivecomputations/dolphin-mistral-24b-venice-edition | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| cohere/command-a | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| cohere/command-r-08-2024 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| cohere/command-r-plus-08-2024 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| cohere/command-r7b-12-2024 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| deepseek/deepseek-chat | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| deepseek/deepseek-chat-v3-0324 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| deepseek/deepseek-chat-v3.1 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| deepseek/deepseek-r1 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| deepseek/deepseek-r1-0528 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| deepseek/deepseek-r1-distill-llama-70b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| deepseek/deepseek-v3.1-terminus | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| deepseek/deepseek-v3.2 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| deepseek/deepseek-v3.2-exp | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| deepseek/deepseek-v4-flash | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| deepseek/deepseek-v4-flash-0731 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| deepseek/deepseek-v4-flash-0731:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| deepseek/deepseek-v4-flash-vision-exp | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| deepseek/deepseek-v4-flash-vision-exp:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| deepseek/deepseek-v4-pro | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| deepseek/deepseek-v4-pro-0813 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| deepseek/deepseek-v4-pro-0813:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| google/gemini-2.5-flash | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| google/gemini-2.5-flash-image | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| google/gemini-2.5-flash-lite | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| google/gemini-2.5-flash-lite:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| google/gemini-2.5-flash:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| google/gemini-2.5-pro | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| google/gemini-2.5-pro-preview | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| google/gemini-2.5-pro-preview-05-06 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| google/gemini-2.5-pro:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| google/gemini-3-flash-preview | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| google/gemini-3-flash-preview:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| google/gemini-3-pro-image | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| google/gemini-3-pro-image-preview | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| google/gemini-3.1-flash-image | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| google/gemini-3.1-flash-image-preview | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| google/gemini-3.1-flash-lite | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| google/gemini-3.1-flash-lite-image | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| google/gemini-3.1-flash-lite-preview | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| google/gemini-3.1-flash-lite:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| google/gemini-3.1-pro-preview | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| google/gemini-3.1-pro-preview-customtools | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| google/gemini-3.1-pro-preview:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| google/gemini-3.5-flash | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| google/gemini-3.5-flash-lite | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| google/gemini-3.5-flash-lite:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| google/gemini-3.5-flash:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| google/gemini-3.6-flash | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| google/gemini-3.6-flash:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| google/gemini-3.7-flash | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| google/gemini-3.7-flash:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| google/gemini-3.8-flash | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| google/gemini-3.8-flash:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| google/gemma-2-27b-it | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| google/gemma-3-12b-it | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| google/gemma-3-27b-it | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| google/gemma-3-4b-it | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| google/gemma-4-26b-a4b-it | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| google/gemma-4-31b-it | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| google/gemma-4-31b-it:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| gryphe/mythomax-l2-13b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| ibm-granite/granite-4.0-h-micro | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| ibm-granite/granite-4.2-8b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| inception/mercury-2 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| inception/mercury-2.5 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| inclusionai/ling-3.0-flash | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| inclusionai/ling-3.0-flash-fin | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| kwaipilot/kat-coder-pro-v2 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| kwaipilot/kat-coder-pro-v2.5 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| mancer/weaver | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| meituan/longcat-2.0 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| meta-llama/llama-3.1-405b-instruct | OpenRouter | failed | 404 | {"error":{"message":"No endpoints found for meta-llama/llama-3.1-405b-instruct.","code":404},"user_id":"user_3HLeY7tYu6sZcGHpPdoSE3u7hUg"} |
| meta-llama/llama-3.1-70b-instruct | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| meta-llama/llama-3.1-8b-instruct | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| meta-llama/llama-3.2-1b-instruct | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| meta-llama/llama-3.2-3b-instruct | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| meta-llama/llama-3.3-70b-instruct | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| meta-llama/llama-4-maverick | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| meta-llama/llama-4-scout | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| meta-llama/llama-guard-4-12b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| meta/muse-glimmer-30b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| meta/muse-glimmer-30b:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| meta/muse-spark-1.1 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| meta/muse-spark-1.2 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| meta/muse-spark-1.2-contributor | OpenRouter | failed | 404 | {"error":{"message":"0 endpoints out of 1 requested are available matching your guardrail restrictions and data policy. We removed them for the follow |
| meta/muse-spark-1.3 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| meta/muse-spark-1.3-contributor | OpenRouter | failed | 404 | {"error":{"message":"0 endpoints out of 1 requested are available matching your guardrail restrictions and data policy. We removed them for the follow |
| microsoft/phi-4 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| microsoft/wizardlm-2-8x22b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| minimax/minimax-01 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| minimax/minimax-m1 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| minimax/minimax-m2 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| minimax/minimax-m2-her | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| minimax/minimax-m2.1 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| minimax/minimax-m2.5 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| minimax/minimax-m2.7 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| minimax/minimax-m3 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| minimax/minimax-m3:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| mistralai/codestral-2501 | OpenRouter | failed | 404 | {"error":{"message":"No endpoints found for mistralai/codestral-2501.","code":404},"user_id":"user_3HLeY7tYu6sZcGHpPdoSE3u7hUg"} |
| mistralai/codestral-2508 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| mistralai/devstral-2512 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| mistralai/ministral-14b-2512 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| mistralai/ministral-3b-2512 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| mistralai/ministral-8b-2512 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| mistralai/mistral-large | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| mistralai/mistral-large-2407 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| mistralai/mistral-large-2512 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| mistralai/mistral-medium-3 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| mistralai/mistral-medium-3-5 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| mistralai/mistral-medium-3-5:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| mistralai/mistral-medium-3.1 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| mistralai/mistral-nemo | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| mistralai/mistral-saba | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| mistralai/mistral-small-24b-instruct-2501 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| mistralai/mistral-small-2603 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| mistralai/mistral-small-3.1-24b-instruct | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| mistralai/mistral-small-3.2-24b-instruct | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| mistralai/mixtral-8x22b-instruct | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| mistralai/voxtral-small-24b-2507 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| moonshotai/kimi-k2 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| moonshotai/kimi-k2-0905 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| moonshotai/kimi-k2-thinking | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| moonshotai/kimi-k2.5 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| moonshotai/kimi-k2.6 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| moonshotai/kimi-k2.7-code | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| moonshotai/kimi-k3 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| moonshotai/kimi-k3:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| morph/morph-v3-fast | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| morph/morph-v3-large | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| nousresearch/hermes-3-llama-3.1-405b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| nousresearch/hermes-3-llama-3.1-70b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| nousresearch/hermes-4-405b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| nousresearch/hermes-4-70b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| nvidia/nemotron-3-nano-30b-a3b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| nvidia/nemotron-3-super-120b-a12b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| nvidia/nemotron-3-ultra-550b-a55b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| nvidia/nemotron-3.5-content-safety | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| nvidia/nemotron-3.5-lightning | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-3.5-turbo | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-3.5-turbo-0613 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-3.5-turbo-16k | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-3.5-turbo-instruct | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-3.5-turbo:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| openai/gpt-4 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-4-turbo | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-4-turbo-preview | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-4-turbo:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| openai/gpt-4.1 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-4.1-mini | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-4.1-mini:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| openai/gpt-4.1-nano | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-4.1-nano:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| openai/gpt-4.1:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| openai/gpt-4o | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-4o-2024-05-13 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-4o-2024-08-06 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-4o-2024-11-20 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-4o-mini | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-4o-mini-2024-07-18 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-4o-mini:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| openai/gpt-4o:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| openai/gpt-5 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-5-image | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-5-image-mini | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-5-mini | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-5-mini:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| openai/gpt-5-nano | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-5-nano:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| openai/gpt-5-pro | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-5-pro:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| openai/gpt-5.1 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-5.1-codex | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-5.1-codex-max | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-5.1-codex-mini | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-5.1:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| openai/gpt-5.2 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-5.2-chat | OpenRouter | failed | 404 | {"error":{"message":"No endpoints found for openai/gpt-5.2-chat.","code":404,"metadata":{"routing_funnel":[{"step":"Initial Endpoints","endpoint_count |
| openai/gpt-5.2-codex | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-5.2-pro | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-5.2-pro:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| openai/gpt-5.2:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| openai/gpt-5.3-codex | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-5.4 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-5.4-image-2 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-5.4-mini | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-5.4-mini:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| openai/gpt-5.4-nano | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-5.4-nano:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| openai/gpt-5.4-pro | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-5.4-pro:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| openai/gpt-5.4:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| openai/gpt-5.5 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-5.5-pro | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-5.5-pro:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| openai/gpt-5.5:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| openai/gpt-5.6-luna | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-5.6-luna-pro | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-5.6-luna-pro:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| openai/gpt-5.6-luna:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| openai/gpt-5.6-sol | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-5.6-sol-pro | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-5.6-sol-pro:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| openai/gpt-5.6-sol:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| openai/gpt-5.6-terra | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-5.6-terra-pro | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-5.6-terra-pro:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| openai/gpt-5.6-terra:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| openai/gpt-5:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| openai/gpt-6-astra | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-6-astra-pro | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-6-astra-pro:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| openai/gpt-6-astra:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| openai/gpt-audio | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-audio-mini | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-chat-latest | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-oss-120b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-oss-120b:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| openai/gpt-oss-20b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/gpt-oss-20b:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| openai/gpt-oss-safeguard-20b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/o1 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/o1-pro | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/o3 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/o3-mini | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/o3-mini-high | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/o3-mini:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| openai/o3-pro | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/o3:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| openai/o4-mini | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/o4-mini-high | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openai/o4-mini:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| openrouter/auto | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openrouter/auto-beta | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openrouter/bodybuilder | OpenRouter | failed | 404 | {"error":{"message":"No endpoints available for openrouter/bodybuilder","code":404}} |
| openrouter/deepseek-chat | OpenRouter | failed | 400 | {"error":{"message":"openrouter/deepseek-chat is not a valid model ID","code":400},"user_id":"user_3HLeY7tYu6sZcGHpPdoSE3u7hUg"} |
| openrouter/fusion | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| openrouter/pareto-code | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| perceptron/perceptron-mk1 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| perplexity/sonar | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| perplexity/sonar-deep-research | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| perplexity/sonar-pro | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| perplexity/sonar-pro-search | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| perplexity/sonar-reasoning-pro | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| poolside/laguna-s-2.1 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| poolside/laguna-xs-2.1 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen-2.5-72b-instruct | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen-2.5-7b-instruct | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen-2.5-coder-32b-instruct | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen-plus | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen-plus-2025-07-28 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen2.5-vl-72b-instruct | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3-14b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3-235b-a22b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3-235b-a22b-2507 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3-235b-a22b-thinking-2507 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3-30b-a3b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3-30b-a3b-instruct-2507 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3-30b-a3b-thinking-2507 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3-32b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3-8b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3-coder | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3-coder-30b-a3b-instruct | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3-coder-flash | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3-coder-next | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3-coder-plus | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3-max | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3-max-thinking | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3-next-80b-a3b-instruct | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3-next-80b-a3b-thinking | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3-vl-235b-a22b-instruct | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3-vl-235b-a22b-thinking | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3-vl-30b-a3b-instruct | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3-vl-30b-a3b-thinking | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3-vl-32b-instruct | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3-vl-8b-instruct | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3-vl-8b-thinking | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3.5-122b-a10b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3.5-27b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3.5-35b-a3b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3.5-397b-a17b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3.5-9b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3.5-9b:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| qwen/qwen3.5-flash-02-23 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3.5-plus-02-15 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3.5-plus-20260420 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3.6-27b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3.6-35b-a3b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3.6-flash | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3.6-max-preview | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3.6-plus | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3.7-flash | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3.7-max | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3.7-plus | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3.8-2.4t-a95b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3.8-2.4t-a95b:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| qwen/qwen3.8-27b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3.8-flash | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| qwen/qwen3.8-max-0902 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| rekaai/reka-edge | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| rekaai/reka-flash-3 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| relace/relace-apply-3 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| relace/relace-search | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| sakana/fugu-ultra | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| sakana/sakana-namazu | OpenRouter | failed | 404 | {"error":{"message":"0 endpoints out of 1 requested are available matching your guardrail restrictions and data policy. We removed them for the follow |
| sao10k/l3-lunaris-8b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| sao10k/l3.1-euryale-70b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| sao10k/l3.3-euryale-70b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| stepfun/step-3.5-flash | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| stepfun/step-3.7-flash | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| tencent/hunyuan-a13b-instruct | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| tencent/hy-mt2-1.8b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| tencent/hy-mt2-30b-a3b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| tencent/hy-mt2-7b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| tencent/hy3 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| tencent/hy3-preview | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| tencent/hy4-preview | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| thedrummer/cydonia-24b-v4.1 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| thedrummer/skyfall-36b-v2 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| thedrummer/unslopnemo-12b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| thinkingmachines/inkling | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| thinkingmachines/inkling-small | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| thinkingmachines/inkling-small:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| thinkingmachines/inkling:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| undi95/remm-slerp-l2-13b | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| upstage/solar-pro-3 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| upstage/solar-pro4 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| writer/palmyra-x5 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| x-ai/grok-2-1212 | OpenRouter | failed | 404 | {"error":{"message":"No endpoints found for x-ai/grok-2-1212.","code":404},"user_id":"user_3HLeY7tYu6sZcGHpPdoSE3u7hUg"} |
| x-ai/grok-4.20 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| x-ai/grok-4.20-multi-agent | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| x-ai/grok-4.3 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| x-ai/grok-4.3:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| x-ai/grok-4.5 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| x-ai/grok-4.6 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| x-ai/grok-build-0.1 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| xiaomi/mimo-v2.5 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| xiaomi/mimo-v2.5-pro | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| z-ai/glm-4.5 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| z-ai/glm-4.5-air | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| z-ai/glm-4.5v | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| z-ai/glm-4.6 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| z-ai/glm-4.6v | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| z-ai/glm-4.7 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| z-ai/glm-4.7-flash | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| z-ai/glm-5 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| z-ai/glm-5-turbo | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| z-ai/glm-5.1 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| z-ai/glm-5.2 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| z-ai/glm-5.2:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| z-ai/glm-5.3 | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| z-ai/glm-5.3-flash | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| z-ai/glm-5.3-flash:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| z-ai/glm-5.3:batch | OpenRouter | failed | 404 | {"error":{"message":"This model is only available through the Batch API. Use the /api/beta/batches endpoint instead.","code":404,"metadata":{"routing_ |
| z-ai/glm-5v-turbo | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| ~anthropic/claude-fable-latest | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| ~anthropic/claude-haiku-latest | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| ~anthropic/claude-opus-latest | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| ~anthropic/claude-sonnet-latest | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| ~deepseek/deepseek-v4-flash-latest | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| ~google/gemini-flash-latest | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| ~google/gemini-pro-latest | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| ~moonshotai/kimi-latest | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| ~openai/gpt-latest | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| ~openai/gpt-mini-latest | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| ~x-ai/grok-latest | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| ~z-ai/glm-flash-latest | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |
| ~z-ai/glm-latest | OpenRouter | failed | 403 | {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/e9de15efe0312af0ee76de8f339e3f0bf |

## Полные результаты по провайдерам

### AI21 Labs

Working: 0 | Failed: 1 | Unavailable: 0 | Total: 1

### Anthropic

Working: 0 | Failed: 3 | Unavailable: 0 | Total: 3

### Cohere

Working: 0 | Failed: 1 | Unavailable: 0 | Total: 1

### DeepSeek

Working: 0 | Failed: 1 | Unavailable: 0 | Total: 1

### Google DeepMind

Working: 1 | Failed: 17 | Unavailable: 0 | Total: 18

### Google DeepMind (gen-lang)

Working: 9 | Failed: 38 | Unavailable: 0 | Total: 47

### Meta

Working: 0 | Failed: 3 | Unavailable: 0 | Total: 3

### Mistral AI

Working: 0 | Failed: 2 | Unavailable: 0 | Total: 2

### OmniRoute

Working: 11 | Failed: 22 | Unavailable: 0 | Total: 38

### OpenCode AI

Working: 0 | Failed: 2 | Unavailable: 0 | Total: 2

### OpenRouter

Working: 6 | Failed: 434 | Unavailable: 0 | Total: 446
