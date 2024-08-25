from motor.motor_asyncio import AsyncIOMotorClient

from bot.config import MONGO_URI

client = AsyncIOMotorClient(MONGO_URI)
db = client.teleforge_db


async def init_db():
    # Create indexes or perform any other initialization
    await db.users.create_index("telegram_id", unique=True)
