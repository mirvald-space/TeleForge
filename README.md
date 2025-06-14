<div align="center">
  <img src="/cover.png" alt="TeleForge Logo" width="500" />
  <h1>TeleForge</h1>
  <p>Production-ready Telegram bot template with clean architecture</p>

  <div>
    <img src="https://img.shields.io/badge/python-3.9%2B-blue" alt="Python 3.9+">
    <img src="https://img.shields.io/badge/aiogram-3.x-blue" alt="aiogram 3.x">
    <img src="https://img.shields.io/badge/MongoDB-Ready-green" alt="MongoDB Ready">
    <img src="https://img.shields.io/badge/i18n-🇬🇧_🇷🇺_🇺🇦-orange" alt="i18n Support">
    <img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT License">
  </div>
</div>

<details open>
<summary>English 🇬🇧</summary>

## About TeleForge

A professional-grade template for Telegram bots based on aiogram 3.x, designed with clean architecture principles and essential production features:

- **Structured Architecture**: Proper separation of concerns with modular design
- **MongoDB Integration**: Async database operations with proper connection pooling
- **Multi-language Support**: Built-in i18n with English, Russian, Ukrainian translations
- **Middleware Stack**: Throttling, session management, language handling
- **Command System**: Well-organized command registration and processing
- **Error Handling**: Comprehensive exception management and logging

## Quick Start

```bash
# Clone repository
git clone https://github.com/mirvald-space/TeleForge.git
cd TeleForge

# Setup environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Compile translations
python compile_translations.py

# Configure environment
cp .env.example .env
# Edit .env with your settings

# Run bot
python -m app
```

## Project Structure

```
app/
├── __init__.py
├── __main__.py          # Entry point
├── config/              # Configuration
│   ├── __init__.py
│   └── settings.py      # Settings from environment
├── database/            # Database layer
│   ├── __init__.py
│   └── mongodb.py       # MongoDB connection
├── handlers/            # Message handlers
│   ├── __init__.py      # Handler registration
│   ├── start.py
│   ├── help.py
│   ├── language.py
│   └── echo.py
├── keyboards/           # Telegram keyboards
│   ├── __init__.py
│   └── language.py      # Language selection
├── middlewares/         # Request middleware
│   ├── __init__.py
│   ├── i18n.py          # Internationalization
│   └── throttling.py    # Rate limiting
└── utils/               # Utilities
    ├── __init__.py
    ├── commands.py      # Bot command setup
    └── misc.py          # Helper functions

locales/                 # Translation files
├── en/LC_MESSAGES/
├── ru/LC_MESSAGES/
└── uk/LC_MESSAGES/
```

## Configuration

`.env` file example:

```
# Bot
BOT_TOKEN=your_telegram_bot_token
BOT_NAME=TeleForge

# Database
MONGODB_URI=mongodb://localhost:27017/tg_bot

# Admin
ADMIN_IDS=123456789,987654321

# Locale
DEFAULT_LANGUAGE=en
```

## Extending

### Adding Handlers

1. Create handler file in `app/handlers/`
2. Define handler function and registration function:

```python
from aiogram import Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from app.middlewares.i18n import _

async def cmd_custom(message: Message) -> None:
    await message.answer(_("Custom command response"))

def register_custom_handlers(dp: Dispatcher) -> None:
    dp.message.register(cmd_custom, Command("custom"))
```

3. Register in `app/handlers/__init__.py`

### Adding Languages

1. Create directory structure:
```bash
mkdir -p locales/new_lang/LC_MESSAGES
```

2. Copy template and translate:
```bash
cp locales/bot.pot locales/new_lang/LC_MESSAGES/bot.po
# Edit .po file with translations
```

3. Compile translations:
```bash
python compile_translations.py
```

4. Update keyboard in `app/keyboards/language.py`

## License

MIT

</details>

<details>
<summary>Русский 🇷🇺</summary>

