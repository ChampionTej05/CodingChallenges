'''
Binary Search Algorithms and related  questions

By Keerti Purswani'''
import math
from re import I


def binary_search_algorithm(arr, key):
    start = 0
    end = len(arr) - 1
    if start == end:
        if arr[start] == key:
            return start
        return -1

    while start <= end:
        mid = start + int((end - start) / 2)
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            end = mid - 1
        elif arr[mid] < key:
            start = mid + 1

    return -1


'''
Sorted (ascending) Array is rotated around PIVOT at some point. Find index of PIVOT  
ex: [5, 6, 7, 8, 9, 10, 1, 2, 3] 10 is pivot 

Logic : For qualifying MID as a pivot in rotated sorted array 
1. MID should be bigger than the mid+1 ==> MID is pivot
2. If not, then if mid is smaller than mid-1 ==> MID-1 is pivot 

this is possibe because one smaller can exists between two bigger elements only if left element is pivot in sorted rotated array. 
Ex: in above case if mid =1 then it is between 10 & 2 and 2 can't be pivot since we know if 1 is smaller than 2 then all elements next to 2 will be in increasing order only that means pivot will be on left side only. 

If the MID is not PIVOT then 
1. Search in left side if low >= mid. Because if low>=mid that means from low to mid there must be some element (including low) which could be maximun element in array (pivot).  If the pivot lies on right side then low < mid. 
ex: [4,5,16,1] if mid == 5 then low<mid ==> pivot on right side.
Simple terms : left side is sorted in ascending order so if mid > mid -1  and mid > low , so that means there is generic trend of ascending sort. So there can't be any number bigger than mid in between low and mid since it is in increasing order 
2. If low < mid ==> Search in right side.


returns : index of pivot element

'''


# O(logN)
#TODO: Doesn't work for sorted non-rotated array cause condition is incorrect
def find_pivot_in_sorted_rotated_array(arr):
    start = 0
    end = len(arr) - 1
    mid = -1

    if len(arr) == 0:
        return -1

    if start == end:
        return start
    # fact: bitnoic or pivot will always exists on non-sorted part of MID
    while (start <= end):
        mid = start + int((end - start) / 2)
        if mid == 0 or mid == len(arr) - 1:
            return mid
        if mid < end and arr[mid] > arr[mid + 1]:
            # element exists on right side and it is smaller than mid --> mid is pivot as only for pivot element on right side is smaller
            return mid
        if mid > start and arr[mid] < arr[mid - 1]:
            # element exists on left and it is bigger than mid --> mid-1 is pivot as only for pivot element on left can be smaller
            return mid - 1
        #search on the left. Strict inequality for case when mid = start, ex: [2,1]
        if arr[start] > arr[mid]:  # left part is non-sorted
            end = mid - 1
        else:  # right part will have it always
            start = mid + 1
    return -1


def find_smallest_element_in_sorted_rotated_array(arr):

    if pivot == -1:
        return -1  # pivot doesn't exist in the array
    elif len(arr) == 1:
        return 0  # for single element , pivot = min
    else:
        pivot = find_pivot_in_sorted_rotated_array(arr)
        if pivot == len(arr) - 1:
            return 0
        return pivot + 1


def find_smallest_element_in_sorted_rotated_array_approach2(arr):
    start = 0
    end = len(arr) - 1
    mid = -1

    if len(arr) == 1:
        return 0

    while start <= end:
        mid = start + int((end - start) / 2)
        if mid < end and arr[mid] > arr[mid + 1]:
            # rightside element is smaller
            return mid + 1
        elif mid > start and arr[mid] < arr[mid - 1]:
            # it is between two bigger elements
            return mid

        # element will be non-sorted part of array always, right next to pivot element
        # handler edge case in non-rotated array when arr[N-1] is pivot

        # for arr = [2,1]
        if arr[start] > arr[mid]:
            end = mid - 1
        elif arr[end] < arr[mid]:
            start = mid + 1
        else:
            # if arr[start] == arr[mid] == arr[end] ==> single element left to compare
            return start
    return -1


# works for duplicate elements in array
def findMin(arr, low, high):

    while (low < high):
        mid = low + (high - low) // 2
        print(low, mid, high)
        if (arr[mid] == arr[high]):
            high -= 1
        elif (arr[mid] > arr[high]):
            low = mid + 1
        else:
            high = mid
    return arr[high]


'''
return -1 if it doesn't exist
'''


def find_element_in_sorted_rotated_array_approach(arr, target):
    start = 0
    end = len(arr) - 1
    mid = -1
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        if arr[0] == target:
            return 0
        return -1

    pivot = find_pivot_in_sorted_rotated_array(arr)
    if arr[pivot] == target:
        return pivot

    left = binary_search_algorithm(arr[:pivot], target)
    right = binary_search_algorithm(arr[pivot + 1:], target)
    print(left, right)
    if left != -1:
        return left
    if right != -1:
        return right + pivot + 1  # if right ==0   then idx = 0 + pivot + 1
    return -1


'''
Find which side of mid is sorted.
If the element exists in bounds of sorted side -> search in that side 
else search in other.
TO check if left side is sorted: arr[low] < arr[mid] 
TO check if right side is sorted : arr[mid] < arr[high]
equality condtion of arr[low] == arr[mid] or arr[mid] == arr[high] can be handled in any one of the side. We will handle it in left side
'''


