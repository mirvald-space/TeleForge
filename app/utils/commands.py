"""
Commands utility for bot commands
"""
from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_bot_commands(bot: Bot) -> None:
    """
    Set bot commands in the menu
    """
    commands = [
        BotCommand(command="start", description="Start the bot"),
        BotCommand(command="help", description="Show help"),
        BotCommand(command="language", description="Change language"),
    ]
    
    await bot.set_my_commands(commands, scope=BotCommandScopeDefault()) 