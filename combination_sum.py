# https://leetcode.com/problems/combination-sum/
'''
Backtrack using base case 

A = []
for i in len(array) {
    
    a. add current element to subset
    b. check if current element in subset , makes the subset sum == target. If yes --> add subset to result 
    c. check if sum(subset) > target: remove the last added element and backtrack
    d. if sum(subset) < target: 
        i. add same element to the subset and recurse 
        ii. add next element 
}
'''


def combinationSum(candidates, target):
    resultArr = []

    for idx in range(len(candidates)):
        subset = []
        subset.append(candidates[idx])
        findAllCombinations(subset, candidates, target, idx, resultArr)
    return resultArr


def findAllCombinations(subset, candidates, target, idx, resultArr):

    subsetSum = sum(subset)
    # check if the sum is obtained or not
    if subsetSum == target:
        resultArr.append(subset)
        print("added subset to result : ", subset)
        return
    if subsetSum > target:
        #last added elements has made sum greater so remove that
        subset.pop()
        return
    if subsetSum < target:
        # we can add differenet element
        for i in range(idx + 1, len(candidates)):
            findAllCombinations(subset + [candidates[i]], candidates, target,
                                i, resultArr)
        # if idx < len(candidates) - 1:

        # add same element again
        findAllCombinations(subset + [candidates[idx]], candidates, target,
                            idx, resultArr)

    return


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        candidates = [2, 3, 5]
        target = 8
        expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        # candidates = [2, 3, 6, 7]
        # target = 7
        # expected = [[2, 2, 3], [7]]
        # candidates = [2]
        # target = 1
        # expected = []
        actual = combinationSum(candidates, target)

        self.assertEqual(expected, actual)


obj = TestProgram()
obj.test_case_1()