import discord
import logging
import random
import os
#structure copied from https://discordpy.readthedocs.io/en/latest/quickstart.html

#this block of code is for debugging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

from discord.ext import commands
#3 lines below copied from https://realpython.com/how-to-make-a-discord-bot-python/
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='join')
async def _test(ctx):
    #response = ' has joined!' #str(ctx.author) + " has joined!"
    await ctx.send(str(ctx.message.author.name))

@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        # else:
        #     raise

#TOKEN is an "environment variable" on my PC. So if you want to run this, let me know and I'll send the required info.
bot.run(TOKEN)
#running this file will activate the bot