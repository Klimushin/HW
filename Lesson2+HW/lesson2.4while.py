n = int(input("Input number :\n"))
a = 10000
while (a >= 1) :
  b = n // a % 10
  print (" +",int(b),"*",int(a), end = "")
  a /= 10
