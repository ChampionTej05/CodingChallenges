'''
Question : Write a function to take Non-empty "DISTINCT" integer array and interger for Target sum. Return any two DISTINCT Numbers that sum up to target sum from an array. Order is not important 
Assumption is there can be at most one pair exists in the array 
Expected Complexity : O(n) Time & O(n) Space
'''
'''
Solution is hash map memoisation. Remember the expectedSum calculated in the Past. While traversing if we find it, return the elements 
'''


class TwoSumNumber():
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    ''' O(N) time & O(N) Space'''

    def two_sum_hash_table(self):
        mapper = {}
        for i in range(len(self.nums)):
            expectedSum = self.target - self.nums[i]
            if expectedSum not in mapper.keys():
                mapper[self.nums[i]] = i
            else:
                return [self.nums[i], expectedSum]

        return []

    ''' O(N) time & O(N) Space'''

    def two_sum_hash_table_multi_answer(self):

        mapper = {}
        answers = []
        for i in range(len(self.nums)):

            expectedSum = self.target - self.nums[i]
            if expectedSum not in mapper.keys():
                mapper[self.nums[i]] = i
            else:
                answers.append([expectedSum, self.nums[i]])

        return answers[::-1]

    ''' O(NlogN) time & O(1) Space'''

    def two_sum_binary_search(self):
        self.nums.sort()
        start = 0
        end = len(self.nums) - 1
        while (start <= end):

            currentSum = self.nums[start] + self.nums[end]
            if currentSum < self.target:
                start = start + 1
            elif currentSum > self.target:
                end = end - 1
            else:
                return [self.nums[start], self.nums[end]]
        return []


'''
Find triplet of numbers such that they sum upto target 
Conditions 
1. Number in each triplet should be ordered in Ascending orders 
2. Triplet themselves should be ordered in Ascending order 

ex: nums = [12, 3, 1, 2, -6, 5, -8, 6], target = 0
Return  : [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
'''


class ThreeSumNumber():
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    ''' O(N^2) [NlogN is smaller than N^2] Solution with O(N) space'''

    def three_sum_hash_table(self):
        answers = []
        self.nums.sort()
        print("Nums Sorted : ", self.nums)
        for i in range(len(self.nums)):
            expectedSum = self.target - self.nums[i]
            twoSumObject = TwoSumNumber(self.nums[i + 1:], expectedSum)
            results = twoSumObject.two_sum_hash_table_multi_answer()
            if len(results) > 0:
                print("nums[i], results", self.nums[i], results)
                for result in results:
                    answers.append([self.nums[i], result[0], result[1]])
        return answers


if __name__ == '__main__':
    nums = [3, 5, -4, 8, 11, 1, -1, 6]
    target = 10
    nums1 = [12, 3, 1, 2, -6, 5, -8, 6]
    target1 = 0
    # twoSumObject = TwoSumNumber(nums, target)
    # result = twoSumObject.two_sum_binary_search()

    threeSumObject = ThreeSumNumber(nums1, target1)
    result = threeSumObject.three_sum_hash_table()
    print(result)