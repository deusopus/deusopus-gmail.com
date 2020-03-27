# 'Guess Again' by Brent K Kohler AKA deusopus
score = 0
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
      print(f"Your score: {score}")
      score += 1
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
guess_again()

while True:
  restart = input("Press 'Enter' to play again. Enter 'exit' to quit: ")
  if restart.lower() != "exit":
    guess_again()
  else:
    print("Thanks for playing!")
    break
