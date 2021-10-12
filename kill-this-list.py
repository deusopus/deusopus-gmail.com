from random import randrange
while True:
  row = []

  for number in range(1,11):
    row.append(randrange(1,11))

  while len(row) > 0:
    random.shuffle(row)
    print(row)
    n = int(input('Which number to remove? '))
    row = [i for i in row if i != n]
    if n != (row):
      print('Try again')
