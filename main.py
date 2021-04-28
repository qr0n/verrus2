import os
os.system("pip install discord-py-slash-command")
import discord
import discord_slash
from discord_slash import SlashCommand
import discord.utils
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
from replit import db
from keep_alive import keep_alive
from discord.ext import commands
import random
import json
import pyfiglet
import datetime
from pprint import pprint
#import pywhatkit as what

bot = commands.Bot(command_prefix= "V", case_insensitive=True)#help_command=None,
#intents=intents

client = discord.Client()

slash = SlashCommand(bot, sync_commands=True)
guild_ids = [759474157330366506, 781968220482699314]
secret_ids = [739887210186145813]
#grp = f"{os.environ.get(grop)}"

invis_av = "https://cdn.discordapp.com/attachments/796589554420678666/803703694146404462/TransparentProfilePic.png"

hello = ""
emb = discord.Embed(title=f"{hello}", description="🏓")
proggress = os.environ.get("progress")

bot.sniped_messages = {}
bot.author_id = 578789460141932555
web = os.environ.get("webhook")
web2 = os.environ.get("webhook2")
web3 = os.environ.get("webhook3")
web4 = os.environ.get("webhook4")
#bad_words = ["TEAST BOY", "<insert bad word>"]

#---------------------------------------------------events---------------------------------------------------------------

extensions = [
    'cogs.Main_Cog',
   # 'cogs.write_cog',
    #'cogs.entir',
    'cogs.bot2'
]

if __name__ == '__main__':
	for extension in extensions:
		bot.load_extension(extension)


@bot.event
async def on_ready():
	activity = discord.Game(name=f"Vhelp for help! | M4 {proggress}%",
	                        type=3)
	await bot.change_presence(status=discord.Status.do_not_disturb,
	                          activity=activity)
	print(f'online {bot.user.name}')




	#for word in bad_words:
	# if word in bad_words:
	#  await ctx.message.delete()


#--------events---------------------------------------------------------------
#---------------------------------------------------commands-------------------------------------------------------------


@bot.command()
async def helsp(ctx):
	embedVar = discord.Embed(title="Help command.",
	                         description="command tray type: `Default`",
	                         color=0x3A56D4)
	embedVar.add_field(name="`Vhelp`",
	                   value="Brings up this embed",
	                   inline=True)
	embedVar.add_field(name="`Vstat`",
	                   value="Brings up the bot's stats/outages/failiures",
	                   inline=True)
	embedVar.add_field(name="`Vadv`",
	                   value="Brings up advanced stats for Verrus bot",
	                   inline=True)
	embedVar.add_field(name="`Vchange`",
	                   value="Changes the bot's presence",
	                   inline=True)
	embedVar.add_field(name="`Vwhois`",
	                   value="Retrive information about a user",
	                   inline=True)
	embedVar.add_field(name="`Vlink`",
	                   value="Redirects the user to the verrus bot website",
	                   inline=True)
	embedVar.add_field(name="`Vwebstat`",
	                   value="Shows current status of the website",
	                   inline=True)
	embedVar.add_field(
	    name="`Vclear`",
	    value=
	    "clears messages from a channel, requires user to have manage messages",
	    inline=True)
	embedVar.add_field(name="`Vban`", value="Bans a user", inline=True)
	embedVar.add_field(name="`Vkick`", value="kicks a user", inline=True)
	embedVar.add_field(name="`Vafk`",
	                   value="sets a AFK message for the user",
	                   inline=True)
	embedVar.add_field(name="`Vlock`",
	                   value="Locks a mentioned channel",
	                   inline=True)
	embedVar.add_field(name="`Vunlock`",
	                   value="Unlocks a mentioned channel",
	                   inline=True)
	embedVar.add_field(name="`Vadd`", value="adds numbers", inline=True)
	embedVar.add_field(name="`Vsubtract`",
	                   value="subtracts 2 numbers",
	                   inline=True)
	embedVar.add_field(name="`Vmultiply`",
	                   value="multiplies 2 numbers",
	                   inline=True)
	embedVar.add_field(name="`Vquickcopy`",
	                   value="creates a message for the user to copy within a few seconds",
	                   inline=True)
	embedVar.add_field(name="`Vquickcopyhelp`",
	                   value="assists a user with quickcopy",
	                   inline=True)
	embedVar.add_field(
	    name="`Vannounce`",
	    value="announces a message in that spesific channel using a embed",
	    inline=True)
	embedVar.add_field(name="`Vascii`", value="cool text format", inline=True)
	await ctx.send(embed=embedVar)

