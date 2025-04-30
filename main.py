import os
import asyncio
from dotenv import load_dotenv
from discord import Intents
from discord.ext import commands


async def main() -> None:
    load_dotenv()
    intents = Intents.all()
    client = commands.Bot(command_prefix='!', intents=intents)

    @client.event
    async def on_ready() -> None:
        print(f'Logged in as {client.user.name} - {client.user.id}')
        print('------')

    for folder in os.listdir('modules'):
        if os.path.exists(os.path.join('modules', folder, 'cog.py')):
            await client.load_extension(f'modules.{folder}.cog')

    await client.start(os.getenv('BOT_TOKEN'))

if __name__ == '__main__':
    asyncio.run(main())