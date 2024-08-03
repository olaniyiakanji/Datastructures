"""
Title: Single Number
Problem:

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
Example:

python

Input: nums = [2,2,1]
Output: 1

Input: nums = [4,1,2,1,2]
Output: 4

Input: nums = [1]
Output: 1

"""

def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Test cases
print(single_number([2, 2, 1]))         # Output: 1
print(single_number([4, 1, 2, 1, 2]))   # Output: 4
print(single_number([1]))               # Output: 1
print(single_number([0, 1, 0]))         # Output: 1
print(single_number([99, 99, 100]))     # Output: 100
