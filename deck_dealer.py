# 'Deck Dealer' by Brent Kaimanu Kohler AKA deusopus
def welcome():
  print("\n")
  print ("Welcome to The Grass Shack Casino")
  x = input(str("Would you like to try your luck?: (Y/n) "))
  if x.lower().strip() == "n":
    y = input(str("Are you sure?: (Y/n) "))
    if y.lower().strip() == "n":
      spin()
    else:
      print("See you next time")
      print("Goodbye")
  else:
    spin()  
  return
def spin():
  t = input(str("Press 'enter' to spin. Type 'exit' to quit.: "))
  if t.lower().strip() == "exit":
    print("You'll be back...")
    print("Bwahahaha!")
    quit()
  else:
    deck_dealer()
  return
def deck_dealer():     
  import random
  slots = ['Ace','Deuce','Cherry','Orange','Lemon','Grape','Plum','Bell','Double Bell','Triple Bell','10','Jack','Queen','King','7','77','777','Bar','Double Bar','Triple Bar','Wild','Wild','Wild','Jackpot','Jackpot','Jackpot']
  n1 = random.choice(slots)
  n2 = random.choice(slots)
  n3 = random.choice(slots)
  n4 = random.choice(slots)
  n5 = random.choice(slots)
  print(n1)
  print(n2)
  print(n3)
  print(n4)
  print(n5)
  spin()
  return
welcome()
