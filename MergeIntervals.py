"""
Title: Merge Intervals
Problem:

Given a collection of intervals, merge all overlapping intervals.
Example:

python

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""
def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort the intervals based on the starting time
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for i in range(1, len(intervals)):
        # If the current interval overlaps with the last interval in merged, merge them
        if intervals[i][0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], intervals[i][1])
        else:
            merged.append(intervals[i])

    return merged

# Test cases
print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))  # Output: [[1,6],[8,10],[15,18]]
print(merge_intervals([[1,4],[4,5]]))                # Output: [[1,5]]
print(merge_intervals([[1,4],[2,3]]))                # Output: [[1,4]]
print(merge_intervals([[1,4],[0,2],[3,5]]))          # Output: [[0,5]]
print(merge_intervals([[1,4],[0,0]]))                # Output: [[0,0],[1,4]]
