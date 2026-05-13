import asyncio
import requests
from telethon import TelegramClient, events

# Telegram API credentials
api_id = 123456
api_hash = "YOUR_API_HASH"

# Telegram group username
GROUP_NAME = "بورصة بالعربي"

# n8n webhook URL
N8N_WEBHOOK_URL = "https://your-n8n-url/webhook/trading"

client = TelegramClient("session", api_id, api_hash)

@client.on(events.NewMessage(chats=GROUP_NAME))
async def handler(event):
    text = event.message.message

    if not text:
        return

    print("New message:", text)

    data = {
        "message": text,
        "chat_id": event.chat_id,
        "message_id": event.message.id
    }

    try:
        response = requests.post(
            N8N_WEBHOOK_URL,
            json=data,
            timeout=10
        )

        print("Sent to n8n:", response.status_code)

    except Exception as e:
        print("Error:", e)

async def main():
    print("Starting Telegram Listener...")

    await client.start()

    print("Bot is running...")

    await client.run_until_disconnected()

asyncio.run(main())
