# Telegram Bot Starter

<div align="center">
  <img src="https://img.shields.io/badge/python-3.9%2B-blue" alt="Python 3.9+">
  <img src="https://img.shields.io/badge/aiogram-3.x-blue" alt="aiogram 3.x">
  <img src="https://img.shields.io/badge/MongoDB-Ready-green" alt="MongoDB Ready">
  <img src="https://img.shields.io/badge/i18n-🇬🇧_🇷🇺_🇺🇦-orange" alt="i18n Support">
  <img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT License">
</div>

<details open>
<summary>English 🇬🇧</summary>

## Power-Up Your Telegram Bot Development

> Start building professional bots in minutes, not days!

A professional-grade template for Telegram bots based on aiogram 3.x. This template embraces clean architecture principles while providing essential features most Telegram bots need, eliminating repetitive boilerplate.

**This is not just another template.** It's a carefully crafted foundation with production-ready features that can scale from simple bots to complex applications.

### 🔥 Why This Template?

- **Developer Experience First**: Clear structure, easy to extend and maintain
- **Real-World Ready**: Includes auth, MongoDB integration, i18n, and more
- **Clean Architecture**: Properly separated concerns, testable and maintainable
- **International Support**: 🇬🇧 English, 🇷🇺 Russian, 🇺🇦 Ukrainian - add more easily
- **Performance Focused**: Async from the ground up with proper error handling

### ⚙️ Key Features

- **Full aiogram 3.x** support with middleware integration
- **MongoDB integration** with Motor (async driver)
- **Multi-language support** with proper i18n implementation
- **Command registration** and management
- **User management** with activity tracking
- **Throttling middleware** to prevent abuse
- **Clean project structure** with proper separation of concerns
- **Environment configuration** with validation

### 🚀 Getting Started

1. Clone this repository
   ```bash
   git clone https://github.com/yourusername/telegram-bot-starter
   cd telegram-bot-starter
   ```

2. Set up a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Compile translations
   ```bash
   python compile_translations.py
   ```

5. Launch MongoDB locally or use a remote instance

6. Create `.env` file with required environment variables (see `ENVIRONMENT.md`)

7. Run the bot
   ```bash
   python -m app
   ```

### 📂 Project Structure

```
├── app/                      # Main application package
│   ├── handlers/             # Message and command handlers
│   ├── middlewares/          # Middleware components
│   ├── database/             # Database integration
│   ├── keyboards/            # Reply and inline keyboards
│   ├── config/               # Configuration management
│   └── utils/                # Utility functions
├── locales/                  # Translation files
│   ├── en/                   # English translations
│   ├── ru/                   # Russian translations
│   └── uk/                   # Ukrainian translations
├── .env.example              # Environment variables example
└── compile_translations.py   # Helper for i18n compilation
```

### 🛠️ Customizing

The template is designed to be extended easily:

1. Add new handlers in `app/handlers/`
2. Create new keyboard layouts in `app/keyboards/`
3. Add more collections/models to `app/database/`
4. Extend the middleware system in `app/middlewares/`

### 🔗 License

MIT — free to use and modify. Attribution appreciated!

</details>

<details>
<summary>Русский 🇷🇺</summary>

## Ускорьте разработку Telegram-ботов

> Начните создавать профессиональных ботов за минуты, а не дни!

Профессиональный шаблон для разработки Telegram-ботов на основе aiogram 3.x. Этот шаблон следует принципам чистой архитектуры и предоставляет основные функции, необходимые большинству Telegram-ботов, избавляя от необходимости повторять шаблонный код.

**Это не просто очередной шаблон.** Это тщательно продуманная основа с готовыми для производства функциями, которые могут масштабироваться от простых ботов до сложных приложений.

### 🔥 Почему этот шаблон?

- **Опыт разработчика на первом месте**: Четкая структура, легко расширять и поддерживать
- **Готов к реальному использованию**: Включает аутентификацию, интеграцию с MongoDB, i18n и многое другое
- **Чистая архитектура**: Правильно разделенные компоненты, тестируемые и поддерживаемые
- **Международная поддержка**: 🇬🇧 Английский, 🇷🇺 Русский, 🇺🇦 Украинский - легко добавить еще
- **Ориентирован на производительность**: Асинхронность с самого начала с правильной обработкой ошибок

### ⚙️ Ключевые особенности

- **Полная поддержка aiogram 3.x** с интеграцией промежуточного ПО
- **Интеграция с MongoDB** с использованием Motor (асинхронный драйвер)
- **Многоязычная поддержка** с правильной реализацией i18n
- **Регистрация и управление командами**
- **Управление пользователями** с отслеживанием активности
- **Промежуточное ПО для ограничения частоты запросов** для предотвращения злоупотреблений
- **Чистая структура проекта** с правильным разделением обязанностей
- **Конфигурация среды** с валидацией

### 🚀 Начало работы

1. Клонировать этот репозиторий
   ```bash
   git clone https://github.com/yourusername/telegram-bot-starter
   cd telegram-bot-starter
   ```

2. Настроить виртуальное окружение
   ```bash
   python -m venv venv
   source venv/bin/activate  # На Windows: venv\Scripts\activate
   ```

3. Установить зависимости
   ```bash
   pip install -r requirements.txt
   ```

