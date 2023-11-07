# https://www.algoexpert.io/questions/same-bsts
'''
Approach : Construct two BSTs and compare them
'''


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(treeNode, key):
    if treeNode is None:
        return

    if treeNode.value > key:
        if treeNode.left is None:
            newNode = BST(key)
            print("newNode: ", newNode.value)
            treeNode.left = newNode

        else:
            insert(treeNode.left, key)
    else:
        if treeNode.right is None:
            newNode = BST(key)
            print("newNode: ", newNode.value)
            treeNode.right = newNode
            treeNode
        else:
            insert(treeNode.right, key)


def constructBST(array):

    arr = array[1:]
    print("arr ")
    root = BST(array[0])
    for item in arr:
        insert(root, item)
        # print("root value", root.value)

    print("inOrder", inOrder(root, []))
    return root


def inOrder(treeNode, nodes=[]):
    if treeNode is None:
        return nodes

    inOrder(treeNode.left, nodes)
    nodes.append(treeNode.value)
    inOrder(treeNode.right, nodes)
    return nodes


def sameBSTs(treeNode1, treeNode2):

    if treeNode1 is None and treeNode2 is None:
        return True

    if treeNode1 is None and treeNode2 is not None:
        return False

    if treeNode1 is not None and treeNode2 is None:
        return False
    #root is same
    if treeNode1.value != treeNode2.value:
        return False

    # check if its leaf node
    if treeNode1.left is None and treeNode2.left is None and treeNode1.right is None and treeNode2.right is None:
        return True

    #check for left
    isLeftValid = False
    isRightValid = False
    isLeftValid = sameBSTs(treeNode1.left, treeNode2.left)
    isRightValid = sameBSTs(treeNode1.right, treeNode2.right)

    return isLeftValid and isRightValid


#  without constructing trees
# messy solution , fix this, this is incorrect
def sameBstsBAD(arrayOne,
                arrayTwo,
                idx1=0,
                idx2=0,
                prevroot1=-1,
                prevroot2=-1):
    if len(arrayOne) != len(arrayTwo):
        return False
    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True

    root1 = arrayOne[idx1]
    root2 = arrayTwo[idx2]

    if root1 != root2:
        return False

    leftRoot1 = findSmall(arrayOne, root1, idx1, prevroot1)
    leftRoot2 = findSmall(arrayTwo, root2, idx2, prevroot2)
    print("leftroot1 for root1", leftRoot1, arrayOne[leftRoot1], root1)
    print("leftRoot2 for root2", leftRoot2, arrayTwo[leftRoot2], root2)
    isLeftValid = False
    #  this is going to be node in tree with no left subtree
    if leftRoot1 == leftRoot2 and leftRoot1 == -1:
        isLeftValid = True
    else:
        isLeftValid = sameBsts(arrayOne, arrayTwo, leftRoot1, leftRoot2, root1,
                               root2)
    if not isLeftValid:
        return isLeftValid

    rightRoot1 = findLarge(arrayOne, root1, idx1, prevroot1)
    rightRoot2 = findLarge(arrayTwo, root2, idx2, prevroot2)
    print("rightRoot1 for root1", rightRoot1, arrayOne[rightRoot1], root1)
    print("rightRoot2 for root2", rightRoot2, arrayTwo[rightRoot2], root2)
    isRightValid = False
    # this is going to be node in tree with no right subtree
    if rightRoot1 == rightRoot2 and rightRoot1 == -1:
        isRightValid = True
    else:
        isRightValid = sameBsts(arrayOne, arrayTwo, rightRoot1, rightRoot2,
                                root1, root2)
    return isLeftValid and isRightValid


def findSmall(array, key, idx1, prevroot):
    import sys
    if idx1 == 0:
        prevroot = sys.maxsize
    for i in range(idx1 + 1, len(array)):
        if array[i] < key and array[i] < prevroot:
            return i
    return -1


def findLarge(array, key, idx1, prevroot):
    import sys
    if idx1 == 0:
        prevroot = -sys.maxsize
    for i in range(idx1 + 1, len(array)):
        if array[i] >= key and array[i] >= prevroot:
            return i

    return -1


# correct and optimal solution
def sameBsts(arrayOne, arrayTwo):
    if len(arrayOne) != len(arrayTwo):
        return False
    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True

    if arrayOne[0] != arrayTwo[0]:
        return False

    smaller1 = findAllSmallerThanRoot(arrayOne)
    smaller2 = findAllSmallerThanRoot(arrayTwo)

    isLeftValid = sameBsts(smaller1, smaller2)
    if not isLeftValid:
        return False

    larger1 = findAllLargerThanRoot(arrayOne)
    larger2 = findAllLargerThanRoot(arrayTwo)
    isRightValid = sameBsts(larger1, larger2)
    if not isRightValid:
        return False
    return isRightValid and isLeftValid


