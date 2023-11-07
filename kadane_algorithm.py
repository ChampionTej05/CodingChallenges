'''
Given an integer array arr, find the contiguous subarray (containing at least one number) which
has the largest sum and return its sum and print the subarray.

Example 1:

Input: arr = [-2,1,-3,4,-1,2,1,-5,4] 

Output: 6 

Explanation: [4,-1,2,1] has the largest sum = 6. 

Examples 2: 

Input: arr = [1] 

Output: 1 

Explanation: Array has only one element and which is giving positive sum of 1. 
'''

import sys


# worst case O(n*n*n)
# can be made O(n*n) if we don't use loop for calculating SUM
def maxSubArrayNaive(nums):
    max_sum = -sys.maxsize - 1
    result = []

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            temp_arr = nums[i:j + 1]
            temp_sum = sum(temp_arr)
            print("Temp Arr {temp_arr} , sum = {temp_sum}".format(
                temp_arr=temp_arr, temp_sum=temp_sum))

            if temp_sum > max_sum:
                max_sum = temp_sum
                result = temp_arr
    return max_sum


def maxSubArrayOptimal(nums):
    max_sum_i_index = 0
    max_sum_so_far = -sys.maxsize - 1
    start_index = 0
    end_index = -1

    for i in range(len(nums)):
        max_sum_i_index += nums[i]

        #if the max sum before this index is benefited from adding this value then only we are going to add it in the subarray

        if max_sum_so_far < max_sum_i_index:
            max_sum_so_far = max_sum_i_index
            end_index = i

        # if the sum after adding this index sum < 0, then using this sum index would never increase our sum in future too , since it is negative. So we will drop this sum and start the subarray from next number

        if max_sum_i_index < 0:
            max_sum_i_index = 0
            start_index = i + 1

    print(
        "Max Sum so Far {max_sum_so_far}, start {start_index} , end {end_index}"
        .format(max_sum_so_far=max_sum_so_far,
                start_index=start_index,
                end_index=end_index))
    return max_sum_so_far


import unittest


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        expected = 6
        self.assertEqual(maxSubArrayOptimal(nums), expected)


obj = TestProgram()
obj.test_case_1()