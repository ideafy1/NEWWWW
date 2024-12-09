from pyrogram import Client
from pyrogram.types import CallbackQuery
from src.states import UserState, user_states

async def handle_callback(client: Client, callback_query: CallbackQuery):
    if callback_query.data == "setup":
        user_id = callback_query.from_user.id
        user_states[user_id] = UserState.WAITING_FOR_ORIGINAL
        await callback_query.message.reply_text(
            "📝 Please enter the text that you want to replace:"
        )
    elif callback_query.data == "help":
        await callback_query.message.reply_text(
            "📖 How to use this bot:\n\n"
            "1. Use /setup to start configuration\n"
            "2. Enter the text you want to replace\n"
            "3. Enter the new text\n"
            "4. Add the bot to your channel as admin\n"
            "5. The bot will automatically replace text in all messages\n\n"
            "Need help? Contact @YourUsername"
        )