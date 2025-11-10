import asyncio
import logging
from aiogram import Bot, Dispatcher
from handlers import router
from config import config
import whisper

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def main():
    bot = Bot(token=config.TELEGRAM_TOKEN)
    dp = Dispatcher()
    model = whisper.load_model("base")
    logger.info("loads model for whisper")
    dp["whisper_model"] = model
    dp.include_router(router)
    
    logger.info("Starting bot...")
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

