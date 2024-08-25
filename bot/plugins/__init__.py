# bot/plugins/__init__.py
from aiogram import Router

from . import example_plugin


def setup_plugins(dp: Router):
    example_plugin.setup(dp)
    # Add more plugins here as needed
    # other_plugin.setup(dp)
