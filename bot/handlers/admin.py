# bot/handlers/admin.py
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.config import ADMIN_IDS
from bot.database.models import User

router = Router()


@router.message(Command("admin"), F.from_user.id.in_(ADMIN_IDS))
async def cmd_admin(message: Message):
    user_count = await User.count_documents({})
    await message.reply(
        f"Hello, admin! There are currently {user_count} users registered."
    )


def register_admin_handlers(dp: Router):
    dp.include_router(router)