## О TeleForge

Профессиональный шаблон для создания Telegram-ботов на базе aiogram 3.x, разработанный с принципами чистой архитектуры и включающий все необходимые для продакшена функции:

- **Структурированная архитектура**: Правильное разделение ответственности с модульным дизайном
- **Интеграция с MongoDB**: Асинхронные операции с базой данных с правильным управлением соединениями
- **Многоязычная поддержка**: Встроенный i18n с переводами на английский, русский, украинский языки
- **Набор middleware**: Ограничение частоты запросов, управление сессиями, обработка языка
- **Система команд**: Хорошо организованная регистрация и обработка команд
- **Обработка ошибок**: Комплексное управление исключениями и логирование

## Быстрый старт

```bash
# Клонировать репозиторий
git clone https://github.com/mirvald-space/TeleForge.git
cd TeleForge

# Настройка окружения
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Компиляция переводов
python compile_translations.py

# Настройка окружения
cp .env.example .env
# Отредактируйте .env вашими настройками

# Запуск бота
python -m app
```

## Структура проекта

```
app/
├── __init__.py
├── __main__.py          # Точка входа
├── config/              # Конфигурация
│   ├── __init__.py
│   └── settings.py      # Настройки из окружения
├── database/            # Слой базы данных
│   ├── __init__.py
│   └── mongodb.py       # Подключение к MongoDB
├── handlers/            # Обработчики сообщений
│   ├── __init__.py      # Регистрация обработчиков
│   ├── start.py
│   ├── help.py
│   ├── language.py
│   └── echo.py
├── keyboards/           # Клавиатуры Telegram
│   ├── __init__.py
│   └── language.py      # Выбор языка
├── middlewares/         # Middleware запросов
│   ├── __init__.py
│   ├── i18n.py          # Интернационалізація
│   └── throttling.py    # Ограничение частоти
└── utils/               # Утиліти
    ├── __init__.py
    ├── commands.py      # Настройка команд бота
    └── misc.py          # Вспомогательные функции

locales/                 # Файлы переводов
├── en/LC_MESSAGES/
├── ru/LC_MESSAGES/
└── uk/LC_MESSAGES/
```

## Конфигурация

Пример файла `.env`:

```
# Бот
BOT_TOKEN=your_telegram_bot_token
BOT_NAME=TeleForge

# База данных
MONGODB_URI=mongodb://localhost:27017/tg_bot

# Админ
ADMIN_IDS=123456789,987654321

# Локализация
DEFAULT_LANGUAGE=ru
```

## Расширение

### Добавление обработчиков

1. Создайте файл обработчика в `app/handlers/`
2. Определите функцию обработчика и функцию регистрации:

```python
from aiogram import Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from app.middlewares.i18n import _

async def cmd_custom(message: Message) -> None:
    await message.answer(_("Ответ на пользовательскую команду"))

def register_custom_handlers(dp: Dispatcher) -> None:
    dp.message.register(cmd_custom, Command("custom"))
```

3. Зарегистрируйте в `app/handlers/__init__.py`

### Добавление языков

1. Создайте структуру директорий:
```bash
mkdir -p locales/new_lang/LC_MESSAGES
```

2. Скопируйте шаблон и переведите:
```bash
cp locales/bot.pot locales/new_lang/LC_MESSAGES/bot.po
# Отредактируйте файл .po с переводами
```

3. Скомпилируйте переводы:
```bash
python compile_translations.py
```

4. Обновите клавиатуру в `app/keyboards/language.py`

## Лицензия

MIT

</details>

<details>
<summary>Українська 🇺🇦</summary>

## Про TeleForge

Професійний шаблон для створення Telegram-ботів на базі aiogram 3.x, розроблений за принципами чистої архітектури та включає всі необхідні для продакшену функції:

