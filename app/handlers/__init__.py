"""
Handlers package
"""
from aiogram import Dispatcher

from app.handlers.start import register_start_handlers
from app.handlers.language import register_language_handlers
from app.handlers.help import register_help_handlers
from app.handlers.echo import register_echo_handlers


def register_all_handlers(dp: Dispatcher) -> None:
    """Register all handlers"""
    # Register handlers (order matters)
    register_start_handlers(dp)
    register_language_handlers(dp)
    register_help_handlers(dp)
    
    # Echo should be last
    register_echo_handlers(dp) 