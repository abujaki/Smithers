'''
Main file for SMITHERS discord bot
'''

__title__ = 'Smithers'
__version__ = '0.0.4'
__status__ = 'Development/Untested'
__authors__=['abujaki']

import discord
from discord.ext import commands
import Token
import random

from Games import dice

description = '''Good day Sir. My name is Smithers, and I am here to serve.'''
bot = commands.Bot(command_prefix='!', description=description)

#---------------------------------------------------------------------Ping/Pongs
@bot.command()
async def ping():
  '''Pong'''
  await bot.say('Pong, Sir.')
@bot.command()
async def pong(): #Because Brandon decided to be cheeky
  '''Ping'''
  await bot.say('Ping, Sir. However, I do believe you have it backwards.')

#------------------------------Dice Rolling. Presently supports one tuple of NdN
##@bot.command()
##async def roll(NdN : str = '1d20'):
##'''Rolls NdN dice'''
##await bot.say(dice.roll(NdN))

#--------------------------------------------------------------------Testing Bed

@bot.command()
async def roll(NdN : str = '1d20', *args):
  '''Test command for new dice roll functions
  -----
  roll - Rolls 1d20
  roll adv/advantage - Rolls 2d20 and drops the lowest
  roll dis/disadv/disadvantage - Rolls 2d20 and drops the highest
  roll XdY - Rolls X Y-sided die
  roll... + X - Adds X to the final dice roll
  roll... - X - Subtracts X from the final dice roll
  roll... d/dl X - Drops the lowest X dice rolls
  roll... dh X - Drops the highest X dice rolls
  
  Untested so far, and incredibly verbose. Good luck everybody!
  TODO - Condense each modifier into one argument, vice a pair.
  '''
  if (NdN == 'adv') or (NdN == 'advantage'):
    result = dice.drop(dice.die('2d20'),1)
    await bot.say('Rolled a `' + str(result[0][0]) + '` on Advantage. *(Dropped `' + str(result[1][0]) +'`)*') 
  elif (NdN == 'dis') or (NdN == 'disadv') or (NdN == 'disadvantage'):
    result = dice.drop(dice.die('2d20'),1,False)
    await bot.say('Rolled a `' + str(result[0][0]) + '` on Disadvantage. *(Dropped `' + str(result[1][0]) +'`)*') 
  elif (len(args)==0):
    await bot.say(dice.roll(NdN))
  elif (len(args) % 2 == 0):
    result = dice.die(NdN) #original dice roll
    modifier = 0 #+/- die result
    dropped = False #For tracking dice dropping
    verbose = ''#'Beginning with a `' + NdN + '` roll of `' + str(result) + '`, and args `' + str(args) + '`\n'
    try:
      for i in range(0,len(args),2):
        try:
          if args[i] == '+': #All descriptions in the last 'verbose' line
            modifier += int(args[i+1])
            #verbose += '`' + args[i+1] + '` is added to the result,\n'
          elif args[i] == '-':
            modifier -= int(args[i+1])
            #verbose += '`' + args[i+1] + '` is subtracted from the result,\n'
          elif (args[i] == 'd') or (args[i] == 'dl'):
            if(dropped):
              verbose += 'A number of dice have already been dropped,\n'
            else:
              result = dice.drop(result,int(args[i+1]))
              dropped = True
              #verbose += 'the lowest `' + args[i+1] + '` rolls are dropped: `' + str(result[1]) + '`,\n'
          elif args[i] == 'dh':
            if(dropped):
              verbose += 'A number of dice have already been dropped,\n'
            else:
              result = dice.drop(result, int(args[i+1]), False)
              dropped = True
              verbose += 'the highest `' + args[i+1] + '` rolls are dropped, `' + str(result[1]) + '`,\n'
          else: #Catch the properly-formed nonsense
            verbose ++ 'skipping the unknown expression `' + str(args[i]) + ' ' + str(args[i+1]) + '`,\n'
        except Exception as e: #Catch the grotesquely errenous nonsense
          print('[WARNING] ' + str(e))
          verbose += 'skipping the malformed expression `' + str(args[i]) + ' ' + str(args[i+1]) + '`,\n'
      ##Bring it all home
      verbose += 'Result: '
      if(dropped):
        verbose += '`' + str(result[0])
        final = dice.sumresult(result[0])
      else:
        verbose += '`' + str(result)
        final = dice.sumresult(result)
      if (modifier >= 0):
        verbose += '+'
      verbose += str(modifier) + '` Equals **`' + str(final + modifier) + '`**.'
      await bot.say(verbose)
    except Exception as e: #wrap it up nicely
      print('[ERROR] ' + str(e))
  else: #Catch an uneven number of args
    await bot.say('Malformed expression in args ' + str(args))

#---------------------------------------------------------------------Bot Events
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
