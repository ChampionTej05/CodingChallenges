import sys
'''
Given array of intergers between 1 to N inclusive where is N is length of array. Write a function that returns first integer that appears more than once when the array is read from left to right 

Expected optimal Complexity : O(N) in time and O(1) in space
'''

#  O(n) in time and O(N) in space
'''
Keep hashmap for values where each bucket represents [value] --> [count, previouslySeen]. Once you see any element more than once (i.e. previouslySeen=true) return the answer
'''


def firstDuplicateValueMapperApproach(array):
    mapper = {}
    for idx in range(len(array)):
        if array[idx] in mapper:
            return array[idx]
        else:
            mapper[array[idx]] = 1


# O(N) in time and O(1) in space
'''
We can use the information that all elements are in range 1..N only.

What we can do is use Indexing to check if we have revisted this index before

arr = [2, 1, 5, 2, 3, 3, 4], now corresponding indexes would ele-1 (since 1..N so we can guarantee that ele-1 is valid index pointing to some element in array)

index_arr= [1,0,4,1,2,2,3] 

 Here that all integers are positive(1..N as given) so while we traverse we would mark that element NEGATIVE. Hence moving left to right if we find any element which is pointing to marked negative element, then that means in past we have seen this getting mapped to some index which we have already visited, so that would be our answer 

if arr[abs(ele)-1] < 0: return ele 
else: arr[abs(ele)-1] *=-1

ex:  arr = [2, 1, 5, 2, 3, 3, 4], iDX = [1,0,4,1,2,2,3]

itr1 : ele =2 , arr[abs(2)-1] = arr[1] = 1 , is it negative ? No --> Mark the pointed element negative  [2, -1, 5, 2, 3, 3, 4]
itr2: ele = 1 , arr[abs(1)-1] =  arr[0] = 2 , negative ? No --> [-2,-1,5, 2, 3, 3, 4]
itr3: ele = 5 arr[5-1]=arr[4]=3, negative ? No --> [-2,-1,5,2,-3,3,4]
itr4: ele = 2 arr[2-1] = arr[1] = -1 , negative ? Yes --> That means in past duplicate value has been mapped to this index because of which we marked this negative. Hence this is first duplicate we have found
'''


def firstDuplicateValueIndexApproach(array):

    for idx in range(len(array)):
        #  abs value because this could be marked negative by some other value as pointed values
        current_value = abs(array[idx])
        if array[current_value - 1] < 0:
            return current_value
        else:
            array[current_value - 1] *= -1
    return -1


array = [19, 4, 1, 6, 2, 5, 20, 13, 8, 6, 11, 12, 12, 12, 11, 18, 7, 13, 6, 10]
# array = [2, 1, 5, 3, 3, 2, 4]
print(firstDuplicateValueIndexApproach(array))