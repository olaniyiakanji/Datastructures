"""

Title: Maximum Subarray
Problem:

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Example:

python

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Input: nums = [1]
Output: 1

Input: nums = [5,4,-1,7,8]
Output: 23

"""

def max_subarray(nums):
    max_current = max_global = nums[0]
    
    for num in nums[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
            
    return max_global

# Test cases
print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 6
print(max_subarray([1]))                             # Output: 1
print(max_subarray([5, 4, -1, 7, 8]))                # Output: 23
print(max_subarray([-1, -2, -3, -4]))                # Output: -1 (edge case: all negative numbers)
print(max_subarray([0, -3, 1, 1]))                   # Output: 2
