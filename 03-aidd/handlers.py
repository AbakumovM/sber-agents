import logging
from aiogram import Router, F
from aiogram.types import Message
from llm_client import call_llm
from config import get_config

router = Router()

# user_id -> list[dict]
user_contexts = {}


@router.message(F.text == "/start")
async def start(message: Message) -> None:
    logging.info("Start command from user %s", message.from_user.id)
    await message.answer("Здравствуйте! Я банковский ассистент. Задайте ваш вопрос.")

@router.message(F.text)
async def answer_with_llm(message: Message) -> None:
    user_id = message.from_user.id
    cfg = get_config()
    max_history = cfg["max_history_messages"]
    # Получить историю
    history = user_contexts.get(user_id, [])
    # Добавить новое сообщение пользователя
    history.append({"role": "user", "content": message.text})
    # Усечь историю
    context = history[-max_history:]
    try:
        logging.info("LLM request for user %s", user_id)
        reply = call_llm(context)
        if not reply:
            reply = "Извините, не удалось получить ответ."
        await message.answer(reply)
        # Добавить ответ ассистента в историю
        history.append({"role": "assistant", "content": reply})
        # Сохраняем усеченную историю обратно
        user_contexts[user_id] = history[-max_history:]
        logging.info("LLM response sent to user %s", user_id)
    except Exception as err:
        logging.error("LLM error for user %s: %s", user_id, err)
        await message.answer("Техническая ошибка. Попробуйте снова позже.")


