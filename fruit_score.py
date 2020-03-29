# 'Fruit Score' by Brent Kaimanu Kohler AKA deusopus
# Guess a fruit on the list and earn a point
# Guess incorrectly and lose a point
# If you lose all your points, "GAME OVER"
# Enter "exit" at any time to quit

def instructions():
  print("\n")
  print ("Welcome to 'Fruit Score' by deusopus")
  print ("Guess a fruit on my list and earn a point")
  print ("Guess incorrectly and lose a point")
  print ("'Game Over' when you lose all your points")
  print ("Type 'exit' at any time to quit")
  print ("\n")
  return

def fruit_score():
  instructions()
  score = 0
  fruits = ['apple', 'pear', 'banana', 'orange', 'lemon', 'lime', 'plum', 'grapes', 'kiwi', 'dragonfruit', 'cherries', 'grapefruit', 'guava', 'mango', 'papaya', 'pomegranate', 'blueberries', 'pineapple', 'strawberries', 'watermelon']
  old_guesses = [] 
  while score >= 0:
    guess = input("Guess a fruit: ")
    if guess == "exit":
      print(f"Score: {score}")
      print("Thanks for playing")
      break
    if fruit.lower().strip() in fruits:
      if guess.lower().strip() not in old_guesses:
        print("Yes")
        old_guesses.append(guess)
        score += 1
        print(f"Score: {score}")
      else:
        print("You already guessed that")
    else:
      score -= 1
      print("Sorry")
      if score <= 0:
        print("GAME OVER")
        print(f"Score: {score}")
        break     
  return
fruit_score()
