from unittest.mock import AsyncMock, patch

import pytest
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.types import User as TelegramUser

from bot.config import ADMIN_IDS
from bot.handlers.admin import cmd_admin
from bot.handlers.user import cmd_start


# Фикстура для создания мок-объекта бота
@pytest.fixture
def bot():
    return AsyncMock(spec=Bot)

# Фикстура для создания диспетчера


@pytest.fixture
def dp(bot):
    dp = Dispatcher()
    return dp

# Фикстура для создания мок-объекта сообщения


@pytest.fixture
def message():
    return AsyncMock(spec=Message)

# Тест для команды /start


async def test_cmd_start(bot, message):
    # Подготовка
    message.from_user = AsyncMock(spec=TelegramUser)
    message.from_user.id = 12345

    # Мокаем метод find_one, чтобы он возвращал None (пользователь не найден)
    with patch('bot.database.models.User.find_one', return_value=None):
        # Мокаем метод commit для User
        with patch('bot.database.models.User.commit', new_callable=AsyncMock):
            # Действие
            await cmd_start(message)

    # Проверка
    message.reply.assert_called_once()
    assert "Welcome to TeleForge" in message.reply.call_args[0][0]

# Тест для команды /admin (с правами администратора)


async def test_cmd_admin_with_rights(bot, message):
    # Подготовка
    message.from_user = AsyncMock(spec=TelegramUser)
    # Используем ID администратора из конфига
    message.from_user.id = ADMIN_IDS[0]

    # Мокаем метод count_documents
    with patch('bot.database.models.User.count_documents',
               new_callable=AsyncMock) as mock_count:
        mock_count.return_value = 10
        # Действие
        await cmd_admin(message)

    # Проверка
    message.reply.assert_called_once()
    assert "There are currently 10 users registered" in message.reply.call_args[0][0]

# Тест для команды /admin (без прав администратора)


async def test_cmd_admin_without_rights(bot, message):
    # Подготовка
    message.from_user = AsyncMock(spec=TelegramUser)
    message.from_user.id = 99999  # ID, которого нет в списке администраторов

    # Действие
    await cmd_admin(message)

    # Проверка
    message.reply.assert_not_called()

# Дополнительные тесты можно добавить здесь

if __name__ == '__main__':
    pytest.main([__file__])
