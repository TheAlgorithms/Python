from typing import Optional


class Node:
    """
    A Node has data variable and pointers to Nodes to its left and right.
    """
    def __init__(self, data: int) -> None:
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


def display(tree: Optional[Node]) -> None:  # In Order traversal of the tree
    """
    >>> root = Node(1)
    >>> root.left = Node(0)
    >>> root.right = Node(2)
    >>> display(root)
    0
    1
    2
    >>> display(root.right)
    2
    """
    if tree:
        display(tree.left)
        print(tree.data)
        display(tree.right)


def depth_of_tree(tree: Optional[Node]) -> int:
    """
    Recursive function that returns the depth of a binary tree.

    >>> root = Node(0)
    >>> depth_of_tree(root)
    1
    >>> root.left = Node(0)
    >>> depth_of_tree(root)
    2
    >>> root.right = Node(0)
    >>> depth_of_tree(root)
    2
    >>> root.left.right = Node(0)
    >>> depth_of_tree(root)
    3
    >>> depth_of_tree(root.left)
    2
    """
    return 1 + max(depth_of_tree(tree.left), depth_of_tree(tree.right)) if tree else 0


def is_full_binary_tree(tree: Node) -> bool:
    """
    Returns True if this is a full binary tree

    >>> root = Node(0)
    >>> is_full_binary_tree(root)
    True
    >>> root.left = Node(0)
    >>> is_full_binary_tree(root)
    False
    >>> root.right = Node(0)
    >>> is_full_binary_tree(root)
    True
    >>> root.left.left = Node(0)
    >>> is_full_binary_tree(root)
    False
    >>> root.right.right = Node(0)
    >>> is_full_binary_tree(root)
    False
    """
    if not tree:
        return True
    if tree.left and tree.right:
        return is_full_binary_tree(tree.left) and is_full_binary_tree(tree.right)
    else:
        return not tree.left and not tree.right


def main() -> None:  # Main function for testing.
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.left.right.left = Node(6)
    tree.right.left = Node(7)
    tree.right.left.left = Node(8)
    tree.right.left.left.right = Node(9)

    print(is_full_binary_tree(tree))
    print(depth_of_tree(tree))
    print("Tree is: ")
    display(tree)


if __name__ == "__main__":
    main()
