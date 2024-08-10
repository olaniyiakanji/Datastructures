"""
Maximum Subarray
Problem:

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Example:

python

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum = 6.

Input: nums = [1]
Output: 1

Input: nums = [5,4,-1,7,8]
Output: 23

"""
def max_sub_array(nums):
    max_current = max_global = nums[0]
    
    for i in range(1, len(nums)):
        max_current = max(nums[i], max_current + nums[i])
        if max_current > max_global:
            max_global = max_current
            
    return max_global

# Test cases
print(max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
print(max_sub_array([1]))                      # Output: 1
print(max_sub_array([5,4,-1,7,8]))             # Output: 23
print(max_sub_array([-1, -2, -3, -4]))         # Output: -1
print(max_sub_array([8, -19, 5, -4, 20]))      # Output: 21
