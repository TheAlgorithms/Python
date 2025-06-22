from __future__ import annotations
from pprint import pformat
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from typing import Any, Self


@dataclass
class Node:
    value: int
    left: Node | None = None
    right: Node | None = None
    parent: Node | None = None

    def __repr__(self) -> str:
        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({f"{self.value}": (self.left, self.right)}, indent=1)


@dataclass
class BinarySearchTree:
    root: Node | None = None

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

    def __insert(self, value) -> None:
        new_node = Node(value)
        if self.empty():
            self.root = new_node
        else:
            parent_node = self.root
            while True:
                if value < parent_node.value:
                    if parent_node.left is None:
                        parent_node.left = new_node
                        break
                    else:
                        parent_node = parent_node.left
                elif parent_node.right is None:
                    parent_node.right = new_node
                    break
                else:
                    parent_node = parent_node.right
            new_node.parent = parent_node

    def search(self, value) -> Node | None:
        if self.empty():
            raise IndexError("Warning: Tree is empty! please use another.")
        node = self.root
        while node is not None and node.value != value:
            node = node.left if value < node.value else node.right
        return node

    def remove(self, value: int) -> None:
        node = self.search(value)
        if node is None:
            raise ValueError(f"Value {value} not found")

        if node.left is None and node.right is None:
            self.__reassign_nodes(node, None)
        elif node.left is None:
            self.__reassign_nodes(node, node.right)
        elif node.right is None:
            self.__reassign_nodes(node, node.left)
        else:
            predecessor = self.get_max(node.left)
            self.remove(predecessor.value)
            node.value = predecessor.value


# 修复的递归函数
def inorder(curr_node: Node | None) -> list[Node]:
    """Inorder traversal (left, self, right)"""
    if curr_node is None:
        return []
    return inorder(curr_node.left) + [curr_node] + inorder(curr_node.right)


def postorder(curr_node: Node | None) -> list[Node]:
    """Postorder traversal (left, right, self)"""
    if curr_node is None:
        return []
    return postorder(curr_node.left) + postorder(curr_node.right) + [curr_node]


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
