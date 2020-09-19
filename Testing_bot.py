import os

import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
my_guild = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event

async def on_ready():
    for guild in client.guilds:
        if guild.name == my_guild:
            break
    
    print (f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id:{guild.id})')
    
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Member:\n - {members}')
            


client.run(token)