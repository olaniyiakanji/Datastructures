"""
Title: Next Greater Element I
Problem:

You are given two arrays nums1 and nums2 where nums1 is a subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.
Example:

python

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: 
For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
For number 1 in the first array, the next greater number for it in the second array is 3.
For number 2 in the first array, there is no next greater number in the second array, so output -1.

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation:
For number 2 in the first array, the next greater number for it in the second array is 3.
For number 4 in the first array, there is no next greater number in the second array, so output -1.
"""
def next_greater_element(nums1, nums2):
    stack = []
    next_greater = {}
    
    for num in nums2:
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)
    
    for num in stack:
        next_greater[num] = -1
    
    return [next_greater[num] for num in nums1]

# Test cases
print(next_greater_element([4,1,2], [1,3,4,2]))  # Output: [-1, 3, -1]
print(next_greater_element([2,4], [1,2,3,4]))    # Output: [3, -1]
print(next_greater_element([1], [1,2,3,4]))      # Output: [2]
print(next_greater_element([4], [4,1,2,3]))      # Output: [-1]
print(next_greater_element([3,1], [1,2,3]))      # Output: [-1, 2]