@bot.command(aliases=["userinfo", "aboutuser"])
async def whois(ctx, member: discord.Member = None):
	member = ctx.author if not member else member
	roles = [role for role in member.roles]
	embed = discord.Embed(colour=member.colour,
	                      timestamp=ctx.message.created_at)
	embed.set_author(name=f"User info - {member}")
	embed.set_thumbnail(url=member.avatar_url)
	embed.set_footer(text=f"Requested by {ctx.author}",
	                 icon_url=ctx.author.avatar_url)
	embed.add_field(name="ID: ", value=member.id, inline=True)
	embed.add_field(
	    name="Created account at: ",
	    value=member.created_at.strftime("%a, %d %#B %Y, %I:%M %p UTC"))
	embed.add_field(
	    name="Joined server at: ",
	    value=member.joined_at.strftime("%a, %d %#B %Y, %I:%M %p UTC"))
	embed.add_field(name=f"Roles ({len(roles)})",
	                value=" ".join([role.mention for role in roles]),
	                inline=True)
	embed.add_field(name="Top role:",
	                value=member.top_role.mention,
	                inline=True)
	embed.add_field(name="Bot? ", value=member.bot, inline=True)
	await ctx.send(embed=embed)


@bot.command(aliases=["purge"])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, limit=3):
  if limit == "100":
    limit = "50"
    await ctx.channel.purge(limit=limit)
    await ctx.send("cleared! <a:yes:793883148215779328>")


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
	await member.kick(reason=reason)


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
	#await member.ban(reason=reason)
	ban_emb = discord.Embed(title=f"{member} was banned. From {ctx.guild.name}, for the reason of {reason} ")
	await ctx.send(embed=ban_emb)


@bot.command(aliases=["8ball", "8b"])
async def _8ball(ctx, *, question):
	responses = [
	    "It is certain.", "It is decidedly so.", "Without a doubt.",
	    "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
	    "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
	    "Reply hazy, try again.", "Ask again later.",
	    "Better not tell you now.", "Cannot predict now.",
	    "Concentrate and ask again.", "Don't count on it.", "My reply is no.",
	    "My sources say no.", "Outlook not so good.", "Very doubtful."
	]
	await ctx.reply(
	    f"Your question was `{question}` And to that I say\n {random.choice(responses)}"
	)


@bot.event
async def on_message_delete(message):
	bot.sniped_messages[message.guild.id] = (message.content, message.author,
	                                         message.channel.name,
	                                         message.created_at)


@bot.command()
async def snipe(ctx):
	try:
		contents, author, channel_name, time = bot.sniped_messages[
		    ctx.guild.id]

	except:
		await ctx.channel.send("Couldn't find a message to snipe!")
		return

	embed = discord.Embed(description=contents,
	                      color=discord.Color.blue(),
	                      timestamp=time)
	embed.set_author(name=f"{author.name}#{author.discriminator}",
	                 icon_url=author.avatar_url)
	embed.set_footer(text=f"Deleted in : #{channel_name}")

	await ctx.channel.send(embed=embed)

@bot.command()
async def time(ctx):
  time_test = discord.Embed(
      description=f"{ctx.message.created_at}"
      )
  await ctx.send(embed=time_test)

@bot.command(aliases=["+", "plus"])
async def add(ctx, left: int, right: int):
	await ctx.send(left + right)


@bot.command(aliases=["-", "subtract"])
async def minus(ctx, left: int, right: int):
	await ctx.send(left - right)


@bot.command(aliases=["×", "multip"])
async def multiply(ctx, left: int, right: int):
	await ctx.send(left * right)


