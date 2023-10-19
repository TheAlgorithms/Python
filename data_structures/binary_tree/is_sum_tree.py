"""
Is a binary tree a sum tree where the value of every non-leaf node is equal to the sum
of the values of its left and right subtrees?
https://www.geeksforgeeks.org/check-if-a-given-binary-tree-is-sumtree
"""
from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass


@dataclass
class Node:
    data: int
    left: Node | None = None
    right: Node | None = None

    def __iter__(self) -> Iterator[int]:
        """
        >>> root = Node(2)
        >>> list(root)
        [2]
        >>> root.left = Node(1)
        >>> tuple(root)
        (1, 2)
        """
        if self.left:
            yield from self.left
        yield self.data
        if self.right:
            yield from self.right

    def __len__(self) -> int:
        """
        >>> root = Node(2)
        >>> len(root)
        1
        >>> root.left = Node(1)
        >>> len(root)
        2
        """
        return sum(1 for _ in self)

    @property
    def is_sum_node(self) -> bool:
        """
        >>> root = Node(3)
        >>> root.is_sum_node
        True
        >>> root.left = Node(1)
        >>> root.is_sum_node
        False
        >>> root.right = Node(2)
        >>> root.is_sum_node
        True
        """
        if not self.left and not self.right:
            return True  # leaf nodes are considered sum nodes
        left_sum = sum(self.left) if self.left else 0
        right_sum = sum(self.right) if self.right else 0
        return all(
            (
                self.data == left_sum + right_sum,
                self.left.is_sum_node if self.left else True,
                self.right.is_sum_node if self.right else True,
            )
        )


@dataclass
class BinaryTree:
    root: Node

    def __iter__(self) -> Iterator[int]:
        """
        >>> list(BinaryTree.build_a_tree())
        [1, 2, 7, 11, 15, 29, 35, 40]
        """
        return iter(self.root)

    def __len__(self) -> int:
        """
        >>> len(BinaryTree.build_a_tree())
        8
        """
        return len(self.root)

    def __str__(self) -> str:
        """
        Returns a string representation of the inorder traversal of the binary tree.

        >>> str(list(BinaryTree.build_a_tree()))
        '[1, 2, 7, 11, 15, 29, 35, 40]'
        """
        return str(list(self))

    @property
    def is_sum_tree(self) -> bool:
        """
        >>> BinaryTree.build_a_tree().is_sum_tree
        False
        >>> BinaryTree.build_a_sum_tree().is_sum_tree
        True
        """
        return self.root.is_sum_node

    @classmethod
    def build_a_tree(cls) -> BinaryTree:
        r"""
        Create a binary tree with the specified structure:
              11
           /     \
          2       29
         / \     /  \
        1   7  15    40
                       \
                        35
        >>> list(BinaryTree.build_a_tree())
        [1, 2, 7, 11, 15, 29, 35, 40]
        """
        tree = BinaryTree(Node(11))
        root = tree.root
        root.left = Node(2)
        root.right = Node(29)
        root.left.left = Node(1)
        root.left.right = Node(7)
        root.right.left = Node(15)
        root.right.right = Node(40)
        root.right.right.left = Node(35)
        return tree

    @classmethod
    def build_a_sum_tree(cls) -> BinaryTree:
        r"""
        Create a binary tree with the specified structure:
             26
            /  \
          10    3
         /  \    \
        4    6    3
        >>> list(BinaryTree.build_a_sum_tree())
        [4, 10, 6, 26, 3, 3]
        """
        tree = BinaryTree(Node(26))
        root = tree.root
        root.left = Node(10)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(6)
        root.right.right = Node(3)
        return tree


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    tree = BinaryTree.build_a_tree()
    print(f"{tree} has {len(tree)} nodes and {tree.is_sum_tree = }.")
    tree = BinaryTree.build_a_sum_tree()
    print(f"{tree} has {len(tree)} nodes and {tree.is_sum_tree = }.")
