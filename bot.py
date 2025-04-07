import os
from dotenv import load_dotenv
from telethon import TelegramClient, events
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from telethon.tl.types import UpdateBotChatInviteRequester

# Load environment variables
load_dotenv()

# Initialize Telegram Client
bot = TelegramClient(
    'auto_approve_bot',
    api_id=int(os.getenv("API_ID")),
    api_hash=os.getenv("API_HASH")
).start(bot_token=os.getenv("BOT_TOKEN"))

@bot.on(events.Raw(types=UpdateBotChatInviteRequester))
async def handle_join_request(event):
    try:
        # Approve the join request
        await bot(GetBotCallbackAnswerRequest(
            peer=event.peer,
            data=event.user_id
        ))
        print(f"Approved join request from user {event.user_id} in channel {event.peer.channel_id}")
    except Exception as e:
        print(f"Error approving request: {str(e)}")

print("Bot is running...")
bot.run_until_disconnected()