@bot.command()
async def afk(ctx, *, reason=None):
	with open('afk.json', 'r') as f:
		afk = json.load(f)

	if not reason:
		reason = 'None'

	afk[f'{ctx.author.id}']['AFK'] = 'True'
	await ctx.send(f'<@{ctx.author.id}> I set your afk Reason: {reason}')

	with open('afk.json', 'w') as f:
		json.dump(afk, f)


@bot.command()
async def guess(ctx):
	print("guess command")


@bot.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel: discord.TextChannel = None, *, Reason=None):
	channel = channel or ctx.channel
	overwrite = channel.overwrites_for(ctx.guild.default_role)
	overwrite.send_messages = False
	await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
	embedAAAAB = discord.Embed(title="Channel locked.🔒",
	                           description=f"Reason: ```md\n{Reason}```",
	                           color=0x3A56D4)
	await ctx.send(embed=embedAAAAB)


@bot.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel: discord.TextChannel = None, Reason=None):
	channel = channel or ctx.channel
	overwrite = channel.overwrites_for(ctx.guild.default_role)
	overwrite.send_messages = None
	await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
	embedAAAAA = discord.Embed(title="Channel unlocked.🔓", color=0x3A56D4)
	await ctx.send(embed=embedAAAAA)


@bot.command(aliases=["embed"])
async def embedsay(ctx, *, arg):
	embed = discord.Embed(title=f"Embed message by {ctx.author.id}",
	                      description=arg)
	await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(manage_messages=True)
async def announce(ctx, *, arg):
	embedpog = discord.Embed(title="**Announcement**",
	                         description="**```md\n#" + arg + "```**",
	                         color=discord.Color.red())
	embedpog.set_footer(text=f"Announcement made by {ctx.author.id} ")
	await ctx.send(embed=embedpog)
	await ctx.message.delete()


@bot.command()
async def ascii(ctx, *, text=None):
	if text is None:
		await ctx.send("You must input some text to make into Ascii!")
		return
	result = pyfiglet.figlet_format(text)

	embed = discord.Embed(description=f"```{result}```")
	await ctx.send(embed=embed)


@bot.command()
async def moreinfo(ctx):
	await ctx.send("this contains crap that you should not worry about ")


@bot.command()
async def poldawadfrwwddwafgl(ctx, question, option1=None, option2=None):
	if option1 == None and option2 == None:
		await ctx.channel.purge(limit=1)
		message = await ctx.send(
		    f"```New poll: \n{question}```\n**✅ = Yes**\n**❎ = No**")
		await message.add_reaction('❎')
		await message.add_reaction('✅')
	elif option1 == None:
		await ctx.channel.purge(limit=1)
		message = await ctx.send(
		    f"```New poll: \n{question}```\n**✅ = {option1}**\n**❎ = No**")
		await message.add_reaction('❎')
		await message.add_reaction('✅')
	elif option2 == None:
		await ctx.channel.purge(limit=1)
		message = await ctx.send(
		    f"```New poll: \n{question}```\n**✅ = Yes**\n**❎ = {option2}**")
		await message.add_reaction('✅')
		await message.add_reaction('❎')
	else:
		await ctx.channel.purge(limit=1)
		message = await ctx.send(
		    f"```New poll: \n{question}```\n**✅ = {option1}**\n**❎ = {option2}**"
		)
		await message.add_reaction('❎')
		await message.add_reaction('❎')


@bot.command()
async def poll(ctx, *, question, option1=None, option2=None):
	embed = discord.Embed(
	    title="New poll!",
	    description=
	    f"```New poll: \n{question}```\n**:one: = {option1}**\n**:two: = {option2}**",
	    color=discord.Color.red())
	await ctx.send(embed=embed)
	message = await ctx.send(embed=embed)
	await message.add_reaction('1️⃣')
	await message.add_reaction('2️⃣')

@bot.command(pass_context=True)
async def join(ctx):
	channel = ctx.message.author.voice.voice_channel
	await bot.join_voice_channel(channel)


@bot.command(pass_context=True)
async def leave(ctx):
	await ctx.voice_client.disconnect()


