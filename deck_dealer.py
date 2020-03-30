# 'Deck Dealer' by Brent Kaimanu Kohler AKA deusopus
def welcome():
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
    print("Bwahahahahahahaha!")
    quit()
  else:
    loop()
  return
def loop():
  for i in range (5):
    deck_dealer()
  if i == 4:  
    spin()
  return
def deck_dealer():     
  import random
  n1 = random.randrange(1,23)
  if n1 == 1:
    print("Ace")
  elif n1 == 2:
    print("Deuce")
  elif n1 == 3:
    print("Cherry")
  elif n1 == 4:
    print("Orange")
  elif n1 == 5:
    print("Lemon")
  elif n1 == 6:
    print("Grape")
  elif n1 == 7:
    print("Plum")
  elif n1 == 8:
    print("Bell")
  elif n1 == 9:
    print("Double Bell")
  elif n1 == 11:
    print("Jack")
  elif n1 == 12:
    print("Queen")
  elif n1 == 13:
    print("King")
  elif n1 == 14:
    print("7")
  elif n1 == 15:
    print("77")
  elif n1 == 16:
    print("777")
  elif n1 == 17:
    print("Bar")
  elif n1 == 18:
    print("Double Bar")
  elif n1 == 19:
    print("Triple Bar")
  elif n1 == 20:
    print("Wild")
  elif n1 == 21:
    print("Wild")
  elif n1 == 22:
    print("Wild")
  else:
    print(n1)
  return
welcome()
