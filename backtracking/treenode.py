class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_paths(root):
    def backtrack(node, path):
        if not node:
            return

        path.append(node.value)

        if not node.left and not node.right:  # Leaf node
            print(" -> ".join(map(str, path)))

        backtrack(node.left, path)
        backtrack(node.right, path)

        path.pop()  # Backtrack to explore other paths

    if not root:
        return

    backtrack(root, [])

# Example usage
# Construct a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Find and print all paths from root to leaf nodes
print("Paths from root to leaf nodes:")
find_paths(root)
