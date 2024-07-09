"""
Sure! Here is today's data structure and algorithm (DSA) problem:
Title: Binary Tree Inorder Traversal
Problem:

Given the root of a binary tree, return the inorder traversal of its nodes' values.
Example:

python

Input: root = [1,null,2,3]
Output: [1,3,2]

Input: root = []
Output: []

Input: root = [1]
Output: [1]
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    stack = []
    current = root
    result = []
    
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right
    
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
root1 = insert_level_order([1, None, 2, None, None, 3], None, 0, 6)
print(inorder_traversal(root1))  # Output: [1, 3, 2]

root2 = insert_level_order([], None, 0, 0)
print(inorder_traversal(root2))  # Output: []

root3 = insert_level_order([1], None, 0, 1)
print(inorder_traversal(root3))  # Output: [1]
