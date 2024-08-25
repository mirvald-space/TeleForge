from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.database import create_user, get_user, update_user

router = Router()

AVAILABLE_LANGUAGES = {
    "en": "English",
    "ru": "Русский"
}


@router.message(CommandStart())
async def cmd_start(message: Message, _: callable):
    user = await get_user(message.from_user.id)
    if not user:
        await create_user({
            "telegram_id": message.from_user.id,
            "language": "en"
        })

    await message.reply(_("start_message"))


@router.message(Command("language"))
async def cmd_language(message: Message, _: callable):
    kb = InlineKeyboardBuilder()
    for lang_code, lang_name in AVAILABLE_LANGUAGES.items():
        kb.button(text=lang_name, callback_data=f"lang_{lang_code}")
    kb.adjust(2)
    await message.reply(_("language_command"), reply_markup=kb.as_markup())


@router.callback_query(F.data.startswith("lang_"))
async def callback_language(callback: CallbackQuery, _: callable):
    lang_code = callback.data.split("_")[1]
    if lang_code in AVAILABLE_LANGUAGES:
        await update_user(callback.from_user.id, {"language": lang_code})
        await callback.message.edit_text(_("language_changed"))
    else:
        await callback.message.edit_text("Invalid language selection.")


def register_user_handlers(dp: Router):
    dp.include_router(router)
