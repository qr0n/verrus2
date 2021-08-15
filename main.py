import discord
from discord import Client
import discord_buttons
from discord_buttons import DiscordButton, Button, ButtonStyle, InteractionType
import discord.ext
import os
import contextlib
import io
from pathlib import Path # For paths
import platform # For stats
import logging
import textwrap
import rsap
from rsap import RSAP
import wikipedia
os.system("pip install chatbotAI")
import chatbot
from chatbot import Chat, register_call
from traceback import format_exception
os.system("pip install discord-py-slash-command")
import discord_slash
from discord_slash import SlashCommand
import discord.utils
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
from replit import db
from keep_alive import keep_alive
from discord.ext import commands, tasks
import random
import json
import pyfiglet
import datetime as dt
import asyncio
from Pag import Pag
import aiohttp
from asyncio import sleep as s
#import pywhatkit as what
#os.system("pip install translator")
from translate import Translator
import typing
#from weather import weather as w
#from main2 import main2 as m3
intents = discord.Intents.default()
intents.members = True
#import yes_no_dialo
Vprefixes = ["V", "#V", "@V", "!V", "^V"]
prefix = ["#", "!", "@", "%", "^"]

bot = commands.Bot(command_prefix="V", case_insensitive=True, intents=intents, reconnect=True,)#help_command=None,
#intents=intents
ddb = DiscordButton(bot)
client = discord.Client()
bo = RSAP(f"{os.environ.get('api')}", bot_name="Verrus", dev_name="Infinity Iron", type="unstable")
slash = SlashCommand(bot, sync_commands=True)
guild_ids = [759474157330366506, 781968220482699314]

#grp = f"{os.environ.get(grop)}"

invis_av = "https://cdn.discordapp.com/attachments/796589554420678666/803703694146404462/TransparentProfilePic.png"

hello = ""
embood = discord.Embed(title="Pronouns", description="She/Her - :woman:\nHe/Him - :man:\nThey/Them - :person_bald:\n Other - :grey_question:", color=0x98ff98)
embeed = discord.Embed(title="Age Roles", description="13-15 - :baby:\n15-17 - :child:\n18+ - :adult:", color=0xCBC3E3)
embad = discord.Embed(title="Pings", description=":speaking_head: - Chat Revive Ping\n:loudspeaker: - Announcements\n🚫 - Horny\n",color=0xfbff00)
emb = discord.Embed(title=f"{hello}", description="🏓")
eas = discord.Embed(title="Relationship Status", description=":broken_heart: - Single\n :heart: - In a relationship\n :yellow_heart: - Its complicated", color=discord.Color.red())
ema = discord.Embed(title="Country", description=":flag_us: - America\n:flag_au: - Australia\n:flag_aq: - Antartica\n:flag_eu: - Europe\n<:d60966d2487e11e7883755ba05ead76e:843368993146535966> - Africa\n:flag_ca: - Canada\n:flag_br: - South America", color=discord.Color.blue())
ema.set_footer()
embody = discord.Embed(title="Extra Pings", description=":loudspeaker:  VC ping\n:exclamation: Event Ping\n:desktop:  Game Ping", color=0x7289da)

bot.sniped_messages = {}
bot.author_id = 578789460141932555
bot.author_id = 578789460141932555
web = os.environ.get("webhook")
web2 = os.environ.get("webhook2")
web3 = os.environ.get("webhook3")
web4 = os.environ.get("webhook4")
web5 = os.environ.get("web5")
#bad_words = ["TEAST BOY", "<insert bad word>"]
wra = os.environ.get("bubble_wrap")
#---------------------------------------------------events---------------------------------------------------------------

@register_call("whoIs")
def who_is(query, session_id="general"):
    try:
        return wikipedia.summary(query)
    except Exception:
        for new_query in wikipedia.search(query):
            try:
                return wikipedia.summary(new_query)
            except Exception:
                pass
    return "I don't know about "+query
template_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"chatbotTemplate","chatbottemplate.template")
chat=Chat(template_file_path)

extensions = [
    'cogs.Main_Cog',
   # 'cogs.write_cog',
    #'cogs.entir',
    'cogs.bot2',
    'cogs.afk'
]

if __name__ == '__main__':
	for extension in extensions:
		bot.load_extension(extension)

