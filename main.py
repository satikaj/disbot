import discord
import os

intents = discord.Intents(messages=True)

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('.hello'):
        await message.channel.send('Hello!', mention_author=True)

client.run(os.getenv('TOKEN'))