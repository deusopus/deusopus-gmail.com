# 'Rochambeau' by Brent K Kohler AKA deusopus
t,w,l,c = 0,0,0,0
def play_again(t,w,l,c):
  y = input("Would you like to play again?: (Y/n)")
  if y.lower().strip() == "n":
    print("See you next time")
    print("Goodbye")
    quit()
  else:
    t = 0
    w = 0
    l = 0
    c = 0
    rochambeau(t,w,l,c)
  return t,w,l,c
def score(t,w,l,c):
  print("Turns: %s" % t)
  print("Wins: %s" % w)
  print("Losses: %s" % l)
  if t == 2:
    if w == 2:
      print("You win!")
      print("Game Over")
      play_again(t,w,l,c)
  if t== 2:
    if w == 1:
      if l == 1:
        print("Here's the tie-breaker...")
  if t == 2:
    if w == 0:
      if l == 2:
        if c <= 0:
          x = input("Try for best 3 out of 5?: (Y/n)")
          if x.lower().strip() == "n":
            print("Better luck next time")
            print("Game Over")
            quit()
          else:
            c += 1
  if t == 3:
    if w == 1:
      if l == 2:
        if c <= 0:
          x = input("Try for best 3 out of 5?: (Y/n)")
          if x.lower().strip() == "n":
            print("Better luck next time")
            print("Game Over")
            quit()
          else:
            c += 1
  if t == 3:
    if w == 0:
      if l == 3:
        print("Thanks for playing!")
        print("Game Over")
        quit()
  if t == 3:
    if w == 2:
      if l == 1:
        print("You win!")
        print("Game Over")
        play_again(t,w,l,c)
  if t == 4:
    if w == 1:
      if l == 3:
        print("So close!")
        print("Game Over")
        play_again(t,w,l,c)
  if t == 4:
    if w == 2:
      if l == 2:
        print("Here's the tie-breaker!")
  if t == 5:
    if w == 2:
      if l == 3:
        print("So close!")
        print("Game Over")
        play_again(t,w,l,c)     
  if t == 5:
    if w == 3:
      if l == 2:
        print("You win!")
        print("Game Over")
        play_again(t,w,l,c)
  return t,w,l,c
def instructions():
  print("Welcome to 'Rochambeau' by deusopus")
  print("The age-old game of Rock, Paper, Scissors")
  print("Type 'exit' at any time to quit")
  print("Have fun!")
  return
def rochambeau(t,w,l,c):
  instructions()
  score(t,w,l,c)
  import random
  import time
  choices = ['rock', 'paper', 'scissors']
  while True:
    c_c = random.choice(choices)
    print("Make your choice...")
    print ("(R)ock, (P)aper, (S)cissors")
    p_c = input("Go!: ")
    if p_c.lower().strip() == "exit":
      print("Thanks for playing")
      print("Goodbye")
      quit()
    if p_c.lower().strip() != "r":
        if p_c.lower().strip() != "p":
          if p_c.lower().strip() != "s":
            print("Invalid choice")
            print("Try again")
            time.sleep(2)
    if p_c.lower().strip() == "r":
      print ("I choose", c_c.title())
      time.sleep(2)
      print("You chose Rock")
      time.sleep(2)
    if p_c.lower().strip() == "p":
      print ("I choose", c_c.title())
      time.sleep(2)
      print("You chose Paper")
      time.sleep(2)
    if p_c.lower().strip() == "s":
      print ("I choose", c_c.title())
      time.sleep(2)
      print("You chose Scissors")
      time.sleep(2)
    if p_c.lower().strip() == "r":
      if c_c == "rock":
        print("Draw")
        time.sleep(2)
        score(t,w,l,c)
      if c_c == "paper":
        print("You lose")
        time.sleep(2)
        t += 1
        l += 1
        score(t,w,l,c)
      if c_c == "scissors":
        print("You win!")
        time.sleep(2)
        t += 1
        w += 1
        score(t,w,l,c)
    if p_c.lower().strip() == "p":
      if c_c == "paper":
        print("Draw")
        time.sleep(2)
        score(t,w,l,c)
      if c_c == "scissors":
        print("You lose")
        time.sleep(2)
        t += 1
        l += 1
        score(t,w,l,c)
      if c_c == "rock":
        print("You win!")
        time.sleep(2)
        t += 1
        w += 1
        score(t,w,l,c)
    if p_c.lower().strip() == "s":
      if c_c == "scissors":
        print("Draw")
        time.sleep(2)
        score(t,w,l,c)
      if c_c == "rock":
        print("You lose")
        time.sleep(2)
        t += 1
        l += 1
        score(t,w,l,c)
      if c_c == "paper":
        print("You win!")
        time.sleep(2)
        t += 1
        w += 1
        score(t,w,l,c) 
rochambeau(t,w,l,c)
