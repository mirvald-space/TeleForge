"""
Echo handler for unhandled messages
"""
from aiogram import Dispatcher, F
from aiogram.types import Message
from datetime import datetime

from app.middlewares.i18n import _
from app.database.mongodb import get_users_collection


async def echo_handler(message: Message) -> None:
    """
    Echo handler for unhandled messages
    """
    # Update user's last activity in database
    await get_users_collection().update_one(
        {"user_id": message.from_user.id},
        {"$set": {"last_activity": datetime.utcnow()}}
    )
    
    # Echo the message
    await message.answer(
        _("I don't understand this command. Use /help to see available commands.")
    )


def register_echo_handlers(dp: Dispatcher) -> None:
    """Register echo handler"""
    # Echo handler should be registered last
    dp.message.register(echo_handler) 