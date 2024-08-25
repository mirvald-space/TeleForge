from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from bot.database.models import User


class LanguageMiddleware(BaseMiddleware):
    async def on_pre_process_message(self, message: types.Message, data: dict):
        user = await User.find_one({"telegram_id": message.from_user.id})
        if user:
            data['language'] = user.language
        else:
            data['language'] = 'en'
