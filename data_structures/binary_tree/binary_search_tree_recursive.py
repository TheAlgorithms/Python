"""
This is a python3 implementation of binary search tree using recursion

To run tests:
python -m unittest binary_search_tree_recursive.py

To run an example:
python binary_search_tree_recursive.py
"""

from __future__ import annotations

import unittest
from collections.abc import Iterator

import pytest


class Node:
    def __init__(self, label: int, parent: Node | None) -> None:
        self.label = label
        self.parent = parent
        self.left: Node | None = None
        self.right: Node | None = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root: Node | None = None

    def empty(self) -> None:
        """
        Empties the tree

        >>> t = BinarySearchTree()
        >>> assert t.root is None
        >>> t.put(8)
        >>> assert t.root is not None
        """
        self.root = None

    def is_empty(self) -> bool:
        """
        Checks if the tree is empty

        >>> t = BinarySearchTree()
        >>> t.is_empty()
        True
        >>> t.put(8)
        >>> t.is_empty()
        False
        """
        return self.root is None

    def put(self, label: int) -> None:
        """
        Put a new node in the tree

        >>> t = BinarySearchTree()
        >>> t.put(8)
        >>> assert t.root.parent is None
        >>> assert t.root.label == 8

        >>> t.put(10)
        >>> assert t.root.right.parent == t.root
        >>> assert t.root.right.label == 10

        >>> t.put(3)
        >>> assert t.root.left.parent == t.root
        >>> assert t.root.left.label == 3
        """
        self.root = self._put(self.root, label)

    def _put(self, node: Node | None, label: int, parent: Node | None = None) -> Node:
        if node is None:
            node = Node(label, parent)
        else:
            if label < node.label:
                node.left = self._put(node.left, label, node)
            elif label > node.label:
                node.right = self._put(node.right, label, node)
            else:
                msg = f"Node with label {label} already exists"
                raise ValueError(msg)

        return node

    def search(self, label: int) -> Node:
        """
        Searches a node in the tree

        >>> t = BinarySearchTree()
        >>> t.put(8)
        >>> t.put(10)
        >>> node = t.search(8)
        >>> assert node.label == 8

        >>> node = t.search(3)
        Traceback (most recent call last):
            ...
        ValueError: Node with label 3 does not exist
        """
        return self._search(self.root, label)

    def _search(self, node: Node | None, label: int) -> Node:
        if node is None:
            msg = f"Node with label {label} does not exist"
            raise ValueError(msg)
        else:
            if label < node.label:
                node = self._search(node.left, label)
            elif label > node.label:
                node = self._search(node.right, label)

        return node

    def remove(self, label: int) -> None:
        """
        Removes a node in the tree

        >>> t = BinarySearchTree()
        >>> t.put(8)
        >>> t.put(10)
        >>> t.remove(8)
        >>> assert t.root.label == 10

        >>> t.remove(3)
        Traceback (most recent call last):
            ...
        ValueError: Node with label 3 does not exist
        """
        node = self.search(label)
        if node.right and node.left:
            lowest_node = self._get_lowest_node(node.right)
            lowest_node.left = node.left
            lowest_node.right = node.right
            node.left.parent = lowest_node
            if node.right:
                node.right.parent = lowest_node
            self._reassign_nodes(node, lowest_node)
        elif not node.right and node.left:
            self._reassign_nodes(node, node.left)
        elif node.right and not node.left:
            self._reassign_nodes(node, node.right)
        else:
            self._reassign_nodes(node, None)

    def _reassign_nodes(self, node: Node, new_children: Node | None) -> None:
        if new_children:
            new_children.parent = node.parent

        if node.parent:
            if node.parent.right == node:
                node.parent.right = new_children
            else:
                node.parent.left = new_children
        else:
            self.root = new_children

    def _get_lowest_node(self, node: Node) -> Node:
        if node.left:
            lowest_node = self._get_lowest_node(node.left)
        else:
            lowest_node = node
            self._reassign_nodes(node, node.right)

        return lowest_node

    def exists(self, label: int) -> bool:
        """
        Checks if a node exists in the tree

        >>> t = BinarySearchTree()
        >>> t.put(8)
        >>> t.put(10)
        >>> t.exists(8)
        True

        >>> t.exists(3)
        False
        """
        try:
            self.search(label)
            return True
        except ValueError:
            return False

    def get_max_label(self) -> int:
        """
        Gets the max label inserted in the tree

        >>> t = BinarySearchTree()
        >>> t.get_max_label()
        Traceback (most recent call last):
            ...
        ValueError: Binary search tree is empty

        >>> t.put(8)
        >>> t.put(10)
        >>> t.get_max_label()
        10
        """
        if self.root is None:
            raise ValueError("Binary search tree is empty")

        node = self.root
        while node.right is not None:
            node = node.right

        return node.label

    def get_min_label(self) -> int:
        """
        Gets the min label inserted in the tree

        >>> t = BinarySearchTree()
        >>> t.get_min_label()
        Traceback (most recent call last):
            ...
        ValueError: Binary search tree is empty

        >>> t.put(8)
        >>> t.put(10)
        >>> t.get_min_label()
        8
        """
        if self.root is None:
            raise ValueError("Binary search tree is empty")

        node = self.root
        while node.left is not None:
            node = node.left

        return node.label

    def inorder_traversal(self) -> Iterator[Node]:
        """
        Return the inorder traversal of the tree

        >>> t = BinarySearchTree()
        >>> [i.label for i in t.inorder_traversal()]
        []

        >>> t.put(8)
        >>> t.put(10)
        >>> t.put(9)
        >>> [i.label for i in t.inorder_traversal()]
        [8, 9, 10]
        """
        return self._inorder_traversal(self.root)

    def _inorder_traversal(self, node: Node | None) -> Iterator[Node]:
        if node is not None:
            yield from self._inorder_traversal(node.left)
            yield node
            yield from self._inorder_traversal(node.right)

    def preorder_traversal(self) -> Iterator[Node]:
        """
        Return the preorder traversal of the tree

        >>> t = BinarySearchTree()
        >>> [i.label for i in t.preorder_traversal()]
        []

        >>> t.put(8)
        >>> t.put(10)
        >>> t.put(9)
        >>> [i.label for i in t.preorder_traversal()]
        [8, 10, 9]
        """
        return self._preorder_traversal(self.root)

    def _preorder_traversal(self, node: Node | None) -> Iterator[Node]:
        if node is not None:
            yield node
            yield from self._preorder_traversal(node.left)
            yield from self._preorder_traversal(node.right)


