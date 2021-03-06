import discord
from discord.ext import commands
import wikipedia,os
from chatbot import Chat, register_call
prefix = "?"
bot = commands.Bot(command_prefix = prefix)

template_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"chatbotTemplate","chatbottemplate.template")
chat=Chat(template_file_path)

@bot.event
async def on_message(message):
    result = chat.respond(message.content)
    if(len(result)<=2048):
        embed=discord.Embed(title="ChatBot AI", description = result, color = (0xF48D1))
        await message.channel.send(embed=embed)
    else:
        embedList = []
        n=2048
        embedList = [result[i:i+n] for i in range(0, len(result), n)]
        for num, item in enumerate(embedList, start = 1):
            if(num == 1):
                embed = discord.Embed(title="ChatBot AI", description = item, color = (0xF48D1))
                embed.set_footer(text="Page {}".format(num))
                await message.channel.send(embed = embed)
            else:
                embed = discord.Embed(description = item, color = (0xF48D1))
                embed.set_footer(text = "Page {}".format(num))
                await message.channel.send(embed = embed)