import os
from dotenv import load_dotenv


def get_config() -> dict:
    load_dotenv()
    telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
    # Iteration 3: require LLM key as well
    if not telegram_bot_token:
        raise RuntimeError("Missing TELEGRAM_BOT_TOKEN")
    if not openrouter_api_key:
        raise RuntimeError("Missing OPENROUTER_API_KEY")

    return {
        "telegram_bot_token": telegram_bot_token,
        "openrouter_api_key": openrouter_api_key,
        "llm_model": os.getenv("LLM_MODEL", "openai/gpt-4"),
        "llm_temperature": float(os.getenv("LLM_TEMPERATURE", "0.7")),
        "llm_max_tokens": int(os.getenv("LLM_MAX_TOKENS", "1000")),
        "max_history_messages": int(os.getenv("MAX_HISTORY_MESSAGES", "10")),
    }


