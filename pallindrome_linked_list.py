# https://www.algoexpert.io/questions/linked-list-palindrome


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# using O(n) space
'''
using reverse function for half of the linked list
'''


def reverseLinkedList(head):
    # Write your code here.
    curr = head
    prev = None

    while (curr is not None):
        saveNode = curr.next
        curr.next = prev
        prev = curr
        curr = saveNode

    return prev


def isEqualLists(list1, list2):
    while (list1 is not None and list2 is not None):
        if list1.value != list2.value:
            return False
        list1 = list1.next
        list2 = list2.next
    return True


def linkedListPalindrome(head):
    # Write your code here.

    from collections import deque
    stack = deque()

    slowPtr = head
    fastPtr = head

    while (fastPtr is not None and fastPtr.next is not None):
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next.next

    #if slowPtr is  on middle node then skip the node
    if fastPtr is not None and fastPtr.next is None:
        slowPtr = slowPtr.next

    revHead = reverseLinkedList(slowPtr)

    return isEqualLists(head, revHead)


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
        ll1 = LinkedList(2).addMany([1, 3, 5, 3, 1, 2])
        ll1 = LinkedList(2)
        expected = True
        actual = linkedListPalindrome(ll1)
        self.assertEqual(expected, actual)


obj = TestProgram()
obj.test_case_1()