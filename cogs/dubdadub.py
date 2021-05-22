import discord
from discord.ext import commands


class DevCommands(commands.Cog, name='Developer Commands'):
	'''These are the developer commands'''

	def __init__(self, bot):
		self.bot = bot

	async def cog_check(self, ctx):  
		'''
		The default check for this cog whenever a command is used. Returns True if the command is allowed.
		'''
		return ctx.author.id == self.bot.author_id

	@commands.command(  # Decorator to declare where a command is.
		name='areload',  # Name of the command, defaults to function name.
		aliases=['arl']  # Aliases for the command.
	)  
	async def areload(self, ctx, cog):
		'''
		Reloads a cog.
		'''
		extensions = self.bot.extensions  # A list of the bot's cogs/extensions.
		if cog == 'all':  # Lets you reload all cogs at once
			for extension in extensions:
				self.bot.unload_extension(cog)
				self.bot.load_extension(cog)
			await ctx.send('Done')
		if cog in extensions:
			self.bot.unload_extension(cog)  # Unloads the cog
			self.bot.load_extension(cog)  # Loads the cog
			await ctx.send(f'Reloaded `{cog}`')  # Sends a message where content='Done'
		else:
			await ctx.send('`404` Cog cannot be found. Please check if you have loaded the cog in `MAIN.PY`')  # If the cog isn't found/loaded.
def setup(bot):
	bot.add_cog(DevCommands(bot))