# Two Number Sum 

Find the numbers in the array, which make up to TargetSum. Array will have distinct numbers. 
There will be always at max one solution possible. 

Leetcode : https://leetcode.com/problems/two-sum/description/ 
AlgoExpert: https://www.algoexpert.io/questions/two-number-sum

## Example 

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

## Solution 

### Approach 1 : Hash Table 
**Complexity**: Time `O(n)`, Space `O(n)`

We use a hash table to store each number as we iterate through the array, allowing us to check if the complement to reach the target sum has already been seen.

Let targetSum = a + b (where a, b are two numbers in the array)

- As we process a number `a`, we check if `target - a` is in our hash map.
- If it is not, we store `a` in the map with it's index : `mapper[a] = i`.
- When we encounter a number `b` such that `b = target - a`, we can look up if we have seen `a` as `a=target-b`.


```code:python
foreach i in range(len(arr))
  a = arr[i]
  b = target-a
  if b in mapper:
    return b, a
  else:
    mapper[a]=i
```

### Approach 2: Binary Search method.
**Complexity**: Time `O(nLogn)`, Space `O(1)`

This approach works by first sorting the array, and then using two pointers to find the two numbers that sum up to the target.


- We start with two pointers, one at the beginning (start) and one at the end (end) of the array.
-If arr[start] + arr[end] is less than the target, we move the start pointer up to increase the sum.
- If it's more, we move the end pointer down to decrease the sum.
- Once we find a pair that adds up to the target, we return their values.
  

```code:python
arr.sort()
start = 0 
end = len(arr) - 1
while start<end:
  currentSum = arr[start] + arr[end]
  if currentSum<target:
    start++
  elif currentSum>target:
    end--
  else:
    return arr[start], arr[end]
return []
```