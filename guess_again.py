# 'Guess Again' by Brent Kaimanu Kohler AKA deusopus
s = 0
def score():
  print(f"Score: {s}")
  if s == 5:
    print("Congratulations.")
    print("You win!")
    print("You have unlocked the secret...")
    print("Goodbye")
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
  p = input("Would you like to play?: (Y/n) ")
  if p.lower().strip() == "n":
    print("Goodbye")
    quit()
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
      print(f"The secret number was {n}")
      s += 1
      score()
      play_again()
    elif i < n:
      print("Your guess is too low")
    elif i > n:
      print("Your guess is too high")
    if t == 2:
      print("Sorry...")
      print("GAME OVER")
      print(f"The secret number was {n}")
      score()
      s = 0
      play_again()
    else:
      print("Try again")
      t += 1
  return
guess_again()
