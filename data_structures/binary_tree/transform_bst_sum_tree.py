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
        """
        Test Case for BinaryTree's __iter__ method:

        >>> tree = BinaryTree()
        >>> root = tree.build_a_tree()
        >>> list(tree)  # Get a list of values using __iter__
        [1, 2, 7, 11, 15, 29, 35, 40]
        """
        if self.root is not None:
            yield from self._traverse_inorder(self.root)

    def __str__(self) -> str:
        """
        Returns a string representation of the inorder traversal of the binary tree.

        Example:
        >>> tree = BinaryTree()
        >>> root = tree.build_a_tree()
        >>> str(tree)
        '1 2 7 11 15 29 35 40'
        """
        return " ".join(str(data) for data in self)

    def _traverse_inorder(self, node: Node) -> int:
        """
        Test Case for BinaryTree's _traverse_inorder method:

        >>> tree = BinaryTree()
        >>> root = tree.build_a_tree()

        # Inorder traversal of the tree should yield nodes in ascending order.
        >>> list(tree._traverse_inorder(root))
        [1, 2, 7, 11, 15, 29, 35, 40]
        """
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
    """
      Test Case for binary_tree_to_sum_tree:
    >>>  tree = BinaryTree()
    >>>  root = tree.build_a_tree()
        # Transform the given binary tree into a sum tree
    >>> binary_tree_to_sum_tree(root)


    >>> root.data
    139
    >>> root.left.data
    31
    >>> root.right.data
    75
    >>> root.left.left.data
    1
    >>> root.left.right.data
    7
    >>> root.right.left.data
    15
    >>> root.right.right.data
    40
    >>> root.right.right.left.data
    35
    """
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


if __name__ == "__main__":
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
