from discord.ext import commands
import os
import google.generativeai as genai


class GenAI(commands.Cog, name="Gen AI"):
    """
    A cog for interacting with a generative AI model.
    """

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def prompt(self, ctx: commands.Context, *, message: str) -> None:
        """
        Prompt command to send a message to the generative AI model.

        This command will take a message from the user and send it to the model.

        The model will then respond with a generated message.
        """
        genai.configure(api_key=os.getenv('GENAI_API_KEY'))
        model = genai.GenerativeModel('gemini-2.0-flash')

        response = model.generate_content(message)
        await ctx.reply(response.text)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(GenAI(bot))