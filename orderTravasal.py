"""
Title: Binary Tree Level Order Traversal
Problem:

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
Example:

python

Input: root = [3,9,20,null,null,15,7]
Output: [[3], [9,20], [15,7]]

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

# Helper function to create a binary tree from a list
def insert_level_order(arr, root, i, n):
    if i < n:
        temp = TreeNode(arr[i])
        root = temp
        root.left = insert_level_order(arr, root.left, 2 * i + 1, n)
        root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
    return root

# Test cases
root1 = insert_level_order([3, 9, 20, None, None, 15, 7], None, 0, 7)
print(level_order(root1))  # Output: [[3], [9, 20], [15, 7]]

root2 = insert_level_order([1], None, 0, 1)
print(level_order(root2))  # Output: [[1]]

root3 = insert_level_order([], None, 0, 0)
print(level_order(root3))  # Output: []

root4 = insert_level_order([1, 2, 3, 4, 5, 6, 7, 8], None, 0, 8)
print(level_order(root4))  # Output: [[1], [2, 3], [4, 5, 6, 7], [8]]
