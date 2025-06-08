"""
Throttling middleware to prevent spam
"""
import time
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message
from aiogram.utils.i18n import gettext as _


class ThrottlingMiddleware(BaseMiddleware):
    """Middleware for throttling"""

    def __init__(self, rate_limit: float = 0.5) -> None:
        """
        Initialize throttling middleware
        
        Args:
            rate_limit: Minimum time between messages in seconds
        """
        self.rate_limit = rate_limit
        self.last_message_time: Dict[int, float] = {}

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        """
        Check if message is not too frequent
        """
        # Only throttle private messages
        if event.chat.type != "private":
            return await handler(event, data)
        
        # Get current time
        current_time = time.time()
        
        # Get user ID
        user_id = event.from_user.id
        
        # Check if user sent message recently
        if user_id in self.last_message_time:
            time_since_last = current_time - self.last_message_time[user_id]
            
            # If message is too frequent, warn user
            if time_since_last < self.rate_limit:
                await event.answer(_("Please don't spam! Wait a moment before sending another message."))
                return None
        
        # Update last message time
        self.last_message_time[user_id] = current_time
        
        # Call next handler
        return await handler(event, data) 