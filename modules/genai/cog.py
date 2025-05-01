from discord.ext import commands
import os
import google.generativeai as genai


class GenAI(commands.Cog, name="Gen AI"):
    """
    A cog for interacting with a generative AI model.
    """

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        genai.configure(api_key=os.getenv('GENAI_API_KEY'))
        self.model = genai.GenerativeModel('gemini-2.0-flash')

    @commands.command()
    async def prompt(self, ctx: commands.Context, *, message: str) -> None:
        """
        Prompt command to send a message to the generative AI model.
        """
        try:
            # Send an initial message
            sent_message = await ctx.reply("Processando sua solicitação, por favor aguarde...")

            # Generate content in streaming mode with a token limit
            response = self.model.generate_content(
                message + '(limit of 4000 characters)',
                stream=True
            )

            # Initialize the message with the first chunk
            new_message_content = ""
            chunk_buffer = []

            for chunk in response:
                chunk_buffer.append(chunk.text)
                if len(chunk_buffer) >= 3:  # Update every 3 chunks
                    new_message_content += ''.join(chunk_buffer)
                    await sent_message.edit(content=new_message_content)
                    chunk_buffer = []

            # Update with any remaining chunks
            if chunk_buffer:
                new_message_content += ''.join(chunk_buffer)
                await sent_message.edit(content=new_message_content)

        except Exception as e:
            print(f"Error: {e}")
            await ctx.reply("Ocorreu um erro ao processar sua solicitação. Tente novamente mais tarde.")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(GenAI(bot))