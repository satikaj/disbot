import discord
import os
from dotenv import load_dotenv

load_dotenv()

class MyClient(discord.Client):
    async def on_ready(self):
        print('***')
        print(f'Logged in as {self.user}')
        print('***')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content.startswith('.hello'):
            await message.reply('Hello!', mention_author=True)

intents = discord.Intents.default()
intents.messages = True

client = MyClient(intents=intents)
client.run(os.getenv('TOKEN'))