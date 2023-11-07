import heapq
from multiprocessing import heap

# minHeap = [5, 6, 9, 1, 3]

# # min heap

# heapq.heapify(minHeap)

# print(minHeap)

# # maxheap
# arr = [2, 3, 1, 8, 9, 1]
# maxHeap = []
# heapq.heapify(maxHeap)

# for element in arr:
#     heapq.heappush(maxHeap, -1 * element)
# print(maxHeap)
# largest_item = heapq.heappop(maxHeap) * (-1)
# print("Largest Item", largest_item)

# # use nsmallest for maxHeap to largest N elements because we have added negative numbers
# n_largest = [-1 * element for element in heapq.nsmallest(3, maxHeap)]
# print("n Largest", n_largest)

# for implementing priority queue

#(priority, taskID)

heapQ = []
heapq.heapify(heapQ)

#add a task
task1 = [0, "Task1"]
#O(N)
heapq.heappush(heapQ, task1)

task2 = [2, "Task2"]
task3 = [1, "Task3"]
task4 = [10, "task4"]
task5 = [-1, "Task5"]
task6 = [2, "Task6"]
task7 = [5, "Task7"]

#O(logN)
heapq.heappush(heapQ, task2)
heapq.heappush(heapQ, task3)
heapq.heappush(heapQ, task4)
heapq.heappush(heapQ, task5)
heapq.heappush(heapQ, task6)
heapq.heappush(heapQ, task7)

# take task with lowest priority

#O(1) to peek top element
smallest_priority = heapQ[0]
print(smallest_priority)

print(heapQ)
# to get top K elements
print(heapq.nsmallest(4, heapQ))

smallest_priority = heapq.heappop(heapQ)
print("Poppee element", smallest_priority)
