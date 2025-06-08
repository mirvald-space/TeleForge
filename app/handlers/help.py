"""
Help command handler
"""
from aiogram import Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from app.middlewares.i18n import _


async def cmd_help(message: Message) -> None:
    """
    Handle /help command
    """
    help_text = _(
        "📚 <b>Available commands:</b>\n\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/language - Change language"
    )
    
    await message.answer(help_text)


def register_help_handlers(dp: Dispatcher) -> None:
    """Register help handlers"""
    dp.message.register(cmd_help, Command("help")) 