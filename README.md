# TeleForge: Universal Telegram Bot Template

TeleForge is a flexible and powerful template for creating Telegram bots of any complexity using Python and the aiogram library. It provides a solid foundation with features like webhooks, MongoDB integration, multi-language support, and a plugin system.

## 🌟 Features

- 🐍 Built with Python 3.9+ and asyncio
- 🤖 Uses aiogram 3.x for efficient Telegram Bot API interaction
- 🌐 Webhook support for responsive bot hosting
- 📊 MongoDB integration with motor and umongo for flexible data storage
- 🔌 Plugin system for easy extensibility
- 🌍 Multi-language support with YAML-based localization
- 🐳 Docker support for easy deployment
- 📊 Logging and monitoring capabilities
- 🧪 Unit testing with pytest
- 🔄 CI/CD ready with GitHub Actions configuration

## 📋 Prerequisites

- Python 3.9 or higher
- MongoDB
- Docker (optional, for containerized deployment)

## 🚀 Quick Start

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/teleforge.git
   cd teleforge
   ```

2. Create a virtual environment and install dependencies:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Set up your environment variables:

   - Copy `.env.example` to `.env`
   - Fill in your Telegram Bot Token, MongoDB URI, and other configuration details

4. Run the bot:
   ```
   python main.py
   ```

## 🐳 Running with Docker

1. Make sure Docker and Docker Compose are installed on your system.

2. Build the Docker image:

   ```
   docker-compose build
   ```

3. Run the bot:
   ```
   docker-compose up -d
   ```

## 🛠 Project Structure

```
teleforge/
├── .github/
│   └── workflows/
│       └── ci.yml
├── bot/
│   ├── __init__.py
│   ├── config.py
│   ├── database/
│   │   ├── __init__.py
│   │   └── models.py
│   ├── handlers/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   └── user.py
│   ├── middlewares/
│   │   ├── __init__.py
│   │   └── language.py
│   └── plugins/
│       ├── __init__.py
│       └── example_plugin.py
├── locales/
│   ├── en.yml
│   └── ru.yml
├── tests/
│   ├── __init__.py
│   └── test_handlers.py
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── main.py
├── README.md
└── requirements.txt
```

## 🔧 Customization

### Adding New Commands

1. Open `bot/handlers/user.py` or create a new file in the `handlers` directory.
2. Define a new async function for your command:

   ```python
   from aiogram import Router
   from aiogram.types import Message
   from aiogram.filters import Command

   router = Router()

   @router.message(Command("yourcommand"))
   async def cmd_yourcommand(message: Message):
       await message.reply("Your command response here")
   ```

3. Register your new handler in `bot/handlers/__init__.py`.

### Creating Plugins

1. Create a new Python file in the `bot/plugins/` directory.
2. Implement your plugin logic, following the structure in `example_plugin.py`.
3. Register your plugin in `bot/plugins/__init__.py`.

### Adding New Languages

1. Create a new YAML file in the `locales/` directory (e.g., `de.yml` for German).
2. Copy the contents of `en.yml` and translate the messages.
3. Update `AVAILABLE_LANGUAGES` in `bot/config.py`.

## 📊 Database Management

TeleForge uses MongoDB with motor and umongo. To work with the database:

1. Define your models in `bot/database/models.py`.
2. Use the models in your handlers or plugins:

   ```python
   from bot.database.models import User

   user = await User.find_one({"telegram_id": message.from_user.id})
   if not user:
       user = User(telegram_id=message.from_user.id)
       await user.commit()
   ```

## 🧪 Running Tests

Execute the test suite with:

```
pytest tests/
```

## 🔄 CI/CD

The project includes a GitHub Actions workflow (`.github/workflows/ci.yml`) that:

- Runs tests on multiple Python versions
- Performs linting checks
- Can be extended to include deployment steps

## 📚 Best Practices

- Keep your bot token and other sensitive information in the `.env` file and never commit it to the repository.
- Regularly update your dependencies to ensure security and benefit from the latest features.
- Write unit tests for new functionality to maintain code quality.
- Use meaningful commit messages and follow Git best practices.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

If you encounter any problems or have any questions, please open an issue in the GitHub repository.

---

Happy coding with TeleForge! 🚀
