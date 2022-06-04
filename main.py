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

    async def on_member_join(self, member):
        guild = member.guild
        welcomeEmbed = discord.Embed(title=f'Welcome {member.name} to {guild.name}!', 
                                    description='Check out the server rules and join the conversation now!', 
                                    color=discord.Colour.random())
        welcomeEmbed.add_field(name='Invited by', value='Me', inline=True)
        welcomeEmbed.add_field(name='Account Created', value=f'{member.created_at}', inline=True)
        welcomeEmbed.add_field(name='Member Count', value=f'{guild.member_count}', inline=True)
        welcomeEmbed.set_thumbnail(url=member.avatar_url)
        if guild.system_channel is not None:
            await guild.system_channel.send(embed=welcomeEmbed)

intents = discord.Intents.default()
intents.messages = True
intents.members = True

client = MyClient(intents=intents)
client.run(os.getenv('TOKEN'))