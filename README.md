# eva-ais — EvaBot AI Model Inventory

Полный каталог LLM-моделей, используемых в инфраструктуре EvaBot, и сканер системы для их обнаружения.

## Быстрый старт

```bash
# Сканировать всю систему и обновить каталог
python3 scripts/scan_all_llms.py

# Просмотр каталога
open reports/system_scan_report.md
```

## Структура репозитория

```
eva-ais/
├── scripts/
│   └── scan_all_llms.py          # Системный сканер (GCP, API, локальные сервисы, конфиги)
├── reports/
│   ├── system_scan_report.md     # Полный Markdown-отчёт
│   ├── models_catalog.json       # Машиночитаемый JSON-каталог
│   └── models_catalog.tsv        # TSV для анализа в таблицах
├── free-models/                  # Бесплатные модели и модели с бесплатной квотой
├── paid-models/                  # Платные (pay-per-use) модели
└── providers/                    # Маркдаун-файлы по каждому провайдеру
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

- **Всего моделей в каталоге:** 63
- **Бесплатных / с бесплатной квотой:** 31
- **Open-Weights (бесплатно):** 7
- **Платных (pay-per-use):** 25

> Запустите `python3 scripts/scan_all_llms.py` для свежего отчёта.
