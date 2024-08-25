from mongo import Document, Instance, fields
from motor.motor_asyncio import AsyncIOMotorDatabase

instance = Instance()


@instance.register
class User(Document):
    telegram_id = fields.IntField(required=True, unique=True)
    language = fields.StrField(default="en")

    class Meta:
        collection_name = "users"


def init_models(database: AsyncIOMotorDatabase):
    instance.set_db(database)
