"""
Title: Binary Tree Right Side View
Problem:

Given the root of a binary tree, imagine yourself standing on the right side of it. Return the values of the nodes you can see ordered from top to bottom.

Example:

python
Copy code
Input: [1,2,3,null,5,null,4]
Output: [1,3,4]
Explanation:
   1            <---
  / \
 2   3         <---
  \   \
   5   4       <---

Input: [1,null,3]
Output: [1,3]
Explanation:
   1            <---
    \
     3         <---

Input: []
Output: []

"""
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def right_side_view(root):
    if not root:
        return []
    
    right_view = []
    queue = deque([root])
    
    while queue:
        level_length = len(queue)
        for i in range(level_length):
            node = queue.popleft()
            if i == level_length - 1:
                right_view.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return right_view

# Test cases
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.right = TreeNode(5)
root1.right.right = TreeNode(4)
print(right_side_view(root1))  # Output: [1, 3, 4]

root2 = TreeNode(1)
root2.right = TreeNode(3)
print(right_side_view(root2))  # Output: [1, 3]

root3 = None
print(right_side_view(root3))  # Output: []
