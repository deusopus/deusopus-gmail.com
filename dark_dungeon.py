# 'Dark Dungeon' by Brent K Kohler AKA deusopus
import random
x = random.randrange(5,15) * 2 
y = random.randrange(5,15) * 2

class Dungeon():
  def __init__(self, length, width, weapon, treasure, enemy):
    self.length = length
    self.width = width
    self.weapon = weapon
    self.treasure = treasure
    self.enemy = enemy
  
  def map(self):
    print()
    print (f"You are in a dark dungeon and it smells of death")
    print(f"The walls are damp and spotted with lichen")
    print (f"It is {(str(self.length))} yards long and {(str(self.width))} yards wide")
    print (f"You have with you as a weapon, a trusty {(self.weapon)}")
    print (f"There is a treasure of {(self.treasure)} somewhere")
    print (f"You will have to fight a {(self.enemy)} to get it")

    return self

  def inventory(self):
    print()
    print (f"You have a trusty {(self.weapon)}")
    if treasure > 0:
      print(f"You have a treasure of {(self.treasure)}")
    if enemy > 0:
      print(f"You have the head of a {(self.enemy)}")
    else:
      print(f"You have a small amount of pocket fluff")

    return self

map1 = Dungeon(x, y, 'bronze sword', 'gold', 'giant fire ant')
map2 = Dungeon(x, y, 'axe', 'jewels', 'man-bear-pig')
map3 = Dungeon(x, y, 'crossbow', 'silver coins', 'disproportionate dwarf')

scenes = [map1, map2, map3]
board = random.choice(scenes)
board.map()

#initial location
zelda_0 = {'x_pos': x/2, 'y_pos': y/2}

def movement():

  print("It is dark")
  print("You hear the faint rattling of chains")
  print()
  print (f"You are at coordinate: X:{zelda_0['x_pos']}, Y:{zelda_0['y_pos']}")

  turn = input('Which direction will you head? (n, s, e, w, l, i, q)')

  x_increment = 0
  y_increment = 0

  if turn == 'n':
    x_increment = 1
  elif turn == 's':
    x_increment = -1
  elif turn == 'w':
    y_increment = -1
  elif turn == 'e':
    y_increment = 1
  elif turn == 'q':
    quit()
  elif turn == 'l':
    look()
  elif turn == 'i':
    board.inventory()
  else:
    turnbase()

  zelda_0['x_pos'] = zelda_0['x_pos'] + x_increment
  zelda_0['y_pos'] = zelda_0['y_pos'] + y_increment

  turnbase()

  return
  
def turnbase():
  if (zelda_0['y_pos']) <= y-y:
    print()
    print('You are at the wall')
    zelda_0['y_pos'] = y-y
  elif (zelda_0['y_pos']) >= y:
    print()
    print('You are at the wall')
    zelda_0['y_pos'] = y
  elif (zelda_0['x_pos']) >= x:
    print()
    print('You are at the wall')
    zelda_0['x_pos'] = x
  elif (zelda_0['x_pos']) <= x-x:
    print()
    print('You are at the wall')
    zelda_0['x_pos'] = x-x
  else:
    print()
    
  return

def look():
  board.map()
  return

#variable assignment
treasure = 0
enemy = 0
turn = 0

while True:  
  movement()
