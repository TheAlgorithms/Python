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

from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from typing import Any, Self


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

    def empty(self) -> bool:
        """
        Returns True if the tree does not have any element(s).
        False if the tree has element(s).

        >>> BinarySearchTree().empty()
        True
        >>> BinarySearchTree().insert(1).empty()
        False
        >>> BinarySearchTree().insert(8, 3, 6, 1, 10, 14, 13, 4, 7).empty()
        False
        """
        return not self.root

    def __insert(self, value) -> None:
        """
        Insert a new node in Binary Search Tree with value label
        """
        new_node = Node(value)  # create a new Node
        if self.empty():  # if Tree is empty
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
                elif parent_node.right is None:
                    parent_node.right = new_node
                    break
                else:
                    parent_node = parent_node.right
            new_node.parent = parent_node

    def insert(self, *values) -> Self:
        for value in values:
            self.__insert(value)
        return self

    def search(self, value) -> Node | None:
        """
        >>> tree = BinarySearchTree().insert(10, 20, 30, 40, 50)
        >>> tree.search(10)
        {'10': (None, {'20': (None, {'30': (None, {'40': (None, 50)})})})}
        >>> tree.search(20)
        {'20': (None, {'30': (None, {'40': (None, 50)})})}
        >>> tree.search(30)
        {'30': (None, {'40': (None, 50)})}
        >>> tree.search(40)
        {'40': (None, 50)}
        >>> tree.search(50)
        50
        >>> tree.search(5) is None  # element not present
        True
        >>> tree.search(0) is None  # element not present
        True
        >>> tree.search(-5) is None  # element not present
        True
        >>> BinarySearchTree().search(10)
        Traceback (most recent call last):
            ...
        IndexError: Warning: Tree is empty! please use another.
        """

        if self.empty():
            raise IndexError("Warning: Tree is empty! please use another.")
        else:
            node = self.root
            # use lazy evaluation here to avoid NoneType Attribute error
            while node is not None and node.value is not value:
                node = node.left if value < node.value else node.right
            return node

    def get_max(self, node: Node | None = None) -> Node | None:
        """
        We go deep on the right branch

        >>> BinarySearchTree().insert(10, 20, 30, 40, 50).get_max()
        50
        >>> BinarySearchTree().insert(-5, -1, 0.1, -0.3, -4.5).get_max()
        {'0.1': (-0.3, None)}
        >>> BinarySearchTree().insert(1, 78.3, 30, 74.0, 1).get_max()
        {'78.3': ({'30': (1, 74.0)}, None)}
        >>> BinarySearchTree().insert(1, 783, 30, 740, 1).get_max()
        {'783': ({'30': (1, 740)}, None)}
        """
        if node is None:
            if self.root is None:
                return None
            node = self.root

        if not self.empty():
            while node.right is not None:
                node = node.right
        return node

    def get_min(self, node: Node | None = None) -> Node | None:
        """
        We go deep on the left branch

        >>> BinarySearchTree().insert(10, 20, 30, 40, 50).get_min()
        {'10': (None, {'20': (None, {'30': (None, {'40': (None, 50)})})})}
        >>> BinarySearchTree().insert(-5, -1, 0, -0.3, -4.5).get_min()
        {'-5': (None, {'-1': (-4.5, {'0': (-0.3, None)})})}
        >>> BinarySearchTree().insert(1, 78.3, 30, 74.0, 1).get_min()
        {'1': (None, {'78.3': ({'30': (1, 74.0)}, None)})}
        >>> BinarySearchTree().insert(1, 783, 30, 740, 1).get_min()
        {'1': (None, {'783': ({'30': (1, 740)}, None)})}
        """
        if node is None:
            node = self.root
        if self.root is None:
            return None
        if not self.empty():
            node = self.root
            while node.left is not None:
                node = node.left
        return node

    def remove(self, value: int) -> None:
        # Look for the node with that label
        node = self.search(value)
        if node is None:
            msg = f"Value {value} not found"
            raise ValueError(msg)

        if node.left is None and node.right is None:  # If it has no children
            self.__reassign_nodes(node, None)
        elif node.left is None:  # Has only right children
            self.__reassign_nodes(node, node.right)
        elif node.right is None:  # Has only left children
            self.__reassign_nodes(node, node.left)
        else:
            predecessor = self.get_max(
                node.left
            )  # Gets the max value of the left branch
            self.remove(predecessor.value)  # type: ignore[union-attr]
            node.value = (
                predecessor.value  # type: ignore[union-attr]
            )  # Assigns the value to the node to delete and keep tree structure

    def preorder_traverse(self, node: Node | None) -> Iterable:
        if node is not None:
            yield node  # Preorder Traversal
            yield from self.preorder_traverse(node.left)
            yield from self.preorder_traverse(node.right)

    def traversal_tree(self, traversal_function=None) -> Any:
        """
        This function traversal the tree.
        You can pass a function to traversal the tree as needed by client code
        """
        if traversal_function is None:
            return self.preorder_traverse(self.root)
        else:
            return traversal_function(self.root)

    def inorder(self, arr: list, node: Node | None) -> None:
        """Perform an inorder traversal and append values of the nodes to
        a list named arr"""
        if node:
            self.inorder(arr, node.left)
            arr.append(node.value)
            self.inorder(arr, node.right)

    def find_kth_smallest(self, k: int, node: Node) -> int:
        """Return the kth smallest element in a binary search tree"""
        arr: list[int] = []
        self.inorder(arr, node)  # append all values to list using inorder traversal
        return arr[k - 1]


def inorder(curr_node: Node | None) -> list[Node]:
    """
    inorder (left, self, right)
    """
    node_list = []
    if curr_node is not None:
        node_list = [*inorder(curr_node.left), curr_node, *inorder(curr_node.right)]
    return node_list


def postorder(curr_node: Node | None) -> list[Node]:
    """
    postOrder (left, right, self)
    """
    node_list = []
    if curr_node is not None:
        node_list = postorder(curr_node.left) + postorder(curr_node.right) + [curr_node]
    return node_list


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
