# 'Guess Again' by Brent Kaimanu Kohler AKA deusopus
turns = 0
score = 0
n1 = 0
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
    print("Thanks anyway")
    print("Goodbye")
    quit()
  return
def guess_again(score,turns,n1):
  import random
  n1 = random.randrange(1,6)
  while True:
    score_keeper(score,turns,n1)
    n = input("Guess: ")
    if n.lower().strip() == "exit":
      print("Thanks for playing!")
      print("Goodbye")
      break
    if int(n) == n1:
      print("Correct!")
      print(f"The secret number was {n1}")
      score += 1
      turns = 0  
    if int(n) < n1:
      print("Your guess is too low")
      turns += 1
      if turns > 2:
        print("Sorry...")
        print("Game Over")
        print(f"The secret number was {n1}") 
        turns = 0
        play_again(score,turns,n1)
    if int(n) > n1:
      print("Your guess is too high")
      turns += 1
      if turns > 2:
        print("Sorry...")
        print("Game Over")
        print(f"The secret number was {n1}")
        turns = 0 
        play_again(score,turns,n1)
  return (score,turns,n1)  
def score_keeper(score,turns,n1):
  print(f"Score: {score}")
  if score == 5:
    print("Congratulations")
    print("You win!")
    print("You have unlocked the secret...")
    print("Goodbye")
    quit()    
  return score,turns,n1
def play_again(score,turns,n1):
  x = input("Press 'enter' to play again. Type 'exit' to quit: ")
  if x.lower().strip() == "exit":
    print("Thanks for playing")
    quit()
  else: 
    guess_again(score,turns,n1)
  return score,turns,n1
instructions()
guess_again(score,turns,n1)