proggress = os.environ.get("progress")

@bot.event
async def on_ready():
    print(f"-----\nLogged in as: {bot.user.name} : {bot.user.id}\n-----\nMy current prefix is: -\n-----")
    data = read_json("blacklist")
    bot.blacklisted_users = data["blacklistedUsers"]
    await bot.change_presence(activity=discord.Game(name=f"Vhelp for help! | M4 {proggress}%"))


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(838155702350381137)
    embed = discord.Embed(title=f"{member.display_name} has joined the server!", description = f"Welcome to the server!", colour = 0x7289da)
    embed.add_field(name = "Username : ", value = f"{member.display_name}")
    embed.add_field(name = "Discord ID : ", value = f"{str(member.id)}")
    embed.add_field(name = "Account Created at : ", value = f"{member.created_at}")
    embed.set_thumbnail(url = member.avatar_url)
    #embed.set_image(url = "https://media3.giphy.com/media/fU4elxKlRsulB4Jy7w/200.gif")
    embed.set_footer(text = channel.guild.name, icon_url=channel.guild.icon_url)
    await channel.send(embed = embed)


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
async def clear(ctx, amount=5):
	await ctx.channel.purge(limit=amount)
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
async def divide(ctx, left : int, right:int):
  await ctx.send(left/right)

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
	embed2.add_field(name='Contributers:', value="[Redacted]#[Redacted]")

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


@bot.command()
async def ts(ctx):
  print("ts was used")

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
		                   avatar_url=f"https://cdn.discordapp.com/attachments/796589554420678666/803703694146404462/TransparentProfilePic.png")

@bot.command()
async def test(ctx, message):
	await ctx.reply("reply")


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
async def setactivity(ctx, *, arg):
	activity = discord.Game(name=f"{arg}",
	                        type=3)
	await bot.change_presence(status=discord.Status.do_not_disturb,
	                          activity=activity)

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
async def role(ctx, arg):
  await ctx.send(f"{dir(discord)}")

@bot.command()
async def t(ctx):
  a = os.system("pip install discord")
  await ctx.send(f"{a}")

@bot.command()
async def exe(ctx, *, arg):
  a = os.system(f"{arg}")
  if arg == "pip uninstall":
    os.system("y")
  await ctx.send("yes")
  if arg == "pip install":
    await ctx.send("installed package")
  await ctx.send(f"{a}")

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
  #await log.send(embed=embed)
  await ctx.send(embed=embed)
  print(ex)

@bot.event
async def on_command_error(ctx, error):
  log = bot.get_channel(801530936356503612)
  embed = discord.Embed(title="Command error")
  embed.add_field(name="The following exeption is the direct cause of the command to fail", value=f"{error}\n[Docs](https://discordpy.readthedocs.io/en/stable/api.html)")
  #await ctx.send(embed=embed)
  await ctx.send(embed=embed)
  print(error)

#-----------------------------------------Slash Commands---------------------------------------




@bot.command()
@commands.has_role("Fleet Admiral")
async def sudo(ctx, member : discord.Member, *, arg):
	async with aiohttp.ClientSession() as session:
		webhook = Webhook.from_url(f'{web}',
		                           adapter=AsyncWebhookAdapter(session))
		await webhook.send(f"{arg}",
		                   username=f"{member.display_name}",
		                   avatar_url=f"{member.avatar_url}")

@bot.command()
#@commands.has_role("...")
async def say(ctx, member : discord.Member, *, arg):
	async with aiohttp.ClientSession() as session:
		webhook = Webhook.from_url(f'{web}',
		                           adapter=AsyncWebhookAdapter(session))
		await webhook.send(f"{arg}",
		                   username=f"{member.display_name}({ctx.author.name})",
		                   avatar_url=f"{member.avatar_url}")

@bot.command()
async def ranmem(ctx, member: discord.Member = None):
  await ctx.send(f"@{random.choice(ctx.guild.members)}")



@bot.command()
@commands.has_permissions(manage_channels=True)
async def pin(ctx, ID):
  message = await ctx.channel.fetch_message(ID)
  await message.pin()


