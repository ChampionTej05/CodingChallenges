'''
https://www.algoexpert.io/questions/node-depths

Q: Return sum of it's node's depth 
Distance b/w node and the root is the depth of node 

Approach : Start from root and increase depth at every interval 
'''


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def nodeDepths(root):
    # Write your code here.
    return nodeDepthsRecursion(root, 0)


def nodeDepthsRecursion(root, currentDepth):

    if root.left is None and root.right is None:
        return currentDepth

    leftSum, rightSum = 0, 0
    if root.left is not None:
        leftSum = nodeDepthsRecursion(root.left, currentDepth + 1)
    if root.right is not None:
        rightSum = nodeDepthsRecursion(root.right, currentDepth + 1)

    return leftSum + rightSum + currentDepth


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        # tree = TestBinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9])
        tree = TestBinaryTree(1).insert([2])
        print(nodeDepths(tree))
        # self.assertEqual(branchSums(tree), [15, 16, 18, 10, 11])


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