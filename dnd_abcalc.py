#D&D Ability Calculator by deusopus
import random
d6a = []
d6b = []
for roll in range(6):
  for roll in range(4):
    d6 = random.randrange(1,7)
    d6a.append(d6)  
  print(d6a)
  d6a.remove(min(d6a))
  d6b.append(d6a)
  print(d6b)
  d6c.append(d6b)
  d6a = []
