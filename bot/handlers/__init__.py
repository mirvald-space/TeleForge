# bot/handlers/__init__.py
from aiogram import Router

from .admin import register_admin_handlers
from .user import register_user_handlers


def register_handlers(dp: Router):
    register_user_handlers(dp)
    register_admin_handlers(dp)
