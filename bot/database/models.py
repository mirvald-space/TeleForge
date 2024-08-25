from motor.motor_asyncio import AsyncIOMotorDatabase


class User:
    collection_name = 'users'

    @classmethod
    async def find_one(cls, db: AsyncIOMotorDatabase, filter):
        return await db[cls.collection_name].find_one(filter)

    @classmethod
    async def create(cls, db: AsyncIOMotorDatabase, user_data):
        result = await db[cls.collection_name].insert_one(user_data)
        return result.inserted_id

    @classmethod
    async def update(cls, db: AsyncIOMotorDatabase, filter, update):
        return await db[cls.collection_name].update_one(filter, update)
