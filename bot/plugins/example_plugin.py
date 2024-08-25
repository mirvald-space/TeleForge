# bot/plugins/example_plugin.py
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("echo"))
async def echo_command(message: Message):
    """
    This handler will be called when user sends `/echo` command
    """
    # Get the text after the command
    echo_text = message.text.split(maxsplit=1)[1] if len(
        message.text.split()) > 1 else "You didn't provide any text to echo!"

    await message.reply(f"Echo: {echo_text}")


@router.message(F.text)
async def echo_all(message: Message):
    """
    This handler will echo all text messages if they don't contain commands
    """
    if not message.text.startswith('/'):
        await message.answer(f"You said: {message.text}")


def setup(dp: Router):
    """
    Setup function for the plugin
    This function will be called by the main application to register the plugin
    """
    dp.include_router(router)
    print("Example plugin has been loaded!")
