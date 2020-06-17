#Authentic D&D Ability Calculator by deusopus
print('Authentic D&D Ability Calculator by deusopus')
print()
import random
d6a = []
drawer = {}
traits = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 
         'Charisma']
for rolla in range(len(traits)):
  for rollb in range(4):
    d6 = random.randrange(1,7)
    d6a.append(d6)  
  print(f'Roll {rolla+1}')
  low = (min(d6a))
  d6a.remove(min(d6a)) 
  print(f'{d6a} Low:{low}')
  total = sum(d6a)
  print(f'{traits[rolla]}: {total}/18')
  print()   
  drawer[traits[rolla]] = d6a
  d6a = []
for key,value in drawer.items():
  print(f'{key:15}{value}{sum(value):5}/18')
