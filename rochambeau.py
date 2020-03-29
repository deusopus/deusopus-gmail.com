# 'Rochambeau' by Brent K Kohler AKA deusopus
# UNDER CONSTRUCTION
t = 0
w = 0
l = 0
def score():
  print(f"Turns: {t}")
  print(f"Wins: {w}")
  print(f"Losses: {l}")
  return
def rochambeau():
  global t
  global w
  global l
  import random
  choices = ['rock', 'paper', 'scissors']
  while True:
    print("Rock, Paper, or Scissors?")
    p_c = str(input("Make your choice: "))
    if p_c == exit:
      quit()
    c_c = random.choice(choices)
    print (c_c.title())
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
  return
rochambeau()
