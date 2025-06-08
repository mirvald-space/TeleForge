"""
MongoDB connection module
"""
import logging
from typing import Optional
from urllib.parse import urlparse

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from app.config.settings import settings

# MongoDB client instance
client: Optional[AsyncIOMotorClient] = None
db: Optional[AsyncIOMotorDatabase] = None


async def setup_mongodb() -> None:
    """Initialize MongoDB connection"""
    global client, db
    try:
        # Create MongoDB client
        logging.info("Connecting to MongoDB...")
        client = AsyncIOMotorClient(settings.mongodb_uri)
        
        # Get database from URI - parse it properly
        parsed_uri = urlparse(settings.mongodb_uri)
        db_name = parsed_uri.path.lstrip('/')
        
        # If no database name in URI or it's empty, use a default name
        if not db_name:
            db_name = "tg_bot"
            logging.warning(f"No database name found in URI. Using default: {db_name}")
        
        db = client[db_name]
        
        # Ping database to verify connection
        await client.admin.command("ping")
        logging.info(f"Connected to MongoDB (database: {db_name})")
    except Exception as e:
        logging.error(f"Failed to connect to MongoDB: {e}")
        raise


async def close_mongodb_connection() -> None:
    """Close MongoDB connection"""
    global client
    if client:
        logging.info("Closing MongoDB connection...")
        client.close()
        logging.info("MongoDB connection closed")


# Collection helpers
def get_users_collection():
    """Get users collection"""
    return db.users


def get_settings_collection():
    """Get settings collection"""
    return db.settings 