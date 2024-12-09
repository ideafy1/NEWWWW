from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

async def start_command(client: Client, message: Message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔧 Setup Text Replacement", callback_data="setup")],
        [InlineKeyboardButton("ℹ️ Help", callback_data="help")]
    ])
    
    await message.reply_text(
        "👋 Welcome to the Text Replacement Bot!\n\n"
        "I can help you automatically replace text in your channel messages.\n"
        "Click the button below to get started!",
        reply_markup=keyboard
    )