- **Структурована архітектура**: Правильний розподіл відповідальності з модульним дизайном
- **Інтеграція з MongoDB**: Асинхронні операції з базою даних з правильним управлінням з'єднаннями
- **Багатомовна підтримка**: Вбудований i18n з перекладами англійською, російською, українською мовами
- **Набір middleware**: Обмеження частоти запитів, управління сесіями, обробка мови
- **Система команд**: Добре організована реєстрація та обробка команд
- **Обробка помилок**: Комплексне управління винятками та логування

## Швидкий старт

```bash
# Клонувати репозиторій
git clone https://github.com/mirvald-space/TeleForge.git
cd TeleForge

# Налаштування середовища
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Компіляція перекладів
python compile_translations.py

# Налаштування середовища
cp .env.example .env
# Відредагуйте .env вашими налаштуваннями

# Запуск бота
python -m app
```

## Структура проекту

```
app/
├── __init__.py
├── __main__.py          # Точка входу
├── config/              # Конфігурація
│   ├── __init__.py
│   └── settings.py      # Налаштування з середовища
├── database/            # Шар бази даних
│   ├── __init__.py
│   └── mongodb.py       # Підключення до MongoDB
├── handlers/            # Обробники повідомлень
│   ├── __init__.py      # Реєстрація обробників
│   ├── start.py
│   ├── help.py
│   ├── language.py
│   └── echo.py
├── keyboards/           # Клавіатури Telegram
│   ├── __init__.py
│   └── language.py      # Вибір мови
├── middlewares/         # Middleware запитів
│   ├── __init__.py
│   ├── i18n.py          # Інтернаціоналізація
│   └── throttling.py    # Обмеження частоти
└── utils/               # Утиліти
    ├── __init__.py
    ├── commands.py      # Налаштування команд бота
    └── misc.py          # Допоміжні функції

locales/                 # Файли перекладів
├── en/LC_MESSAGES/
├── ru/LC_MESSAGES/
└── uk/LC_MESSAGES/
```

## Конфігурація

Приклад файлу `.env`:

```
# Бот
BOT_TOKEN=your_telegram_bot_token
BOT_NAME=TeleForge

# База даних
MONGODB_URI=mongodb://localhost:27017/tg_bot

# Адмін
ADMIN_IDS=123456789,987654321

# Локалізація
DEFAULT_LANGUAGE=uk
```

## Розширення

### Додавання обробників

1. Створіть файл обробника в `app/handlers/`
2. Визначте функцію обробника та функцію реєстрації:

```python
from aiogram import Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from app.middlewares.i18n import _

async def cmd_custom(message: Message) -> None:
    await message.answer(_("Відповідь на користувацьку команду"))

def register_custom_handlers(dp: Dispatcher) -> None:
    dp.message.register(cmd_custom, Command("custom"))
```

3. Зареєструйте в `app/handlers/__init__.py`

### Додавання мов

1. Створіть структуру директорій:
```bash
mkdir -p locales/new_lang/LC_MESSAGES
```

2. Скопіюйте шаблон і перекладіть:
```bash
cp locales/bot.pot locales/new_lang/LC_MESSAGES/bot.po
# Відредагуйте файл .po з перекладами
```

3. Скомпілюйте переклади:
```bash
python compile_translations.py
```

4. Оновіть клавіатуру в `app/keyboards/language.py`

## Ліцензія

MIT

</details>

<div align="center">
  <h3>Crafted with ❤️ by a developer who understands Telegram bots</h3>
  
  <a href="https://github.com/mirvald-space/TeleForge/stargazers">
    <img src="https://img.shields.io/github/stars/mirvald-space/TeleForge.svg?style=social&label=Star&maxAge=2592000" alt="GitHub stars">
  </a>
  <a href="https://github.com/mirvald-space/TeleForge/network">
    <img src="https://img.shields.io/github/forks/mirvald-space/TeleForge.svg?style=social&label=Fork&maxAge=2592000" alt="GitHub forks">
  </a>
</div> 