@bot.command(aliases=["si"])
async def serverinfo(ctx):

	role_count = len(ctx.guild.roles)
	list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]
	staff_roles = ["[Redacted]"]

	embed2 = discord.Embed(timestamp=ctx.message.created_at,
	                       color=ctx.author.color)
	embed2.add_field(name='Name', value=f"{ctx.guild.name}", inline=True)
	embed2.add_field(name='Owner', value=f"{ctx.guild.owner}", inline=True)
	embed2.add_field(name='Verification Level',
	                 value=str(ctx.guild.verification_level),
	                 inline=True)
	embed2.add_field(name='Highest role',
	                 value=ctx.guild.roles[-2],
	                 inline=True)
	#embed2.add_field(name='Contributers:', value="[Redacted]#[Redacted]")

	for r in staff_roles:
		role = discord.utils.get(ctx.guild.roles, name=r)
		if role:
			members = '\n'.join([member.name
			                     for member in role.members]) or "None"
			embed2.add_field(name=role.name, value=members)

	embed2.add_field(name='Number of roles',
	                 value=str(role_count),
	                 inline=True)
	embed2.add_field(name='Number Of Members',
	                 value=ctx.guild.member_count,
	                 inline=True)
	##list_of_bots)))
	embed2.add_field(
	    name='Created At',
	    value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'),
	    inline=True)
	embed2.set_thumbnail(url=ctx.guild.icon_url)
	embed2.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
	#embed2.set_footer(text=f"{bot.user.name}{bot.user.name}", #icon_url=self.bot.user.avatar_url)

	await ctx.send(embed=embed2)


@bot.command()
async def server_guard(ctx):

	async with aiohttp.ClientSession() as session:
		webhook = Webhook.from_url(f'{web}',
		                           adapter=AsyncWebhookAdapter(session))
		await webhook.send(f'server guard has now been turned ', username='')




@bot.command(aliases=["wbp", "webhookp", "wbping"])
async def ping(ctx):
	async with aiohttp.ClientSession() as session:
		webhook = Webhook.from_url(f'{web}',
		                           adapter=AsyncWebhookAdapter(session))
		await webhook.send(embed=emb,
		                   username=f"Ping: {round(bot.latency * 1000)}ms",
		                   avatar_url=f"{invis_av}")

@bot.command()
async def mask(ctx, *, arg):
  
	async with aiohttp.ClientSession() as session:
		webhook = Webhook.from_url(f'{web}',
		                           adapter=AsyncWebhookAdapter(session))
		await webhook.send(f"{arg}",
		                   username=f"Masked",
		                   avatar_url=f"https://cdn.disc`rdapp.com/attachments/796589554420678666/803703694146404462/TransparentProfilePic.png")

@bot.command(aliases=["r1"])
async def rule1(ctx):
	await ctx.reply("✯   1. Respect all members. This is an online social media platform where people from across the world are being collected together. A chance to meet new strangers, be nice with them.")


@bot.command(aliases=["r2"])
async def rule2(ctx):
	await ctx.reply("✯   2. Listen to all staff members such as admins. our positions are important and we aim to do right by them and take care of the server. we worked hard to build it to what it is right now, so please do appreciate it. If a staff says not to do this, then don’t. If you have a complaint about one of my staff members then please do DM me about it.")


@bot.command(aliases=["r3"])
async def rule3(ctx):
	await ctx.reply(
	    "✯   3. Discrimination is not allowed at all. Being rude or mean to anyone is not okay. Please learn some manners and be polite. Swearing is allowed as long as it’s not offending someone massively."
	)


@bot.command(aliases=["r4"])
async def rule4(ctx):
	await ctx.reply("✯   4. Don’t leak private information of anyone without their permission. They have entrusted it with you for a reason. Keep the secrets and appreciate it. This will make you appear as trustworthy, and that decision is better.")


@bot.command(aliases=["r5"])
async def rule5(ctx):
	await ctx.reply(	    "✯   5. No usage of slurs. We don’t support this type of acts as it’s very offensive. Videos, pictures, and usernames containing slurs are included. Failure to do so, will result into an instant ban."
)



