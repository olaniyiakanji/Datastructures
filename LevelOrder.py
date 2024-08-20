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

# Test cases
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20, TreeNode(15), TreeNode(7))
print(level_order(root1))  # Output: [[3], [9, 20], [15, 7]]

root2 = TreeNode(1)
print(level_order(root2))  # Output: [[1]]

root3 = None
print(level_order(root3))  # Output: []

root4 = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
print(level_order(root4))  # Output: [[1], [2, 3], [4, 5]]

root5 = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
print(level_order(root5))  # Output: [[1], [2, 3], [4]]
