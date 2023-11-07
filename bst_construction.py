'''
Construct a BST instance
Insert 
Remove --> method should remove only first instance of value. Calling remove on single node should not perform any operations.
'''

# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
# from platform import node
import time


class BST:
    LEFT = 1
    RIGHT = 0

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return '[ ' + str(self.value) + ' ]'

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        self.insertNode(self, value)

    def insertNode(self, root, value):
        if value < root.value:
            if root.left is None:
                newNode = BST(value)
                root.left = newNode
                return
            self.insertNode(root.left, value)
        else:
            if root.right is None:
                newNode = BST(value)
                root.right = newNode
                return
            self.insertNode(root.right, value)
        return

    def contains(self, value):
        # Write your code here.
        if self is None:
            return False
        # print("Checking for Self.value : ", self.value)
        if self.value == value:
            return True

        if self.value > value:
            #go left
            if self.left is None:
                return False
            return self.left.contains(value)
        elif self.value < value:
            #go right
            if self.right is None:
                return False
            return self.right.contains(value)

    '''
    Case 1: Node is leaf node --> remove directly 
    Case 2: Node has left child only --> replace node with it's left child 
    Case 3: Node has right child only --> replace node with it's right child 
    Case 4: Node has both left and right child --> 
            * find the largest value in left subtree 
            * Make the largest value node's parent 's child as NULL (delink lead node)
            * Copy Largest value to nodeToRemove position
    '''

    def remove(self, value):
        # find the node to be deleted
        nodeToRemove, parent = self.findNode(value)
        print("node to remove: ", nodeToRemove)
        if nodeToRemove == None:
            return

        # Case 1
        if nodeToRemove.left == None and nodeToRemove.right == None:
            print("Case 1 ")
            if parent == None:
                #only node left in tree , don't do anything
                return
            else:
                childOn = self.whereDoesChildBelong(nodeToRemove, parent)
                if childOn == self.LEFT:
                    parent.left = None
                else:
                    parent.right = None
            return

        # Case 2
        if nodeToRemove.left != None and nodeToRemove.right == None:
            print("Case 2 ")
            if parent == None:
                # Root node and it has only left subtree
                # move the root to node.left
                self.value = nodeToRemove.left.value
                #order is very important
                '''
                insert(10), insert(5), remove(10)
                if the order is flipped, self.left = None and then right 
                side will be lost
                '''
                self.right = nodeToRemove.left.right
                self.left = nodeToRemove.left.left
                return

            childOn = self.whereDoesChildBelong(nodeToRemove, parent)
            if childOn == self.LEFT:
                parent.left = nodeToRemove.left
                nodeToRemove.left = None
            else:
                parent.right = nodeToRemove.left
                nodeToRemove.left = None
            return
        # Case 3
        if nodeToRemove.right != None and nodeToRemove.left == None:
            print("Case 3 ")
            if parent == None:
                self.value = nodeToRemove.right.value
                self.left = nodeToRemove.right.left
                self.right = nodeToRemove.right.right
                return
            childOn = self.whereDoesChildBelong(nodeToRemove, parent)
            if childOn == self.LEFT:
                parent.left = nodeToRemove.right
                nodeToRemove.right = None
            else:
                parent.right = nodeToRemove.right
                nodeToRemove.right = None
            return

        # Case 4
        # if nodeToRemove.left != None and nodeToRemove.right != None:
        #     # find maximum node in left subtree
        #     maxNodeLeftTree = nodeToRemove.left.findMaxNode()
        #     maxNodeLeftTree, maxNodeLeftTreeParent = self.findNode(
        #         maxNodeLeftTree.value)

        #     # copy the node value
        #     nodeToRemove.value = maxNodeLeftTree.value

        #     # if the maxNodeLeftTree is simply leaf node; delink it
        #     if maxNodeLeftTree.left == None and maxNodeLeftTree.right == None:
        #         if maxNodeLeftTree.value <= maxNodeLeftTreeParent.value:
        #             maxNodeLeftTreeParent.left = None
        #         else:
        #             maxNodeLeftTreeParent.right = None
        #         return
        #     else:
        #         # recursively delete the maxNodeLeftTree
        #         maxNodeLeftTree.remove(maxNodeLeftTree.value)
        #     return

        # Case 4
        if nodeToRemove.left != None and nodeToRemove.right != None:
            print("Case 4 ")
            # find minimum node in right subtree
            maxNodeRightTree = nodeToRemove.right.findMinNode()
            maxNodeRightTree, maxNodeRightTreeParent = nodeToRemove.right.findNode(
                maxNodeRightTree.value)

            # copy the node value
            nodeToRemove.value = maxNodeRightTree.value

            # if the maxNodeRightTree is simply leaf node; delink it
            if maxNodeRightTree.left == None and maxNodeRightTree.right == None:
                if maxNodeRightTreeParent == None:
                    # it means this is exact right node of nodeToRemove
                    nodeToRemove.right = None
                    return
                if maxNodeRightTree.value < maxNodeRightTreeParent.value:
                    maxNodeRightTreeParent.left = None
                else:
                    maxNodeRightTreeParent.right = None
                return
            else:
                # recursively delete the maxNodeLeftTree
                maxNodeRightTree.remove(maxNodeRightTree.value)

            # can't do this simple recursion because if single node to delete then we don't do anything
            # nodeToRemove.right.remove(maxNodeRightTree.value)
            return

    # find max node object in tree
    def findMaxNode(self):
        if self.right == None:
            return self
        return self.right.findMaxNode()

    def findMinNode(self):
        if self.left == None:
            return self
        return self.left.findMinNode()

    def findNode(self, value):
        parent = None
        current = self

        while (current != None):
            time.sleep(1)
            print("Current : ", current)
            if current.value == value:
                return current, parent

            if current.value > value:
                # left
                parent = current
                current = current.left
                # pass
            else:
                # right
                parent = current
                current = current.right
                # pass
        return None, None

    def whereDoesChildBelong(self, child, parent):
        # assumed child and parent exists
        if child.value < parent.value:
            return self.LEFT
        else:
            return self.RIGHT


