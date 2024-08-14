"""
Title: Binary Tree Level Order Traversal
Problem:

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
Example:

python

Input: root = [3,9,20,None,None,15,7]
Output: [[3],[9,20],[15,7]]

Input: root = [1]
Output: [[1]]

Input: root = []
Output: []

"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result

# Helper function to build a binary tree from a list
def build_tree(values):
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root

# Test cases
root1 = build_tree([3,9,20,None,None,15,7])
print(level_order(root1))  # Output: [[3], [9, 20], [15, 7]]

root2 = build_tree([1])
print(level_order(root2))  # Output: [[1]]

root3 = build_tree([])
print(level_order(root3))  # Output: []

root4 = build_tree([1,2,3,4,5,6,7])
print(level_order(root4))  # Output: [[1], [2, 3], [4, 5, 6, 7]]
