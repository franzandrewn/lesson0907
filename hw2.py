# Через цикл while запрашиваем число, если четное число, то его необходимо добавить в список и запросить ввод нового;
# если нечетное, то его в список не вносим, выводим в консоль, что не принято, спрашиваем снова
# если 0, то заканчиваем
# в список попало > 10 значений, цикл прервать
def inputLoop():
  nums = []
  isEnd = False
  while not isEnd:
    num = int(input("Введите число: ").strip())
    if num == 0 or len(nums) == 10:
      isEnd = True
    elif num % 2 == 0:
      nums.append(num)
    else:
      print("Вы ввели нечетное число, пропускаю")
  return nums

def inputLoopAlt():
  nums = []
  num = 1
  while num != 0 and len(nums) != 10:
    num = int(input("Введите число: ").strip())
    if num % 2 == 0:
      nums.append(num)
    else:
      print("Вы ввели нечетное число, пропускаю")
  return nums

print(inputLoop())

gotNumbers = inputLoop()