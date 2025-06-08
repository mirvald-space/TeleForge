"""
Language selection handler
"""
from aiogram import Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from app.database.mongodb import get_users_collection
from app.keyboards.language import get_language_keyboard
from app.middlewares.i18n import i18n, _


async def cmd_language(message: Message) -> None:
    """
    Handle /language command - show language selection keyboard
    """
    await message.answer(
        _("🌐 Please select your language:"),
        reply_markup=get_language_keyboard()
    )


async def process_language_selection(callback: CallbackQuery) -> None:
    """
    Process language selection from inline keyboard
    """
    # Get language code from callback data
    lang_code = callback.data.split("_")[1]
    
    # Update user's language preference in database
    await get_users_collection().update_one(
        {"user_id": callback.from_user.id},
        {"$set": {"language": lang_code}}
    )
    
    # Set language for current session
    i18n.current_locale = lang_code
    
    # Answer callback query
    await callback.answer(_("Language changed"))
    
    # Get translated language name based on selected language
    language_name = ""
    if lang_code == "en":
        language_name = _("English")
    elif lang_code == "ru":
        language_name = _("Russian")
    elif lang_code == "uk":
        language_name = _("Ukrainian")
    
    # Edit message with confirmation
    await callback.message.edit_text(
        _("✅ Your language has been set to: {language}").format(
            language=language_name
        )
    )


def register_language_handlers(dp: Dispatcher) -> None:
    """Register language handlers"""
    dp.message.register(cmd_language, Command("language"))
    dp.callback_query.register(process_language_selection, F.data.startswith("lang_")) 