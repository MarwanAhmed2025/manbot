import os
from telethon import TelegramClient, events
API_ID=int("35469979")
API_HASH="896f98c871cafe2f6d064bbcbdd4930a"
BOT_TOKEN="8764144018:AAEafolKUYuUGmuH3mQaHX6Tc77GESCr9HA"
client=TelegramClient('s',API_ID,API_HASH).start(bot_token=BOT_TOKEN)
@client.on(events.NewMessage(pattern='/start'))
async def s(e):await e.reply("ok")
client.run_until_disconnected()
