'''
find the pair with smallest distance on the number line from two array 
https://www.algoexpert.io/questions/smallest-difference
'''


def smallest_difference(arr, brr):
    # Write your code here.
    import sys
    minSum = sys.maxsize
    pair1 = -1
    pair2 = -1
    for i in range(len(arr)):
        for j in range(len(brr)):
            temp = abs(arr[i] - brr[j])
            if temp < minSum:
                minSum = temp
                pair1 = arr[i]
                pair2 = brr[j]
    return [pair1, pair2]


def smallest_difference_optimal(arr, brr):
    # Write your code here.
    import sys
    minSum = sys.maxsize
    pair1 = -1
    pair2 = -1

    arr.sort()
    brr.sort()
    i = 0
    j = 0
    while (i < len(arr) and j < len(brr)):
        temp = abs(arr[i] - brr[j])
        if temp == 0:
            return [arr[i], brr[j]]
        if temp < minSum:
            minSum = temp
            pair1 = arr[i]
            pair2 = brr[j]
        if arr[i] < brr[j]:
            i += 1
        else:
            j += 1
    return [pair1, pair2]


# https://www.geeksforgeeks.org/two-elements-whose-sum-is-closest-to-zero/
def closestToZero(self, arr, n):
    # your code here
    import sys
    maxSum = sys.maxsize
    low = 0
    high = len(arr) - 1
    arr.sort()
    while (low < high):
        temp = arr[low] + arr[high]
        # print(temp, maxSum, low, high)
        if abs(temp) < abs(maxSum):
            maxSum = temp
        elif abs(temp) == abs(maxSum):
            maxSum = max(maxSum, temp)

        if temp < 0:
            low += 1
        else:
            high -= 1

    return maxSum
