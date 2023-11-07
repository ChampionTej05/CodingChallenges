'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note : that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.
'''


# this works for duplicate values in the array too 
'''
Kth largest elements in the array is nothing but Kth elements of max-heap 
So construct a max-heap with all values and remove the k-1 values from it 
'''
def findKthLargest(nums, k):
    import heapq 

    pq = []

    for i in range(len(nums)):
        heapq.heappush(pq, -1*nums[i])

    #remove k-1 elements and get the kth element
    counter = k-1
    while counter >0:
        heapq.heappop(pq)
        counter -=1
    
    return -1*pq[0]
