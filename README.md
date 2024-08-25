# TeleForge: Universal Telegram Bot Template

TeleForge is a flexible and powerful template for creating Telegram bots using Python and the aiogram library. It provides a solid foundation with features like webhooks, MongoDB integration, multi-language support, and a plugin system.

## Features

- 🐍 Built with Python 3.9+ and asyncio
- 🤖 Uses aiogram 3.x for efficient Telegram Bot API interaction
- 🌐 Webhook support for responsive bot hosting
- 📊 MongoDB integration with motor for flexible data storage
- 🔌 Plugin system for easy extensibility
- 🌍 Multi-language support with YAML-based localization
- 🐳 Docker support for easy deployment
- 📊 Logging and monitoring capabilities
- 🧪 Unit testing support

## Prerequisites

- Python 3.9 or higher
- MongoDB
- Docker (optional, for containerized deployment)

## Quick Start

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

## Project Structure

```
teleforge/
├── bot/
│   ├── __init__.py
│   ├── config.py
│   ├── database/
│   ├── handlers/
│   ├── middlewares/
│   ├── plugins/
│   └── utils/
├── locales/
│   ├── en.yml
│   └── ru.yml
├── tests/
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── main.py
├── README.md
└── requirements.txt
```

## Customization

### Adding New Commands

1. Open `bot/handlers/user.py` or create a new file in the `handlers` directory.
2. Define a new async function for your command and use the appropriate decorator.
3. Register your new handler in `bot/handlers/__init__.py`.

### Creating Plugins

1. Create a new Python file in the `bot/plugins/` directory.
2. Implement your plugin logic, following the structure in `example_plugin.py`.
3. Register your plugin in `bot/plugins/__init__.py`.

### Adding New Languages

1. Create a new YAML file in the `locales/` directory (e.g., `de.yml` for German).
2. Copy the contents of `en.yml` and translate the messages.
3. Update `AVAILABLE_LANGUAGES` in `bot/handlers/user.py`.

## Running Tests

Execute the test suite with:

```
pytest tests/
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Happy coding with TeleForge! 🚀
