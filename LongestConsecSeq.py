"""
Title: Longest Consecutive Sequence
Problem:
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example:
python
Copy code
Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore, its length is 4.

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""
def longest_consecutive(nums):
    num_set = set(nums)
    longest_streak = 0
    
    for num in num_set:
        # Only start counting if `num` is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            
            longest_streak = max(longest_streak, current_streak)
    
    return longest_streak

# Test cases
print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # Output: 4
print(longest_consecutive([0,3,7,2,5,8,4,6,0,1]))   # Output: 9
print(longest_consecutive([1, 9, 3, 10, 4, 20, 2]))  # Output: 4
print(longest_consecutive([]))                      # Output: 0
print(longest_consecutive([1]))                     # Output: 1
