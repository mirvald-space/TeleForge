from motor.motor_asyncio import AsyncIOMotorClient

from bot.config import MONGO_URI

from .models import User

client = AsyncIOMotorClient(MONGO_URI)
db = client.get_default_database()


async def init_db():
    await db[User.collection_name].create_index("telegram_id", unique=True)


async def get_user(telegram_id):
    return await User.find_one(db, {"telegram_id": telegram_id})


async def create_user(user_data):
    return await User.create(db, user_data)


async def update_user(telegram_id, update_data):
    return await User.update(db, {"telegram_id": telegram_id}, {"$set": update_data})
