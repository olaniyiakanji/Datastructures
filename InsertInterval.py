"""
Title: Insert Interval
Problem:
You are given an array of non-overlapping intervals intervals where intervals[i] = [start_i, end_i] represent the start and the end of the ith interval and intervals is sorted in ascending order by start_i. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example:
python
Copy code
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]

Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]

Input: intervals = [[1,5]], newInterval = [2,3]
Output: [[1,5]]

Input: intervals = [[1,5]], newInterval = [2,7]
Output: [[1,7]]
"""
def insert(intervals, newInterval):
    merged = []
    i = 0
    n = len(intervals)
    
    # Add all intervals before newInterval
    while i < n and intervals[i][1] < newInterval[0]:
        merged.append(intervals[i])
        i += 1
    
    # Merge intervals that overlap with newInterval
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    merged.append(newInterval)
    
    # Add all intervals after newInterval
    while i < n:
        merged.append(intervals[i])
        i += 1
    
    return merged

# Test cases
print(insert([[1,3],[6,9]], [2,5]))          # Output: [[1,5],[6,9]]
print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))  # Output: [[1,2],[3,10],[12,16]]
print(insert([], [5,7]))                      # Output: [[5,7]]
print(insert([[1,5]], [2,3]))                 # Output: [[1,5]]
print(insert([[1,5]], [2,7]))                 # Output: [[1,7]]
print(insert([[1,2],[3,4],[5,6]], [0,0]))     # Output: [[0,0],[1,2],[3,4],[5,6]]
