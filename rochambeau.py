# 'Rochambeau' by Brent K Kohler AKA deusopus
t = 0
w = 0
l = 0
def play_again():
  global t
  global w
  global l
  y = input("Would you like to play again?: (Y/n)")
  if y.lower().strip() == "n":
    print("See you next time")
    print("Goodbye")
    quit()
  else:
    t = 0
    w = 0
    l = 0
    rochambeau()
  return
def score():
  global t
  global w
  global l
  print(f"Turns: {t}")
  print(f"Wins: {w}")
  print(f"Losses: {l}")
  if t == 2:
    if w == 2:
      print("You win!")
      print("Game Over")
      play_again()
  if t== 2:
    if w == 1:
      if l == 1:
        print("Here's the tie-breaker...")
  if t == 2:
    if w == 0:
      if l == 2:
        print("Sorry...")
        print("Game Over")
        play_again()
  if t == 3:
    if w == 2:
      if l == 1:
        print("You win!")
        print("Goodbye")
        play_again()
  if t == 3:
    if w == 1:
      if l == 2:
          x = input("Try for best 3 out of 5?: (Y/n)")
          if x.lower().strip() == "n":
            print("Thanks for trying")
            print("Game Over")
            quit()
  if t == 4:
    if w == 1:
      if l == 3:
        print("Sorry...")
        print("Game Over")
        play_again()
  if t == 4:
    if w == 2:
      if l == 2:
        print("Here's the tie-breaker!")
  if t == 5:
    if w == 2:
      if l == 3:
        print("Sorry...")
        print("Game Over")
        play_again()     
  if t == 5:
    if w == 3:
      if l == 2:
        print("You win!")
        print("Game Over")
        play_again()
  return
def instructions():
  print("\n")
  print("Welcome to 'Rochambeau' by deusopus")
  print("The age-old game of Rock, Paper, Scissors")
  print("Type 'exit' at any time to quit")
  print("Have fun!")
  print("\n")
  return
def rochambeau():
  global t
  global w
  global l
  instructions()
  score()
  import random
  choices = ['rock', 'paper', 'scissors']
  while True:
    c_c = random.choice(choices)
    print ("\n")
    print ("Rock, Paper, Scissors")
    p_c = input("Go!: ")
    if p_c.lower().strip() == "exit":
      print("Thanks for playing")
      print("Goodbye")
      quit()
    print ("I choose", c_c.title())
    print ("\n")
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
