'''
Dice roller extension for Smithers
'''

__title__ = 'dice'
__version__ = '0.0.2'

import random

def roll(input: str):
  '''The main function that Smithers presently uses.
  Resulting die rolls are formatted and returned to the calling function
  '''
  try:
    rolls, limit = map(int, input.split('d'))
    if(limit <= 0):
      return('Positive integers only, please.')
    if(rolls == 1):
      return('The result of the `d' + str(limit) + '` roll is `' + str(random.randint(1,limit)) + '`.')
    else:
      result = []
      summation = 0
      for r in range(rolls):
        result.append(random.randint(1,limit))
        summation += result[r]
      result.sort(reverse=True)
      return('The result of the `' + input + '` roll is `' + str(summation) + '`.\nThe individual rolls are `' + str(result) + '`.')
  except Exception as e:
    print(e)
    return('Format has to be NdN, Sir.')

def die(input: str):
  '''Rolls a NdN die and returns the list of results'''
  rolls, limit = map(int, input.split('d'))
  if((limit <= 0) or (rolls <=0)):
    return [0]
  elif(rolls==1):
    return [random.randint(1,limit)]
  else:
    result = []
    summation = 0
    for r in range(rolls):
      result.append(random.randint(1,limit))
    result.sort(reverse=True)
    return result

def sumresult(result):
  '''Returns the sum of a list'''
  summation = 0
  for i in range(len(result)):
    summation += result[i]
  return summation

def drop(result, num, lowest=True):
  '''
  Returns a list of two sorted lists formatted thusly:
  [[Remaining Numbers],[Dropped Numbers]]
  '''
  num = 0 - num
  if(lowest): #Drop the lowest x numbers
    result.sort(reverse=True)
    return [result[:num], result[num:]]
  else: #Drop the highest x numbers
    result.sort()
    return[result[:num].sort(reverse=True), result[num:].sort(reverse=True)]
