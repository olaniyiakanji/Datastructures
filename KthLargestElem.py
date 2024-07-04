"""
Title: Kth Largest Element in an Array
Problem:

Given an integer array nums and an integer k, return the kth largest element in the array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
Example:

python

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""
import heapq

def find_kth_largest(nums, k):
    # Create a min-heap with the first k elements
    heap = nums[:k]
    heapq.heapify(heap)
    
    # Iterate through the rest of the elements
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)
    
    # The top of the heap is the kth largest element
    return heap[0]

# Test cases
print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))  # Output: 5
print(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # Output: 4
print(find_kth_largest([1], 1))  # Output: 1
print(find_kth_largest([7, 6, 5, 4, 3, 2, 1], 5))  # Output: 3
print(find_kth_largest([2, 1], 2))  # Output: 1
