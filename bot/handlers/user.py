# bot/handlers/user.py
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.database.models import User

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    user = await User.find_one({"telegram_id": message.from_user.id})
    if not user:
        user = User(telegram_id=message.from_user.id)
        await user.commit()

    await message.reply(
        "Hello! I'm TeleForge, a universal Telegram bot. How can I help you?"
    )


def register_user_handlers(dp: Router):
    dp.include_router(router)
