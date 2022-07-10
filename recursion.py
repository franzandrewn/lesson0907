def rec():
  print(1)
  rec()

# rec()

def printNto1(n):
  if n!=0:
    print(n)
    printNto1(n-1)

def fib(n):
  if n < 3:
    return 1
  else:
    return fib(n-1) + fib(n-2)

# printNto1(10)

print(fib(10))