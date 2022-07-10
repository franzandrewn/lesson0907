
def findMax(nums):
  maxElem = nums[0]
  for num in nums:
    if num > maxElem:
      maxElem = num
  return maxElem

def findMin(nums):
  minElem = nums[0]
  for num in nums:
    if num < minElem:
      minElem = num
  return minElem

def findMaxIndex(nums):
  maxElem = nums[0]
  maxIndex = 0
  for i in range(len(nums)):
    num = nums[i]
    if num > maxElem:
      maxElem = num
      maxIndex = i
  return maxIndex

def linearSearch(nums, target):
  for i in range(len(nums)):
    if nums[i] == target:
      return i
  return -1

def binarySearch(nums, target):
  # Переменные для границы рассматриваемого диапазона
  # В самом начале рассматривается весь список, поэтому нужен первый и последний индекс
  left = 0 
  right = len(nums) - 1
  mid = -1
  while left <= right:
    # Находим средний индекс
    mid = int((left + right) / 2)
    print("left: " + str(left) + " right: " + str(right) + "\nmid: " + str(mid) + " nums[mid]: " + str(nums[mid]))
    # В случае если мы попали по необходимому элементу, вернуть его индекс
    if nums[mid] == target:
      return mid
    # в случае если не попали, подправить левую/правую границу
    elif nums[mid] > target:
      right = mid - 1
    else:
      left = mid + 1
  print("last mid:" + str(mid))
  return 1 - len(nums) + mid

def interpolationSearch(nums, target):
  left = 0 
  right = len(nums) - 1
  guess = -1
  while left <= right:
    guess = round(left + ((target - nums[left]) * (right - left) / (nums[right] - nums[left])))
    print("left: " + str(left) + " right: " + str(right) + "\nguess: " + str(guess) + " nums[guess]: " + str(nums[guess]))
    if nums[guess] == target:
      return guess
    elif nums[guess] > target:
      right = guess - 1
    else:
      left = guess + 1
  return 1 - len(nums) + guess

numbers = [-1,1,3,5,10,15,16,25]
# print(findMax(numbers))
# print(findMin(numbers))

# print(linearSearch(numbers, -10))
# print(linearSearch(numbers, 101))

# numbers.sort()
# print(numbers[0])
# print(numbers[len(numbers) - 1])

# print(max(numbers))
# print(min(numbers))

# print("Попытка найти 17")
# print(binarySearch(numbers, 17))
# print("Попытка найти 3")
# print(binarySearch(numbers,3))
# print("Попытка найти 12")
# print(binarySearch(numbers,12))
# numbers.insert(binarySearch(numbers,12), 12)
# print(numbers)

numbers = [1,3,5,6,7,9,11,11]
print("Попытка найти двоичным поиском 1")
print(binarySearch(numbers, 1))
print("Попытка найти интерполяцей 1")
print(interpolationSearch(numbers, 1))