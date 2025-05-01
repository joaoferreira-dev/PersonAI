from discord.ext import commands
from src.utils.logger import logger

class Ping(commands.Cog, name="Ping"):
    """
    A simple ping command to check if the bot is working.
    """

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context) -> None:
        """
        Ping command to check if the bot is working.
        """
        logger.info(f"Ping command called by {ctx.author.name}")
        await ctx.reply('Pong!')

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Ping(bot))