import os
from dotenv import load_dotenv
from telethon import TelegramClient, events

# Load environment variables
load_dotenv()

# Initialize Telegram Client
bot = TelegramClient(
    'auto_approve_bot',
    api_id=int(os.getenv("API_ID")),
    api_hash=os.getenv("API_HASH")
).start(bot_token=os.getenv("BOT_TOKEN"))

# Event handler for join requests
@bot.on(events.ChatRequest(chats=[]))  # Empty list means all allowed chats
async def handle_join_request(event):
    try:
        # Automatically approve join request
        await event.approve()
        print(f"Approved join request from user {event.user_id} in channel {event.chat_id}")
    except Exception as e:
        print(f"Error approving request: {str(e)}")

# Start the bot
print("Bot is running...")
bot.run_until_disconnected()