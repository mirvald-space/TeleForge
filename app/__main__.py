"""
Main entry point for the bot
"""
import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties

from app.config.settings import settings
from app.database.mongodb import setup_mongodb
from app.handlers import register_all_handlers
from app.middlewares import setup_middlewares
from app.middlewares.i18n import i18n
from app.utils.commands import set_bot_commands


async def main() -> None:
    """Main function to start the bot"""
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )

    # Initialize bot and dispatcher
    bot = Bot(
        token=settings.bot_token, 
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher(storage=MemoryStorage())

    # Setup MongoDB connection
    await setup_mongodb()

    # Setup middlewares
    setup_middlewares(dp)

    # Register all handlers
    register_all_handlers(dp)

    # Set bot commands
    await set_bot_commands(bot)

    # Start polling
    logging.info("Starting bot")
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped") 