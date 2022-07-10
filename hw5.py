# Шейкерная сортировка

def shakerSort(ints):
  if len(ints) < 2:
    return
  left = 0
  right = len(ints) - 1

  while left <= right:
    for i in range(left, right):
      if ints[i] > ints[i+1]:
        (ints[i], ints[i+1]) = (ints[i+1], ints[i])
    right-=1
    print(f"after going up: {ints}")
    for i in range(right, left, -1):
      if ints[i] < ints[i-1]:
        (ints[i], ints[i-1]) = (ints[i-1], ints[i])
    left+=1
    print(f"after going down: {ints}")
    print()

ints = [2, 6,1,23,-6,8,4,1,78]
shakerSort(ints)
print(ints)