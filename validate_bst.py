class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


import sys


def validateBst_Helper(tree, min_ele=-sys.maxsize, max_ele=sys.maxsize):

    # min_ele = -sys.maxsize
    # max_ele = sys.maxsize
    '''
    Every node will have max and min value possible which will be corresponding to it's parent and grandparent. 
    
    '''

    if not tree: return True

    if min_ele >= tree.value or tree.value >= max_ele:
        return False

    isLeftValid = True
    isRightValid = True
    if tree.left:
        isLeftValid = validateBst_Helper(tree.left, min_ele, tree.value)

    if tree.right:
        isRightValid = validateBst_Helper(tree.right, tree.value, max_ele)

    return isLeftValid and isRightValid


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        # root = BST(10)
        # root.left = BST(5)
        # root.left.left = BST(2)
        # root.left.left.left = BST(1)
        # root.left.right = BST(5)
        # root.right = BST(15)
        # root.right.left = BST(13)
        # root.right.left.right = BST(14)
        # root.right.right = BST(22)

        # # print(inOrderTraversal(root))
        # self.assertEqual(validateBst_Helper(root), True)

        # root = BST(10)
        # root.left = BST(5)
        # root.left.right = BST(10)
        # root.right = BST(15)
        # self.assertEqual(validateBstUsingInOrder(root), False)

        root = BST(2)
        root.left = BST(2)
        root.right = BST(2)

        self.assertEqual(validateBst_Helper(root), False)


obj = TestProgram()
obj.test_case_1()