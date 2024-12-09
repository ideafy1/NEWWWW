from motor.motor_asyncio import AsyncIOMotorClient
from src.config import MONGODB_URI, DB_NAME
import logging

logger = logging.getLogger(__name__)

class Database:
    def __init__(self):
        try:
            self.client = AsyncIOMotorClient(MONGODB_URI)
            self.db = self.client[DB_NAME]
            self.replacements = self.db.replacements
            logger.info("Database connection established successfully")
        except Exception as e:
            logger.error(f"Database connection error: {e}")
            raise

    async def save_replacement(self, user_id: int, original_text: str, replacement_text: str):
        try:
            await self.replacements.update_one(
                {'user_id': user_id},
                {'$set': {
                    'original_text': original_text,
                    'replacement_text': replacement_text
                }},
                upsert=True
            )
        except Exception as e:
            logger.error(f"Error saving replacement: {e}")
            raise

    async def get_replacement(self, user_id: int):
        try:
            return await self.replacements.find_one({'user_id': user_id})
        except Exception as e:
            logger.error(f"Error getting replacement: {e}")
            raise

db = Database()