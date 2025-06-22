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

>>> t = BinarySearchTree().insert(8, 3, 6, 1, 10, 14, 13, 4, 7)
>>> print(" ".join(repr(i.value) for i in t.traversal_tree()))
8 3 1 6 4 7 10 14 13

>>> tuple(i.value for i in t.traversal_tree(inorder))
(1, 3, 4, 6, 7, 8, 10, 13, 14)
>>> tuple(t)
(1, 3, 4, 6, 7, 8, 10, 13, 14)
>>> t.find_kth_smallest(3, t.root)
4
>>> tuple(t)[3-1]
4

>>> print(" ".join(repr(i.value) for i in t.traversal_tree(postorder)))
1 4 7 6 3 13 14 10 8
>>> t.remove(20)
Traceback (most recent call last):
    ...
ValueError: Value 20 not found
>>> BinarySearchTree().search(6)
Traceback (most recent call last):
    ...
IndexError: Warning: Tree is empty! please use another.

Other example:

>>> testlist = (8, 3, 6, 1, 10, 14, 13, 4, 7)
>>> t = BinarySearchTree()
>>> for i in testlist:
...     t.insert(i)  # doctest: +ELLIPSIS
BinarySearchTree(root=8)
BinarySearchTree(root={'8': (3, None)})
BinarySearchTree(root={'8': ({'3': (None, 6)}, None)})
BinarySearchTree(root={'8': ({'3': (1, 6)}, None)})
BinarySearchTree(root={'8': ({'3': (1, 6)}, 10)})
BinarySearchTree(root={'8': ({'3': (1, 6)}, {'10': (None, 14)})})
BinarySearchTree(root={'8': ({'3': (1, 6)}, {'10': (None, {'14': (13, None)})})})
BinarySearchTree(root={'8': ({'3': (1, {'6': (4, None)})}, {'10': (None, {'14': ...
BinarySearchTree(root={'8': ({'3': (1, {'6': (4, 7)})}, {'10': (None, {'14': (13, ...

Prints all the elements of the list in order traversal
>>> print(t)
{'8': ({'3': (1, {'6': (4, 7)})}, {'10': (None, {'14': (13, None)})})}

Test existence
>>> t.search(6) is not None
True
>>> 6 in t
True
>>> t.search(-1) is not None
False
>>> -1 in t
False

>>> t.search(6).is_right
True
>>> t.search(1).is_right
False

>>> t.get_max().value
14
>>> max(t)
14
>>> t.get_min().value
1
>>> min(t)
1
>>> t.empty()
False
>>> not t
False
>>> for i in testlist:
...     t.remove(i)
>>> t.empty()
True
>>> not t
True
"""

from __future__ import annotations

from dataclasses import dataclass
from pprint import pformat
from typing import Iterator


@dataclass
class Node:
    value: int
    left: Node | None = None
    right: Node | None = None
    parent: Node | None = None  # For easier deletion

    @property
    def is_right(self) -> bool:
        return bool(self.parent and self is self.parent.right)

    def __iter__(self) -> Iterator[int]:
        if self.left:
            yield from self.left
        yield self.value
        if self.right:
            yield from self.right

    def __repr__(self) -> str:
        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({f"{self.value}": (self.left, self.right)}, indent=1)


@dataclass
class BinarySearchTree:
    root: Node | None = None

    def __bool__(self) -> bool:
        return self.root is not None

    def __iter__(self) -> Iterator[int]:
        if self.root:
            yield from self.root
        return iter(())

    def __str__(self) -> str:
        return str(self.root) if self.root else "Empty tree"

    def __reassign_nodes(self, node: Node, new_children: Node | None) -> None:
        if new_children is not None:
            new_children.parent = node.parent

        if node.parent is not None:
            if node.is_right:
                node.parent.right = new_children
            else:
                node.parent.left = new_children
        else:
            self.root = new_children

    def empty(self) -> bool:
        return self.root is None

    def __insert(self, value: int) -> None:
        new_node = Node(value)
        if self.empty():
            self.root = new_node
            return

        parent_node = self.root
        while parent_node:
            if value < parent_node.value:
                if parent_node.left is None:
                    parent_node.left = new_node
                    new_node.parent = parent_node
                    return
                parent_node = parent_node.left
            else:
                if parent_node.right is None:
                    parent_node.right = new_node
                    new_node.parent = parent_node
                    return
                parent_node = parent_node.right

    def insert(self, *values: int) -> BinarySearchTree:
        for value in values:
            self.__insert(value)
        return self

    def search(self, value: int) -> Node | None:
        if self.empty():
            raise IndexError("Warning: Tree is empty! please use another.")

        node = self.root
        while node is not None and node.value != value:
            if value < node.value:
                node = node.left
            else:
                node = node.right
        return node

    def get_max(self, node: Node | None = None) -> Node | None:
        if node is None:
            node = self.root
        if node is None:
            return None

        while node.right is not None:
            node = node.right
        return node

    def get_min(self, node: Node | None = None) -> Node | None:
        if node is None:
            node = self.root
        if node is None:
            return None

        while node.left is not None:
            node = node.left
        return node

    def remove(self, value: int) -> None:
        node = self.search(value)
        if node is None:
            error_msg = f"Value {value} not found"
            raise ValueError(error_msg)

        if node.left is None and node.right is None:
            self.__reassign_nodes(node, None)
        elif node.left is None:
            self.__reassign_nodes(node, node.right)
        elif node.right is None:
            self.__reassign_nodes(node, node.left)
        else:
            predecessor = self.get_max(node.left)
            if predecessor is not None:
                self.remove(predecessor.value)
                node.value = predecessor.value

    def preorder_traverse(self, node: Node | None) -> Iterator[Node]:
        if node is not None:
            yield node
            yield from self.preorder_traverse(node.left)
            yield from self.preorder_traverse(node.right)

    def traversal_tree(self, traversal_function=None) -> Iterator[Node]:
        if traversal_function is None:
            return self.preorder_traverse(self.root)
        return traversal_function(self.root)

    def inorder(self, arr: list[int], node: Node | None) -> None:
        if node:
            self.inorder(arr, node.left)
            arr.append(node.value)
            self.inorder(arr, node.right)

    def find_kth_smallest(self, k: int, node: Node) -> int:
        arr: list[int] = []
        self.inorder(arr, node)
        return arr[k - 1]


def inorder(curr_node: Node | None) -> list[Node]:
    """Inorder traversal (left, self, right)"""
    if curr_node is None:
        return []
    return [*inorder(curr_node.left), curr_node, *inorder(curr_node.right)]


def postorder(curr_node: Node | None) -> list[Node]:
    """Postorder traversal (left, right, self)"""
    if curr_node is None:
        return []
    return [*postorder(curr_node.left), *postorder(curr_node.right), curr_node]


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
