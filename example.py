import discord
import logging
import os
#structure copied from https://discordpy.readthedocs.io/en/latest/quickstart.html

#3 lines below copied from https://realpython.com/how-to-make-a-discord-bot-python/
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


#this block of code is for debugging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

#client variable handles all events
client = discord.Client()



#the bot handles different events that it receives from the client
@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD) #finds predetermined guild from .env
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return
#if you type $hello the bot will return Hello!
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    elif message.content == 'raise-exception':
        raise discord.DiscordException

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

#TOKEN is an "environment variable" on my PC. So if you want to run this, let me know and I'll send the required info.
client.run(TOKEN)
#running this file will activate the bot