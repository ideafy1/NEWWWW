from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from src.states import UserState, user_states
from src.database import db
import logging

logger = logging.getLogger(__name__)

async def handle_text_input(client: Client, message: Message):
    try:
        user_id = message.from_user.id
        
        if user_id not in user_states:
            await message.reply_text("Please use /setup to start the configuration.")
            return

        if user_states[user_id] == UserState.WAITING_FOR_ORIGINAL:
            user_states[user_id] = UserState.WAITING_FOR_REPLACEMENT
            await db.save_replacement(user_id, message.text, "")
            await message.reply_text(
                "✅ Original text saved!\n\n"
                "Now, enter the text that you want to see instead:"
            )
        
        elif user_states[user_id] == UserState.WAITING_FOR_REPLACEMENT:
            original_data = await db.get_replacement(user_id)
            await db.save_replacement(user_id, original_data['original_text'], message.text)
            del user_states[user_id]
            
            keyboard = InlineKeyboardMarkup([[
                InlineKeyboardButton("🔄 Update Configuration", callback_data="setup")
            ]])
            
            await message.reply_text(
                "✅ Setup complete!\n\n"
                f"I will replace:\n"
                f"'{original_data['original_text']}'\n"
                f"with:\n"
                f"'{message.text}'\n\n"
                "Make sure to add me as an administrator in your channel!",
                reply_markup=keyboard
            )
    except Exception as e:
        logger.error(f"Error in handle_text_input: {e}")
        await message.reply_text("❌ An error occurred. Please try again.")