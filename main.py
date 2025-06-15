
import logging
import asyncio
from aiogram import Bot, Dispatcher
from config import config
from handlers.weather import router
from aiogram.types import BotCommand

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TELEGRAM_TOKEN)
dp = Dispatcher()

async def set_bot_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Запустити бота"),
        BotCommand(command="help", description="Допомога / список команд"),
    ]
    await bot.set_my_commands(commands)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await set_bot_commands(bot)

    dp.include_router(router)  # Підключаємо обробники

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
