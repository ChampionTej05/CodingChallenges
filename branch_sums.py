'''
https://www.algoexpert.io/questions/branch-sums

Question : returns list of its branch sums ordered from leftmost branch sum to rightmost branch sum. 
branch sum --> Sum of values from Root to Leaf 

Approach : 
Using Recursion:  While moving down from the root to it's branch , pass down the currentSum and if the pointer hit the leaf print out the current sum 
'''


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    return branchSumRecursion(root, 0, [])


def branchSumRecursion(root, currentSum, sumArray):
    currentSum = currentSum + root.value
    if root.left == None and root.right == None:
        # hit the leaf
        sumArray.append(currentSum)
        # print(currentSum)
        return sumArray

    if root.left is not None:
        sumArray = branchSumRecursion(root.left, currentSum, sumArray)
    if root.right is not None:
        sumArray = branchSumRecursion(root.right, currentSum, sumArray)

    return sumArray


# test Code

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        tree = TestBinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])
        print(branchSums(tree))
        self.assertEqual(branchSums(tree), [15, 16, 18, 10, 11])


class TestBinaryTree(BinaryTree):
    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = TestBinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = TestBinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self


obj = TestProgram()
obj.test_case_1()