@bot.command()
async def edit(ctx, * , arg):    
    #files = ["exe1", "exe2", "exe3", "exe4", "exe5"]
    with open('empty.py', 'w') as y:
      y.write(f"import main\n{arg}\nmain()")
    await ctx.send("your code will be reviewed")


@bot.command()
async def timerhelp(ctx):
  await ctx.send("helps you set a reminder")

@bot.command()
async def reminder(ctx, tme:int , *, msg):
  async with ctx.typing():

    author = ctx.author
  while True:
    await s(60*tme)
    embed = discord.Embed(title="Reminder", description=f"**{msg}** time of next reminder {tme} Minutes", colour=ctx.author.color, timestamp=ctx.message.created_at)
    await ctx.send(ctx.author.mention)
    await ctx.send(embed=embed)
    await author.send(embed=embed)

@bot.command()
async def tier(ctx, tm=10):
  while True:
    await s(1*tm)
    embed = discord.Embed(title="Timer", description=f"timer set for 10 min\n time remaining {tm}", color=ctx.author.color, timestamp=ctx.message.created_at)
    await ctx.send(embed=embed)

@bot.command()
async def invert(ctx,  *, message):
    if ctx.author != bot.user:
        await ctx.send(message[::-1])

@bot.command()
async def timer(ctx, timer: int = None):
  if timer is not None:
    timer *= 1
    embed = discord.Embed(title="Timer", description=f"{timer}", color=ctx.author.color, timestamp = ctx.message.created_at)
    message = await ctx.send(embed=embed)
    while timer > 0: 
      timer -= 1
      new = discord.Embed(title = "Timer", description=f"{timer} Minutes", color= ctx.author.color, timestamp = ctx.message.created_at)
      await message.edit(embed=new)
      await s(60)

  
@bot.command()
async def country(ctx):
      async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(f'{web5}',adapter=AsyncWebhookAdapter(session))
        await webhook.send(embed=ema, username='Country', avatar_url=invis_av)
        #await ctx.send(f"{id}")
  
@bot.command()
async def rstatus(ctx):
      async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(f'{web5}',adapter=AsyncWebhookAdapter(session))
        await webhook.send(embed=eas, username='Relationship status', avatar_url=invis_av)
        #await ctx.send(f"{id}")
  
@bot.command()
async def pings(ctx):
      async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(f'{web5}',adapter=AsyncWebhookAdapter(session))
        await webhook.send(embed=embad, username='Country', avatar_url=invis_av)
        #await ctx.send(f"{id}")
  
@bot.command()
async def age(ctx):
      async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(f'{web5}',adapter=AsyncWebhookAdapter(session))
        await webhook.send(embed=embeed, username='Age', avatar_url=invis_av)
        #await ctx.send(f"{id}")

@bot.command()
async def pronouns(ctx):
      async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(f'{web5}',adapter=AsyncWebhookAdapter(session))
        await webhook.send(embed=embood, username='Pronouns', avatar_url=invis_av)
        #await ctx.send(f"{id}")

@bot.command()
async def extrapings(ctx):
      async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(f'{web5}',adapter=AsyncWebhookAdapter(session))
        await webhook.send(embed=embody, username='Extra Pings', avatar_url=invis_av)
        #await ctx.send(f"{id}")

@bot.command()
async def bubblewrap(ctx):
  embed= discord.Embed(title="Bubble wrap", description="||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n", color=ctx.author.color, timestamp=ctx.message.created_at)
  await ctx.send(embed=embed)

@bot.command()
async def cdis(ctx, arg):
  if arg == True:
    await ctx.send("A is True")

#@bot.command()
#async def botinfo(ctx):
  #await ctx.send(application_info())

@bot.command()
async def m2(ctx, * ,arg):
  await ctx.send(keep_alive)

@bot.command()
async def translate(ctx, anguage, *, argument):
  translator= Translator(to_lang=f"{anguage}")
  translation = translator.translate(f"{argument}")
  print(translation) 
  await ctx.send(translation)




