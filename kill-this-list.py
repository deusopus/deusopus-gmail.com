import random
from random import randrange

while True:

    lst = []
    for item in range(0,10):
        while len(lst) < 11:
            lst.append(randrange(0,7))
            print(lst)

    for item in range(0,len(lst)):
        while len(lst) > 1:
            lst.remove(random.choice(lst))
            print(lst)
