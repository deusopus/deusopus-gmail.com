# 'Guess Again' by Brent K Kohler AKA deusopus
def guess_again():
  import random
  n = random.randrange(11)
  x = 0
  print("Guess a number between 1 and 10")
  while True:
    i = int(input("Guess: "))
    if i == n:
      print("Correct")
      break
    if x == 2:
      print("Sorry")
      print("Game Over")
      print(f"The number was {n}")
      break
    else:
      print("Wrong")
      x += 1
guess_again()
