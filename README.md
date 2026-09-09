# eva-ais — EvaBot AI Model Inventory

Полный каталог LLM-моделей, используемых в инфраструктуре EvaBot, и сканер системы для их обнаружения.

## Быстрый старт

```bash
# Сканировать всю систему и обновить каталог
python3 scripts/scan_all_llms.py

# Тестировать все модели из каталога
python3 scripts/test_all_models.py

# Получить свежие модели 2025-2026 гг. с лидербордов
python3 scripts/fresh_models.py
```

### Отчёты

| Файл | Описание |
|---|---|
| `reports/system_scan_report.md` | Полный Markdown-отчёт по сканеру |
| `reports/models_catalog.json` | Машиночитаемый JSON-каталог (56 моделей) |
| `reports/models_catalog.tsv` | TSV для анализа в таблицах |
| `reports/model_test_results.json` | Результаты тестов всех 562 моделей (27 работают) |
| `reports/model_test_results.tsv` | TSV-версия результатов тестов |
| `reports/model_test_report.md` | Markdown-отчёт по тестам |
| `reports/fresh_models_comparison.md` | Топ-30 платных и бесплатных моделей 2025–2026 |
| `reports/fresh_models_raw.json` | Сырые данные с 8 источников (588 моделей) |

## Структура репозитория

```
eva-ais/
├── scripts/
│   ├── scan_all_llms.py          # Системный сканер (GCP, API, локальные сервисы, конфиги)
│   ├── test_all_models.py        # Тестер: проверяет статус каждой модели
│   └── fresh_models.py           # Сбор свежих моделей 2025-2026 с лидербордов
├── reports/
│   ├── system_scan_report.md     # Полный Markdown-отчёт сканера
│   ├── models_catalog.json       # Машиночитаемый JSON-каталог
│   ├── models_catalog.tsv        # TSV для анализа в таблицах
│   ├── model_test_results.json   # Результаты тестов всех моделей
│   ├── model_test_results.tsv    # TSV-версия результатов тестов
│   ├── model_test_report.md      # Markdown-отчёт по тестам
│   ├── fresh_models_comparison.md# Топ-30 платных/бесплатных моделей 2025-2026
│   └── fresh_models_raw.json     # Сырые данные с 8 источников
├── free-models/                  # Маркдаун-файлы бесплатных моделей (31 файлов)
├── paid-models/                  # Маркдаун-файлы платных моделей (25 файлов)
└── providers/                    # Маркдаун-файлы по каждому провайдеру (11 файлов)
```

## Сканер (`scan_all_llms.py`)

Скрипт выполняет комплексное сканирование:

| № | Что сканируется | Источник |
|---|---|---|
| 1 | GCP проекты, сервисы, биллинг | `gcloud projects list`, `gcloud services list` |
| 2 | Локальный бэкенд | `http://127.0.0.1:8000/api/models` |
| 3 | OmniRoute daemon | `http://127.0.0.1:20128/v1/models` |
| 4 | OpenRouter API | `https://openrouter.ai/api/v1/models` |
| 5 | Gemini API | `https://generativelanguage.googleapis.com` |
| 6 | HuggingFace configs | `opencode.json`, `kilo.jsonc`, `mcp.json` |
| 7 | API ключи в `.env` | `/var/www/evabot-backend/.env` |
| 8 | Локальные LLM-сервисы | Скан портов 11434, 1234, 8080, etc. |
| 9 | Docker контейнеры | `docker ps` |
| 10 | Файлы конфигураций | 6 файлов конфигов |

## Каталог моделей

### Провайдеры

| Провайдер | Бесплатных | Платных | Статус |
|---|---|---|---|
| Google Gemini / Vertex AI | 18 (12 + 6 open-weights) | 12 | Активен |
| OpenRouter | 21 | 410 | Активен |
| OmniRoute Daemon | 33 (бесплатные роуты) | 1 | Активен |
| HuggingFace Inference | 136 | 0 (free tier) | Конфигурирован |
| OpenCode Platform | 2 | 0 | Активен |
| Groq | — | — | Через OmniRoute |
| Cloudflare Workers AI | 7 | 0 | Через OmniRoute |
| Z.ai (GLM) | — | — | Через OmniRoute |
| Cerebras | — | — | Конфигурирован |
| Mistral AI | — | — | Конфигурирован |

### Итоги (локальный каталог)

- **Моделей в каталоге (scan_all_llms.py):** 56
- **Бесплатных / с бесплатной квотой:** 31
- **Open-Weights (бесплатно):** 7
- **Платных (pay-per-use):** 25

### Итоги (тесты model_test_results.json)

- **Всего моделей протестировано:** 562
- **Работают:** 27 (Google Gemini gen-lang key ✓, OmniRoute/Groq routes ✓, 6 OpenRouter free ✓)
- **Не работают:** 524 (OpenRouter платные — нужен баланс; OpenRouter free — rate-limited; Groq/Cerebras 403; OpenCode — API key не настроен)

### Итоги (fresh_models.py — 2025–2026)

- **Всего свежих моделей:** 588
- **Бесплатных:** 42+ (OpenRouter 21, Kilo Code 14+, Cloudflare 65, Gemini Free Quota, OpenCode 2, FreeLLMAPI 605 models/34 providers)
- **Платных:** 546
- **Новых (не в каталоге):** 30+
- **Источники:** OpenRouter (431), Mistral (46), CloudFlare AI (65), HuggingFace (25), Gemini API (21)
- **Новые бесплатные провайдеры:** Kilo Code (14+ free, $0.00/1M), FreeLLMAPI (605 models/34 providers, 7.4B tokens/mo), Cloudflare Workers AI (65 models, 10K neurons/day)

### Агрегаторы бесплатных LLM

| Сайт | Моделей | Провайдеров | Фичи |
|---|---|---|---|
| FreeLLMAPI | 605 | 34 | $0/self-hosted router, 7.4B tokens/mo |
| Free LLM API Hub | 331+ | 25+ | Verified, daily sync |
| Token Gratis | 323 | 25 | Индонезийский, fallback chains |
| Kilo Code | 14+ | 8+ | Live leaderboard, кодинг-бенчмарки |
| free-llm-api-watch | — | — | GitHub tracker (daily commits) |
| Free-LLM Atlas | 46+ | 46+ | Automated probing |

### Бесплатные модели по провайдерам

| Провайдер | Бесплатных моделей | Работают | Примечание |
|---|---|---|---|
| Google Gemini | 10 | ✅ 10 | Free Quota (15 RPM/1M TPM) |
| OmniRoute | 11 | ✅ 11 | Через локальный daemon |
| OpenRouter | 21 | ✅ 6 | 15 rate-limited |
| OpenCode | 2 | ❌ | OPENCODE_API_KEY не настроен |
| Kilo Code | 14+ | ❓ | $0.00/1M, требует аккаунт |
| Cloudflare AI | 65 | ❓ | 10K neurons/day free tier |
| FreeLLMAPI | 100+ | ❓ | Агрегатор 34 провайдеров |

> Запустите `python3 scripts/scan_all_llms.py` для свежего отчёта.
