# 'Deck Dealer' by Brent Kaimanu Kohler AKA deusopus
def deck_dealer():
  import random
  n1 = random.randrange(1,14)
  if n1 == 1:
    print("Ace")
  elif n1 == 2:
    print("Deuce")
  elif n1 == 11:
    print("Jack")
  elif n1 == 12:
    print("Queen")
  elif n1 == 13:
    print("King")
  else:
    print(n1)
  return
deck_dealer()
deck_dealer()
deck_dealer()
deck_dealer()
deck_dealer()
