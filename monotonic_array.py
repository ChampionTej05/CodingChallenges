'''
Check if array is monotonic or not 
Monotonic : if elemenents from left to right are entirely non-increasing or entirely non-decreasing

non-increasing ==> Same or less 
non-decreasing ==> Same or more

'''


def is_monotonic(arr):
    if len(arr) < 2:
        return True

    trend = -1
    #  0 --down , 1 --up
    for i in range(len(arr) - 1):

        if arr[i] > arr[i + 1]:
            # set trend to down but first check if it was up or not
            if trend == 1:
                return False
            trend = 0
        elif arr[i] < arr[i + 1]:
            if trend == 0:
                return False
            trend = 1
    return True


arr = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
brr = [1, 1, 1, 22, 22, 23, 45, 41]
print(is_monotonic(brr))