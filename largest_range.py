'''
largest range of integers contained in array 
output = [2,6] implies array has subarray [2,3,4,5,6]
'''

# O(nlogn) solution

from threading import local


def largestRange(array):

    if len(array) == 1:
        return [array[0], array[0]]
    array = list(set(array))
    array.sort()
    print("Sorted Array ", array)
    import sys
    ansIdx = -1
    maxCount = -sys.maxsize - 1

    startIdx = -1
    count = 1

    for i in range(len(array) - 1):
        if array[i + 1] - array[i] == 1:
            if startIdx == -1:
                startIdx = i
            count += 1

        else:
            if count > maxCount:
                ansIdx = startIdx
                maxCount = count
            startIdx = -1
            count = 1

    if count > maxCount:
        ansIdx = startIdx
        maxCount = count

    print("Ans Idx", ansIdx)
    print("maxCount ", maxCount)

    result = [array[ansIdx], array[ansIdx + maxCount - 1]]
    print("result", result)
    return result


''' 
optimal approach using hashtable

Use Hash table to find faster if element exists in the array or not 

Initialise Hash table with all numbers as unvisited 

Find first non-visited number in array 
  1. left = number -1 ; this loop will ensure to trace all numbers which are consecutively less than NUMBER in the array 
    a. while left in array: 
        hash[left] = visited 
        left = left -1 
        length+=1
  2. right = number + 1
    a. while right in array :
        hash[right] = visited 
        right = right + 1
        length+=1
  3. compare the length calculated with globalLength and store the result accordingly
    if global < length:
        rangeStart = left + 1 (extra 1 decremented due to while loop condition)
        rangeEnd = right - 1 ( same as above)
        global = length
'''


# O(n) in space and O(n) in time
def largestRangeOptimal(array):
    mapper = {}

    for item in array:
        mapper[item] = False
    import sys
    globalLength = -sys.maxsize - 1
    rangeStart = -1
    rangeEnd = -1
    for item in array:
        localLength = 0
        if mapper[item]:
            continue

        mapper[item] = True
        leftRange = item - 1
        rightRange = item + 1

        while leftRange in mapper:
            mapper[leftRange] = True
            leftRange -= 1
            localLength += 1

        while rightRange in mapper:
            mapper[rightRange] = True
            rightRange += 1
            localLength += 1

        if globalLength < localLength:
            rangeStart = leftRange + 1
            rangeEnd = rightRange - 1
            globalLength = localLength

    print("Range Start and Range End ", rangeStart, rangeEnd)
    return [rangeStart, rangeEnd]


# array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
# array = [1, 2]
# array = [4, 2, 1, 3]
# array = [4, 2, 1, 3, 6]
array = [8, 4, 2, 10, 3, 6, 7, 9, 1]
# array = [
#     19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, 8, 7, 6, 15, 12, 12, 2, 1, 6,
#     13, 14
# ]
array1 = [
    0, 9, 19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, 8, 7, 6, 15, 12, 12, 2,
    1, 6, 13, 14
]
array2 = [10, 0, 1]
array3 = [1, 1, 1, 3, 4]
largestRangeOptimal(array)
largestRange(array)