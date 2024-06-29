"""
binary tree inversion
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

    # Recursively invert the left and right subtrees
    invert_tree(root.left)
    invert_tree(root.right)

    return root

# Helper function to print the binary tree in level order
def print_tree(root):
    if not root:
        return "Empty tree"
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            if node:
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                level.append("null")
        result.append(level)
    
    return result

# Test cases
root1 = TreeNode(4)
root1.left = TreeNode(2)
root1.right = TreeNode(7)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(3)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(9)

print("Original tree:", print_tree(root1))
inverted_root1 = invert_tree(root1)
print("Inverted tree:", print_tree(inverted_root1))

root2 = None
print("Original tree:", print_tree(root2))
inverted_root2 = invert_tree(root2)
print("Inverted tree:", print_tree(inverted_root2))
