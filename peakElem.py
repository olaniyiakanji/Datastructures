"""
Title: Find Peak Element
Problem:

A peak element is an element that is strictly greater than its neighbors. Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index of any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.

Example:

python
Copy code
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

"""
def find_peak_element(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    
    return left

# Test cases
print(find_peak_element([1, 2, 3, 1]))  # Output: 2
print(find_peak_element([1, 2, 1, 3, 5, 6, 4]))  # Output: 5
print(find_peak_element([1]))  # Output: 0 (edge case: single element)
print(find_peak_element([1, 2, 3, 4, 5]))  # Output: 4 (last element is peak)
print(find_peak_element([5, 4, 3, 2, 1]))  # Output: 0 (first element is peak)