@bot.command(aliases=["r6"])
async def rule6(ctx):
	await ctx.reply(
	    "✯   6. Use each channel correctly. Take a look at the label and the names and use them for their right usage. Different channels are made for a reason."
	)


@bot.command(aliases=["r7"])
async def rule7(ctx):
	await ctx.reply(
	    "✯   7. Don’t spam nor ping random users without their permission, it can be annoying. and don’t spam in random channels. The “this isn’t spam I only sent it once in each minute’ excuse is dumb. If a staff members finds it as spam, then it is spam. Sending the same message over and over is considered that. Use the right channel for spamming such as #∥⋆··⋆➻🍁⌜spam⌟.")


@bot.command(aliases=["r8"])
async def rule8(ctx):
	await ctx.reply("✯   8. Don’t send nsfw content in other channels. Some people do not like seeing it and find it very disgusting. We made a role and a channel for the nsfw content, you’re more than welcome to post it there.. this also goes for the nsfw memes. Take your horny ass there.")


@bot.command(aliases=["r9"])
async def rule9(ctx):
	await ctx.reply("✯   9. Don’t send stupid weird messages or things. I mean seriously, be normal. If someone finds your messages offensive, then stop and don’t continue doing at it.")
	  
	  
@bot.command(aliases=["r10"])
async def rule10(ctx):
	await ctx.reply("✯   11. Causing fights is prohibited. If you came here looking for drama or troubles then go look somewhere else please. This isn’t made to entertain you. I know we have troublemakers in here, for those who are reading this.. be a good kid will you?. Those actions could offend someone and we don’t really appreciate it, so forget it.")
	
	
@bot.command(aliases=["r11"])
async def rule11(ctx):
	await ctx.reply("✯   10. Please do avoid religious and politic topics talk, as it sometimes make rage between members and causes troubles. We wouldn’t like for that to happen so please steer clear from it.")
	
	
@bot.command(aliases=["r12"])
async def rule12(ctx):
	await ctx.reply("✯   12. If a member in this server is harassing, or verbally abusing you in DMs, please do inform any of the staff members. We don’t support such acts and will try to make an action for it to stop. We promise to try our best in sorting it out.")
	
	
@bot.command(aliases=["r13"])
async def rule13(ctx):
	await ctx.reply ("✯   13. Don’t ask to be given any specific roles because it’s completely annoying. Maybe ask once, but spamming and whining about it isn’t cool. Grow up honestly.") 
	
	
@bot.command(aliases=["r14"])
async def rule14(ctx):
	await ctx.reply ("✯   14. Don’t cause riots. You may think you seem cool doing it, but it’s honestly disturbing. Planning to overthrow or elect someone to something is not funny. This is very annoying. Just stop.")
	
	
@bot.command(aliases=["r15"])
async def rule15(ctx):
	await ctx.reply("✯   15. Use your common sense. If you’re wondering what you’re gonna say next is offensive or not, just don’t say it. If you’re wondering about what you’re doing next is wrong or not, just don’t do it. We don’t need to start tolerating kids into what’s right or not. Learn it by yourself and do better.")
	
	
@bot.command(aliases=["r16"])
async def rule16(ctx):
	await ctx.reply ("✯   16. If we found an account that is only few days old in this server. We will require you to do a verification test. Failure to pass this test will result to a kick. Don’t ask why, we have many fake people with fake accounts running around, we’d like to steer clear of them.")
	
@bot.command(aliases=["r17"])
async def rule17(ctx):
	await ctx.reply ("✯   17. We have made a new program of person verification. It’s made to declare wether you’re a real person or not. You will go under tests, to prove you’re real. Sounds dumb I know, but it’s necessary. At the end of the trial you will be given a verified role. If you’re interested in undergoing it, tell a staff remember to assign you the  ‘@verification in process‘ role. You will have access to channels that will help you in learning more about it.")
	
@bot.command(aliases=["r18"])
async def rule18(ctx):
	await ctx.reply("✯   18. If you notice anyone breaking the rules, or is causing a mess please do inform the staff members. Ping @Queen and it would be sorted out.") 
	
