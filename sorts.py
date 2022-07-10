# nums.sort()
# print(nums)

def bubbleSort(nums):
  for i in range(len(nums)):
    countWrong = 0
    for index in range(len(nums) - 1):
      if nums[index] > nums[index+1]:
        countWrong+=1
        (nums[index], nums[index+1]) = (nums[index+1], nums[index])
    if countWrong == 0:
      break
    print(nums)

def quickSort(nums):
  print("got list: " + str(nums))
  if len(nums) < 2:
    return nums
  pivot = nums.pop()
  moreThan = []
  lessThan = []
  for element in nums:
    if element > pivot:
      moreThan.append(element)
    else:
      lessThan.append(element)
  print("pivot: " + str(pivot) + " less: " + str(lessThan) + " more: " + str(moreThan))
  print()
  sortedLeft = quickSort(lessThan)
  sortedRight = quickSort(moreThan)
  result = sortedLeft + [pivot] + sortedRight
  return result


nums = [5, 10, 2, -8, 50, 2, 5, -100, 101, 10, 42]
# bubbleSort(nums)
nums = quickSort(nums)
print(nums)