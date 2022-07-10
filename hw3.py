# числа фибоначчи

def fibonnacciNumbers(num):
  result = []
  f1 = 1
  f2 = 1
  result.append(f1)
  result.append(f2)
  for _ in range(num-2):
    f3 = f1 + f2
    result.append(f3)
    f1 = f2
    f2 = f3
  return result

print(fibonnacciNumbers(int(input())))