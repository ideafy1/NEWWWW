from pyrogram import Client
from pyrogram.types import Message
from src.config import ADMIN_ID
from src.database import db
import logging

logger = logging.getLogger(__name__)

async def handle_channel_messages(client: Client, message: Message):
    try:
        admin_data = await db.get_replacement(int(ADMIN_ID))
        if not admin_data:
            return

        if message.text and admin_data['original_text'] in message.text:
            new_text = message.text.replace(
                admin_data['original_text'],
                admin_data['replacement_text']
            )
            await message.edit_text(new_text)
    except Exception as e:
        logger.error(f"Error in handle_channel_messages: {e}")