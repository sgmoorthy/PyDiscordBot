import os

import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_member_join(member):
    await memeber.create_dm()
    await member.dm_channel.send(
        f'Hi {memeber.name} , nameshtey and welcome to Viyomam BOT!'
    )


client.run(token)