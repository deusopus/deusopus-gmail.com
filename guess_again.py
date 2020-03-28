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
def instructions():
  print("\n")
  print("I am The Great Enigma!")
  print("I am thinking of a number between 1 and 5...")
  print("You have three chances to guess correctly.")
  print("Guess correctly and earn a point.")
  print("Guess incorrectly and lose your points.")
  print("Earn 5 points and you win the game.")
  print("\n")
  return
instructions()
def guess_again():
  import random
  global s
  n = random.randrange(1,6)
  t = 0
  while True:
    score()
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
