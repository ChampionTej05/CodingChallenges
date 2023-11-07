'''
https://www.algoexpert.io/questions/find-loop

For explanation read Gayle's book : Page No 224
'''


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoopUsingExtraSpace(head):
    # Write your code here.
    # used specifically since there can be cycle causing duplication
    mapper = set()
    while head != None:
        if head in mapper:
            return head
        else:
            mapper.add(head)
        head = head.next
    return head


#
def findLoop(head):
    # find the collision point
    fastPtr = head
    slowPtr = head

    # this loop condition is needed to check if loop exists or not
    while (fastPtr != None and fastPtr.next != None):
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next.next
        if slowPtr == fastPtr:
            #loop found
            break

    if fastPtr == None or fastPtr.next == None:
        #that means fastPtr has reached the end of list without colliding with slowPtr--> No loop exists in  the linkedList
        return None

    #Now collision point is inside the loop
    #move the slowPtr to head of the list
    slowPtr = head

    # find meeting point
    while (slowPtr != fastPtr):
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next

    return slowPtr
