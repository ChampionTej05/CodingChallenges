'''
Product Sum of array : [x, [y,z]] = x + 2* (y+z)
'''


def isList(array):
    return type(array) == type([])


def productSum(array, depth=1):
    localSum = 0

    for ele in array:
        if isList(ele):
            localSum += productSum(ele, depth + 1)
        else:
            localSum += ele
    return localSum * depth


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
        self.assertEqual(productSum(test), 12)


obj = TestProgram()
obj.test_case_1()