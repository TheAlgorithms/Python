"""
Given the root of a binary tree, invert the tree, and return its root.

Leetcode problem reference: https://leetcode.com/problems/invert-binary-tree/
"""

from __future__ import annotations
from typing import Optional


class Node:
    """
    A Node has value variable and pointers to Nodes to its left and right.
    """

    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Node | None = None
        self.right: Node | None = None


def get_tree_inorder(tree: Optional[Node], tree_list: list = None) -> list:
    r"""
    Prints the inorder traversal of a tree

    >>> tree = Node(1)
    >>> tree.left = Node(2)
    >>> tree.right = Node(3)
    >>> tree.left.left = Node(4)
    >>> tree.left.right = Node(5)
    >>> tree.right.left = Node(6)
    >>> tree.right.right = Node(7)
    >>> get_tree_inorder(tree)
    [4, 2, 5, 1, 6, 3, 7]
    """
    if tree_list is None:
        tree_list = []

    if tree:
        get_tree_inorder(tree.left, tree_list)
        tree_list.append(tree.value)
        get_tree_inorder(tree.right, tree_list)

    return tree_list


def invert_binary_tree(root: Optional[Node]) -> None:
    r"""
    The tree looks like this
          1
         /  \
        2    3
       / \    \
      4   5    6
     / \   \
    7   8   9


    >>> tree = Node(1)
    >>> tree.left = Node(2)
    >>> tree.right = Node(3)
    >>> tree.left.left = Node(4)
    >>> tree.left.right = Node(5)
    >>> tree.right.right = Node(6)
    >>> tree.left.left.left = Node(7)
    >>> tree.left.left.right = Node(8)
    >>> tree.left.right.right = Node(9)

    >>> get_tree_inorder(tree)
    [7, 4, 8, 2, 5, 9, 1, 3, 6]
    >>> inverted_tree = invert_binary_tree(tree)
    >>> get_tree_inorder(inverted_tree)
    [6, 3, 1, 9, 5, 2, 8, 4, 7]

    The inverted tree looks like this
          1
         /  \
        3    2
       /    / \
      6    5   4
          /   / \
         9   8   7
    """

    if root != None:  # If root is not None
        temp: Node = root.left  # Save left Node in a temp variable
        # Swap the Nodes
        root.left = root.right
        root.right = temp
        # Now, invoke the function recursively for both the children
        invert_binary_tree(root.left)
        invert_binary_tree(root.right)
    # Return the Node
    return root


if __name__ == "__main__":
    import doctest

    doctest.testmod()
