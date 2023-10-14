class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)
        print(node.value, end=" ")  # You can modify this to store or process the values as needed
        in_order_traversal(node.right)

# Example usage
# Construct a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Perform in-order traversal
print("In-order traversal:")
in_order_traversal(root)
