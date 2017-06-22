import discord
from discord.ext import commands
import Token
import random

description = '''Good day Sir. My name is Smithers, and I am here to serve.'''

bot = commands.Bot(command_prefix='!', description=description)

#Ping/Pongs
@bot.command()
async def ping():
    await bot.say('Pong, Sir.')
@bot.command()
async def pong(): #Because Brandon decided to be cheeky
  await bot.say('Ping, Sir. However, I do believe you have it backwards.')

#Dice Rolling. Presently supports one tuple of NdN
@bot.command()
async def roll(dice : str = '1d20'):
  try:
    rolls, limit = map(int, dice.split('d'))
    result = []
    summation = 0
  except Exception:
    await bot.say('Format has to be in NdN, Sir.')
    return
  for r in range(rolls):
      result.append(random.randint(1,limit))
      summation += result[r]

  result.sort()
  result.reverse()
  await bot.say('The result of the `' + dice + '` roll is `' + str(summation) + '`.\n The individual rolls are `' + str(result) + '`, Sir.')

#Test for whisper function
#@bot.command()
#async def whisper(message):
#    await bot.whisper('Yes, Sir.')

#Trying to get Smithers to logout instead of timeout
#@bot.command()
#async def goodnight():
#  await bot.say('At your command, I shall retire. Goodnight, Sir.')
#  bot.logout()

@bot.event
async def on_ready():
  print('Logged in as')
  print(bot.user.name)
  print(bot.user.id)
  print('------')

bot.run(Token.__token__)
