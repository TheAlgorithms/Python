from __future__ import annotations

class Node:
    def __init__(self, number: int) -> None:
        self.data = number
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None) -> None:
        self.root = root

    def __iter__(self) -> int:
        if self.root is not None:
            yield from self._traverse_inorder(self.root)

    def __str__(self) -> str:
        return " ".join(str(data) for data in self)

    def _traverse_inorder(self, node: Node) -> int:
        if node is not None:
            yield from self._traverse_inorder(node.left)
            yield node.data
            yield from self._traverse_inorder(node.right)

    def build_a_tree(self) -> Node:
        # Create a binary tree with the specified structure
        self.root = Node(11)
        self.root.left = Node(2)
        self.root.right = Node(29)
        self.root.left.left = Node(1)
        self.root.left.right = Node(7)
        self.root.right.left = Node(15)
        self.root.right.right = Node(40)
        self.root.right.right.left = Node(35)
        return self.root

def transform_tree_util(root: Node | None) -> None:
    if root is None:
        return

    # Recur for right subtree
    transform_tree_util(root.right)

    # Update sum
    global total
    total = total + root.data

    # Store old sum in the current node
    root.data = total - root.data

    # Recur for left subtree
    transform_tree_util(root.left)

def binary_tree_to_sum_tree(root: Node | None) -> None:
    # Call the utility function to transform the tree
    transform_tree_util(root)

if __name__ == '__main__':
    total = 0
    tree = BinaryTree()
    root = tree.build_a_tree()
    # Transform the tree
    binary_tree_to_sum_tree(root)
    print("Transformed Tree:")
    print(tree)
    
    """
    Test Cases:
    
    >>> root = Node(11)
    >>> root.left = Node(2)
    >>> root.right = Node(29)
    >>> transform_tree(root)
    >>> root.data
    60
    >>> root.left.data
    31
    >>> root.right.data
    29
    """
