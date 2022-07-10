def maxMin(ints):
  if len(ints) > 0:
    maxInt = ints[0]
    maxIndex = 0

    minInt = ints[0]
    minIndex = 0
    for index in range(len(ints)):
      num = ints[index]
      if num > maxInt:
        maxInt = num
        maxIndex = index
      if num < minInt:
        minInt = num
        minIndex = index

    # for (index, num) in enumerate(ints):
    #   if num > maxInt:
    #     maxInt = num
    #     maxIndex = index
    #   if num < minInt:
    #     minInt = num
    #     minIndex = index
    
    # print("Max index = " + str(maxIndex) + ", min index = " + str(minIndex))
    print(f"Max element = {maxInt} on index = {maxIndex}, min element = {minInt} on index = {minIndex}")


maxMin([1,2,3,4,5,6,7])