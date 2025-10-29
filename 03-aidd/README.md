# AIDD Telegram LLM-бот (MVP)

Минимально жизнеспособный Telegram-бот, отвечающий на вопросы в роли банковского консультанта через OpenRouter.

## Требования
- Python 3.11+
- uv (менеджер окружений и зависимостей)
- Telegram Bot Token
- OpenRouter API Key

## Установка
```bash
uv sync
```

## Конфигурация
Создайте файл `.env` по образцу `env.template` и укажите значения:
```
TELEGRAM_BOT_TOKEN=...  # токен Telegram-бота
OPENROUTER_API_KEY=...  # ключ OpenRouter
LLM_MODEL=openai/gpt-4
LLM_TEMPERATURE=0.7
LLM_MAX_TOKENS=1000
MAX_HISTORY_MESSAGES=10
```

## Запуск
```bash
make run
```

## Как это работает
- `bot.py` — точка входа, настраивает aiogram и polling
- `handlers.py` — команда `/start`, диалог с контекстом (в памяти), логирование
- `llm_client.py` — запросы к LLM через OpenRouter (клиент `openai`)
- `config.py` — загрузка переменных окружения

## Структура проекта (основное)
```
project/
├── bot.py
├── handlers.py
├── llm_client.py
├── config.py
├── Makefile
├── pyproject.toml
├── env.template
└── docs/
    ├── idea.md
    ├── vision.md
    ├── conventions.md
    ├── tasklist.md
    └── workflow.md
```

## Логи
- INFO — ключевые шаги (получение сообщения, вызов LLM, отправка ответа)
- ERROR — ошибки (исключения при вызове LLM и др.)

## Принципы
Следуем KISS и YAGNI: только необходимый функционал для проверки идеи.
