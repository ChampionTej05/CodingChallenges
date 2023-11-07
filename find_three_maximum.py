'''
Find 3 largest numbers from the array (len>3)

Solve using O(n) time and ideally O(1) space 
'''


def findThreeLargestNumbers(array):
    if len(array) < 3:
        return []

    temp = array[:3]

    # const time for sorting array of size
    temp.sort()
    #adjust pointers
    min_ele, mid_ele, max_ele = temp
    print("Initial : ", min_ele, max_ele, mid_ele)
    for idx in range(3, len(array)):
        key = array[idx]
        if key >= max_ele:
            min_ele = mid_ele
            mid_ele = max_ele
            max_ele = key

        elif key >= mid_ele:
            min_ele = mid_ele
            mid_ele = key
        elif key >= min_ele:
            min_ele = key

    return [min_ele, mid_ele, max_ele]


def findThreeLargestNumbersNew(array):
    '''
    Keep constant array to keep top 3 elements everytime and sort them (constant time as array size is constant).
    We used size of 4 because first element is always going to change, so if we use 3 size array , 1st largest element in the result will be lost. 
    ex: [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
    ans : [18, 141, 541
    
    '''
    import sys
    temp = [-sys.maxsize] * 4
    for key in array:
        temp[0] = key
        temp.sort()

    print(temp)
    return temp[1:]


import unittest


class TestCase(unittest.TestCase):
    def testCase(self):
        array = [10, 5, 9, 10, 12]
        expected = [10, 10, 12]
        actual = findThreeLargestNumbersNew(array)
        self.assertEqual(actual, expected)


obj = TestCase()
obj.testCase()