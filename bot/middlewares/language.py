from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message

from bot.database import get_user
from bot.utils.localization import get_string


class LanguageMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        user = await get_user(event.from_user.id)
        if user:
            language = user.get('language', 'en')
        else:
            language = 'en'

        data['language'] = language
        data['_'] = get_string(language)

        return await handler(event, data)


def setup_middlewares(dp):
    dp.message.middleware(LanguageMiddleware())
