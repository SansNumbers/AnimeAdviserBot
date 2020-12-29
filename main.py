import os
import random

#from keep_alive import keep_alive

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='qwerty', help='Shows different words.')
async def nine_nine(ctx):
    man_words = ['manovec','well played']

    response = random.choice(man_words)
    await ctx.send(response)

@bot.command()
async def test(ctx, *args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))

#keep_alive()
bot.run(TOKEN)