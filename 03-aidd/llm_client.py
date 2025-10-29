from typing import List, Dict
import logging
from openai import OpenAI
from config import get_config


def build_system_prompt() -> str:
    return "Ты — профессиональный консультант банка. Отвечай ясно, корректно и по делу."


def call_llm(messages: List[Dict[str, str]]) -> str:
    cfg = get_config()
    api_key = cfg["openrouter_api_key"]
    model = cfg["llm_model"]
    temperature = cfg["llm_temperature"]
    max_tokens = cfg["llm_max_tokens"]

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    full_messages = [{"role": "system", "content": build_system_prompt()}] + messages

    logging.info("Calling LLM: model=%s", model)
    resp = client.chat.completions.create(
        model=model,
        messages=full_messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return resp.choices[0].message.content or ""


