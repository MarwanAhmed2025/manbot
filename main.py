import os
import asyncio
from telethon import TelegramClient, events
from telethon.tl.functions.messages import ImportChatInviteRequest

API_ID = int(os.getenv('35469979'))
API_HASH = os.getenv('896f98c871cafe2f6d064bbcbdd4930a')
SESSION_NAME = 'session'

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.reply("اهلا! ابعتلي لينك دعوة جروب وانا هدخل فيه \nمثال: https://t.me/+xxxxxxx")

@client.on(events.NewMessage(pattern='https://t.me/\\+'))
async def join_group(event):
    link = event.text
    hash = link.split('+')[1]
    try:
        await client(ImportChatInviteRequest(hash))
        await event.reply("✅ تم الانضمام للجروب بنجاح")
    except Exception as e:
        await event.reply(f"❌ فشل الانضمام: {str(e)}")

print("Bot is running...")
client.start()
client.run_until_disconnected()