class BinarySearchTreeTest(unittest.TestCase):
    @staticmethod
    def _get_binary_search_tree() -> BinarySearchTree:
        r"""
              8
             / \
            3   10
           / \    \
          1   6    14
             / \   /
            4   7 13
             \
              5
        """
        t = BinarySearchTree()
        t.put(8)
        t.put(3)
        t.put(6)
        t.put(1)
        t.put(10)
        t.put(14)
        t.put(13)
        t.put(4)
        t.put(7)
        t.put(5)

        return t

    def test_put(self) -> None:
        t = BinarySearchTree()
        assert t.is_empty()

        t.put(8)
        r"""
              8
        """
        assert t.root is not None
        assert t.root.parent is None
        assert t.root.label == 8

        t.put(10)
        r"""
              8
               \
                10
        """
        assert t.root.right is not None
        assert t.root.right.parent == t.root
        assert t.root.right.label == 10

        t.put(3)
        r"""
              8
             / \
            3   10
        """
        assert t.root.left is not None
        assert t.root.left.parent == t.root
        assert t.root.left.label == 3

        t.put(6)
        r"""
              8
             / \
            3   10
             \
              6
        """
        assert t.root.left.right is not None
        assert t.root.left.right.parent == t.root.left
        assert t.root.left.right.label == 6

        t.put(1)
        r"""
              8
             / \
            3   10
           / \
          1   6
        """
        assert t.root.left.left is not None
        assert t.root.left.left.parent == t.root.left
        assert t.root.left.left.label == 1

        with pytest.raises(ValueError):
            t.put(1)

    def test_search(self) -> None:
        t = self._get_binary_search_tree()

        node = t.search(6)
        assert node.label == 6

        node = t.search(13)
        assert node.label == 13

        with pytest.raises(ValueError):
            t.search(2)

    def test_remove(self) -> None:
        t = self._get_binary_search_tree()

        t.remove(13)
        r"""
              8
             / \
            3   10
           / \    \
          1   6    14
             / \
            4   7
             \
              5
        """
        assert t.root is not None
        assert t.root.right is not None
        assert t.root.right.right is not None
        assert t.root.right.right.right is None
        assert t.root.right.right.left is None

        t.remove(7)
        r"""
              8
             / \
            3   10
           / \    \
          1   6    14
             /
            4
             \
              5
        """
        assert t.root.left is not None
        assert t.root.left.right is not None
        assert t.root.left.right.left is not None
        assert t.root.left.right.right is None
        assert t.root.left.right.left.label == 4

        t.remove(6)
        r"""
              8
             / \
            3   10
           / \    \
          1   4    14
               \
                5
        """
        assert t.root.left.left is not None
        assert t.root.left.right.right is not None
        assert t.root.left.left.label == 1
        assert t.root.left.right.label == 4
        assert t.root.left.right.right.label == 5
        assert t.root.left.right.left is None
        assert t.root.left.left.parent == t.root.left
        assert t.root.left.right.parent == t.root.left

        t.remove(3)
        r"""
              8
             / \
            4   10
           / \    \
          1   5    14
        """
        assert t.root is not None
        assert t.root.left.label == 4
        assert t.root.left.right.label == 5
        assert t.root.left.left.label == 1
        assert t.root.left.parent == t.root
        assert t.root.left.left.parent == t.root.left
        assert t.root.left.right.parent == t.root.left

        t.remove(4)
        r"""
              8
             / \
            5   10
           /      \
          1        14
        """
        assert t.root.left is not None
        assert t.root.left.left is not None
        assert t.root.left.label == 5
        assert t.root.left.right is None
        assert t.root.left.left.label == 1
        assert t.root.left.parent == t.root
        assert t.root.left.left.parent == t.root.left

    def test_remove_2(self) -> None:
        t = self._get_binary_search_tree()

        t.remove(3)
        r"""
              8
             / \
            4   10
           / \    \
          1   6    14
             / \   /
            5   7 13
        """
        assert t.root is not None
        assert t.root.left is not None
        assert t.root.left.left is not None
        assert t.root.left.right is not None
        assert t.root.left.right.left is not None
        assert t.root.left.right.right is not None
        assert t.root.left.label == 4
        assert t.root.left.right.label == 6
        assert t.root.left.left.label == 1
        assert t.root.left.right.right.label == 7
        assert t.root.left.right.left.label == 5
        assert t.root.left.parent == t.root
        assert t.root.left.right.parent == t.root.left
        assert t.root.left.left.parent == t.root.left
        assert t.root.left.right.left.parent == t.root.left.right

    def test_empty(self) -> None:
        t = self._get_binary_search_tree()
        t.empty()
        assert t.root is None

    def test_is_empty(self) -> None:
        t = self._get_binary_search_tree()
        assert not t.is_empty()

        t.empty()
        assert t.is_empty()

    def test_exists(self) -> None:
        t = self._get_binary_search_tree()

        assert t.exists(6)
        assert not t.exists(-1)

    def test_get_max_label(self) -> None:
        t = self._get_binary_search_tree()

        assert t.get_max_label() == 14

        t.empty()
        with pytest.raises(ValueError):
            t.get_max_label()

    def test_get_min_label(self) -> None:
        t = self._get_binary_search_tree()

        assert t.get_min_label() == 1

        t.empty()
        with pytest.raises(ValueError):
            t.get_min_label()

    def test_inorder_traversal(self) -> None:
        t = self._get_binary_search_tree()

        inorder_traversal_nodes = [i.label for i in t.inorder_traversal()]
        assert inorder_traversal_nodes == [1, 3, 4, 5, 6, 7, 8, 10, 13, 14]

    def test_preorder_traversal(self) -> None:
        t = self._get_binary_search_tree()

        preorder_traversal_nodes = [i.label for i in t.preorder_traversal()]
        assert preorder_traversal_nodes == [8, 3, 1, 6, 4, 5, 7, 10, 14, 13]


