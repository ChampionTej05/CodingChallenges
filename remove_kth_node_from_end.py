# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
    backPtr = head
    forwardPtr = head

    #set the forward ptr at kth location
    count = 0
    while (count < k):
        forwardPtr = forwardPtr.next
        count += 1

    # move both pointers till forwardPtr reaches end i.e forwardPtr will travel N-K steps

    while (forwardPtr != None):
        backPtr = backPtr.next
        forwardPtr = forwardPtr.next

    #now backPtr will be at (N-K)th node from beginning i.e Kth node from the last

    print("Back Ptr valueL ", backPtr.value)

    #remove node by copying it's data

    backPtr.value = backPtr.next.value
    backPtr.next = backPtr.next.next


import unittest


class StartLinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


linkedListClass = LinkedList
# if hasattr(program, "LinkedList"):
#     linkedListClass = program.LinkedList


class LinkedList(linkedListClass):
    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        print(nodes)
        return nodes


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = LinkedList(0).addMany([1, 2, 3, 4, 5])
        expected = LinkedList(0).addMany([1, 2, 3, 5])
        removeKthNodeFromEnd(test, 2)
        self.assertEqual(test.getNodesInArray(), expected.getNodesInArray())


obj = TestProgram()
obj.test_case_1()
