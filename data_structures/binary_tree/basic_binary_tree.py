from __future__ import annotations


class Node:
    """
    A Node has data variable and pointers to Nodes to its left and right.
    """

    def __init__(self, data: int) -> None:
        self.data = data
        self.left: Node | None = None
        self.right: Node | None = None


class BinaryTree:
    """
    A BinaryTree has a root node and methods for creating and manipulating binary trees.
    """

    def __init__(self, root_data: int) -> None:
        self.root = Node(root_data)

    def display(self, tree: Node | None) -> None:
        """
        In Order traversal of the tree
        >>> tree = BinaryTree(1)
        >>> tree.root.left = Node(0)
        >>> tree.root.right = Node(2)
        >>> tree.display(tree.root)
        0
        1
        2
        >>> tree.display(tree.root.right)
        2
        """
        if tree:
            self.display(tree.left)
            print(tree.data)
            self.display(tree.right)

    def depth_of_tree(self, tree: Node | None) -> int:
        """
        Recursive function that returns the depth of a binary tree.
        >>> tree = BinaryTree(0)
        >>> tree.depth_of_tree(tree.root)
        1
        >>> tree.root.left = Node(0)
        >>> tree.depth_of_tree(tree.root)
        2
        >>> tree.root.right = Node(0)
        >>> tree.depth_of_tree(tree.root)
        2
        >>> tree.root.left.right = Node(0)
        >>> tree.depth_of_tree(tree.root)
        3
        >>> tree.depth_of_tree(tree.root.left)
        2
        """
        return (
            1 + max(self.depth_of_tree(tree.left), self.depth_of_tree(tree.right))
            if tree
            else 0
        )

    def is_full_binary_tree(self, tree: Node) -> bool:
        """
        Returns True if this is a full binary tree
        >>> tree = BinaryTree(0)
        >>> tree.is_full_binary_tree(tree.root)
        True
        >>> tree.root.left = Node(0)
        >>> tree.is_full_binary_tree(tree.root)
        False
        >>> tree.root.right = Node(0)
        >>> tree.is_full_binary_tree(tree.root)
        True
        >>> tree.root.left.left = Node(0)
        >>> tree.is_full_binary_tree(tree.root)
        False
        >>> tree.root.right.right = Node(0)
        >>> tree.is_full_binary_tree(tree.root)
        False
        """
        if not tree:
            return True
        if tree.left and tree.right:
            return self.is_full_binary_tree(tree.left) and self.is_full_binary_tree(
                tree.right
            )
        else:
            return not tree.left and not tree.right


def main() -> None:
    """
    Main function for testing.
    """
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.left.right.left = Node(6)
    tree.root.right.left = Node(7)
    tree.root.right.left.left = Node(8)
    tree.root.right.left.left.right = Node(9)

    print(tree.is_full_binary_tree(tree.root))
    print(tree.depth_of_tree(tree.root))
    print("Tree is: ")
    tree.display(tree.root)


if __name__ == "__main__":
    main()
