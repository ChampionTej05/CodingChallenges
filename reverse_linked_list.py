# https://www.algoexpert.io/questions/reverse-linked-list


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


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
