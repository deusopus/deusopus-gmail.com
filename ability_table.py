#Authentic D&D Ability Calculator by deusopus
#returns a table of ability allotments based on rolls
import random
d6a = []
drawer = {}
traits = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 
         'Charisma']
for rolla in range(len(traits)):
  for rollb in range(4):
    d6 = random.randrange(1,7)
    d6a.append(d6)  
  low = (min(d6a))
  d6a.remove(min(d6a)) 
  total = sum(d6a) 
  drawer[traits[rolla]] = d6a
  d6a = []
for key,value in drawer.items():
  print(f'{key:15}{value}{sum(value):5}/18')
