"""
Miscellaneous utilities
"""
import logging
from typing import List, Union

from app.config.settings import settings


def is_admin(user_id: int) -> bool:
    """
    Check if user is admin
    
    Args:
        user_id: Telegram user ID
        
    Returns:
        bool: True if user is admin
    """
    return user_id in settings.admin_ids


def log_errors(f):
    """
    Decorator for error logging
    """
    async def wrapper(*args, **kwargs):
        try:
            return await f(*args, **kwargs)
        except Exception as e:
            logging.exception(f"Error in {f.__name__}: {e}")
            raise
    return wrapper 