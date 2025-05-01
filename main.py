import os
import asyncio
from dotenv import load_dotenv
from discord import Intents
from discord.ext import commands
from src.utils.logger import logger


async def main() -> None:
    load_dotenv()
    intents = Intents.all()
    client = commands.Bot(command_prefix=os.getenv('BOT_PREFIX'), intents=intents)

    @client.event
    async def on_ready() -> None:
        print(f'Logged in as {client.user.name} - {client.user.id}')
        print('------')

    for folder in os.listdir('modules'):
        if os.path.exists(os.path.join('modules', folder, 'cog.py')):
            logger.info(f'Loading {folder} cog...')
            await client.load_extension(f'modules.{folder}.cog')

    await client.start(os.getenv('BOT_TOKEN'))
    logger.info('Bot started successfully!')

if __name__ == '__main__':
    asyncio.run(main())