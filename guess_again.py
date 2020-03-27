# 'Guess Again' by Brent K Kohler AKA deusopus
def guess_again():
  import random
  n = random.randrange(1,6)
  t = 0
  print("Guess a number between 1 and 5")
  while True:
    i = int(input("Guess: "))
    if i == num:
      print("You Win!")
      print(f"The number was {n}")
      break
    if t == 2:
      print("Sorry...")
      print("Game Over")
      print(f"The number was {n}")
      break
    else:
      print("Wrong")
      print("Try again")
      t += 1
  return
guess_again()

while True:
  x = input("Press 'Enter' to play again. Enter 'exit' to quit: ")
  if x.lower() != "exit":
    guess_again()
  else:
    print("Thanks for playing!")
    break
