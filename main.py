import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

from bot.config import BOT_TOKEN, WEBAPP_HOST, WEBAPP_PORT, WEBHOOK_PATH, WEBHOOK_URL
from bot.database import init_db
from bot.handlers import register_handlers
from bot.middlewares import setup_middlewares
from bot.plugins import setup_plugins
from bot.utils.logger import setup_logger

logger = logging.getLogger(__name__)


async def on_startup(bot: Bot):
    await bot.set_webhook(WEBHOOK_URL)
    logger.info(f"Webhook set to {WEBHOOK_URL}")
    await init_db()


async def on_shutdown(bot: Bot):
    await bot.delete_webhook()
    logger.info("Bot shutdown complete")


async def main():
    # Setup logging
    setup_logger()

    # Initialize bot and dispatcher
    bot = Bot(token=BOT_TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    # Setup middlewares
    setup_middlewares(dp)

    # Register handlers
    register_handlers(dp)

    # Setup plugins
    setup_plugins(dp)

    # Setup webhook
    app = web.Application()
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
    )
    webhook_requests_handler.register(app, path=WEBHOOK_PATH)

    # Setup startup and shutdown events
    app.on_startup.append(lambda app: asyncio.create_task(on_startup(bot)))
    app.on_shutdown.append(lambda app: asyncio.create_task(on_shutdown(bot)))

    # Setup aiohttp application
    setup_application(app, dp, bot=bot)

    # Start webhook
    logger.info(f"Starting webhook on {WEBAPP_HOST}:{WEBAPP_PORT}")
    web.run_app(app, host=WEBAPP_HOST, port=WEBAPP_PORT)

if __name__ == '__main__':
    asyncio.run(main())
