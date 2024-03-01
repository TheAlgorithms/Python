"""
Binary Tree Flattening Algorithm

This code defines an algorithm to flatten a binary tree into a linked list
represented using the right pointers of the tree nodes. It uses in-place
flattening and demonstrates the flattening process along with a display
function to visualize the flattened linked list.
https://www.geeksforgeeks.org/flatten-a-binary-tree-into-linked-list

Author: Arunkumar A
Date: 04/09/2023
"""
from __future__ import annotations


class TreeNode:
    """
    A TreeNode has data variable and pointers to TreeNode objects
    for its left and right children.
    """

    def __init__(self, data: int) -> None:
        self.data = data
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


def build_tree() -> TreeNode:
    """
    Build and return a sample binary tree.

    Returns:
        TreeNode: The root of the binary tree.

    Examples:
        >>> root = build_tree()
        >>> root.data
        1
        >>> root.left.data
        2
        >>> root.right.data
        5
        >>> root.left.left.data
        3
        >>> root.left.right.data
        4
        >>> root.right.right.data
        6
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)
    return root


def flatten(root: TreeNode | None) -> None:
    """
    Flatten a binary tree into a linked list in-place, where the linked list is
    represented using the right pointers of the tree nodes.

    Args:
        root (TreeNode): The root of the binary tree to be flattened.

    Examples:
        >>> root = TreeNode(1)
        >>> root.left = TreeNode(2)
        >>> root.right = TreeNode(5)
        >>> root.left.left = TreeNode(3)
        >>> root.left.right = TreeNode(4)
        >>> root.right.right = TreeNode(6)
        >>> flatten(root)
        >>> root.data
        1
        >>> root.right.right is None
        False
        >>> root.right.right = TreeNode(3)
        >>> root.right.right.right is None
        True
    """
    if not root:
        return

    # Flatten the left subtree
    flatten(root.left)

    # Save the right subtree
    right_subtree = root.right

    # Make the left subtree the new right subtree
    root.right = root.left
    root.left = None

    # Find the end of the new right subtree
    current = root
    while current.right:
        current = current.right

    # Append the original right subtree to the end
    current.right = right_subtree

    # Flatten the updated right subtree
    flatten(right_subtree)


def display_linked_list(root: TreeNode | None) -> None:
    """
    Display the flattened linked list.

    Args:
        root (TreeNode | None): The root of the flattened linked list.

    Examples:
        >>> root = TreeNode(1)
        >>> root.right = TreeNode(2)
        >>> root.right.right = TreeNode(3)
        >>> display_linked_list(root)
        1 2 3
        >>> root = None
        >>> display_linked_list(root)

    """
    current = root
    while current:
        if current.right is None:
            print(current.data, end="")
            break
        print(current.data, end=" ")
        current = current.right


if __name__ == "__main__":
    print("Flattened Linked List:")
    root = build_tree()
    flatten(root)
    display_linked_list(root)