import unittest


def printTree(node, level=0):
    if node != None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.value))
        printTree(node.right, level + 1)


def print2DTree(root, space=0, LEVEL_SPACE=5):
    if (root == None): return
    space += LEVEL_SPACE
    print2DTree(root.right, space)
    # print() # neighbor space
    for i in range(LEVEL_SPACE, space):
        print(end=" ")
    print("|" + str(root.value) + "|<")
    print2DTree(root.left, space)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        '''
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)

        root.insert(12)
        self.assertTrue(root.right.left.left.value == 12)
        # root.insert(24)
        print("--------------------------------")
        print2DTree(root)
        print("--------------------------------")
        # print(root.findMaxNode())
        # node, parent = root.findNode(1)
        # print(node)
        # print(parent)

        root.remove(10)
        self.assertTrue(not root.contains(10))
        # self.assertTrue(root.value == 12)
        print("--------------------------------")
        print2DTree(root)
        print("--------------------------------")

        self.assertTrue(root.contains(12))

        # root.remove(10)
        # self.assertTrue(not root.contains(10))
        # self.assertTrue(root.value == 12)

        self.assertTrue(root.contains(15))

        # newRoot = BST(10)
        # print("--------------------------------")
        # print2DTree(newRoot)
        # print("--------------------------------")
        # newRoot.remove(10)
        # print("--------------------------------")
        # print2DTree(newRoot)
        # print("--------------------------------")
        '''
        root = BST(10)
        root.insert(5)
        root.insert(15)
        root.insert(5)
        root.insert(13)
        root.insert(22)
        root.insert(1)
        root.insert(14)
        root.insert(12)

        print("--------------------------------")
        print2DTree(root)
        print("--------------------------------")

        root.remove(5)
        print("--------------------------------")
        print2DTree(root)
        print("--------------------------------")


obj = TestProgram()
obj.test_case_1()