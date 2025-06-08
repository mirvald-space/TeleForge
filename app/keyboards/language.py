"""
Language selection keyboard
"""
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.i18n import gettext as _
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.middlewares.i18n import _


def get_language_keyboard() -> InlineKeyboardMarkup:
    """
    Create language selection keyboard
    
    Returns:
        InlineKeyboardMarkup: Keyboard with language options
    """
    builder = InlineKeyboardBuilder()
    
    # Add language buttons
    builder.row(
        InlineKeyboardButton(text="🇺🇸 English", callback_data="lang_en"),
        InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru"),
        InlineKeyboardButton(text="🇺🇦 Українська", callback_data="lang_uk"),
    )
    
    return builder.as_markup() 