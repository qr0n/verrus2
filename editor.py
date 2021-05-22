def convert(time):
  pos = ["s","m","h","d"]
  time_dict = {"s" : 1, "m" : 60, "h" : 3600, "d": 3600*24}

  unit = time[-1]

  if unit not in pos:
    return -1
  try:
    val = int(time[:-1])
  except:
    return -2

  return val * time_dict[unit]

@client.command()
@commands.has_permissions(kick_members=True)
async def giveaway(ctx):
  await ctx.send("Let's start with this giveaway! Answer these questions within 15 seconds!")

  questions = ["Which channel should it be hosted in?", "What should be the duration of the giveaway? (s|m|h|d)", "What is the prize of the giveaway?"]

  answers = []

  def check(m):
    return m.author == ctx.author and m.channel == ctx.channel

  for i in questions:
    await ctx.send(i)

    try:
      msg = await client.wait_for('messsage', timeout=15.0, check=check)
    except asyncio.TimeoutError:
      await ctx.send('You didn\'t answer in time, please be quicker next time!')
      return
    else: 
      answers.append(msg.content)

  try:
    c_id = int(answers[0][2:-1])
  except:
    await ctx.send(f"You didn't mention a channel properly. Do it like this {ctx.channel.mention} next time.")
    return

  channel = client.get_channel(c_id)

  time = convert(answers[1])
  if time == -1:
    await ctx.send(f"You didn't answer with a proper unit. Use (s|m|h|d) next time!")
    return
  elif time == -2:
    await ctx.send(f"The time just be an integer. Please enter an integer next time.")
    return
  
  prize = answers[2]

  await ctx.send(f"The giveaway will be in {channel.mention} and will last {answers[1]} seconds!")

  embed = discord.embed(title = "Giveaway!", description = f"{prize}", color = ctx.author.color)

  embed.add_field(name = "Hosted by:", value = ctx.author.mention)

  embed.set_footer(text = f"Ends {answers[1]} from now!")

  my_msg = await channel.send(embed = embed)

  await my_msg.add_reaction("🎉")

  await asyncio.sleep(time)

  new_msg = await channel.fetch_message(my_msg.id)

  users = await new_msg.reactions[0].users().flatten()
  users.pop(users.index(client.user))

  winner = random.choice(users)

  await channel.send(f"Congratulations! {winner.mention} won the prize: {prize}!")


@client.command()
@commands.has_permissions(kick_members=True)
async def reroll(ctx, channel : discord.TextChannel, id_ : int):
  try:
    new_msg = await channel.fetch_message(id_)
  except:
    await ctx.send("The ID that was entered was incorrect, make sure you have entered the correct giveaway message ID.")
  users = await new_msg.reactions[0].users().flatten()
  users.pop(users.index(client.user))

  winner = random.choice(users)

  await channel.send(f"Congratulations the new winner is: {winner.mention} for the giveaway rerolled!")