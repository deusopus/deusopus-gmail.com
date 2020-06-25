def fib():
  n1 = 0
  n2 = 1
  f=[n1,n2]
  print (f)
  for i in range (1,10):
    n3 = n2 + n1
    f.append(n3)
    n1 = n2
    n2 = n3
    print(f)
  return
fib()
