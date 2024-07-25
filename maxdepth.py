"""
Title: Minimum Depth of Binary Tree
Problem:

Given a binary tree, find its minimum depth. The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Example:

python
Copy code
Input: root = [3,9,20,null,null,15,7]
Output: 2

Input: root = [2,null,3,null,4,null,5,null,6]
Output: from collections import deque
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def min_depth(root):
    if not root:
        return 0
    
    queue = deque([(root, 1)])
    
    while queue:
        node, depth = queue.popleft()
        if not node.left and not node.right:
            return depth
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))

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
print(min_depth(root1))  # Output: 2

root2 = insert_level_order([2, None, 3, None, 4, None, 5, None, 6], None, 0, 9)
print(min_depth(root2))  # Output: 5

root3 = insert_level_order([], None, 0, 0)
print(min_depth(root3))  # Output: 0

root4 = insert_level_order([1], None, 0, 1)
print(min_depth(root4))  # Output: 1



