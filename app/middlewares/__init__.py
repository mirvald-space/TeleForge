"""
Middlewares package
"""
from aiogram import Dispatcher

from app.middlewares.i18n import I18nMiddleware
from app.middlewares.throttling import ThrottlingMiddleware


def setup_middlewares(dp: Dispatcher) -> None:
    """Setup middlewares for dispatcher"""
    # Setup i18n middleware
    i18n = I18nMiddleware()
    dp.message.middleware(i18n)
    dp.callback_query.middleware(i18n)
    
    # Setup throttling middleware
    throttling = ThrottlingMiddleware()
    dp.message.middleware(throttling) 