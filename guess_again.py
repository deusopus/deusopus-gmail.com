# 'Guess Again' by Brent Kaimanu Kohler AKA deusopus
score,turns,round = 0,0,1
def instructions():
  print("\n")
  print("I am The Great Enigma!")
  print("I am thinking of a number between 1 and 5...")
  print("You have three chances to guess correctly")
  print("Guess correctly and earn a point")
  print("Guess incorrectly and lose your points")
  print("Earn 5 points and you win the game")
  print("Type 'exit' at any time to quit")
  print("\n")
  p = input("Would you like to play?: (Y/n) ")
  if p.lower().strip() == "n":
    print("See you next time")
    print("Game Over")
    quit()
  else:
    print("Let us begin...")
  return
def guess_again(score,turns,round):
  import time
  import random
  n1 = random.randrange(1,6)
  while True:
    score_keeper(score,turns,round)
    n = input("Guess: ")
    if n.lower().strip() == "exit":
      print("Game Over")
      print("Goodbye")
      quit()
    if int(n) == n1:
      print("Correct!")
      score += 1
      time.sleep(1)
      print(f"The secret number was {n1}")
      time.sleep(1)
      if score == 5:
        score_keeper(score,turns,round)
      print("You're learning my secrets...")
      time.sleep(1)
      print("You won't guess again!")
      time.sleep(1)
      round += 1
      turns = 0  
      guess_again(score,turns,round)
    if int(n) < n1:
      print("Your guess is too low")
      time.sleep(1)
      print("Guess again...")
      time.sleep(1)
      turns += 1
      if turns > 2:
        print("Sorry...")
        print("Game Over")
        print(f"The secret number was {n1}")
        time.sleep(1)
        play_again(score,turns,round)
    if int(n) > n1:
      print("Your guess is too high")
      time.sleep(1)
      print("Guess again...")
      time.sleep(1)
      turns += 1
      if turns > 2:
        print("Sorry...")
        print("Game Over")
        print(f"The secret number was {n1}")
        time.sleep(1)
        play_again(score,turns,round)
  return score,turns,round 
def score_keeper(score,turns,round):
  print(f"Round: {round}")
  print(f"Score: {score}")
  if score == 5:
    print("Congratulations!")
    print("You win")
    print("You have unlocked the secret...")
    print("Game Over")
    play_again(score,turns,round)
  return score,turns,round
def play_again(score,turns,round):
  x = input("Press 'enter' to play again. Type 'exit' to quit: ")
  if x.lower().strip() == "exit":
    print("Game Over")
    quit()
  else: 
    score,turns,round = 0,0,1
    guess_again(score,turns,round)
  return score,turns,round
instructions()
guess_again(score,turns,round)