@bot.command(pass_context = True)
async def ai(ctx,*,message):
    result = chat.respond(message)
    if(len(result)<=2048):
        embed=discord.Embed(title="ChatBot AI", description = result, color = (0xF48D1))
        await ctx.reply(embed=embed)
    else:
        embedList = []
        n=2048
        embedList = [result[i:i+n] for i in range(0, len(result), n)]
        for num, item in enumerate(embedList, start = 1):
            if(num == 1):
                embed = discord.Embed(title="ChatBot AI", description = item, color = (0xF48D1))
                embed.set_footer(text="Page {}".format(num))
                await ctx.reply(embed = embed)
            else:
                embed = discord.Embed(description = item, color = (0xF48D1))
                embed.set_footer(text = "Page {}".format(num))
                await ctx.reply(embed = embed)



@bot.command()
@commands.has_permissions(manage_channels=True)
async def gdm(ctx, member : discord.Member, name=None, *, Time):
  tim = Time * 60
  guild = ctx.guild
  channel = await guild.create_text_channel(f"{name}")
  ch = bot.fetch_channel(channel)
  await ctx.send(f"made {channel}") 
  await s(tim)
  await ch.delete()
  
@bot.command()
async def emoji(ctx):
  guild = ctx.guild
  await ctx.send(guild.emojis)
@bot.command(name="eval", aliases=["exec"])
@commands.is_owner()
async def _eval(ctx, *, code):
    code = clean_code(code)

    local_variables = {
        "discord": discord,
        "commands": commands,
        "bot": bot,
        "ctx": ctx,
        "channel": ctx.channel,
        "author": ctx.author,
        "guild": ctx.guild,
        "message": ctx.message,
        "os" : os
    }

    stdout = io.StringIO()

    try:
        with contextlib.redirect_stdout(stdout):
            exec(
                f"async def func():\n{textwrap.indent(code, '    ')}", local_variables,
            )

            obj = await local_variables["func"]()
            result = f"{stdout.getvalue()}\n-- {obj}\n"
    except Exception as e:
        result = "".join(format_exception(e, e, e.__traceback__))

    pager = Pag(
        timeout=100,
        entries=[result[i: i + 2000] for i in range(0, len(result), 2000)],
        length=1,
        prefix="```py\n",
        suffix="```"
    )

    a = await pager.start(ctx)
    await ctx.send(a)

def clean_code(content):
    if content.startswith("```") and content.endswith("```"):
        return "\n".join(content.split("\n")[1:])[:-3]
    else:
        return content

@bot.command()
@commands.is_owner()
async def off(ctx):
  embed = discord.Embed(title="Switch", description="Y/N\nps: Vai and other externally connected recources will still be available.", color=ctx.author.color)
  m = await ctx.send(embed=embed,
        buttons=[Button(style=ButtonStyle.red, label="Kill"), 
        Button(style=ButtonStyle.blue, label="Don't Kill")
        ],
    )

  res = await ddb.wait_for_button_click(m)
  await res.respond(
        type=InteractionType.ChannelMessageWithSource,
        content=f'{res.button.label} clicked'
    )
  if res.button.label == "Don't Kill":
    await ctx.send("process was canceled")
    return
  await ctx.send("Shutting off verrus bot")
  await bot.logout()

@bot.command()
async def dif(ctx):
  difftest = await ctx.send("theo", buttons=[Button(style=ButtonStyle.blue, label="h"), Button(ButtonStyle.blue, label="Don't Kill")])

  b = await ddb.wait_for_button_click(difftest)
  if b.button.label == "h":
    await b.respond(
        type=InteractionType.ChannelMessageWithSource,
        content=f'{b} was clicked'
    )
  else:
    await ctx.send("h wasnt clicked")

@bot.command()
async def pingweb(ctx, *, arg: str):
  await ctx.send("Pinging {}".format(arg))
  await ping(arg)

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n-----")




bot.version = '0.0.4'

bot.blacklisted_users = []



@bot.event
async def on_message(message):
    #ignore ourselves
    if message.author.id == bot.user.id:
        return

    #blacklist system
    if message.author.id in bot.blacklisted_users:
        return

    if message.content.lower().startswith("help"):
        await message.channel.send("Hey! Why don't you run the help command with `Vhelp`")

    await bot.process_commands(message)

@bot.command()
@commands.is_owner()
async def blacklist(ctx, user: discord.Member):
    if ctx.message.author.id == user.id:
        await ctx.send("Hey, you cannot blacklist yourself!")
        return

    bot.blacklisted_users.append(user.id)
    data = read_json("blacklist")
    data["blacklistedUsers"].append(user.id)
    write_json(data, "blacklist")
    await ctx.send(f"Hey, I have blacklisted {user.name} for you.")

