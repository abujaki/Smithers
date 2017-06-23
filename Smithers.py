'''
Main file for SMITHERS discord bot
'''

__title__ = 'Smithers'
__version__ = '0.0.3'
__authors__=['abujaki']

import discord
from discord.ext import commands
import Token
import random

from Games import dice

description = '''Good day Sir. My name is Smithers, and I am here to serve.'''
bot = commands.Bot(command_prefix='!', description=description)

#Ping/Pongs
@bot.command()
async def ping():
  '''Pong'''
  await bot.say('Pong, Sir.')
@bot.command()
async def pong(): #Because Brandon decided to be cheeky
  '''Ping'''
  await bot.say('Ping, Sir. However, I do believe you have it backwards.')

#Dice Rolling. Presently supports one tuple of NdN
@bot.command()
async def roll(NdN : str = '1d20'):
  '''Rolls NdN dice'''
  await bot.say(dice.roll(NdN))

@bot.event
async def on_ready():
  print('------')
  print('[INFO] Logged in as ' + bot.user.name)
  print('[INFO] Client ID: ' + bot.user.id)
  print('------')

#For security purposes, the token is saved as a string literal in Token.__token__
#Token.py has been added to the .gitignore so it does not get posted publicly.
#This function launches the bot and connects it to the server.
bot.run(Token.__token__)
