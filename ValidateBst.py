"""
Problem:
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example:
python
Copy code
Input: root = [2,1,3]
Output: True

Input: root = [5,1,4,null,null,3,6]
Output: False
Explanation: The root node's value is 5 but its right child's value is 4.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root):
    def helper(node, lower=float('-inf'), upper=float('inf')):
        if not node:
            return True
        
        val = node.val
        if val <= lower or val >= upper:
            return False
        
        if not helper(node.right, val, upper):
            return False
        if not helper(node.left, lower, val):
            return False
        
        return True
    
    return helper(root)

# Test cases
# Example 1:
root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)
print(is_valid_bst(root1))  # Output: True

# Example 2:
root2 = TreeNode(5)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
root2.right.left = TreeNode(3)
root2.right.right = TreeNode(6)
print(is_valid_bst(root2))  # Output: False
