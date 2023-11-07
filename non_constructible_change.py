'''
Non Constructible Change : Given array of coins, find out the MIN change you CAN NOT make out of the array. Array can contain duplicates. If no coins are given, answer is 1

This can be interpreted as minimum sum which does not exists in the array
'''
''' Approach 1 : Brute Force 
Sort the array. Start from 1 and try to find if sum exists in array or not. 
Checking if elements in the Array sums to Target can not be solved in polynomial time until is approximated. Knapsack 0/1 problem 
'''
''' Approach 2 : Optimal 
Detailed Notes written in algoexpert scratchpad 

Sort the coins array 
Let solution = {} set such that we can make change = sum(elements) out of all elements inside solutions set. In such change+1 is minium change we won't be able to make 
For any coin to be included in solution, it has satisfy condition that 
change+1 >= coinValue. If coinValue doesn't satisfy condition, that means if we include this coin in Solution set, we won't ever be able to generate change+1 value

'''


def find_non_constructible_change(coins):
    changeDone = 0
    coins.sort()
    for coin in coins:
        if changeDone + 1 >= coin:
            changeDone += coin
        else:
            return changeDone + 1
    return changeDone + 1


arr = [1, 5, 1, 1, 1, 10, 15, 20, 100]
print(find_non_constructible_change(arr))