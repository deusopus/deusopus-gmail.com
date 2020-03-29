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
  import random
  score = 0
  hint = 0
  instructions()
  fruit = ['apple', 'pear', 'banana', 'orange', 'lemon', 'lime', 'plum', 'grapes', 'kiwi', 'dragonfruit', 'cherries', 'grapefruit', 'guava', 'mango', 'papaya', 'pomegranate', 'blueberries', 'pineapple', 'strawberries', 'watermelon']
  old_fruit = [] 
  while score >= 0:
    guess = input("Guess a fruit: ")
    if guess == "exit":
      print(f"Score: {score}")
      print("Goodbye")
      print("Thanks for playing")
      break
    if guess.lower().strip() in fruit:
      if guess.lower().strip() not in old_fruit:
        print("Yes")
        old_fruit.append(guess)
        fruit.remove(guess)
        score += 1
        print(f"Score: {score}")
    else:
      if guess.lower().strip() in old_fruit:
        print("You already guessed that")
        print(f"Score: {score}")
        hint += 1
        if hint > 2:
          h = len(fruit)
          i = random.randrange(h)
          print("Here's a hint")
          hint = 0
          print(fruit[i])
      else:
        score -= 1
        print("Sorry")
        print(f"Score: {score}")
        if score <= 0:
          print("You lost all your points")
          print("GAME OVER")
          break     
  return
fruit_score()
