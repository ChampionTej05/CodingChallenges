'''
Merge Overlapping Intervals 

[[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]] 

==> [[1, 2], [3, 8], [9, 10]] 
if the two intervals overlap, merge them together 
ex: [3,5] [4,7] --> [3, 7]

'''


def isOverlapping(interval_1, interval_2):
    if interval_1[1] > interval_2[1]:
        # Completely inside the interval_1
        return interval_1
    if interval_1[1] > interval_2[0]:
        # start is inside the interval
        return [interval_1[0], interval_2[1]]
    return interval_1


'''
Sort the intervals based on start time first 
For every interval, check the continuos overlapping using start and end pointer
If the current interval is found to be non overlapping. 
Add the previous intervals maintained till now to list and reset pointer to current intervals.

Edge Case: First interval will be in the result by default and 
last interval will be added to result because of exit of loop 
'''


def mergeOverlappingIntervals(intervals):
    result = []
    intervals = sorted(intervals, key=lambda x: x[0])
    print("Sorted Intervals  ", intervals)
    lengthOfIntervals = len(intervals)
    intervalStart = intervals[0][0]
    intervalEnd = intervals[0][1]
    # result.append()
    for i in range(1, lengthOfIntervals):
        print("---------")
        print("Interval in Consideration : ", intervals[i])
        print("Start and End : ", intervalStart, intervalEnd)
        print("---------")
        if intervalEnd >= intervals[i][0]:
            # if new interval is completely inside old interval, so we should take end value as max of the both end values
            intervalEnd = max(intervals[i][1], intervalEnd)
        else:
            # merge ended , create new interval
            newInterval = [intervalStart, intervalEnd]
            intervalStart, intervalEnd = intervals[i]
            result.append(newInterval)
        print(result)

    result.append([intervalStart, intervalEnd])
    return result


'''
https://www.geeksforgeeks.org/binary-insertion-sort/#:~:text=Approach%20to%20implement%20Binary%20Insertion,element%20is%20at%20index%20pos.

Correct logic using this 
'''


def positionToInsertInSortedInterval(intervals, newInterval):
    start = 0
    end = len(intervals) - 1
    print(intervals)
    mid = 0
    targetStart = newInterval[0]
    while (start <= end):
        mid = start + (end - start) // 2
        print(start, mid, end)
        midStart = intervals[mid][0]

        if midStart > targetStart:
            end = mid - 1
        elif midStart < targetStart:
            start = mid + 1
        else:
            return mid + 1
    return start


def insertIntervals(intervals, newInterval):
    '''
    intervals is sorted array by start time.
    intervals[i] = [start[i], end[i]]
    '''

    # we can use binary search to find the position of element in array

    targetIndex = positionToInsertInSortedInterval(intervals, newInterval)
    print("Mid and element", targetIndex, intervals[targetIndex])
    newArr = intervals[:targetIndex] + [newInterval] + intervals[targetIndex:]
    return newArr


def positionToInsertInSortedArray(arr, target):
    start = 0  #
    end = len(arr) - 1
    mid = 0
    while (start <= end):
        mid = start + (end - start) // 2
        print(start, mid, end)
        if (arr[mid] > target):
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            return mid + 1
    return start


def insertElementInBinarySearch(arr, target):
    targetIndex = positionToInsertInSortedArray(arr, target)

    # now start = end = mid
    # insert element at mid location
    print("Mid and element", targetIndex, arr[targetIndex])
    newArr = arr[:targetIndex] + [target] + arr[targetIndex:]
    return newArr


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
        expected = [[1, 2], [3, 8], [9, 10]]
        actual = mergeOverlappingIntervals(intervals)
        print("Result Received : ", actual)
        self.assertEqual(actual, expected)


# obj = TestProgram()
# obj.test_case_1()

# arr = [[1, 22], [-20, 30]]
# print(mergeOverlappingIntervals(arr))
# arr = [1, 4, 6, 8, 12, 15, 17]
# # brr = [1, 3, 6, 8, 12]
# print(insertElementInBinarySearch(arr, 5))

intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]

newInterval = [4, 8]

print(insertIntervals(intervals, newInterval))