def find_element_in_sorted_rotated_array_approach_2(arr, target):
    start = 0
    end = len(arr) - 1
    mid = -1
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        if arr[0] == target:
            return 0
        return -1

    while (start <= end):
        mid = start + int((end - start) / 2)
        if arr[mid] == target:
            return mid
        # check if left side is sorted
        if arr[start] <= arr[mid]:
            # check if element in bounds of left side
            if arr[start] <= target and arr[
                    mid] > target:  # we don't need to check arr[mid] >= target as == will be handled in above case
                end = mid - 1
            else:
                start = mid + 1
        else:  # right side is sorted
            # chck if element in bounds of right side
            if arr[mid] < target and arr[end] >= target:
                start = mid + 1
            else:
                end = mid - 1
    return -1


'''
# this is incorrect implementation because for bitnoic point(only 1 should exists in bitnoic sequence), we should always look for trend which can only be seen from adjancent elements
def find_bitonic_point_in_bitonic_sequence_approach2(arr):
    start = 0
    end = len(arr) - 1
    mid = -1

    if len(arr) == 0:
        return -1

    if start == end:
        return start
    # fact: bitnoic or pivot will always exists on non-sorted part of MID
    while (start <= end):
        mid = start + int((end - start) / 2)
        if mid == 0 or mid == len(arr) - 1:
            return mid
        if mid < end and arr[mid] > arr[mid + 1]:
            # element exists on right side and it is smaller than mid --> mid is pivot as only for pivot element on right side is smaller
            return mid
        if mid > start and arr[mid] < arr[mid - 1]:
            # element exists on left and it is bigger than mid --> mid-1 is pivot as only for pivot element on left can be smaller
            return mid - 1
        #search on the left. Strict inequality for case when mid = start, ex: [2,1]
        if arr[end] > arr[mid]:  # left part is non-sorted
            end = mid - 1
        else:  # right part will have it always
            start = mid + 1
    return -1
'''


def find_bitonic_point_in_bitonic_sequence(arr):
    # approach by Keerti
    start = 0
    end = len(arr) - 1
    if len(arr) == 0:
        return -1
    if start == end:
        return start
    while (start <= end):
        mid = start + int((end - start) / 2)
        print(start, mid, end)
        if (mid == 0 or arr[mid - 1] < arr[mid]) and (mid == len(arr) - 1 or
                                                      arr[mid] > arr[mid + 1]):
            return mid
        if arr[mid - 1] < arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1  # pivot is always found in an array


''' 
Lower bound index for an sorted array
This returns the index of element smaller than or equal to TARGET.
If the element is smaller than the minimum element it will return -1 
If the element is bigger than maximum element it will return N-1

NOTE: In case of duplicate elements it will return leftmost element 
 
'''


def find_lower_bound_element(arr, target):
    N = len(arr)
    if N == 0:
        return -1
    if target < arr[0]:
        return -1
    # ensure that we are not looking greater than or equal to but ONLY Strict greater
    if target >= arr[N - 1]:
        return N - 1

    start = 0
    end = N - 1
    mid = -1
    while (start <= end):
        mid = start + int((end - start) / 2)
        print(start, mid, end)

        # for getting lower bound element
        if target > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

        # for getting upperbound element
        # if target < arr[mid]:
        #     end = mid - 1
        # else:
        #     start = mid + 1
    return mid - 1


# For inserting in sorted array we find the upper bound of an array and then move array by one side from there onwards
''' Upper bound : Strictly greater than TARGET element
if it is greater than max returns N 
if it smaller than min return 0


'''
# lowerBound = upperbound - 1 (for distinct array)


def find_upper_bound_element(arr, target):
    N = len(arr)
    if N == 0:
        return -1
    if target <= arr[0]:
        return 0
    # ensure that we are not looking greater than or equal to but ONLY Strict greater
    if target > arr[N - 1]:
        return N

    start = 0
    end = N - 1
    mid = -1
    while (start <= end):
        mid = start + int((end - start) / 2)
        print(start, mid, end)

        # for getting upperbound element
        if target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return mid


# def find_upper_bound_element(arr, target):

if __name__ == '__main__':
    # nums = [-4, -1, 1, 3, 5, 6, 8, 11]
    # target = -1
    # result = binary_search_algorithm(nums, target)
    # print(result)
    rotated_arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    dup_arr = [10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8]
    drr = [2, 3, 10, 1]
    arr = [1, 2, 3, 4, 5]
    crr = [5, 2]
    mrr = [1, 5, 11, 13]

    # brr = [10, 20, 30, 40, 50, 5, 7]
    # result = find_pivot_in_sorted_rotated_array(dup_arr)

    # result1 = find_smallest_element_in_sorted_rotated_array_approach2(arr)
    # result = find_element_in_sorted_rotated_array_approach_2(rotated_arr, 11)
    # print(result)
    # print(result1)
    # if result == -1:
    #     # array is not rotated
    #     print(arr[-1])
    # else:
    #     print(arr[result])
    # idx = find_smallest_element_in_sorted_rotated_array(brr)
    # # print(brr[idx])
    # obj = Solution()
    # print(obj.findMin(crr, len(crr)))

    arr = [1, 2, 3, 3, 3, 3, 3, 5, 6, 7, 8, 9, 10]
    brr = [1, 3]
    drr = [1, 2, 3, 4, 7, 9, 10]
    crr = [1, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6]
    # lower = find_lower_bound_element(drr, 5)
    # upper = find_upper_bound_element(drr, 5)
    # print(lower, upper)

    # arr = [3, 3, 3, 3, 3, 3, 3, 5, 1, 3]
    # result = findMin(arr, 0, len(arr) - 1)
    # # result1 = find_smallest_element_in_sorted_rotated_array_approach2(arr)
    # print(result)

    arr = [4, 10, 10, 9, 8, 7, 5, 4, 3, 2, 1]
    result1 = find_bitonic_point_in_bitonic_sequence(arr)
    print(result1)
