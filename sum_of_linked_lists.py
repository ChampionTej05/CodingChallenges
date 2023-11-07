'''

Original Question : https://www.algoexpert.io/questions/sum-of-linked-lists
'''
'''
Let's first solve easy one where head is least significant bit 

ex:
L1 = 2 -> 4 ->1 , L2 = 9 -> 1 
L1+L2 = 142+19 = 161
'''

from unittest import result


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        print("Node value : ", self.value)


# head is least significant bit
def sumOfLinkedListsv1(linkedListOne, linkedListTwo):
    # Write your code here.

    resultArr = []
    addList(linkedListOne, linkedListTwo, 0, resultArr)
    # print(resultArr)
    resultLinkedList = LinkedList(resultArr[0].value)
    # print("Head", resultLinkedList)
    current = resultLinkedList
    for idx in range(1, len(resultArr)):
        print("item ", resultArr[idx].value)
        current.next = LinkedList(resultArr[idx].value)
        current = current.next

    return resultLinkedList


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.

    resultArr = []
    resultLinkedList = addList(linkedListOne, linkedListTwo, 0, resultArr)
    return resultLinkedList


def addList(L1, L2, carry, resultArr):

    if L1 == None and L2 == None and carry == 0:
        return None

    currentSum = 0
    if L1 != None:
        currentSum += L1.value

    if L2 != None:
        currentSum += L2.value

    currentSum += carry
    result = LinkedList(currentSum % 10)
    carry = 1 if currentSum > 9 else 0

    resultArr.append(result)
    if L1 != None or L2 != None:
        newNode = addList(None if not L1 else L1.next,
                          None if not L2 else L2.next, carry, resultArr)
        result.next = newNode
    return result


import unittest


class LinkedList(LinkedList):
    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self


def getNodesInArray(output):
    nodes = []
    current = output
    while current is not None:
        nodes.append(current.value)
        current = current.next
    print(nodes)
    return nodes


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        ll1 = LinkedList(2).addMany([4, 7, 1])
        ll2 = LinkedList(9).addMany([4, 5])
        expected = LinkedList(1).addMany([9, 2, 2])
        actual = sumOfLinkedLists(ll1, ll2)
        self.assertEqual(getNodesInArray(actual), getNodesInArray(expected))


obj = TestProgram()
obj.test_case_1()