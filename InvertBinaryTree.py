"""
Title: Invert Binary Tree
Problem:

Given the root of a binary tree, invert the tree, and return its root.
Example:

python

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Input: root = [2,1,3]
Output: [2,3,1]

Input: root = []
Output: []

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root):
    if root is None:
        return None
    
    # Swap the left and right children
    root.left, root.right = root.right, root.left
    
    # Recur for left and right subtrees
    invert_tree(root.left)
    invert_tree(root.right)
    
    return root

# Helper function to print the tree in level order
def print_level_order(root):
    if not root:
        return []
    
    result, queue = [], [root]
    while queue:
        level = []
        next_queue = []
        for node in queue:
            if node:
                level.append(node.val)
                next_queue.append(node.left)
                next_queue.append(node.right)
            else:
                level.append(None)
        result.append(level)
        queue = next_queue
    
    # Remove trailing Nones
    while result and all(v is None for v in result[-1]):
        result.pop()
    
    return result

# Test cases
root1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
inverted_root1 = invert_tree(root1)
print(print_level_order(inverted_root1))  # Output: [[4], [7, 2], [9, 6, 3, 1]]

root2 = TreeNode(2, TreeNode(1), TreeNode(3))
inverted_root2 = invert_tree(root2)
print(print_level_order(inverted_root2))  # Output: [[2], [3, 1]]

root3 = None
inverted_root3 = invert_tree(root3)
print(print_level_order(inverted_root3))  # Output: []