4. Скомпилировать переводы
   ```bash
   python compile_translations.py
   ```

5. Запустить MongoDB локально или использовать удаленный экземпляр

6. Создать файл `.env` с необходимыми переменными окружения (см. `ENVIRONMENT.md`)

7. Запустить бота
   ```bash
   python -m app
   ```

### 📂 Структура проекта

```
├── app/                      # Основной пакет приложения
│   ├── handlers/             # Обработчики сообщений и команд
│   ├── middlewares/          # Компоненты промежуточного ПО
│   ├── database/             # Интеграция с базой данных
│   ├── keyboards/            # Клавиатуры ответов и инлайн-клавиатуры
│   ├── config/               # Управління конфігурацією
│   └── utils/                # Служебные функции
├── locales/                  # Файлы переводов
│   ├── en/                   # Английские переводы
│   ├── ru/                   # Русские переводы
│   └── uk/                   # Украинские переводы
├── .env.example              # Пример переменных окружения
└── compile_translations.py   # Помощник для компиляции i18n
```

### 🛠️ Настройка

Шаблон разработан для легкого расширения:

1. Добавьте новые обработчики в `app/handlers/`
2. Создайте новые макеты клавиатур в `app/keyboards/`
3. Добавьте дополнительные коллекции/модели в `app/database/`
4. Расширяйте систему промежуточного ПЗ в `app/middlewares/`

### 🔗 Лицензия

MIT — свободно для использования и модификации. Атрибуция приветствуется!

</details>

<details>
<summary>Українська 🇺🇦</summary>

## Прискорте розробку Telegram-ботів

> Почніть створювати професійних ботів за хвилини, а не дні!

Професійний шаблон для розробки Telegram-ботів на основі aiogram 3.x. Цей шаблон дотримується принципів чистої архітектури та надає основні функції, необхідні більшості Telegram-ботів, позбавляючи від необхідності повторювати шаблонний код.

**Це не просто черговий шаблон.** Це ретельно продумана основа з готовими для виробництва функціями, які можуть масштабуватися від простих ботів до складних додатків.

### 🔥 Чому цей шаблон?

- **Досвід розробника на першому місці**: Чітка структура, легко розширювати та підтримувати
- **Готовий до реального використання**: Включає автентифікацію, інтеграцію з MongoDB, i18n та багато іншого
- **Чиста архітектура**: Правильно розділені компоненти, що тестуються та підтримуються
- **Міжнародна підтримка**: 🇬🇧 Англійська, 🇷🇺 Російська, 🇺🇦 Українська - легко додати ще
- **Орієнтований на продуктивність**: Асинхронність з самого початку з правильною обробкою помилок

### ⚙️ Ключові особливості

- **Повна підтримка aiogram 3.x** з інтеграцією проміжного ПЗ
- **Інтеграція з MongoDB** з використанням Motor (асинхронний драйвер)
- **Багатомовна підтримка** з правильною реалізацією i18n
- **Реєстрація та управління командами**
- **Управління користувачами** з відстеженням активності
- **Проміжне ПЗ для обмеження частоти запитів** для запобігання зловживанням
- **Чиста структура проекту** з правильним розподілом обов'язків
- **Конфігурація середовища** з валідацією

### 🚀 Початок роботи

1. Клонувати цей репозиторій
   ```bash
   git clone https://github.com/yourusername/telegram-bot-starter
   cd telegram-bot-starter
   ```

2. Налаштувати віртуальне оточення
   ```bash
   python -m venv venv
   source venv/bin/activate  # На Windows: venv\Scripts\activate
   ```

3. Встановити залежності
   ```bash
   pip install -r requirements.txt
   ```

4. Скомпілювати переклади
   ```bash
   python compile_translations.py
   ```

5. Запустити MongoDB локально або використовувати віддалений екземпляр

6. Створити файл `.env` з необхідними змінними оточення (див. `ENVIRONMENT.md`)

7. Запустити бота
   ```bash
   python -m app
   ```

### 📂 Структура проекту

```
├── app/                      # Основний пакет додатку
│   ├── handlers/             # Обробники повідомлень та команд
│   ├── middlewares/          # Компоненти проміжного ПЗ
│   ├── database/             # Інтеграція з базою даних
│   ├── keyboards/            # Клавіатури відповідей та інлайн-клавіатури
│   ├── config/               # Управління конфігурацією
│   └── utils/                # Службові функції
├── locales/                  # Файли перекладів
│   ├── en/                   # Англійські переклади
│   ├── ru/                   # Російські переклади
│   └── uk/                   # Українські переклади
├── .env.example              # Приклад змінних оточення
└── compile_translations.py   # Помічник для компіляції i18n
```

### 🛠️ Налаштування

Шаблон розроблено для легкого розширення:

1. Додайте нові обробники в `app/handlers/`
2. Створіть нові макети клавіатур у `app/keyboards/`
3. Додайте додаткові колекції/моделі в `app/database/`
4. Розширюйте систему проміжного ПЗ в `app/middlewares/`

### 🔗 Ліцензія

MIT — вільно для використання та модифікації. Атрибуція вітається!

</details>

---

<div align="center">
  <h3>Crafted with ❤️ by a developer who understands Telegram bots</h3>
  <p>Based on real-world experience and best practices</p>
</div> 