@bot.command(aliases=["r19"])
async def rule19(ctx):
	await ctx.reply ("✯   19. Follow all the rules, it isn’t hard being a decent person.")


@bot.command(aliases=["r20"])
async def rule20(ctx):
	await ctx.reply ("✯   20. Have fun :]")
	
@bot.command(aliases=["ws1"])
async def warning1(ctx):
	await ctx.reply ("✾    1. If you break simple rules or do small offensive actions, the staff members will give you a verbal warning and a mute at first. Continuing with your stupid actions will result to an official warning. ")
	
	
@bot.command(aliases=["ws2"])
async def warning2(ctx):
	await ctx.reply ("✾    2. If you break massive rules or do very offensive actions, the staff members will give you an instant official warning. Refusing to listen and stop with result into either an instant ban or kick (according to how bad it is). ")
	
@bot.command(aliases=["ws3"])
async def warning3(ctx):
	await ctx.reply ("✾    3. You will receive a kick after getting three warnings. You can join, but if you receive two more warnings then you’ll get a ban from the server completely.")
	

@bot.command()
async def magic(ctx, *, arg):
  if arg == "test":
    await ctx.send("magic word is found :]")
  elif arg == "a":
    await ctx.send("k k kk  k k kk k k k")
  elif arg == "":
    await ctx.send("provide the argument -_-")
  else:
    await ctx.send("magic word is not found >:[")
    
@bot.command()
async def invite(ctx, arg):
	await ctx.send(
	    f"https://discord.com/api/oauth2/authorize?client_id={arg}&permissions=2147479543&scope=bot"
	)

@bot.command(aliases=["quickc", "qcopy", "qc"])
async def quickcopy(ctx, *, arg):
  e = discord.Embed(
    description=f"{arg}"
    )
  await ctx.send(embed=e)
  #await ctx.send(f" quick copy requested by: {ctx.author.mention}")

@bot.command(aliases=["hyperl", "hlink", "hl"])
async def hyperlink(ctx, option1, option2):
  e = discord.Embed(
    description=f"[{option1}]({option2})"
    )
  await ctx.send(embed=e)

@bot.command()
async def hyperlinkhelp(ctx):
  await ctx.send("Vhyperlink \n aliases Vhyperl, hlink, hl, is a type of link shortner that is customizable with text \n `Usage:` Vhyperlink <Text to click on> <link> addional info no spaces are allowed")

@bot.command(aliases=["developervision", "developerv", "dvision"])
async def dv(ctx, *, arg):
  dv = discord.Embed(
    description=f"\{arg}")
  await ctx.send(embed=dv)

@bot.command()
async def errus(ctx):
  print(".")

@bot.command(aliases=["qchelp"])
async def qch(ctx):
  await ctx.send("Vquickcopy is a utility command used to copy text quickly usage: `Vqc <text>` when you want to copy the text long press on the embed **DISCAIMER** quick copy currently only works on the mobile version of Discord")

@bot.command()
async def elimate(ctx):
  colors = ["<@&806409519147515905>", "<@&806409545475293224>", "<@&806409581264764928>", "<@&806409667470819358>", "<@&806409694125097029>", "<@&806409724877996073>","<@&806409755618050069>"]
  await ctx.send(f"{random.choice(colors)} is out GG!")

@bot.command(aliases=["h"])
@commands.has_permissions(manage_channels=True)
async def hide(ctx, channel: discord.TextChannel = None, *, Reason=None):
	channel = channel or ctx.channel
	overwrite = channel.overwrites_for(ctx.guild.default_role)
	overwrite.view_channel = False
	await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
	embedAAAAB = discord.Embed(title="Channel Hidden.➖",
	                           description=f"Reason: ```md\n{Reason}```",
	                           color=0x3A56D4)
	await ctx.send(embed=embedAAAAB)

