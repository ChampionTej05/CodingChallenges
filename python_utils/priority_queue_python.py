# https://www.geeksforgeeks.org/priority-queue-using-queue-and-heapdict-module-in-python/

from queue import PriorityQueue

priority_queue = PriorityQueue()

priority_queue.put((1, 'a'))
priority_queue.put((2, 'b'))
priority_queue.put((11, 'x'))
priority_queue.put((-1, 'd'))
priority_queue.put((-3, 'f'))

print(priority_queue)

#get first element priority
print(priority_queue.queue[0])

#print queue (prints array used to maintain queue)
print(priority_queue.queue)

popped_element = priority_queue.get()
print(popped_element)

#update the priority of top element

get_top = priority_queue.get()
new_element = (7, get_top[1])
priority_queue.put(new_element)

print(priority_queue.queue)

#to get items in actual order of elements as in heap

while not priority_queue.empty():
    print(priority_queue.get())
