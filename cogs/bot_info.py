from discord.ext import commands
from discord import app_commands, Interaction

class BotInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="bot_info", description="Odkaz na repozitář bota.")
    async def botinfo(self, interaction: Interaction):
        await interaction.response.send_message("https://github.com/gr3i/BizzyBot", ephemeral=False)

async def setup(bot):
    await bot.add_cog(BotInfo(bot))

