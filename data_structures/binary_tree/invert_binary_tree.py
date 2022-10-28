"""
Illustrate how to invert a binary tree.
Author: Pranav Gor
https://www.geeksforgeeks.org/write-an-efficient-c-function-to-convert-a-tree-into-its-mirror-tree/
"""


class Node:
    """Defining a BinaryTree Node"""

    def __init__(self, data: int) -> None:
        self.data = data
        self.left: Node | None = None
        self.right: Node | None = None


def insert(node: Node | None, value: int) -> Node | None:
    """
    >>> root = Node(12345)
    >>> root_after_insertion = insert(root, 67890)
    >>> root.left == root_after_insertion.left
    True
    >>> root.right == root_after_insertion.right
    True
    >>> root.data == root_after_insertion.data
    True
    >>> root = insert(None,12345)
    >>> root.data
    12345
    """

    # If the tree is empty, set the new as root.
    if node is None:
        node = Node(value)
        return node

    # Since tree is not empty, we insert the new node
    # If the value of the new node < that of the current node,
    # add it to the left subtree and proceed recursively.
    if value < node.data:
        node.left = insert(node.left, value)

    # Else, if the value of the new node >= that of the current node,
    # add it to the right subtree and proceed recursively.
    else:
        node.right = insert(node.right, value)
    return node


def make_tree() -> Node | None:
    """
    # Creating a binary search tree
    >>> root = make_tree()
    >>> root.data
    5
    >>> root.left.data
    3
    >>> root.right.data
    7
    """
    root = Node(5)
    insert(root, 3)
    insert(root, 7)
    insert(root, 4)
    insert(root, 6)
    insert(root, 2)
    insert(root, 8)
    insert(root, 1)
    insert(root, 9)
    return root


def invert(root: Node | None) -> Node | None:  # if node is None, return None
    """
    >>> root = make_tree()
    >>> root = invert(root)
    >>> root.data
    5
    >>> seven = root.left
    >>> seven.data
    7
    >>> three = root.right
    >>> three.data
    3
    >>> eight = seven.left
    >>> eight.data
    8
    >>> six = seven.right
    >>> six.data
    6
    >>> four = three.left
    >>> four.data
    4
    >>> two = three.right
    >>> two.data
    2
    """

    # If current node exists, we swap the left and right child
    # and recursively invert the left and right subtree to invert the entire tree.
    if root:
        root.left, root.right = root.right, root.left
        invert(root.left)
        invert(root.right)

    return root


def main() -> None:
    # main function
    root = make_tree()
    invert(root)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
