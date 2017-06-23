'''
Character management extension for Smithers
'''

__title__ ='Character'
__version__='0.1'

import dice

def generate(verbose=False):
  character = {'STR':0,'DEX':0,'CON':0,'INT':0,'WIS':0,'CHA':0}
  if verbose:
    for i in character:
      result = dice.drop(dice.die('4d6'),1)
      character[i] = dice.sumresult(result[0])
      print(i + ':' + str(character[i]) + ', Rolled: ' + str(result[0])  + ', dropped ' + str(result[1]) + '.')
  else: 
    for i in character:
      character[i] = dice.sumresult(dice.drop(dice.die('4d6'),1)[0])
  return character
        
def bonus(aspect):
  if(aspect % 2 != 0):
    result = aspect - 11
  else:
    result = aspect - 10
  return int(result / 2)
    
def show(character):
  for i in ('STR','DEX','CON','INT','WIS','CHA'):
    strang = i + ':' + str(character[i]) + ' ('
    abonus = bonus(character[i])
    if abonus >= 0:
       strang += '+'
    strang += str(abonus) + ')'
    print(strang)
