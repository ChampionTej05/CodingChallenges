# https://www.algoexpert.io/questions/min-rewards
'''
All students must receive rewards

'''
'''
Approach (Might be correct but very difficult to implement)
1. Find min element index and start assigning value in left and right part 
2. For right part with arr[i] > arr[i-1]
    a. Check if there is continous DIP starting with arr[i] 
    b. Let C be the length of DIP array 
    c. value(arr[i]) = max(value(arr[i-1]) + 1, c+1)
3. For right part with arr[i] < arr[i-1] 
    a. value(arr[i]) = min ( value(arr[i-1]) -1, c )
    
4. Repeat similar steps for left part
'''
'''
Approach 2 : 
1. Find local mins and local maximums 
2. Start from local min and expand in both direction till you hit local max in both sides by incrementing values. Don't assign values to localMax during this phase as we are not sure about it's correct value yet
3. Do this for all  local mins 
4. Once done, assign values to localMaximums according to the adjacent values
'''


def findLocalMinimumsInArray(array):
    localMins = []

    for idx in range(len(array)):
        if idx == 0:
            if array[idx] < array[idx + 1]:
                localMins.append(idx)
        elif idx == len(array) - 1:
            if array[idx] < array[idx - 1]:
                localMins.append(idx)
        else:
            if array[idx] < array[idx + 1] and array[idx] < array[idx - 1]:
                localMins.append(idx)
    print("localMins: ", localMins)
    for item in localMins:
        print(array[item])
    return localMins


def findLocalMaximumsInArray(array):
    localMaxs = []

    for idx in range(len(array)):
        if idx == 0:
            if array[idx] > array[idx + 1]:
                localMaxs.append(idx)
        elif idx == len(array) - 1:
            if array[idx] > array[idx - 1]:
                localMaxs.append(idx)
        else:
            if array[idx] > array[idx + 1] and array[idx] > array[idx - 1]:
                localMaxs.append(idx)
    print("localMaxs: ", localMaxs)
    for item in localMaxs:
        print(array[item])
    return localMaxs


#  optimal O(n) space and O(n) time [ use hashmap for search to make it O(n)]
def minRewards(scores):
    if len(scores) == 1:
        return 1
    rewards = [0] * len(scores)

    localMins = findLocalMinimumsInArray(scores)
    localMaxs = findLocalMaximumsInArray(scores)

    for localMinIdx in localMins:
        print("Current local min idx and number", localMinIdx,
              scores[localMinIdx])
        rewards[localMinIdx] = 1

        leftRange = localMinIdx - 1
        rightRange = localMinIdx + 1

        while (leftRange >= 0):
            if leftRange in localMaxs:
                break
            rewards[leftRange] = rewards[leftRange + 1] + 1

            leftRange -= 1
        while (rightRange < len(scores)):
            if rightRange in localMaxs:
                break
            rewards[rightRange] = rewards[rightRange - 1] + 1

            rightRange += 1

        print("Rewards ", rewards)

    #assign values to localMaximums now
    for localMaxIdx in localMaxs:
        if localMaxIdx == 0:
            rewards[localMaxIdx] = rewards[localMaxIdx + 1] + 1
        elif localMaxIdx == len(scores) - 1:
            rewards[localMaxIdx] = rewards[localMaxIdx - 1] + 1
        else:
            rewards[localMaxIdx] = max(rewards[localMaxIdx - 1],
                                       rewards[localMaxIdx + 1]) + 1
    print("Final Result L ", rewards)
    print("Total Rewards: ", sum(rewards))
    return sum(rewards)


#above minRewards can also be written as


def minRewardsReWritten(scores):
    if len(scores) == 1:
        return 1
    rewards = [1] * len(scores)
    localMins = findLocalMinimumsInArray(scores)
    for localMinIdx in localMins:
        leftRange = localMinIdx - 1
        rightRange = localMinIdx + 1

        while leftRange >= 0 and scores[leftRange] > scores[leftRange + 1]:
            rewards[leftRange] = max(rewards[leftRange],
                                     rewards[leftRange + 1] + 1)
            leftRange -= 1

        while rightRange < len(scores) and scores[rightRange] > scores[
                rightRange - 1]:
            rewards[rightRange] = max(rewards[rightRange],
                                      rewards[rightRange - 1] + 1)
            rightRange += 1

    print(rewards)
    return sum(rewards)


'''
Here we set the values and backtrack it if there is any change needed for the values
'''


# O(n*n)
def minRewardsBruteForce(scores):
    rewards = [1] * len(scores)
    for i in range(1, len(scores)):
        print("i ", i)
        j = i - 1
        if scores[i] > scores[j]:
            rewards[i] = rewards[j] + 1
        else:
            #fix all the values left to i matching current criteria
            while (j >= 0 and scores[j] > scores[j + 1]):
                rewards[j] = max(rewards[j], rewards[j + 1] + 1)
                j -= 1
        print("rewards: ", rewards)
    print(rewards)
    return sum(rewards)


'''
We can do this more simply by doing two passes. 
In left to right pass : We find all values such that right side element is greater than left side element and increment their values 

In right to left pass: We find all values such that left side element is greater than right side element and set the value 
value = max (existinValue, valueOfRightSide+1)
'''


def minRewardsOptimal(scores):
    rewards = [1] * len(scores)

    # left pass
    for i in range(1, len(scores)):
        if scores[i] > scores[i - 1]:
            rewards[i] = rewards[i - 1] + 1
    print("left ", rewards)
    #right pass
    for i in range(len(scores) - 2, -1, -1):
        if scores[i] > scores[i + 1]:
            rewards[i] = max(rewards[i], rewards[i + 1] + 1)
    print("Right", rewards)
    return sum(rewards)


array = [2, 1, 18, 3, 0, 8, 7, 6, 5, 10, 16, 12, 11, 9]
array1 = [8, 4, 2, 1, 3, 6, 7, 9, 5]
array2 = [10, 5]
array3 = [0, 4, 2, 1, 3]
array4 = [1]
# findLocalMinimumsInArray(array)
# findLocalMaximumsInArray(array)

# minRewards(array4)
# minRewardsBruteForce(array1)
# minRewardsOptimal(array1)
minRewardsReWritten(array1)
