import discord
import logging
import random
import os
from gamestate import GameState
import text
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

game = GameState()

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='join')
async def join(ctx):
    game.join(ctx.message.author.name)
    await ctx.send(str(ctx.message.author.name) + ' has joined!')

@bot.command(name='players')
async def check_players(ctx):
    await ctx.send(game.check_players())

@bot.command(name='begin')
async def start_game(ctx):
    await ctx.send(text.narrative())
    await ctx.send(text.points)
    game.game_start()
    #await ctx.send(text.rules)
    #await ctx.send(text.help)

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