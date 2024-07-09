"""
Title: Find the Duplicate Number
Problem:

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive, there is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.
Example:

python

Input: nums = [1,3,4,2,2]
Output: 2

Input: nums = [3,1,3,4,2]
Output: 3


"""
def find_duplicate(nums):
    # Floyd's Tortoise and Hare (Cycle Detection)
    tortoise = nums[0]
    hare = nums[0]
    
    # Phase 1: Finding the intersection point of the two runners
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    
    # Phase 2: Finding the entrance to the cycle
    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]
    
    return hare

# Test cases
print(find_duplicate([1, 3, 4, 2, 2]))  # Output: 2
print(find_duplicate([3, 1, 3, 4, 2]))  # Output: 3
print(find_duplicate([1, 1]))           # Output: 1
print(find_duplicate([1, 2, 2]))        # Output: 2
