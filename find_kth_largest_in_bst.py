# https://www.algoexpert.io/questions/find-kth-largest-value-in-bst


# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    # Write your code here.
    nodes = inOrderTraversalReverse(tree, [], k)
    print("ans ", nodes)
    return nodes[-1]
    # return -1


# O(h + k) time and O(k) space
def inOrderTraversalReverse(tree, nodes, k):
    if tree is None or len(nodes) >= k:
        return nodes
    nodes = inOrderTraversalReverse(tree.right, nodes, k)
    if len(nodes) == k:
        print("returning with K elements", nodes)
        return nodes
    nodes.append(tree.value)
    nodes = inOrderTraversalReverse(tree.left, nodes, k)
    return nodes


#  O(n) space and time
# return len(nodes)-k th value from nodes array
def inOrderTraversal(tree, nodes):
    if tree is None:
        return nodes
    inOrderTraversal(tree.left, nodes)
    nodes.append(tree.value)
    inOrderTraversal(tree.right, nodes)
    return nodes


#using class to encapsulate the information


class TreeInfo:
    def __init__(self, nodesVisited, currentNodeVisited):
        self.nodesVisited = nodesVisited
        self.currentNodeVisited = currentNodeVisited


def reverseInOrderTraversal(treeNode, k, treeInfo):

    if treeNode is None or treeInfo.nodesVisited >= k:
        return
    reverseInOrderTraversal(treeNode.right, k, treeInfo)

    if treeInfo.nodesVisited < k:
        treeInfo.nodesVisited += 1
        treeInfo.currentNodeVisited = treeNode.value
        reverseInOrderTraversal(treeNode.left, k, treeInfo)


def findKthLargestValueInBstV1(tree, k):
    treeInfo = TreeInfo(0, None)
    reverseInOrderTraversal(tree, k, treeInfo)
    return treeInfo.currentNodeVisited


def reverseInOrderTraversalReverse(treeNode, k, treeInfo):

    if treeNode is None or treeInfo.nodesVisited >= k:
        return
    reverseInOrderTraversalReverse(treeNode.left, k, treeInfo)

    if treeInfo.nodesVisited < k:
        treeInfo.nodesVisited += 1
        treeInfo.currentNodeVisited = treeNode.value
        reverseInOrderTraversalReverse(treeNode.right, k, treeInfo)


def findKthSmallestValueInBstV1(tree, k):
    treeInfo = TreeInfo(0, None)
    reverseInOrderTraversalReverse(tree, k, treeInfo)
    return treeInfo.currentNodeVisited


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(15)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.left.right = BST(3)
        root.left.right = BST(5)
        root.right = BST(20)
        root.right.left = BST(17)
        root.right.right = BST(22)
        k = 3
        expected = 17
        actual = findKthSmallestValueInBstV1(root, k)
        kthSmallestExpected = 3
        self.assertEqual(actual, kthSmallestExpected)


obj = TestProgram()
obj.test_case_1()