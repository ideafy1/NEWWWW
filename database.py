from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGODB_URI, DB_NAME

class Database:
    def __init__(self):
        self.client = AsyncIOMotorClient(MONGODB_URI)
        self.db = self.client[DB_NAME]
        self.replacements = self.db.replacements

    async def save_replacement(self, user_id: int, original_text: str, replacement_text: str):
        await self.replacements.update_one(
            {'user_id': user_id},
            {'$set': {
                'original_text': original_text,
                'replacement_text': replacement_text
            }},
            upsert=True
        )

    async def get_replacement(self, user_id: int):
        return await self.replacements.find_one({'user_id': user_id})