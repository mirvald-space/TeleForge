import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не установлен в переменных окружения")

WEBHOOK_HOST = os.getenv("WEBHOOK_HOST")
if not WEBHOOK_HOST:
    raise ValueError("WEBHOOK_HOST не установлен в переменных окружения")

WEBHOOK_PATH = f"/webhook/{BOT_TOKEN}"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise ValueError("MONGO_URI не установлен в переменных окружения")

WEBAPP_HOST = os.getenv("WEBAPP_HOST", "0.0.0.0")
WEBAPP_PORT = int(os.getenv("WEBAPP_PORT", 8000))

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE", "en")
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
ADMIN_IDS = list(map(int, os.getenv("ADMIN_IDS", "").split(",")))

print(f"WEBHOOK_URL: {WEBHOOK_URL}")  # Для отладки, удалите после проверки