@bot.command(aliases=["uh"])
@commands.has_permissions(manage_channels=True)
async def unhide(ctx, channel: discord.TextChannel = None, *, Reason=None):
	channel = channel or ctx.channel
	overwrite = channel.overwrites_for(ctx.guild.default_role)
	overwrite.view_channel = None
	await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
	embedAAAAB = discord.Embed(
    title="Channel Unhidden.👁️", 
    color=0x3A56D4)
	await ctx.send(embed=embedAAAAB)



@bot.command()
@commands.has_role("...")
async def off(ctx):
  await bot.logout()
  await ctx.send("place holder")


@bot.command(pass_context=True)
async def meme(ctx):
    embed = discord.Embed(title="Hideaki Meme", description="",color=discord.Colour.red())
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)

@bot.command()
async def store(ctx, arg):
  db[f"{ctx.author.id}"] = f"{arg}"
  await ctx.send("Your message has been registered! ")


@bot.command()
async def change_presence(ctx):
  presence= input("whats the presence you want to display?\n")
  activity = discord.Game(
    name=f"{presence}", type=3
  )
  await bot.change_presence(
    status=discord.Status.do_not_disturb,
    activity=activity
  )
  e = discord.Embed(
    title="**Console Message**",
    description=f'Presence changed to `"{presence}"`')
  await ctx.send(embed=e)

@bot.command()
async def input_test(ctx):
  m = input("he")
  if m == "?":
    await ctx.send("L")

@bot.command()
async def install(ctx, arg):
  await ctx.send("installing packge")
  os.system(f"pip install {arg}")
  await ctx.send("installed")

@bot.command()
async def uninstall(ctx, arg):
  await ctx.send("uninstalling package")
  os.system(f"pip uninstall {arg}")
  await ctx.send("are you sure? (Y/N)")

@bot.command()
async def send(ctx, *, arg):
  await ctx.send("Sending")
  #what.sendwhatmsg_to_group(f"{grp}", f"{arg}", 00,15)

@slash.slash(guild_ids=guild_ids)
async def complain(ctx, *, arg):
  complains = bot.get_channel(818829266967068702)
  embed1234 = discord.Embed(
    title="Complaint:",
    description=f"```{arg}```",
    color=0x3A56D4)
  await complains.send(embed=embed1234)

@bot.command()
async def fix(ctx):
  await ctx.send("Auto recovery mode")
  await ctx.send("Reinstaslling discord")
  os.system("pip install discord")
  await ctx.send("Installed")
  await ctx.send("Reinstaslling discord.py")
  os.system("pip install discord.py")
  await ctx.send("Installed")
  await ctx.send("Reinstaslling discord-py-slash-command")
  os.system("pip install discord-py-slash-command")
  await ctx.send("Installed")
  await ctx.send("Reinstaslling pyfiglet")
  os.system("pip install pyfiglet")
  await ctx.send("Installed")
  await ctx.send("Reinstaslling OS")
  os.system('pip install os')
  await ctx.send("Installed")
  await ctx.send("Package errors are fixed")

@bot.command()
async def translate(ctx, option1, option2=None, option3=None, option4=None, option5=None, option6=None):
  if option1.startswith("h"):
    h = "hi"
  await ctx.send(f"{h}")
  
@bot.command()
async def role(ctx, arg):
  await ctx.send(f"{dir(discord)}")

@bot.command()
async def t(ctx):
  a = os.system("pip install discord")
  await ctx.send(f"{a}")

@bot.command()
async def exe(ctx, *, arg):
  if arg == "pip uninstall":
    os.system("y")
  await ctx.send("yes")
  if arg == "pip install":
    await ctx.send("installed package")
  await ctx.send("working out your code")
  os.system(f"{arg}")
@bot.command()
async def e(ctx, option1, option2, arg):
  with open(f'{option1}', f'{option2}') as g:
    yes = json.load(g)

    yes[f"{arg}"]["yea"]
    await ctx.send(f"{yes}\n {g}")

@bot.event
async def on_slash_command_error(ctx, ex):
  
  log = bot.get_channel(801530936356503612)
  embed = discord.Embed(title="Slash command error")
  embed.add_field(name="The following exeption is the direct cause of the slash command to fail", value=f"{ex}\n[Slash Docs](https://discord-py-slash-command.readthedocs.io/en/latest/quickstart.html)")
  await log.send(embed=embed)
  print(ex)

