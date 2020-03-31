# 'Rochambeau' by Brent K Kohler AKA deusopus
t = 0
w = 0
l = 0
c = 0
def score():
  print(f"Turns: {t}")
  print(f"Wins: {w}")
  print(f"Losses: {l}")
  if t == 2:
    if w == 2:
      print("You win!")
      print("Goodbye")
      quit()
  if t == 2:
    if w == 0:
      if l == 2:
        print("Sorry...")
        print("You lose")
        quit()
  if t == 3:
    if w == 2:
      if l == 1:
        print("You win!")
        print("Goodbye")
        quit()   
  if t == 3:
    if w == 1:
      if l == 2:
        if c < 1:
          x = input("Try for best 3 out of 5?: (Y/n)")
          if x.lower().strip() == "n":
            print("Better luck next time")
            print("Goodbye")
            quit()
  if t == 4:
    if w == 1:
      print("Sorry...")
      print("You lose")
      quit()
  if t == 5:
    if w <= 2:
      if l >= 3:
        print("Sorry...")
        print("You lose")
        quit()           
  if t == 5:
    if w == 3:
      if l == 2:
        print("You win!")
        print("Goodbye")
        quit()
  return
def instructions():
  print("Welcome to 'Rochambeau' by deusopus")
  print("The age-old game of Rock, Paper, Scissors")
  print("Type 'exit' at any time to quit")
  print("Have fun!")
  return
def rochambeau():
  instructions()
  score()
  global t
  global w
  global l
  global c
  import random
  choices = ['rock', 'paper', 'scissors']
  while True:
    c_c = random.choice(choices)
    print ("Rock, Paper, Scissors")
    p_c = input("Go: ")
    if p_c.lower().strip() == "exit":
      quit()
    print ("I choose", c_c.title())
    if p_c.lower().strip() == "rock":
      if c_c == "rock":
        print("Draw")
        score()
      if c_c == "paper":
        print("You lose")
        t += 1
        l += 1
        score()
      if c_c == "scissors":
        print("You win!")
        t += 1
        w += 1
        score()
    if p_c.lower().strip() == "paper":
      if c_c == "paper":
        print("Draw")
        score()
      if c_c == "scissors":
        print("You lose")
        t += 1
        l += 1
        score()
      if c_c == "rock":
        print("You win!")
        t += 1
        w += 1
        score()
    if p_c.lower().strip() == "scissors":
      if c_c == "scissors":
        print("Draw")
        score()
      if c_c == "rock":
        print("You lose")
        t += 1
        l += 1
        score()
      if c_c == "paper":
        print("You win!")
        t += 1
        w += 1
        score() 
    else:
      if p_c.lower().strip() != "rock":
        if p_c.lower().strip() != "paper":
          if p_c.lower().strip() != "scissors":
            print("Invalid choice")
            print("Try again")
    
rochambeau()
