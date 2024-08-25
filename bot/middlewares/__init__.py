from aiogram import Dispatcher

from .language import LanguageMiddleware


def setup_middlewares(dp: Dispatcher):
    dp.middleware.setup(LanguageMiddleware())