@bot.event
async def on_command_error(ctx, error):
  log = bot.get_channel(801530936356503612)
  embed = discord.Embed(title="Command Error")
  embed.add_field(name="The following exeption was the direct cause for the command to fail",value=f"{error}\n [Docs](https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#)")
  await ctx.send(embed=embed)
  await log.send(embed=embed)
#-----------------------------------------Slash Commands---------------------------------------

@slash.slash(guild_ids=guild_ids)
async def getenv(ctx, Var):
  m = os.environ.get(f"{Var}")
  await ctx.send(content=f"{m}", hidden=True)

@slash.slash(name="premium", guild_ids=guild_ids)
async def _premium(ctx):
  if ctx.guild.id in guild_ids:
    await ctx.send(content="This guild is registered as a preminum guild!", hidden=True)
  else:
    await ctx.send(content="This is not a premium guild", hidden=True)

@slash.slash(name="save", guild_ids=guild_ids)
async def _save(ctx, arg):
  await ctx.send(content="message saved!", hidden=True)

@slash.slash(guild_ids=guild_ids)
async def hexe(ctx, *, arg):
  if arg.startswith("pip uninstall"):
     arg = None
  a = os.system(f"{arg}")
  await ctx.send("yes", hidden=True)
  if arg == "pip install":
    await ctx.send("installed package", hidden=True)
  await ctx.send(f"{a}", hidden=True)
  print(f"{ctx.author.name}, {arg}")

@slash.slash(guild_ids=guild_ids, description="locked to level 5")
@commands.has_role("...")
async def sudo(ctx, member : discord.Member, *, arg):
	async with aiohttp.ClientSession() as session:
		webhook = Webhook.from_url(f'{web}',
		                           adapter=AsyncWebhookAdapter(session))
		await webhook.send(f"{arg}",
		                   username=f"{member.display_name}",
		                   avatar_url=f"{member.avatar_url}")




@slash.slash(guild_ids=guild_ids)
#@commands.has_role("...")
async def mebot(ctx):
	async with aiohttp.ClientSession() as session:
		webhook = Webhook.from_url(f'{web}',
		                           adapter=AsyncWebhookAdapter(session))
		await webhook.send(f"temporaily disabled",
		                   username=f"{ctx.author.display_name}",
		                   avatar_url=f"{ctx.author.avatar_url}")

@bot.command()
async def edit(ctx, * , arg):    
    #files = ["exe1", "exe2", "exe3", "exe4", "exe5"]
    with open('empty.py', 'w') as y:
      y.write(f"import main\n{arg}\nmain()")
    await ctx.send("your code will be reviewed")

@slash.slash(guild_ids=guild_ids)

async def change(ctx, *, new_status=None):
	activity = discord.Game(name=f"{new_status}",
	                        type=3)
	await bot.change_presence(status=discord.Status.do_not_disturb,
	                          activity=activity)



#@bot.command()
#async def test(ctx):
 #       webhook = await ctx.channel.create_webhook(name=ctx.author.name)
  #      webhooks = await ctx.channel.webhooks()
   #     for webhook in webhooks:
    ##ezmessages", username=ctx.author.name, avatar_url=ctx.author.avatar_url)


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"loaded {extension}")


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"unloaded {extension}")

@bot.command()
async def reload(ctx, extension):
  bot.unload(f"cogs.{extension}")
  bot.load(f"cogs.{extension}")

@bot.command()
async def urls(ctx):
    wlist = []
    for w in await ctx.guild.webhooks():
        wlist.append(f"{w.name} - {w.url}")
    content = "\n".join(wlist)
    await ctx.send(content)

async def save_audit_logs(guild):
     with open(f'audit_logs_{guild.name}', 'w+') as f:
          async for entry in guild.audit_logs(limit=100):
               f.write('{0.user} did {0.action} to {0.target}'.format(entry))

@bot.command()
async def audit(ctx):
         await save_audit_logs(ctx.channel.guild)

keep_alive()
bot.run(os.environ.get('TOKEN'))



                