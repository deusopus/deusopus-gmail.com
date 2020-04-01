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
    print("Bwahahahahahaha!")
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
  slots = ['Ace','Deuce','Cherry','Orange','Lemon','Grape','Plum','Bell','Double Bell','Triple Bell','10','Jack','Queen','King','7','77','777','Bar','Double Bar','Triple Bar','Wild','Wild','Wild','Jackpot']
  n1 = random.choice(slots)
  print(n1)
  return
welcome()
