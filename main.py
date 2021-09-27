import discord
import os
import json
import random
import asyncio
from discord.ext import tasks
from itertools import cycle
from keep_alive import keep_alive

bot = discord.Client()
status = cycle(['Hello There', 'General Kenobi'])

@bot.event
async def on_ready():
    change_status.start()
    print('Logged in as {0.user}'.format(bot))

@tasks.loop(seconds=5)
async def change_status():
  await bot.change_presence(activity=discord.Game(next(status)))


@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  if message.content.startswith('Hello There'):
    await message.channel.send('General Kenobi')
    print('Hello There - General Kenobi')

  if message.content.startswith('Hello there'):
    await message.channel.send('General Kenobi')
    print('Hello there - General Kenobi')

  if message.content.startswith('hello there'):
    await message.channel.send('General Kenobi')
    print('hello there - General Kenobi')

  if message.content.startswith('>ping'):
    await message.channel.send(f'The ping is {round(bot.latency * 1000)}ms')
    print ('Ping sent')

  if message.content.startswith('>code'):
    await message.channel.send('You can finde the code here: https://gist.github.com/realshouzy/806b036a70529eaf12454958ddfff377')
    print('Codelink sent')

  if message.content.startswith('>invite'):
    await message.channel.send('This is the invitelink: https://discord.com/api/oauth2/authorize?client_id=851400158158782514&permissions=84992&scope=bot')
    print('Invitelink send')

  if message.content.startswith('>stats'):
    await message.channel.send(f'The bot is on {len(bot.guilds)} servers.')
    print('Stats send')

  if message.content.startswith('>vote'):
    await message.channel.send('You can vote for the bot here if you like it: https://top.gg/bot/851400158158782514')
    print('Votelink send')

  if message.content.startswith('>website'):
    await message.channel.send('https://hello-there.shouzy.repl.co')
    print('Websitelink sent')

  if message.content.startswith('>help'):
    await message.channel.send('So the main function of this bot is to write "General Kenobi" when you write "Hello There"(or "Hello there"/"hello there"). It also has a few commands with the prefix ">", like ">ping" for the latency, ">invite" to get the invite link of the bot and ">vote" to get the vote link of the bot. You can also read the code if you want with ">code".')
    print('helpcommand process')


keep_alive()
bot.run(os.getenv('TOKEN'))
