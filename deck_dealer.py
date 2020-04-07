# 'Deck Dealer' by Brent Kaimanu Kohler AKA deusopus

def welcome():
  print("\n")
  print ("Welcome to The Grass Shack Casino"+"\U0001F340")
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
  import time
  slots = ['Ace','Deuce','Cherry','Orange','Lemon','Grape','Plum','Bell','Double Bell','Triple Bell','10','Jack','Queen','King','7','77','777','Bar','Double Bar','Triple Bar','Wild','Wild','Wild','Jackpot','Jackpot','Jackpot']
  n1 = random.choice(slots)
  n2 = random.choice(slots)
  n3 = random.choice(slots)
  n4 = random.choice(slots)
  n5 = random.choice(slots)
  time.sleep(.3)
  print(n1)
  time.sleep(.3)
  print(n2)
  time.sleep(.3)
  print(n3)
  time.sleep(.3)
  print(n4)
  time.sleep(.3)
  print(n5)
  time.sleep(.3)
  spin()
  return
welcome()
