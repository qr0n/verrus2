import discord
import asyncio
from discord.ext import commands

class cog_name(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@commands.command(name="hac")
async def _a(self, ctx):
  await self.bot.say("yea")

def setup(bot):
    bot.add_cog(cog_name(bot))