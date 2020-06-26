#displays a random character combination from every possible character combination
import random
race = ['Dwarf','Elf','Halfling','Human','Dragonborn','Gnome','Half-Elf','Half-Orc','Tiefling']
classification = ['Barbarian','Bard','Cleric','Druid','Fighter','Monk','Paladin','Ranger','Rogue','Sorcerer','Warlock','Wizard']
background = ['Acolyte','Charlatan','Entertainer','Folk-Hero','Guild Artisan','Hermit','Noble','Outlander','Sage','Sailor','Soldier','Urchin']
combinations = []
for choice1 in race:
  for choice2 in classification:
    for choice3 in background:
      combinations.append(choice1+":"+choice2+":"+choice3)

randomchoice = random.choice(combinations)
print(randomchoice)
