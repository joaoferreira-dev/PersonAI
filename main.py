import discord
from discord.ext import commands

import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    print('------')

@bot.command()
async def ping(ctx):
    await ctx.reply('Pong!')


bot.run(token=os.getenv('BOT_TOKEN'))