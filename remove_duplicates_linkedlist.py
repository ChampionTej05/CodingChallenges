class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return "LinkedList Value:% s Next:% s" % (self.value, self.next)


def create_linked_list(linkedList, value):
    if linkedList is None:
        return LinkedList(value)
    node = LinkedList(value)
    linkedList.next = node
    return node


def insert_linked_list(linkedList, value):
    if linkedList is None:
        return LinkedList(value)

    head = linkedList
    while (head.next is not None):
        head = head.next
    node = LinkedList(value)
    head.next = node
    return linkedList


def bulk_insert_linked_list(values):
    head = LinkedList(values[0])
    ptr = head
    for i in range(1, len(values) - 1):
        node = LinkedList(values[i])
        ptr.next = node
        ptr = node
    return head


def list_print(linkedList):
    ptr = linkedList
    while (ptr is not None):
        print(ptr.value)
        ptr = ptr.next


def remove_duplicates_elements_from_sorted_list(head):
    if head is None:
        return head
    if head.next is None:
        return head

    slowPtr = head
    fastPtr = head.next

    while (fastPtr is not None):
        if fastPtr.value == slowPtr.value:
            fastPtr = fastPtr.next
        else:
            slowPtr.next = fastPtr
            slowPtr = fastPtr
            fastPtr = fastPtr.next

    slowPtr.next = None  #  this is needed if 5,8,11,11 then fastPtr will be none at end and slowPtr will point to first 11 so duplicate won't get removed
    return head


def remove_duplicates_elements_from_sorted_list_Approach2(head):
    if head is None:
        return head
    if head.next is None:
        return head

    slowPtr = head
    while (slowPtr is not None):
        fastPtr = slowPtr.next
        while (fastPtr is not None and fastPtr.value == slowPtr.value):
            fastPtr = fastPtr.next
        slowPtr.next = fastPtr
        slowPtr = fastPtr

    return head


# def remove_duplicates_elements(linkedList):

if __name__ == '__main__':
    # headPtr = create_linked_list(None, 1)
    # tailPtr = create_linked_list(headPtr, 2)
    # tailPtr = create_linked_list(tailPtr, 3)
    # tailPtr = create_linked_list(tailPtr, 4)

    # head = None
    # head = insert_linked_list(head, 1)
    # # print(head)
    # head = insert_linked_list(head, 2)
    # # print(head)
    # head = insert_linked_list(head, 3)
    # print(head)

    # list_print(head)

    # ptr = head
    # while (ptr != None):
    #     print(ptr.value)
    #     ptr = ptr.next

    values = [1, 1, 3, 4, 4, 4, 5, 6, 6]
    head = bulk_insert_linked_list(values)
    # list_print(head)
    newHead = remove_duplicates_elements_from_sorted_list(head)
    list_print(newHead)