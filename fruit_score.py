# Fruit Score by Brent Kaimanu Kohler AKA deusopus
# Guess a fruit on the list and earn a point
# Guess incorrectly and lose a point
# If you lose all your points, "GAME OVER"
# Enter "exit" at any time to quit

print ("Welcome to 'Fruit Score'")
print ("Guess a fruit on my list and earn a point")
print ("Guess incorrectly and lose a point")
print ("'Game Over' when you lose all your points")
print ("Type 'exit' at any time to quit")
print ("Enjoy!")

def fruit_score():
  score = 0
  fruits = ['apple', 'pear', 'banana', 'orange', 'lemon', 'lime', 'plum', 'grapes', 'kiwi']
  while score >= 0:
    fruit = input("Guess a fruit: ")
    if fruit == "exit":
      print(f"Score: {score}")
      print("Thanks for playing")
      break
    if fruit.lower() in fruits:
      print("Yes")
      score += 1
      print(f"Score: {score}")
    else:
      score -= 1
      print("No")
      if score <= 0:
        print("Game Over")
        break     
      else:
        print(f"Score: {score}")
  return
fruit_score()
