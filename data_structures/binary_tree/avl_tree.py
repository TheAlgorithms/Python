from __future__ import annotations

import math
import random
from typing import Any


class MyQueue:
    def __init__(self) -> None:
        self.data: list[Any] = []
        self.head: int = 0
        self.tail: int = 0

    def is_empty(self) -> bool:
        return self.head == self.tail

    def push(self, data: Any) -> None:
        self.data.append(data)
        self.tail += 1

    def pop(self) -> Any:
        ret = self.data[self.head]
        self.head += 1
        return ret


class MyNode:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.left: MyNode | None = None
        self.right: MyNode | None = None
        self.height: int = 1

    def get_data(self) -> Any:
        return self.data

    def get_left(self) -> MyNode | None:
        return self.left

    def get_right(self) -> MyNode | None:
        return self.right

    def get_height(self) -> int:
        return self.height

    def set_left(self, node: MyNode | None) -> None:
        self.left = node

    def set_right(self, node: MyNode | None) -> None:
        self.right = node

    def set_height(self, height: int) -> None:
        self.height = height


def get_height(node: MyNode | None) -> int:
    return node.get_height() if node else 0


def my_max(a: int, b: int) -> int:
    return a if a > b else b


def right_rotation(node: MyNode) -> MyNode:
    ret = node.get_left()
    assert ret is not None
    node.set_left(ret.get_right())
    ret.set_right(node)

    node.set_height(my_max(get_height(node.get_left()), get_height(node.get_right())) + 1)
    ret.set_height(my_max(get_height(ret.get_left()), get_height(ret.get_right())) + 1)

    return ret


def left_rotation(node: MyNode) -> MyNode:
    ret = node.get_right()
    assert ret is not None
    node.set_right(ret.get_left())
    ret.set_left(node)

    node.set_height(my_max(get_height(node.get_left()), get_height(node.get_right())) + 1)
    ret.set_height(my_max(get_height(ret.get_left()), get_height(ret.get_right())) + 1)

    return ret


def lr_rotation(node: MyNode) -> MyNode:
    node.set_left(left_rotation(node.get_left()))
    return right_rotation(node)


def rl_rotation(node: MyNode) -> MyNode:
    node.set_right(right_rotation(node.get_right()))
    return left_rotation(node)


def insert_node(node: MyNode | None, data: Any) -> MyNode:
    if node is None:
        return MyNode(data)

    if data < node.get_data():
        node.set_left(insert_node(node.get_left(), data))

        if get_height(node.get_left()) - get_height(node.get_right()) == 2:
            left_child = node.get_left()
            if data < left_child.get_data():
                node = right_rotation(node)
            else:
                node = lr_rotation(node)

    else:
        node.set_right(insert_node(node.get_right(), data))

        if get_height(node.get_right()) - get_height(node.get_left()) == 2:
            right_child = node.get_right()
            if data < right_child.get_data():
                node = rl_rotation(node)
            else:
                node = left_rotation(node)

    node.set_height(my_max(get_height(node.get_left()), get_height(node.get_right())) + 1)
    return node


class AVLtree:
    def __init__(self) -> None:
        self.root: MyNode | None = None

    def insert(self, data: Any) -> None:
        self.root = insert_node(self.root, data)

    def get_height(self) -> int:
        return get_height(self.root)


# ✅ NEW FEATURE (YOUR CONTRIBUTION)

def inorder_traversal(root, result):
    """
    Performs inorder traversal of AVL tree and stores result.
    """
    if root:
        inorder_traversal(root.get_left(), result)
        result.append(root.get_data())
        inorder_traversal(root.get_right(), result)


def avl_sort(arr):
    """
    Sorts a list using AVL Tree.

    Example:
    >>> avl_sort([3,1,2])
    [1, 2, 3]
    """
    tree = AVLtree()

    for value in arr:
        tree.insert(value)

    result = []
    inorder_traversal(tree.root, result)

    return result