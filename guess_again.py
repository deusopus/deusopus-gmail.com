# 'Guess Again' by Brent K Kohler AKA deusopus

def guess_again():
  import random
  n = random.randrange(1,6)
  x = 0
  print("Guess a number between 1 and 5")
  while True:
    i = int(input("Guess: "))
    if i == n:
      print("You Win!")
      print(f"The number was {n}")
      break
    if x == 2:
      print("Sorry...")
      print("Game Over")
      print(f"The number was {n}")
      break
    else:
      print("Wrong")
      print("Try again")
      x += 1
  return
guess_again()

while True:
  restart = input("Press 'Enter' to play again. Enter 'exit' to quit: ")
  if restart.lower() != "exit":
    guess_again()
  else:
    print("Thanks for playing!")
    break
  
