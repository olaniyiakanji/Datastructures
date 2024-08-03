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

"""
xplanation:

    Bitwise XOR Operation:
        XOR of a number with itself is 0 (e.g., a ^ a = 0).
        XOR of a number with 0 is the number itself (e.g., a ^ 0 = a).
        XOR is commutative and associative, so the order in which we apply it does not matter.
    Iterate Through the Array:
        XOR all the numbers together. Pairs of the same number will cancel out to 0, leaving the single number as the result.
    Result:
        The final value of result will be the number that appears only once in the array.


"""

# Test cases
print(single_number([2, 2, 1]))         # Output: 1
print(single_number([4, 1, 2, 1, 2]))   # Output: 4
print(single_number([1]))               # Output: 1
print(single_number([0, 1, 0]))         # Output: 1
print(single_number([99, 99, 100]))     # Output: 100
