r"""
A binary search Tree

Example
              8
             / \
            3   10
           / \    \
          1   6    14
             / \   /
            4   7 13

>>> tree = BinarySearchTree()
>>> tree.insert(8, 3, 6, 1, 10, 14, 13, 4, 7)
>>> tuple(node.value for node in tree.traversal_tree())  # inorder traversal (sorted)
(1, 3, 4, 6, 7, 8, 10, 13, 14)
>>> tuple(node.value for node in tree.traversal_tree(postorder))
(1, 4, 7, 6, 3, 13, 14, 10, 8)

>>> tuple(tree)
(1, 3, 4, 6, 7, 8, 10, 13, 14)
>>> iter_t = iter(tree)
>>> next(iter_t)
1
>>> next(iter_t)
3
>>> tuple(tree)[3-1]  # 3rd smallest element in a zero-indexed tuple
4
>>> sum(tree)
66

>>> tuple(node.value for node in tree.traversal_tree(postorder))
(1, 4, 7, 6, 3, 13, 14, 10, 8)
>>> tree.remove(20)
Traceback (most recent call last):
    ...
ValueError: Value 20 not found

Other example:

>>> values = (8, 3, 6, 1, 10, 14, 13, 4, 7)
>>> tree = BinarySearchTree()
>>> for value in values:
...     tree.insert(value)

Prints all the elements of the list in order traversal
>>> print(tree)
{'8': ({'3': (1, {'6': (4, 7)})}, {'10': (None, {'14': (13, None)})})}

Test existence
>>> 6 in tree
True
>>> -1 in tree
False

>>> tree.search(6).is_right
True
>>> tree.search(1).is_right
False

>>> max(tree)
14
>>> min(tree)
1
>>> not tree
False
>>> for value in values:
...     tree.remove(value)
>>> list(tree)
[]
>>> not tree
True
"""
from __future__ import annotations

from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    value: int
    left: Node | None = None
    right: Node | None = None
    parent: Node | None = None  # Added in order to delete a node easier

    def __iter__(self) -> Iterator[int]:
        """
        >>> list(Node(0))
        [0]
        >>> list(Node(0, Node(-1), Node(1), None))
        [-1, 0, 1]
        """
        yield from self.left or []
        yield self.value
        yield from self.right or []

    def __repr__(self) -> str:
        from pprint import pformat

        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({f"{self.value}": (self.left, self.right)}, indent=1)

    @property
    def is_right(self) -> bool:
        return bool(self.parent and self is self.parent.right)


@dataclass
class BinarySearchTree:
    root: Node | None = None

    def __bool__(self) -> bool:
        return bool(self.root)

    def __iter__(self) -> Iterator[int]:
        yield from self.root or []

    def __str__(self) -> str:
        """
        Return a string of all the Nodes using in order traversal
        """
        return str(self.root)

    def __reassign_nodes(self, node: Node, new_children: Node | None) -> None:
        if new_children is not None:  # reset its kids
            new_children.parent = node.parent
        if node.parent is not None:  # reset its parent
            if node.is_right:  # If it is the right child
                node.parent.right = new_children
            else:
                node.parent.left = new_children
        else:
            self.root = new_children

    def __insert(self, value) -> None:
        """
        Insert a new node in Binary Search Tree with value label
        """
        new_node = Node(value)  # create a new Node
        if not self:  # if Tree is empty
            self.root = new_node  # set its root
        else:  # Tree is not empty
            parent_node = self.root  # from root
            if parent_node is None:
                return
            while True:  # While we don't get to a leaf
                if value < parent_node.value:  # We go left
                    if parent_node.left is None:
                        parent_node.left = new_node  # We insert the new node in a leaf
                        break
                    else:
                        parent_node = parent_node.left
                else:
                    if parent_node.right is None:
                        parent_node.right = new_node
                        break
                    else:
                        parent_node = parent_node.right
            new_node.parent = parent_node

    def insert(self, *values) -> None:
        for value in values:
            self.__insert(value)

    def search(self, value) -> Node | None:
        if not self:
            raise IndexError("Warning: Tree is empty! please use another.")
        node = self.root
        # use lazy evaluation here to avoid NoneType Attribute error
        while node and node.value is not value:
            node = node.left if value < node.value else node.right
        return node

    def get_max(self, node: Node | None = None) -> Node | None:
        """
        We go deep on the right branch
        """
        if node is None:
            if not self.root:
                return None
            node = self.root

        if self:
            while node.right is not None:
                node = node.right
        return node

    def remove(self, value: int) -> None:
        # Look for the node with that label
        node = self.search(value)
        if not node:
            msg = f"Value {value} not found"
            raise ValueError(msg)

        if node.left is None and node.right is None:  # If it has no children
            self.__reassign_nodes(node, None)
        elif node.left is None:  # Has only right children
            self.__reassign_nodes(node, node.right)
        elif node.right is None:  # Has only left children
            self.__reassign_nodes(node, node.left)
        else:
            # Gets the max value of the left branch
            predecessor = self.get_max(node.left)
            self.remove(predecessor.value)  # type: ignore
            # Assigns the value to the node to delete and keep tree structure
            node.value = predecessor.value  # type: ignore

    @classmethod
    def preorder_traverse(cls, node: Node | None) -> Iterable:
        if node:
            yield node  # Preorder Traversal
            yield from cls.preorder_traverse(node.left)
            yield from cls.preorder_traverse(node.right)

    def inorder(self, arr: list, node: Node | None) -> None:
        """Perform an inorder traversal and append values of the nodes to
        a list named arr"""
        if node:
            self.inorder(arr, node.left)
            arr.append(node.value)
            self.inorder(arr, node.right)

    def traversal_tree(self, traversal_function=None) -> Any:
        """
        This function traversal the tree.
        You can pass a function to traversal the tree as needed by client code
        """
        return (traversal_function or inorder)(self.root)


def inorder(curr_node: Node | None) -> list[Node]:
    """
    inorder (left, self, right)
    """
    node_list = []
    if curr_node:
        node_list = inorder(curr_node.left) + [curr_node] + inorder(curr_node.right)
    return node_list


def postorder(curr_node: Node | None) -> list[Node]:
    """
    postorder (left, right, self)
    """
    node_list = []
    if curr_node:
        node_list = postorder(curr_node.left) + postorder(curr_node.right) + [curr_node]
    return node_list


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
