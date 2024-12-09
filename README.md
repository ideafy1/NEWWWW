# Telegram Text Replacement Bot

This bot automatically replaces specified text in channel messages.

## Setup Instructions

1. Create a `.env` file with your credentials (see `.env.example`)
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the bot:
   ```
   python bot.py
   ```

## Usage

1. Start the bot with `/start`
2. Use `/setup` to configure text replacement
3. Add the bot as an administrator to your channel
4. The bot will automatically replace text in all channel messages

## Security Notes

- Keep your `.env` file secure and never share your credentials
- Only channel administrators can use the bot
- The bot requires administrator privileges in the channel