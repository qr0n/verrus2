import discord
import asyncio
import aiohttp
from discord.ext import commands

class cog_name(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@commands.command(name="ahac", pass_context=True)
async def _a(self, ctx):
  await self.bot.say("yea")

@commands.command()
async def urban(self, *, search_terms : str):
        """Urban Dictionary search"""
        search_terms = search_terms.split(" ")
        search_terms = "+".join(search_terms)
        search = "http://api.urbandictionary.com/v0/define?term=" + search_terms
        try:
            async with aiohttp.get(search) as r:
                result = await r.json()
            if result["list"] != []:
                definition = result['list'][0]['definition']
                example = result['list'][0]['example']
                await self.bot.say("**Definition:** " + definition + "\n\n" + "**Example:** " + example )
            else:
                await self.bot.say("Your search terms gave no results.")
        except:
            await self.bot.say("Error.")

def setup(bot):
    bot.add_cog(cog_name(bot))