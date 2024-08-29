"""
Title: Course Schedule
Problem:

There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1. Some courses may have prerequisites, for example, to take course 0 you have to first take course 1, which is expressed as a pair: [0, 1].

Given the total number of courses and a list of prerequisite pairs, return whether it is possible to finish all courses.

Example:

python
Copy code
Input: numCourses = 2, prerequisites = [[1,0]]
Output: True
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: False
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. 
It is from collections import defaultdict
"""
def can_finish(numCourses, prerequisites):
    graph = defaultdict(list)
    visited = [0] * numCourses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
    
    def dfs(course):
        if visited[course] == 1:  # cycle detected
            return False
        if visited[course] == 2:  # already checked, no cycle
            return True
        
        visited[course] = 1  # mark as visiting
        
        for neighbor in graph[course]:
            if not dfs(neighbor):
                return False
        
        visited[course] = 2  # mark as visited
        return True
    
    for course in range(numCourses):
        if not dfs(course):
            return False
    
    return True

# Test cases
print(can_finish(2, [[1,0]]))        # Output: True
print(can_finish(2, [[1,0],[0,1]]))  # Output: False
print(can_finish(4, [[1,0],[2,0],[3,1],[3,2]]))  # Output: True
print(can_finish(3, [[0,1],[0,2],[1,2]]))        # Output: True
print(can_finish(3, [[1,0],[0,1],[1,2]]))        # Output: False



