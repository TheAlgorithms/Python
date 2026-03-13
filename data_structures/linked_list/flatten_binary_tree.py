"""
Flatten a binary tree to a linked list in-place.

The algorithm modifies the given binary tree so that it becomes a right-skewed
linked list following preorder traversal order (root -> left -> right).

Time complexity: O(n)
Space complexity: O(1) (excluding recursion stack)

Doctest:
>>> # build tree: [1,2,5,3,4,None,6]
>>> root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
>>> flatten(root)
>>> to_list(root)
[1, 2, 3, 4, 5, 6]

>>> # single node
>>> root = TreeNode(0)
>>> flatten(root)
>>> to_list(root)
[0]
"""

from __future__ import annotations
from typing import Optional, List
import doctest


class TreeNode:
    """
    Node of a binary tree.

    Attributes:
        val (int): Node value.
        left (Optional[TreeNode]): Left child.
        right (Optional[TreeNode]): Right child.
    """

    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


def flatten(root: Optional[TreeNode]) -> None:
    """
    Flatten the binary tree rooted at `root` into a right-skewed linked list
    following preorder traversal. Modifies the tree in-place.

    Args:
        root (Optional[TreeNode]]): Root of the binary tree.

    Returns:
        None
    """
    current = root
    while current:
        if current.left:
            # Find rightmost node of left subtree (predecessor)
            predecessor = current.left
            while predecessor.right:
                predecessor = predecessor.right

            # Move current.right after predecessor
            predecessor.right = current.right
            # Make left subtree the new right subtree
            current.right = current.left
            current.left = None
        current = current.right


def to_list(root: Optional[TreeNode]) -> List[int]:
    """
    Helper to collect values from the flattened tree following right pointers.

    Args:
        root (Optional[TreeNode]): Root of the (flattened) tree.

    Returns:
        List[int]: Values in order along right pointers.
    """
    result: List[int] = []
    node = root
    while node:
        result.append(node.val)
        node = node.right
    return result


if __name__ == "__main__":
    # Run doctests when executed as a script.
    # This is intended for local checks only. Formal tests should go in tests/.
    failures, tests = doctest.testmod(report=False)
    if failures:
        print(f"Doctest failures: {failures} out of {tests} tests.")
    else:
        print(f"All {tests} doctests passed.")
