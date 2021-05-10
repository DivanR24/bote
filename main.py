import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
from discord.ext.commands import Bot
from discord import Intents

intents = Intents.all()
bot = Bot(intents=intents, command_prefix='`')
client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
      return
    if message.content.lower() == 'ping':
        ping_list = ['pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', 'pong', "legendary ping pong ball"]
        response = random.choice(ping_list)
        await message.channel.send(response)
    if message.content.lower() == 'pong':
        ping_list = ['ping']
        response = random.choice(ping_list)
        await message.channel.send(response)
    if message.content == 'code':
        await message.author.send("https://repl.it/@DivanR24/Discord-Bot#main.py")






client.run(os.getenv('TOKEN'))     

keep_alive()