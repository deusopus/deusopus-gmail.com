# 'Rochambeau' by Brent K Kohler AKA deusopus
t,w,l = 0,0,0
def play_again(t,w,l):
  y = input("Would you like to play again?: (Y/n)")
  if y.lower().strip() == "n":
    print("See you next time")
    print("Goodbye")
    quit()
  else:
    t = 0
    w = 0
    l = 0
    rochambeau(t,w,l)
  return t,w,l
def score(t,w,l):
  print("Turns: %s" % t)
  print("Wins: %s" % w)
  print("Losses: %s" % l)
  if t == 2:
    if w == 2:
      if l == 0:
        print("Perfect!")
        print("GAME OVER")
        play_again(t,w,l)
  if t == 2:
    if w == 1:
      if l == 1:
        print("You've got this...")
  if t == 2:
    if w == 0:
      if l == 2:
        chance = input("Try for best 3 out of 5?: (Y/n)")
        if chance.lower().strip() == "n":
          print("Better luck next time!")
          print("GAME OVER")
          quit()   
  if t == 3:
    if w == 1:
      if l == 2:
        print("Keep trying...")
  if t == 3:
    if w == 2:
      if l == 1:
         print("Good job...")
         print("GAME OVER")
         play_again(t,w,l)
  if t == 3:
    if w == 0:
      if l == 3:
        print("Sorry...")
        print("GAME OVER")
        play_again(t,w,l)
  if t == 4
    if w == 1:
      if l == 3:
        print("Nice try...")
        print("GAME OVER")
        play_again(t,w,l) 
  if t == 5:
    if w == 3:
      if l == 2:
        print("Excellent!")
        print("GAME OVER")
        play_again(t,w,l)     
  if t == 5:
    if w == 2:
      if l == 3:
        print("Better luck next time!")
        print("GAME OVER")
        play_again(t,w,l)
  return t,w,l
def instructions():
  print("Welcome to 'Rochambeau' by deusopus")
  print("The age-old game of Rock, Paper, Scissors")
  print("Type 'exit' at any time to quit")
  print("Have fun!")
  return
def rochambeau(t,w,l):
  instructions()
  score(t,w,l)
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
      print("You've chosen Rock")
      time.sleep(2)
      print ("I chose", c_c.title())
      time.sleep(2)
    if p_c.lower().strip() == "p":
      print("You've chosen Paper")
      time.sleep(2)
      print ("I chose", c_c.title())
      time.sleep(2)
    if p_c.lower().strip() == "s":
      print("You've chosen Scissors")
      time.sleep(2)
      print ("I chose", c_c.title())
      time.sleep(2)
    if p_c.lower().strip() == "r":
      if c_c == "rock":
        print("Draw")
        time.sleep(2)
        score(t,w,l)
      if c_c == "paper":
        print("You lose")
        time.sleep(2)
        t += 1
        l += 1
        score(t,w,l)
      if c_c == "scissors":
        print("You win!")
        time.sleep(2)
        t += 1
        w += 1
        score(t,w,l)
    if p_c.lower().strip() == "p":
      if c_c == "paper":
        print("Draw")
        time.sleep(2)
        score(t,w,l)
      if c_c == "scissors":
        print("You lose")
        time.sleep(2)
        t += 1
        l += 1
        score(t,w,l)
      if c_c == "rock":
        print("You win!")
        time.sleep(2)
        t += 1
        w += 1
        score(t,w,l)
    if p_c.lower().strip() == "s":
      if c_c == "scissors":
        print("Draw")
        time.sleep(2)
        score(t,w,l)
      if c_c == "rock":
        print("You lose")
        time.sleep(2)
        t += 1
        l += 1
        score(t,w,l)
      if c_c == "paper":
        print("You win!")
        time.sleep(2)
        t += 1
        w += 1
        score(t,w,l) 
rochambeau(t,w,l)
