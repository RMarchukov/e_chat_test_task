import os
import asyncio
from dotenv import load_dotenv
from telethon import TelegramClient


load_dotenv()

TELEGRAM_API_ID = os.environ.get("TELEGRAM_API_ID")
TELEGRAM_API_HASH = os.environ.get("TELEGRAM_API_HASH")
TELEGRAM_BOT_ID = os.environ.get("TELEGRAM_BOT_ID")


async def get_telegram_messages():
    client = TelegramClient('test', int(TELEGRAM_API_ID), TELEGRAM_API_HASH)
    await client.start()
    bot = await client.get_entity(int(TELEGRAM_BOT_ID))
    all_messages = await client.get_messages(bot, limit=1000)
    return all_messages


messages = asyncio.run(get_telegram_messages())
last_message = messages[0].text
for message in reversed(messages):
    print(message.text)
print(last_message)
