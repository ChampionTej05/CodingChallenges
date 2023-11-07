'''
Given array of intergers and integer. Move all instances of integer in array to end of array and return array.
It should be done In-place and order of elements doesn't matter in input array a
'''


#  O(NLogN) solution
def move_element_to_end(array, toMove):
    array.sort()
    if toMove not in array:
        return array
    idx = array.index(toMove)
    count = array.count(toMove)
    ptr = idx + count

    # move all elements from [ptr..N] to [idx..idx+count]

    movedElements = 0
    while movedElements < count and idx + count < len(array):
        array[idx] = array[idx + count]
        idx += 1

    while idx < len(array):
        array[idx] = toMove
        idx += 1
    print(array)


'''
Swap elements of start and end 
Start -->Points to element equal to toMove 
End --> Points to elements not equal to toMove
'''


def move_element_to_end_optimal(array, toMove):
    if len(array) < 2:
        return array
    start = 0
    end = len(array) - 1

    while start <= end:
        if array[end] != toMove and array[start] == toMove:
            array[start], array[end] = array[end], array[start]
            start += 1
            end -= 1

        if array[end] == toMove:
            end -= 1
        if array[start] != toMove:
            start += 1
        # print(start, end, array)
        # print("----")

    print(array)


array = [2, 1, 2, 2, 2, 3, 4, 2]
move_element_to_end_optimal(array, 2)
