"""
Given the root of a binary tree, check whether it is a mirror of itself
(i.e., symmetric around its center).

Leetcode reference: https://leetcode.com/problems/symmetric-tree/
"""
from __future__ import annotations

from dataclasses import dataclass

@dataclass
class Node:
    """
    A Node has data variable and pointers to Nodes to its left and right.
    """
    data: int
    left: Node | None = None
    right: Node | None = None

def make_symmetric_tree() -> Node:
        r"""
        Create a symmetric tree for testing.
        The tree looks like this:
               1
             /   \
            2     2
          / \    / \
         3   4   4  3
        """
        tree = Node(1)
        tree.left = Node(2)
        tree.right = Node(2)
        tree.left.left = Node(3)
        tree.left.right = Node(4)
        tree.right.left = Node(4)
        tree.right.right = Node(3)
        return tree

def make_asymmetric_tree() -> Node:
        r"""
        Create a asymmetric tree for testing.
        The tree looks like this:
               1
             /   \
            2     2
          / \    / \
         3   4   3  4
        """
        tree = Node(1)
        tree.left = Node(2)
        tree.right = Node(2)
        tree.left.left = Node(3)
        tree.left.right = Node(4)
        tree.right.left = Node(3)
        tree.right.right = Node(4)
        return tree

class SymmetricTree:
    def is_symmetric_tree(self, tree: Node) -> bool:
        r"""
        Test cases for is_symmetric_tree function        

        >>> SymmetricTree().is_symmetric_tree(make_symmetric_tree())
        True

        >>> SymmetricTree().is_symmetric_tree(make_asymmetric_tree())
        False
        """
        if tree is None:
            # An empty tree is considered symmetric.
            return True
        return self.is_mirror(tree.left, tree.right)

    def is_mirror(self, left: Node | None, right: Node | None) -> bool:
        """
        >>> tree1 = make_symmetric_tree()
        >>> tree1.right.right = Node(3)
        >>> SymmetricTree().is_mirror(tree1.left, tree1.right)
        True

        >>> tree2 = make_asymmetric_tree()
        >>> SymmetricTree().is_mirror(tree2.left, tree2.right)
        False
        """
        if left is None and right is None:
            # Both sides are empty, which is symmetric.
            return True
        if left is None or right is None:
            # One side is empty while the other is not, which is not symmetric.
            return False
        if left.data == right.data:
            # The values match, so check the subtree
            return self.is_mirror(left.left, right.right) and self.is_mirror(
                left.right, right.left
            )
        return False


if __name__ == "__main__":
    from doctest import testmod

    testmod()
