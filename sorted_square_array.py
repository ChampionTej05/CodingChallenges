'''
https://www.algoexpert.io/questions/sorted-squared-array

Non-empty array of Integers(negative & positive) values sorted in ascending orders. Return a new array of the same length as the original array with the squares of the original integers also sorted in ascending order.
'''

import sys


# this is assumed that array will have enough capacity to hold new element
# arr is empty array of highest INT_MIN
def insert_in_sorted_array(arr, target, currentLength):
    length = len(arr)
    # if length == 0:
    #     arr.append(target)
    #     return arr

    for j in range(currentLength - 1, -1, -1):
        # print(j, arr[j], target)
        if (arr[j] > target):
            arr[j + 1] = arr[j]
        else:
            arr[j + 1] = target
            return arr

    arr[0] = target  # condition when target is smallest element in the array
    return arr


def sorted_squared_array(arr):
    minSize = -sys.maxsize - 1
    result = [minSize] * len(arr)
    currentLength = 0
    for element in arr:
        result = insert_in_sorted_array(result, element**2, currentLength)
        currentLength += 1
        # print(result)
    return result


'''
Approach : start and end will keep track of smallest and largest number of Arr we have traversed till now. We will find out which one is largest in ABSOLUTE from arr[start] & arr[end], whichever is largest will go in result array and then we will move forward accordingly.

How to append in result.
1. Enter the result array using append and then return reverse of it
2. Populate reverse with dummy values and of size len(arr) and keep on adding from the last [ this will work with any language considering arrays are not extendible]
'''


def sorted_squared_array_optimal_solution(arr):
    result = []
    length = len(arr)

    # result.append(arr[0]**2)
    start = 0  # start of arr
    end = length - 1  # ending of arr
    idx = length - 1  # keeps track of result array

    # using Approach 2

    result = [0] * length
    while (idx >= 0):
        print("Start : {start} -> {value}".format(start=start,
                                                  value=arr[start]))
        print("End : {end} -> {value}".format(end=end, value=arr[end]))
        print("Idx: ", idx)
        if abs(arr[start]) > abs(arr[end]):
            result[idx] = arr[start]**2
            start += 1
        else:
            result[idx] = arr[end]**2
            end -= 1
        idx -= 1
        print(result)
        print("*********")
    return result


if __name__ == '__main__':
    # minSize = -sys.maxsize - 1
    # arr = [-1, 5, 1, 0, 6, -9, 3, 0]
    # # arr = [5, 1, 2, 6, 9, 3]
    # result = [minSize] * len(arr)
    # print(result)
    # currentLength = 0
    # for ele in arr:
    #     print("-----------")
    #     result = insert_in_sorted_array(result, ele, currentLength)
    #     print(result)
    #     currentLength += 1
    #     print("------------")
    # print(result)

    arr = [1, 2, 3, 5, 6, 8, 9]
    brr = [-9, -7, -3, 1, 2, 3, 5, 6]
    crr = [-2, 0, 2, 3]
    drr = [1]
    # result = sorted_squared_array(brr)
    # print(result)

    input = drr
    result1 = sorted_squared_array_optimal_solution(input)
    assert len(result1) == len(input)
    print(result1)