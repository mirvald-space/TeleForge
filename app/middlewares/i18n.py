"""
I18n middleware for language support
"""
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User
from aiogram.utils.i18n import I18n, gettext as _

from app.config.settings import settings
from app.database.mongodb import get_users_collection


# Initialize I18n
i18n = I18n(path=settings.i18n_path, default_locale=settings.default_language, domain=settings.i18n_domain)

# Make i18n available globally
_ = i18n.gettext


class I18nMiddleware(BaseMiddleware):
    """Middleware for i18n support"""

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        """
        Set user's language for the handler
        """
        # Get user from event
        user = data.get("event_from_user")
        
        if user:
            # Try to get user's language from database
            user_data = await get_users_collection().find_one({"user_id": user.id})
            
            locale = settings.default_language
            if user_data and "language" in user_data:
                # Set language from database
                locale = user_data["language"]
            
            # Set current locale for this request
            i18n.current_locale = locale
            
        # Add i18n to data context
        data["i18n"] = i18n
        
        # Call next handler
        return await handler(event, data) 