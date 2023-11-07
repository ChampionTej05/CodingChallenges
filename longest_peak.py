'''
Write a function that takes in array of integers and returns the length of longest peak in the array. 

Peak is defined as adjancent integers in the array that are STRICTLY increasing until they reach a TIP (highest value in peak) at which point they become STRICTLY decreasing. 

At least 3 integers are required to form a peak. 

NOTE: Adjancent elements to peak should be STRICTLY increasing & decreasing respectively.
'''

import sys


# Doesn'work
def findPeakInArray(array):

    peakCountingPart = False
    peakFound = False
    startIdx = -1
    peakIdx = -1
    for idx in range(len(array) - 1):
        # elements are in STRICT increasing order
        if array[idx] < array[idx + 1]:
            if not peakCountingPart:
                peakCountingPart = True
                # peak counting started from here
                startIdx = idx
            elif peakCountingPart and peakFound:
                count = idx - startIdx + 1
                print(startIdx, peakIdx, idx)
                return [peakIdx, count]
        # we are seeing decreasing part from previous increasing part
        elif array[idx] > array[idx + 1] and peakCountingPart:
            if not peakFound:
                peakFound = True

                peakIdx = idx
                print("Peak found", peakIdx)

                # return array[idx]
        else:
            # reset our range
            peakCountingPart = False
            startIdx = -1

    return [peakIdx, 0]


# Doesn'work
def findLongestPeakInArray(array):
    count = 0
    longestPeakIdx = -1
    currentIdx, localCount = findPeakInArray(array)
    print("First CurrentIdx and localCount", currentIdx, localCount)
    if currentIdx == -1:
        return count

    longestPeakIdx = currentIdx
    while (currentIdx != -1):
        localCurrentIdx, localCount = findPeakInArray(array[currentIdx:])
        if localCurrentIdx != -1:
            currentIdx = localCurrentIdx + currentIdx
            if localCount > count:
                count = localCount
                longestPeakIdx = currentIdx
        else:
            break

    # while (currentIdx != -1):
    #     currentIdx, localCount = findPeakInArray(array[currentIdx:])
    #     if localCount > count:
    #         count = localCount
    #         longestPeakIdx = currentIdx
    print("Longest Peak Idx is : and element is : ", longestPeakIdx,
          array[longestPeakIdx])
    return count


# https://www.geeksforgeeks.org/longest-mountain-subarray/ , try to make your solution like this


# TODO: This is incorrect. Let us check this once
def findLocalPeakInArray(arr):
    #  trend 0-->UP and 1 --> DOWN
    # print("Array : ", arr)
    if len(arr) < 3:
        return [-1, 0]
    trend = 'UP'
    if arr[0] > arr[1]:
        trend = 'DOWN'
    peakIdx = -1
    startIdx = 0
    count = 0
    change = 0
    for idx in range(1, len(arr)):
        # print("element and trend", arr[idx], trend)
        if arr[idx - 1] < arr[idx]:
            if trend == 'DOWN':
                if change == 1:
                    count = idx - startIdx
                    # print("Count calculated ", count)
                    return [idx - 1, count]
                else:
                    startIdx = idx - 1
            trend = 'UP'

        elif arr[idx - 1] > arr[idx]:
            if trend == 'UP':
                peakIdx = idx - 1
                change = 1
                if idx == len(arr) - 1:
                    count = idx - startIdx + 1
                    # print("Count calculated ", count)
                    return [idx - 1, count]
            trend = 'DOWN'
        else:
            trend = -1  #trend reset
            startIdx = idx

    # # this is needed if trend ends on last number [1,4,10,2]
    # if trend == 'DOWN':
    #     return [len(arr) - 1, len(arr) - startIdx]
    return [peakIdx, 0]


# Doesn'work
def findGlobalPeakInArray(arr):
    if len(arr) < 3:
        return 0
    currentIdx = 0
    globalCount = 0
    peakIdx = -1
    while (currentIdx < len(arr)):
        localCurrentIdx, localCount = findLocalPeakInArray(arr[currentIdx:])
        # print("Local Answers: ", localCurrentIdx, localCount)
        if localCurrentIdx != -1:
            currentIdx = currentIdx + localCurrentIdx
            if localCount > globalCount:
                globalCount = localCount
                peakIdx = currentIdx
        else:
            break
    # print("PeakIdx & Count", peakIdx, globalCount)
    return globalCount


'''
1. for every number, find numbers smaller than it on left i.e if(arr[i-1]<arr[i]) ==> left[i] = left[i-1] + 1
2. for every number, find numbers greater than it on left i.e if(arr[i+1]<arr[i]) ==> right[i] = right[i+1] + 1
3. find out max(left[i]+right[i]+1, existingMax) for every i and get the max length of peak

this works because it calcutaes, for particular arr[i] how many elements are exactly smaller than it in continous fashion on left and how many elements are smaller than it on right in continous fashion on right. We take sum of left + right and add 1 (counting arr[i] as it was not counted in left or right part)
'''


# Working solution
def findLongestPeakTwoArray(arr):
    if len(arr) < 3:
        return 0
    left = [0] * len(arr)
    right = [0] * len(arr)

    for idx in range(1, len(arr)):
        if (arr[idx - 1] < arr[idx]):
            left[idx] = left[idx - 1] + 1

    for idx in range(len(arr) - 2, -1, -1):
        if arr[idx + 1] < arr[idx]:
            right[idx] = right[idx + 1] + 1

    maxCount = 0
    for idx in range(len(arr)):
        # else we will count same size elements as peak ex: [1,2,2,2,2]
        if left[idx] != 0 and right[idx] != 0:
            temp = left[idx] + right[idx] + 1
            if maxCount < temp:
                maxCount = temp
    return maxCount


def longestPeak(arr):
    # Write your code here.
    globalCount = 0
    i = 1
    peakIdx = -1
    while (i < len(arr) - 1):
        print("idx:", i)
        if not (arr[i - 1] < arr[i] and arr[i] > arr[i + 1]):
            i += 1
            continue
        peakIdx = i

        # find peak first in the array
        # while (i<len(arr)):

        localCount = 1  # counting peak itself
        j = peakIdx - 1
        while (j >= 0 and arr[j] < arr[j + 1]):
            j -= 1
            localCount += 1

        k = peakIdx + 1
        while (k < len(arr) and arr[k - 1] > arr[k]):
            k += 1
            localCount += 1
        print("LocalCount : ", localCount)
        if globalCount < localCount:
            globalCount = localCount
        i = k

    return globalCount


if __name__ == '__main__':

    array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
    brray = [1, 4, 10, 2]
    crray = [1, 2, 2, 0]
    # results = findLongestPeakInArray(brray)
    # results = findGlobalPeakInArray(brray)
    enu = list(enumerate(array))
    print(enu)
    results = longestPeak(array)

    print(results)
