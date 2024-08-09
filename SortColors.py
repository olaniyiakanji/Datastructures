"""
itle: Sort Colors
Problem:

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example:

python
Copy code
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Input: nums = [2,0,1]
Output: [0,1,2]

Input: nums = [0]
Output: [0]

Input: nums = [1,0]
Output: [0,1]
"""

def sort_colors(nums):
    low, mid, high = 0, 0, len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1

# Test cases
nums1 = [2, 0, 2, 1, 1, 0]
sort_colors(nums1)
print(nums1)  # Output: [0, 0, 1, 1, 2, 2]

nums2 = [2, 0, 1]
sort_colors(nums2)
print(nums2)  # Output: [0, 1, 2]

nums3 = [0]
sort_colors(nums3)
print(nums3)  # Output: [0]

nums4 = [1, 0]
sort_colors(nums4)
print(nums4)  # Output: [0, 1]

nums5 = [1, 2, 0]
sort_colors(nums5)
print(nums5)  # Output: [0, 1, 2]
