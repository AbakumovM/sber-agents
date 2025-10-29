.PHONY: install run lint env-template

install:
	uv sync

run:
	uv run python bot.py

lint:
	python -m compileall .

env-template:
	@echo "TELEGRAM_BOT_TOKEN=" > env.template
	@echo "OPENROUTER_API_KEY=" >> env.template
	@echo "LLM_MODEL=openai/gpt-4" >> env.template
	@echo "LLM_TEMPERATURE=0.7" >> env.template
	@echo "LLM_MAX_TOKENS=1000" >> env.template
	@echo "MAX_HISTORY_MESSAGES=10" >> env.template


