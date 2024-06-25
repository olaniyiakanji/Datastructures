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

Solution:

We can perform a level order traversal using a queue. We will enqueue the root node and then process each level by dequeuing nodes and enqueuing their children.
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
def create_binary_tree(arr):
    if not arr:
        return None

    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1

    while queue and i < arr.length:
        node = queue.popleft()
        
        if arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        
        if i < arr.length and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    
    return root

# Test cases
root1 = create_binary_tree([3, 9, 20, None, None, 15, 7])
print(level_order(root1))  # Output: [[3], [9, 20], [15, 7]]

root2 = create_binary_tree([1])
print(level_order(root2))  # Output: [[1]]

root3 = create_binary_tree([])
print(level_order(root3))  # Output: []
