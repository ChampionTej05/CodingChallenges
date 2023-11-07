# https://www.algoexpert.io/questions/subarray-sort

'''
Easier solution to understand
Logic : Find the range of index which is un-sorted.
Find minItem in the array which is not sorted and find maxItem in the array which is not sorted. 

Find the left most value close to minItem in the array
Find the right most value close to maxItem in the array

'''

def subarraySort(array):
    # Write your code here.
    import sys
    minItem = sys.maxsize - 1
    maxItem = -sys.maxsize - 1
    minItemIdx = -1
    maxItemIdx = -1
    outOfOrderElementExists = False
    for i in range(len(array)):
        item = array[i]
        if isItOutOfOrder(array, i, item):
            outOfOrderElementExists = True
            # find min and max out of order elements in the array
            print("out of order. ", item)
            if item < minItem:
                minItem = item
                minItemIdx = i
            if item > maxItem:
                maxItem = item
                maxItemIdx = i

    print("minItem", minItem)
    print("maxItem", maxItem)
    if not outOfOrderElementExists:
        return [-1, -1]
    i = 0
    while (i < len(array) and array[i] <= minItem):
        i += 1

    j = len(array) - 1
    while (j >= 0 and array[j] >= maxItem):
        j -= 1

    print("start ", i)
    print("end", j)

    return [i, j]


def isItOutOfOrder(array, i, num):
    if i == 0:
        return num > array[i + 1]
    elif i == len(array) - 1:
        return num < array[i - 1]
    else:
        return num < array[i - 1] or num > array[i + 1]


# https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/
'''
Approach : 
1.Find the subarray in right side which is continous non-increasing (let R be the starting of this array)
2. L = 0 is the start of left array 
3. Now to ensure that array is sorted interval L..R should be sorted and 
there should not exists any element in right side of subarray which is less than any element in left side of array (merge sort logic)
ex: left = [1,2,3] and right = [2,3,5] then we can't merge this two arrays to get sorted array because 2 in right subarray is less than 3 in left sub array.
So we would remove element from right subarray (we can remove from left also but for that we have to first calculate left then)
4. Keep on ensuring step3 till the point of time 
    a. left array is contigious non-decreasing subarray 
    b. there does not exists any element such that arr[left] > arr[right]
5. While performing Step3 , keep the minimum different b/w left and right pointers which would be our answer 

'''


def findLengthOfShortestSubarray(array):
    leftPtr = 0
    rightPtr = len(array) - 1
    # find right subarray
    while (rightPtr > 0):
        if array[rightPtr] >= array[rightPtr - 1]:
            rightPtr -= 1
        else:
            break

    print("RightPtr and element", rightPtr, array[rightPtr])

    # find left subarray satisfying two condition mentioned in step4
    # minDiff is set rightPtr because what if complete left array needed to be removed
    minDifference = rightPtr
    while (leftPtr < rightPtr):
        if leftPtr == 0 or array[leftPtr] >= array[leftPtr - 1]:
            # we are in the contigious left sub array

            while (rightPtr < len(array) and array[rightPtr] < array[leftPtr]):
                rightPtr += 1
                # increase window by removing right subarray elements
            #extra -1 because we have to exclude boundary elements as those are valid elements in merged array
            # ex: if L=3 and R =8 that means remove elements at index [4,5,6,7]
            if rightPtr - leftPtr - 1 < minDifference:
                minDifference = rightPtr - leftPtr - 1
                #keeping track of shortest difference we have got till now

            leftPtr += 1

        else:
            break
    print("min difference : ", minDifference)
    return minDifference


array = [1, 2, 3, 10, 4, 2, 3, 5]
array1 = [5, 4, 3, 2, 1]
array2 = [1, 2, 3]
array3 = [2, 2, 2, 1, 1, 1]
# subarraySort(array)
findLengthOfShortestSubarray(array)
