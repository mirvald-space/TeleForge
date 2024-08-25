# bot/config.py
import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_IDS = list(map(int, os.getenv("ADMIN_IDS", "").split(",")))
MONGO_URI = os.getenv("MONGO_URI")

# Webhook configuration
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
WEBHOOK_HOST = os.getenv("WEBHOOK_HOST")
WEBHOOK_PATH = os.getenv("WEBHOOK_PATH")
WEBAPP_HOST = os.getenv("WEBAPP_HOST", "0.0.0.0")
WEBAPP_PORT = int(os.getenv("WEBAPP_PORT", 8000))

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE", "en")
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
