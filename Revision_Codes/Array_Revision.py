import unittest

'''
#Two Sum Problem 
ex: 2,7,11,15 Target = 9 , ans = (0,1)

For each value x in arr, store INDEX in MAP. 
So if (target-x) exists in map then, we have encountered the value in the past. 
So pair would be (currentindex, map[target-x])
'''
def twoSum(nums, target) :
    mapper = {}
    
    for i in range(len(nums)):
        item = nums[i]
        if target-item in mapper:
            print("Result : ", (mapper[target-item], i))
            return [mapper[target-item], i]
        else:
            mapper[item] = i 
            

class TestTwoSum(unittest.TestCase):
    
    def test_case(self):
        arr = [2,7,11,15]
        expected = [0,1]
        target = 9
        actual = twoSum(arr,target)
        self.assertEqual(expected, actual)
    


# two_sum_object = TestTwoSum()
# two_sum_object.test_case()


'''
#Best time to buy and sell stock
ex: [7,1,5,3,6,4] ans= 5 (day 2 to day 5)
Logic : Use 2-ptr approach. Increment the sellPtr everytime against buyptr 
If the current transaction gives profit <0 --> we set buyptr=sellptr. This is because no matter what values comes after 7 in above example, 1 is always smaller,so it will always give higher profit than 7
'''
def maxProfit(prices):
    
    currentProfit = 0 
    maxProfit =0
    buyPtr = 0 
    sellPtr = 1 
    
    if len(prices) == 0:
        return 0
    
    while (sellPtr < len(prices)):
        currentProfit = prices[sellPtr] - prices[buyPtr]
        
        if currentProfit <0:
            # buptr value would never have place in max-profit against sell-ptr value, as sell-ptr value always give greater profit as it is less than buyptr 
            buyPtr = sellPtr
            sellPtr+=1
            continue
        if currentProfit > maxProfit:
            maxProfit = currentProfit
        
        sellPtr+=1
    return maxProfit
            
    
'''
Product of Array except self
ex: [1,2,3,4] ans = [24,12,8,6]
'''

def productExceptSelf(nums):
    
    if len(nums) == 0:
        return []
    
    left = [1]*len(nums)
    right = [1] * len(nums)
    
    left[0]= nums[0]
    for i in range(1, len(nums)):
        left[i] = left[i-1] * nums[i]
        
    right[-1] = nums[-1]
    for i in reversed(range(len(nums)-1)):
        right[i]=right[i+1] * nums[i]
        
    print(left)
    print(right)
    
    
    answer = []
    
    for i in range(len(nums)):
        if i ==0:
            answer.append(right[1])
        elif i==len(nums)-1:
            answer.append(left[-2])
        else:
            answer.append(left[i-1]*right[i+1])
           
    print(answer)
    return answer

# nums = [1,2,3,4]
# productExceptSelf(nums)
'''
Maximum Contigious Subarray Sum (Kadane Algorithm)
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
'''

def maxSubArray (nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    import sys

    max_sum_till_now = 0 
    global_max_sum = -sys.maxsize -1 

    for i in range(len(nums)):
        max_sum_till_now +=nums[i]

        if global_max_sum < max_sum_till_now:
            global_max_sum = max_sum_till_now

        if max_sum_till_now <0:
            max_sum_till_now =0
    return  global_max_sum


'''
Maximum Product SubArray 

ex: [2,3,-2,4] ans = 6 (2,3)


Solution by NeetCode : https://www.youtube.com/watch?v=lXVy6YWFcRM
Cases 
1. If all the numbers in the array are ALL positive --> Max Sub Array Product is 1toN
2. If all the numbers in the array are ALL negative --> Max Sub Array Product will  
    - Even numbers of negative values --> product of all
    - odd numbers of positive values --> MAX_NUM of the array 
    
3. If we have 0 value in the between , we will reset our SUMs to neutrual value of 1

For each index , keep max_product_so_far and min_product_so_far
For any new value, we would multiply it with both and calculate new max & min values. 
Min value is needed if we have negative numbers in the subarray so that min_so_far*item will give positive value
'''


def maxProduct(nums):
    
    result = max(nums) # default value will be maximum number in the array 
    
    max_so_far, min_so_far = 1,1
    
    for i in range(len(nums)):
        ele = nums[i]
        if ele ==0:
            #reset values
            max_so_far, min_so_far = 1,1
            continue
        
        #even ele can be maximum 
        '''
        consider the array of [-1,8]
        after using -1, Max=-1, Min=-1
        now eq will be max_so_far=max(-1*8,-1*8,8)
        in this ele is greatest number 
        '''
        temp_max_so_far = ele*max_so_far
        max_so_far = max(temp_max_so_far, ele*min_so_far, ele) # [-1,8]
        min_so_far = min(temp_max_so_far, ele*min_so_far,ele) # [-1,-8]
        
        result = max(result, max_so_far, min_so_far)
        
    return result
        
        
'''
Search in rotated sorted array 
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

'''
def find_element_in_sorted_rotated_array_approach_2(arr, target):
    start = 0
    end = len(arr) - 1
    mid = -1
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        if arr[0] == target:
            return 0
        return -1

    while (start <= end):
        mid = start + int((end - start) / 2)
        if arr[mid] == target:
            return mid
        # check if left side is sorted
        if arr[start] <= arr[mid]:
            # check if element in bounds of left side
            if arr[start] <= target and arr[
                    mid] > target:  # we don't need to check arr[mid] >= target as == will be handled in above case
                end = mid - 1
            else:
                start = mid + 1
        else:  # right side is sorted
            # chck if element in bounds of right side
            if arr[mid] < target and arr[end] >= target:
                start = mid + 1
            else:
                end = mid - 1
    return -1