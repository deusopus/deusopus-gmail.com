# 'Deck Dealer' by Brent Kaimanu Kohler AKA deusopus
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
    print("Plum")
  elif n1 == 5:
    print("Bell")
  elif n1 == 11:
    print("Jack")
  elif n1 == 12:
    print("Queen")
  elif n1 == 13:
    print("King")
  elif n1 == 14:
    print("'7'")
  elif n1 == 15:
    print("77")
  elif n1 == 16:
    print("777")
  elif n1 == 19:
    print("Bar")
  elif n1 == 20:
    print("Double Bar")
  elif n1 == 21:
    print("Triple Bar")
  elif n1 == 22:
    print("Wild")
  else:
    print(n1)
  return
deck_dealer()
deck_dealer()
deck_dealer()
deck_dealer()
deck_dealer()
