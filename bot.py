from pyrogram import Client, filters
from src.config import BOT_TOKEN, API_ID, API_HASH
from src.handlers import (
    start_command,
    handle_callback,
    setup_command,
    handle_text_input,
    handle_channel_messages
)
import asyncio
import logging

logger = logging.getLogger(__name__)

# Initialize bot
app = Client(
    "text_replacement_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Register handlers
app.on_message(filters.command("start"))(start_command)
app.on_callback_query()(handle_callback)
app.on_message(filters.command("setup"))(setup_command)
app.on_message(filters.private & filters.text & ~filters.command)(handle_text_input)
app.on_message(filters.channel)(handle_channel_messages)

async def main():
    try:
        await app.start()
        logger.info("Bot started successfully!")
        await app.idle()
    except Exception as e:
        logger.error(f"Error starting bot: {e}")
    finally:
        await app.stop()

if __name__ == "__main__":
    asyncio.run(main())