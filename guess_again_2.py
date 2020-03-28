# 'Guess Again' by Brent K Kohler AKA deusopus
s = 0
def guess_again(s):
  import random
  n = random.randrange(1,6)
  x = 0
  print("Guess a number between 1 and 5")
  print(n)
  while True:
    i = int(input("Guess: "))
    if i == n:
      print("Correct!")
      print(f"The number was {n}")
      s += 1
      print(f"Score: {s}")
      break
    if x == 2:
      print("Sorry...")
      print("Game Over")
      print(f"The number was {n}")
      break
    else:
      print("Wrong")
      x += 1
  return s
guess_again(s)

while True:
  s = guess_again(s)
  x = input("Press 'enter' to play again. Type 'exit' to quit: ")
  if x.lower() != 'exit':
    guess_again(s)
  else:
    print("Thanks for playing!")
    break
