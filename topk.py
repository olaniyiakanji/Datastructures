"""
Title: Top K Frequent Elements
Problem:

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Example:

python

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]
"""
import heapq
from collections import Counter

def top_k_frequent(nums, k):
    # Count the frequency of each element
    count = Counter(nums)
    
    # Use a heap to find the k most frequent elements
    return heapq.nlargest(k, count.keys(), key=count.get)

# Test cases
print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))  # Output: [1, 2]
print(top_k_frequent([1], 1))  # Output: [1]
print(top_k_frequent([4, 1, -1, 2, -1, 2, 3], 2))  # Output: [-1, 2]
print(top_k_frequent([1,2,3,4,5,6,7,8,9,9,9,9], 3))  # Output: [9, 1, 2] (order may vary)
