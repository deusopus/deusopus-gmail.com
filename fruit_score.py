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
  fruit = ['cranberries','crab apples','grapes','coconut','clementines','chokecherries','fig','cranberries','wild blueberries','watermelon','water coconut','ugli fruit','tangerine','surinam cherry','sugar apple','strawberry papaya','strawberry guava','strawberries','star fruit','south african baby pineapple','soursop','sharon fruit','sapote','sapodilla','salmonberry','rose apple','red currants','red banana','raspberries','raisins','quince','pummelo','pomegranate','plum,dried','plum','plantain','pineapple','persimmon','persian melon','pear','peach','passion fruit','papaya','orange','nectarine', 'mulberries','mediterranean medlar','maradol papaya','mandarin orange','mangosteen','mango','mamey sapote','lychee','loquat','longan','loganberries','lime','lemon','kumquat','kiwifruit','kiwano','key lime','kaffir lime','jujube','jambolan','jackfruit','huckleberries','honeydew melon','honeycrisp apple','guava','grapes','grapefruit','grape juice','golden kiwifruit','galia melon','fig,dried','feijoa','elderberries','durian','date plum','dates','custard apple','crenshaw melon','cherries','cherimoya','casaba melon','carissa','caribbean june plum','cara cara navel orange','cape gooseberries','cantaloupe','canary melon','cactus pear','breadfruit','boysenberries','blueberries','blood orange','blackberries','black currants','black crowberry','barbados cherry','banana','avocado','asian pears','armenian cucumber','apricots','apple']
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
          print(fruit[i])
          hint = 0
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
