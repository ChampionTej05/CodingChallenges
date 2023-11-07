class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "[ % s ] -> " % (self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        temp = self.head
        print(" ---------------- ")
        while (temp is not None):
            print(temp, end=" ")
            temp = temp.next
        print(" ---------------- ")
        return ""

    def insert_at_begin(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        temp = self.head
        while (temp.next is not None):
            temp = temp.next
        new_node = Node(value)
        temp.next = new_node

    # assumed index is always less than length of queue
    # 0-based indexing
    # resultant element will be inserted at idx+1
    def insert_after_index(self, value, idx):
        counter = 0
        temp = self.head
        while (counter < idx):
            temp = temp.next
            counter += 1
        next_ptr = temp.next
        new_node = Node(value)
        temp.next = new_node
        new_node.next = next_ptr

    def insert_after_node(self, prev_node, value):
        new_node = Node(value)
        if prev_node is None:
            self.head = new_node
            return
        new_node.next = prev_node.next
        prev_node.next = new_node


if __name__ == "__main__":

    linked_list = LinkedList()
    linked_list.insert_at_begin(1)
    linked_list.insert_at_begin(2)
    linked_list.insert_at_begin(3)
    print(linked_list)

    linked_list.insert_at_end(5)
    linked_list.insert_at_end(6)
    print(linked_list)

    linked_list.insert_after_index(10, 1)
    linked_list.insert_after_index(11, 5)
    print(linked_list)

    linked_list.insert_after_node(linked_list.head, 98)
    print(linked_list)
