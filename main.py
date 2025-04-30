import discord
from discord.ext import commands

import google.generativeai as genai

import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv('GENAI_API_KEY'))
model = genai.GenerativeModel('gemini-2.0-flash')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready() -> None:
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    print('------')

@bot.command()
async def ping(ctx: commands.Context) -> None:
    await ctx.reply('Pong!')

@bot.command()
async def chat(ctx: commands.Context, *, message: str) -> None:
    response = model.generate_content(message)
    await ctx.reply(response.text)



bot.run(token=os.getenv('BOT_TOKEN'))