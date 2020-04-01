# 'Fruit Score' by Brent Kaimanu Kohler AKA deusopus
# Guess a fruit on the list and earn a point
# Guess incorrectly and lose a point
# If you lose all your points, "GAME OVER"
# Enter "exit" at any time to quit
score = 0
g = 0
a = 0
h = 0
def instructions():
  print("\n")
  print ("Welcome to 'Fruit Score' by deusopus")
  print ("Guess a fruit on my list and earn a point")
  print ("Guess incorrectly and lose a point")
  print ("'Game Over' when you lose all your points")
  print ("Type 'exit' at any time to quit")
  print ("\n")
  return
def fruit_score(score,g,a,h):
  import random
  instructions()
  fruit = ['yuzu','tamarind','strawberry','star fruit','soursop','raspberry','quince','pineberry','pineapple','persimmon','pear','peach','passionfruit','papaya','orange','mulberry','watermelon','mango','lime','lemon','kumquat','kiwifruit','plum','jackfruit','guava','grapes','gooseberry','fig','dragonfruit','durian','coconut','cherry','blueberry','blackberry','banana','avocado','apricot','apple']
  old_fruit = []
  while True:
    score_keeper(score,g,a,h)
    guess = input("Guess a fruit: ")
    if guess.lower().strip() == "exit":
      print("Goodbye")
      print("Thanks for playing")
      break
    if guess.lower().strip() not in fruit:
      if guess.lower().strip() in old_fruit:
        print("You already guessed that")
        h += 1
        if h == 2:
          print("Here's a hint")
          h1 = random.choice(fruit)
          print(h1.title())   
          h = 0
    if guess.lower().strip() in fruit:
      print("Yes")
      fruit.remove(guess)
      old_fruit.append(guess)
      score += 1
      g += 1
      a += 1
      if g == 3:
        print("Good job!")
        g = 0
      if a == 5:
        print("Awesome!")
        a = 0
    if guess.lower().strip() not in fruit:
      if guess.lower().strip() not in old_fruit:
        print("Sorry")
        score -= 1
        if score <= 0:
          score = 0
          print(f"Score: {score}")
          print("Game Over")
          break
  return score,g,a,h
def score_keeper(score,g,a,h):
  print(f"Score: {score}")
  return (score,g,a,h)
fruit_score(score,g,a,h)
