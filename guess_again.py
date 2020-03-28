# 'Guess Again' by Brent Kaimanu Kohler AKA deusopus
s = 0
def score():
  print(f"Score: {s}")
  if s == 5:
    print("You win!")
    print("Thanks for playing")
    quit()
  return
def play_again():
  x = input("Press 'enter' to play again. Type 'exit' to quit: ")
  if x.lower() != "exit":
    guess_again()
  else: 
    print("Thanks for playing!")
    quit()
  return
def guess_again():
  import random
  global s
  n = random.randrange(1,6)
  t = 0
  print("Guess a number between 1 and 5")
  while True:
    i = int(input("Guess: "))
    if i == n:
      print("Correct!")
      print(f"The number was {n}")
      s += 1
      score()
      play_again()
    if t == 2:
      print("Sorry...")
      print("Game Over")
      print(f"The number was {n}")
      score()
      s = 0
      play_again()
    else:
      print("Wrong")
      print("Try again")
      t += 1
  return
guess_again()
