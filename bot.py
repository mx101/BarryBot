from utils import *

import os
import discord
from dotenv import load_dotenv
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    barryisms = [
        '#think',
        'along the way...',
        'Hey Band!',
        'Birthday!'
    ]

    if message.content == '!Barryism':
        response = random.choice(barryisms)
        await message.channel.send(response)

client.run(TOKEN)
