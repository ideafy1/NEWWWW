from pyrogram import Client
from pyrogram.types import Message
from src.states import UserState, user_states

async def setup_command(client: Client, message: Message):
    user_id = message.from_user.id
    user_states[user_id] = UserState.WAITING_FOR_ORIGINAL
    await message.reply_text(
        "📝 Please enter the text that you want to replace:"
    )