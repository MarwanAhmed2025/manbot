import asyncio
from telethon import TelegramClient, events
from telethon.tl.functions.messages import ImportChatInviteRequest

API_ID = 35469979
API_HASH = "896f98c871cafe2f6d064bbcbdd4930a"

client = TelegramClient('session', API_ID, API_HASH) # هيقرا session.session تلقائي

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.reply("شغال! ابعتلي لينك +")

@client.on(events.NewMessage(pattern='https://t.me/\\+'))
async def join_group(event):
    hash = event.text.split('+')[1]
    try:
        await client(ImportChatInviteRequest(hash))
        await event.reply("✅ دخلت الجروب")
    except Exception as e:
        await event.reply(f"❌ {e}")

client.start()
client.run_until_disconnected()
