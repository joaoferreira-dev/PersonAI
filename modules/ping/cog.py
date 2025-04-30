from discord.ext import commands

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
        await ctx.reply('Pong!')

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Ping(bot))