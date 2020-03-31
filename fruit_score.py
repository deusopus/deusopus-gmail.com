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
  good = 0
  awesome = 0
  instructions()
  fruit = ['yuzu','tamarind','strawberry','star fruit','soursop','raspberry','quince','pineberry','pineapple','persimmon','pear','peach','passionfruit','papaya','orange','mulberry','watermelon','mango','lime','lemon','kumquat','kiwifruit','plum','jackfruit','guava','grape','gooseberry','fig','dragonfruit','durian','coconut','cherry','blueberry','blackberry','banana','avocado','apricot','apple']
  old_fruit = [] 
  while score >= 0:
    guess = input("Guess a fruit: ")
    if guess.lower().strip() == "exit":
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
        good += 1
        awesome += 1
        if good == 3:
          print("Good job!")
          good = 0
        if awesome == 5:
          print("Awesome!")
          awesome = 0
        print(f"Score: {score}")
    else:
      if guess.lower().strip() in old_fruit:
        print("You already guessed that")
        print(f"Score: {score}")
        hint += 1
        if hint == 2:
          h = len(fruit)
          i = random.randrange(h)
          print("Here's a hint")
          print (fruit[i].title())
          hint = 0
      else:
        score -= 1
        print("Sorry")
        print(f"Score: {score}")
        if score <= 0:
          print("You lost all your points")
          print("Game Over")
          break     
  return
fruit_score()
