"""
Start command handler
"""
from aiogram import Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

from app.middlewares.i18n import _
from app.database.mongodb import get_users_collection


async def cmd_start(message: Message) -> None:
    """
    Handle /start command - greet the user and save to database
    """
    # Save user to database if not exists
    user_id = message.from_user.id
    username = message.from_user.username
    full_name = message.from_user.full_name
    
    # Get current timestamp
    from datetime import datetime
    now = datetime.utcnow()
    
    # Update user in database with upsert
    await get_users_collection().update_one(
        {"user_id": user_id},
        {
            "$set": {
                "username": username,
                "full_name": full_name,
                "last_activity": now
            },
            "$setOnInsert": {
                "registered_at": now
            }
        },
        upsert=True
    )
    
    # Send welcome message
    await message.answer(
        _(
            "👋 Hello, {full_name}!\n\n"
            "Welcome to the bot. Use /help to see available commands."
        ).format(full_name=full_name)
    )


def register_start_handlers(dp: Dispatcher) -> None:
    """Register start handlers"""
    dp.message.register(cmd_start, Command("start")) 