@bot.command()
@commands.is_owner()
async def unblacklist(ctx, user: discord.Member):
    bot.blacklisted_users.remove(user.id)
    data = read_json("blacklist")
    data["blacklistedUsers"].remove(user.id)
    write_json(data, "blacklist")
    await ctx.send(f"Hey, I have unblacklisted {user.name} for you.")

@bot.command()
async def stats(ctx):
    """
    A usefull command that displays bot statistics.
    """
    pythonVersion = platform.python_version()
    dpyVersion = discord.__version__
    serverCount = len(bot.guilds)
    memberCount = len(set(bot.get_all_members()))

    embed = discord.Embed(title=f'{bot.user.name} Stats', description='\uFEFF', colour=ctx.author.colour, timestamp=ctx.message.created_at)

    embed.add_field(name='Bot Version:', value=bot.version)
    embed.add_field(name='Python Version:', value=pythonVersion)
    embed.add_field(name='Discord.Py Version', value=dpyVersion)
    embed.add_field(name='Total Guilds:', value=serverCount)
    embed.add_field(name='Total Users:', value=memberCount)
    embed.add_field(name='Bot Developers:', value=f"<@{bot.author_id}>")

    embed.set_footer(text=f"Carpe Noctem | {bot.user.name}")
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)

    await ctx.send(embed=embed)

def read_json(filename):
    with open(f"{cwd}/bot_config/{filename}.json", "r") as file:
        data = json.load(file)
    return data

def write_json(data, filename):
    with open(f"{cwd}/bot_config/{filename}.json", "w") as file:
        json.dump(data, file, indent=4)

@bot.command()
@commands.has_permissions(administrator=True)
async def channelr(ctx, flag=None):
  edit = await ctx.send("Cuerating the most random channel name")
  words0 = ["maybe", " ", "keep", "alive", "ai", "perhaps", "eeorn", "im", "so", "quirky", "silver", "god", "odd", "awesome", "hi", "bye", "elaborate", "nut", "big", "delicius", "koko", "tree", "palm", "uses", "tree"]
  words1 = ["maybe", " ", "keep", "alive", "ai", "perhaps", "eeorn", "im", "so", "quirky", "silver", "god", "odd", "awesome", "hi", "bye", "elaborate", "nut", "big", "delicius", "koko", "tree", "palm", "uses", "tree"]
  words2 = ["maybe", " ", "keep", "alive", "ai", "perhaps", "eeorn", "im", "so", "quirky", "silver", "god", "odd", "awesome", "hi", "bye", "elaborate", "nut", "big", "delicius", "koko", "tree", "palm", "uses", "tree"]
  prew1 = random.choice(words0)
  prew2 = random.choice(words1)
  prew3 = random.choice(words2)




  a = f"{prew1} {prew2} {prew3}"
  if flag.endswith("--N"):
    await edit.edit("Generated random words")
    r = bot.get_channel(ctx.channel.id)
    await r.edit(reason=None ,name="∥⋆··⋆➻🍁⌜{}⌟".format(a))
    return
  elif flag.endswith("$ai"):
    m = await ctx.send("using AI to generate name")
    await m.edit(f"{a} were the words selected")
    ai = bo.ai_response(f"{a}")
    await m.edit(f"{a} were the words selected to which the bot replied {ai}")
    a_rep = bot.get_channel(ctx.channel.id)
    await a_rep.edit(reason=None, name=f"∥⋆··⋆➻🍁⌜{ai}⌟")

@bot.command()
async def aburn(ctx, *, search_terms : str):
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
                await ctx.send("**Definition:** " + definition + "\n\n" + "**Example:** " + example )
            else:
                await ctx.reply("Your search terms gave no results.", mention_author=False)
        except Exception:
            await ctx.send("Oh no it appears we ran into a error!")
run_time_var = []
def Clear_List():
  if len(run_time_var) > 3: 
    for i in run_time_var:
      run_time_var.remove(i)