def binary_search_tree_example() -> None:
    r"""
    Example
                  8
                 / \
                3   10
               / \    \
              1   6    14
                 / \   /
                4   7 13
                \
                5

    Example After Deletion
                  4
                 / \
                1   7
                     \
                      5

    """

    t = BinarySearchTree()
    t.put(8)
    t.put(3)
    t.put(6)
    t.put(1)
    t.put(10)
    t.put(14)
    t.put(13)
    t.put(4)
    t.put(7)
    t.put(5)

    print(
        """
            8
           / \\
          3   10
         / \\    \\
        1   6    14
           / \\   /
          4   7 13
           \\
            5
        """
    )

    print("Label 6 exists:", t.exists(6))
    print("Label 13 exists:", t.exists(13))
    print("Label -1 exists:", t.exists(-1))
    print("Label 12 exists:", t.exists(12))

    # Prints all the elements of the list in inorder traversal
    inorder_traversal_nodes = [i.label for i in t.inorder_traversal()]
    print("Inorder traversal:", inorder_traversal_nodes)

    # Prints all the elements of the list in preorder traversal
    preorder_traversal_nodes = [i.label for i in t.preorder_traversal()]
    print("Preorder traversal:", preorder_traversal_nodes)

    print("Max. label:", t.get_max_label())
    print("Min. label:", t.get_min_label())

    # Delete elements
    print("\nDeleting elements 13, 10, 8, 3, 6, 14")
    print(
        """
          4
         / \\
        1   7
             \\
              5
        """
    )
    t.remove(13)
    t.remove(10)
    t.remove(8)
    t.remove(3)
    t.remove(6)
    t.remove(14)

    # Prints all the elements of the list in inorder traversal after delete
    inorder_traversal_nodes = [i.label for i in t.inorder_traversal()]
    print("Inorder traversal after delete:", inorder_traversal_nodes)

    # Prints all the elements of the list in preorder traversal after delete
    preorder_traversal_nodes = [i.label for i in t.preorder_traversal()]
    print("Preorder traversal after delete:", preorder_traversal_nodes)

    print("Max. label:", t.get_max_label())
    print("Min. label:", t.get_min_label())


if __name__ == "__main__":
    binary_search_tree_example()