def findAllSmallerThanRoot(array):
    key = array[0]
    smaller = []
    # skip first element as it is root
    for i in range(1, len(array)):
        if array[i] < key:
            smaller.append(array[i])
    return smaller


def findAllLargerThanRoot(array):
    key = array[0]
    larger = []
    # skip first element as it is root
    for i in range(1, len(array)):
        if array[i] >= key:
            larger.append(array[i])
    return larger


# this is better and correct code for above messy code
import sys


def sameBSTsNonMessy(arrayOne,
                     arrayTwo,
                     idx1=0,
                     idx2=0,
                     minValue=-sys.maxsize,
                     maxValue=sys.maxsize):

    # leaf node
    if idx1 == -1 or idx2 == -1:
        return idx1 == idx2

    if arrayOne[idx1] != arrayTwo[idx2]:
        return False

    leftRootIdx1 = getIdxOfFirstSmaller(arrayOne, idx1, minValue)
    leftRootIdx2 = getIdxOfFirstSmaller(arrayTwo, idx2, minValue)

    currentValue = arrayOne[idx1]  # since both values are same
    isLeftValid = sameBSTsNonMessy(arrayOne, arrayTwo, leftRootIdx1,
                                   leftRootIdx2, minValue, currentValue)

    if not isLeftValid: return False

    rightRootIdx1 = getIdxOfFirstBigger(arrayOne, idx1, maxValue)
    rightRootIdx2 = getIdxOfFirstBigger(arrayTwo, idx2, maxValue)

    isRightValid = sameBSTsNonMessy(arrayOne, arrayTwo, rightRootIdx1,
                                    rightRootIdx2, currentValue, maxValue)

    return isLeftValid and isRightValid


def getIdxOfFirstSmaller(array, startIdx, minVal):
    # we have placed lower bound on result value that it can not be greater than minValue which is basically value of previous parent node.
    # this ensures that we by mistake does not find a value which is not under current parent node
    #ex: [10,8,2,5,1,15] func(5) will find value 2 or 1 smaller value but actually in tree, it would not be under 5 or it's parent(8) so every value which 5 can find, will have lower bound of it's parent value

    for i in range(startIdx + 1, len(array)):
        if array[i] < array[startIdx] and array[i] >= minVal:
            return i
    return -1


def getIdxOfFirstBigger(array, startIdx, maxVal):
    # we have placed upper bound check on result value
    # this ensures that we look for the value in the current parent subtree only
    #ex: [10,8,5,15,12] , and if we call func for value 5 then it might give result as 15 but actually 15 is not under left subtree of 8 (parent of 5)

    for i in range(startIdx + 1, len(array)):
        if array[i] >= array[startIdx] and array[i] < maxVal:
            return i
    return -1


def sameBstsPractice(arrayOne: list, arrayTwo: list):

    # base conditions
    if len(arrayOne) != len(arrayTwo):
        return False
    if len(arrayOne) == 0:
        return True

    if arrayOne[0] != arrayTwo[0]:
        return False

    # root is same now

    leftSubTreeOne = findSmallerThanRoot(arrayOne)
    leftSubTreeTwo = findSmallerThanRoot(arrayTwo)

    isLeftValid = sameBstsPractice(leftSubTreeOne, leftSubTreeTwo)
    if not isLeftValid: return False

    rightSubTreeOne = findLargetThanRoot(arrayOne)
    rightSubTreeTwo = findLargetThanRoot(arrayTwo)

    isRightValid = sameBstsPractice(rightSubTreeOne, rightSubTreeTwo)
    if not isRightValid:
        return False
    return True


def findSmallerThanRoot(array):
    root = array[0]
    smaller = []
    for i in range(1, len(array)):
        if array[i] < root:
            smaller.append(array[i])

    return smaller


def findLargetThanRoot(array):
    root = array[0]
    larger = []
    for i in range(1, len(array)):
        if array[i] >= root:
            larger.append(array[i])
    return larger


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        arrayOne = [10, 15, 8, 12, 94, 81, 5, 2, 11]
        arrayTwo = [10, 8, 5, 15, 2, 12, 11, 94, 81]

        # root1 = constructBST(arrayOne)
        # root2 = constructBST(arrayTwo)
        # nodes = inOrder(root, [])
        # print(nodes)
        # self.assertEqual(sameBSTs(root1, root2), True)
        arrayOne = [10, 15, 8, 12, 5]
        arrayTwo = [10, 8, 5, 15, 12]
        self.assertEqual(sameBstsPractice(arrayOne, arrayTwo), True)


obj = TestProgram()
obj.test_case_1()
