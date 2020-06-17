#Authentic D&D Ability Calculator by deusopus
print('Authentic D&D Ability Calculator by deusopus')
import random
d6a = []
traits = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 
         'Charisma']
for rolla in range(len(traits)):
  for rollb in range(4):
    d6 = random.randrange(1,7)
    d6a.append(d6)  
  d6a.remove(min(d6a))
  print(f'Roll {rolla+1}')
  print(d6a)
  total = sum(d6a)
  print(f'{traits[rolla]}: {total}/18')
  d6a = []
