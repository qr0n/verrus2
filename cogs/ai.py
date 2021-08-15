@bot.event
async def on_message(message):
    channeler = bot.get_channel(845684085460697118)
    if(message.channel.id == 845684085460697118):
      channeler = bot.get_channel(845684085460697118)
    else:
      return
    result = chat.respond(message.content)
    if bot.user == message.author:
      return 
    if(len(result)<=2048):
        embed=discord.Embed(title="ChatBot AI", description = result, color =message.author.color)
        await channeler.send(embed=embed)
        await bot.process_commands(message)
    else:
        embedList = []
        n=2048
        embedList = [result[i:i+n] for i in range(0, len(result), n)]
        for num, item in enumerate(embedList, start = 1):
            if(num == 1):
                embed = discord.Embed(title="ChatBot AI", description = item, color = (0xF48D1))
                embed.set_footer(text="Page {}".format(num))
                await channeler.send(embed = embed)
                await bot.process_commands(message)
            else:
                embed = discord.Embed(description = item, color = (0xF48D1))
                embed.set_footer(text = "Page {}".format(num))
                await channeler.send(embed = embed)
                await bot.process_commands(message)