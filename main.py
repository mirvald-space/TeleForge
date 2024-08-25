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


async def on_startup(bot: Bot, app: web.Application):
    try:
        await init_db()
        await bot.set_webhook(WEBHOOK_URL)
        logger.info(f"Webhook set to {WEBHOOK_URL}")
    except Exception as e:
        logger.error(f"Error during startup: {e}")
        raise


async def on_shutdown(bot: Bot, app: web.Application):
    await bot.delete_webhook()
    await bot.session.close()
    logger.info("Bot shutdown complete")


async def main():
    setup_logger()

    bot = Bot(token=BOT_TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    setup_middlewares(dp)
    register_handlers(dp)
    setup_plugins(dp)

    app = web.Application()
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
    )
    webhook_requests_handler.register(app, path=WEBHOOK_PATH)

    app.on_startup.append(lambda app: on_startup(bot, app))
    app.on_shutdown.append(lambda app: on_shutdown(bot, app))

    setup_application(app, dp, bot=bot)

    logger.info(f"Starting webhook on {WEBAPP_HOST}:{WEBAPP_PORT}")
    return app

if __name__ == '__main__':
    try:
        app = asyncio.run(main())
        web.run_app(app, host=WEBAPP_HOST, port=WEBAPP_PORT)
    except Exception as e:
        logger.error(f"Error in main: {e}")
        raise