@bot.listen('on_message')
async def wdqudqw(message):
  if len(run_time_var) > 3: 
    for i in run_time_var:
      run_time_var.remove(i)
  
  if message.channel.id == 876139985231806468:
    if message.author.id == 780835623006240809:
      print("message recived decoding now")
      print(message.content)
      if message.content.startswith("name="):
        print("caught message content")
        run_time_var.append(message.content[6:])
        print(run_time_var)
      elif message.content.startswith("guild_id="):
        print("caught message content")
        run_time_var.append(message.content[10:])
        print(run_time_var)
      elif message.content.startswith("channel_id="):
        print("caught message content")
        run_time_var.appxend(message.content[11:])
        print(run_time_var)
      ran = bot.get_channel(838155702350381137)
      await ran.send(message.content)
      for i in run_time_var:
        try:
          for vars in run_time_var:
            e = bot.get_channel(vars)
            print(e)
            t = bot.get_guild(vars)
            print(t)
            a = vars
            print(a)
            await e.send(f"message destination {t} attempting to get message {a}")
        except Exception as E:
          await ran.send("Oh no an uncaught exception occured {}".format(E))

@tasks.loop(hours=1)
async def called_once_a_day():
    message_channel = bot.get_channel(845368382173085756)
    embed = discord.Embed(title=f"Package Configuration, Getting channel:{message_channel} <a:yes:793883148215779328>")
    msg = await message_channel.send(embed=embed)
    print(f"Got channel {message_channel} <a:yes:793883148215779328>")
    embed2 = discord.Embed(title=f"Package Configuration", description=f"Got channel: {message_channel} <a:yes:793883148215779328>\nUpdating packages")
    await msg.edit(embed=embed2)
    os.system("pip install discord")
    embed3 = discord.Embed(title=f"Package Configuration", description=f"Got channel:{message_channel} <a:yes:793883148215779328>\n Updating Packages <a:yes:793883148215779328>\n ```py\npip install discord```")
    await msg.edit(embed=embed3)
    os.system("pip install discord.py")
    embed4 = discord.Embed(title=f"Package Configuration", description=f"Got channel:{message_channel} <a:yes:793883148215779328>\n Updating Packages\n ```py\npip install discord\n ✔️ done\n\npip install discord-py-slash-command``` ")
    await msg.edit(embed=embed4)
    os.system("pip install discord-py-slash-command")
    embed5 = discord.Embed(title=f"Package Configuration", description=f"Got channel:{message_channel} <a:yes:793883148215779328>\n Updating Packages\n ```py\npip install discord\n ✔️ done\n\npip install discord-py-slash-command\n ✔️ done\n\npip install pyfiglet``` ")
    await msg.edit(embed=embed5)
    os.system("pip install pyfiglet")
    embed7 = discord.Embed(title=f"Package Configuration", description=f"Got channel:{message_channel} <a:yes:793883148215779328>\n Updating Packages\n ```py\npip install discord\n ✔️ done\n\npip install discord-py-slash-command\n ✔️ done\n\npip install pyfiglet\n ✔️ done\n\npip install translate``` ")
    await msg.edit(embed=embed7) 
    os.system("pip install translator")
    embed8 = discord.Embed(title=f"Package Configuration", description=f"Got channel:{message_channel} <a:yes:793883148215779328>\n Updating Packages\n ```py\npip install discord\n ✔️ done\n\npip install discord-py-slash-command\n ✔️ done\n\npip install pyfiglet\n ✔️ done\n\npip install translate\n ✔️ done\n\npip install chatbotAI```")
    await msg.edit(embed=embed8)
    os.system("pip install chatbotAI")
    embed9 = discord.Embed(title=f"Package Configuration", description=f"Got channel:{message_channel} <a:yes:793883148215779328>\n Updating Packages\n ```py\npip install discord\n ✔️ done\n\npip install discord-py-slash-command\n ✔️ done\n\npip install pyfiglet\n ✔️ done\n\npip install translate\n ✔️ done\n\npip install chatbotAI\n ✔️ done```")
    embed8.set_footer(text="[Package Configuration Updated]")
    await msg.edit(embed=embed9)


@called_once_a_day.before_loop
async def before():
    await bot.wait_until_ready()
    print("Finished waiting")
called_once_a_day.start()


#m2()
keep_alive()
bot.run(os.environ.get('T'), bot=True)