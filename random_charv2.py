#displays a random character identity combination 
#from every possible character combination in D&D

def random_character():

  from random import randrange
  from random import seed

  race = ['Dwarf','Elf','Halfling','Human','Dragonborn','Gnome','Half-Elf','Half-Orc','Tiefling']
  classification = ['Barbarian','Bard','Cleric','Druid','Fighter','Monk','Paladin','Ranger','Rogue','Sorcerer','Warlock','Wizard']
  background = ['Acolyte','Charlatan','Entertainer','Folk-Hero','Guild Artisan','Hermit','Noble','Outlander','Sage','Sailor','Soldier','Urchin']
  characters = []
  for choice1 in race:
    for choice2 in classification:
      for choice3 in background:
        characters.append(choice1+"-"+choice2+"-"+choice3)

  print("Random D&D Identity Generator")
  choices = len(characters)
  randomchoice = randrange(choices)
  print(characters[randomchoice])
  x = input("Hit 'Enter' to choose another or type 'exit' to quit: ")
  if x.lower().strip() == "exit":
    print("Thanks!")
    quit()
  else:
    random_character()

random_character()
