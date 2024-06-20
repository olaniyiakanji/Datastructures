"""
Given an array containing n distinct numbers taken from the range 0 to n, find the one number that is missing from the array.
Input: [3, 0, 1]
Output: 2

Input: [9,6,4,2,3,5,7,0,1]
Output: 8

"""

def find_missing_number(nums):
    n = len(nums)
    total = n * (n + 1) // 2
    sum_of_nums = sum(nums)
    missing_number = total - sum_of_nums
    return missing_number

# Test cases
print(find_missing_number([3, 0, 1]))  # Output: 2
print(find_missing_number([9,6,4,2,3,5,7,0,1]))  # Output: 8
print(find_missing_number([0, 1, 2, 3, 4, 5, 6, 7, 8, 10]))  # Output: 9
