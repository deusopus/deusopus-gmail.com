#Authentic D&D Ability Calculator by deusopus
import random
d6a = []
abils = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']
for rolla in range(len(abils)):
  for rollb in range(4):
    d6 = random.randrange(1,7)
    d6a.append(d6)  
  d6a.remove(min(d6a))
  print(f"Roll {rolla+1}")
  print(d6a)
  total = sum(d6a)
  print(f"{abs[rolla]}: {total}/18")
  d6a = []
