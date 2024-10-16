"""
Implementation of an auto-balanced binary tree!
For doctests run following command:
python3 -m doctest -v avl_tree.py
For testing run:
python avl_tree.py
"""

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
        self.tail = self.tail + 1

    def pop(self) -> Any:
        ret = self.data[self.head]
        self.head = self.head + 1
        return ret

    def count(self) -> int:
        return self.tail - self.head

    def print_queue(self) -> None:
        print(self.data)
        print("**************")
        print(self.data[self.head : self.tail])


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

    def set_data(self, data: Any) -> None:
        self.data = data

    def set_left(self, node: MyNode | None) -> None:
        self.left = node

    def set_right(self, node: MyNode | None) -> None:
        self.right = node

    def set_height(self, height: int) -> None:
        self.height = height


def get_height(node: MyNode | None) -> int:
    if node is None:
        return 0
    return node.get_height()


def my_max(a: int, b: int) -> int:
    if a > b:
        return a
    return b


def right_rotation(node: MyNode) -> MyNode:
    r"""
            A                      B
           / \                    / \
          B   C                  Bl  A
         / \       -->          /   / \
        Bl  Br                 UB Br  C
       /
     UB
    UB = unbalanced node
    """
    print("left rotation node:", node.get_data())
    ret = node.get_left()
    assert ret is not None
    node.set_left(ret.get_right())
    ret.set_right(node)
    h1 = my_max(get_height(node.get_right()), get_height(node.get_left())) + 1
    node.set_height(h1)
    h2 = my_max(get_height(ret.get_right()), get_height(ret.get_left())) + 1
    ret.set_height(h2)
    return ret


def left_rotation(node: MyNode) -> MyNode:
    """
    a mirror symmetry rotation of the left_rotation
    """
    print("right rotation node:", node.get_data())
    ret = node.get_right()
    assert ret is not None
    node.set_right(ret.get_left())
    ret.set_left(node)
    h1 = my_max(get_height(node.get_right()), get_height(node.get_left())) + 1
    node.set_height(h1)
    h2 = my_max(get_height(ret.get_right()), get_height(ret.get_left())) + 1
    ret.set_height(h2)
    return ret


def lr_rotation(node: MyNode) -> MyNode:
    r"""
            A              A                    Br
           / \            / \                  /  \
          B   C    LR    Br  C       RR       B    A
         / \       -->  /  \         -->    /     / \
        Bl  Br         B   UB              Bl    UB  C
             \        /
             UB     Bl
    RR = right_rotation   LR = left_rotation
    """
    left_child = node.get_left()
    assert left_child is not None
    node.set_left(left_rotation(left_child))
    return right_rotation(node)


def rl_rotation(node: MyNode) -> MyNode:
    right_child = node.get_right()
    assert right_child is not None
    node.set_right(right_rotation(right_child))
    return left_rotation(node)


def insert_node(node: MyNode | None, data: Any) -> MyNode | None:
    if node is None:
        return MyNode(data)
    if data == node.get_data():
        return node
    if data < node.get_data():
        node.set_left(insert_node(node.get_left(), data))
        if (
            get_height(node.get_left()) - get_height(node.get_right()) == 2
        ):  # an unbalance detected
            left_child = node.get_left()
            assert left_child is not None
            if (
                data < left_child.get_data()
            ):  # new node is the left child of the left child
                node = right_rotation(node)
            else:
                node = lr_rotation(node)
    else:
        node.set_right(insert_node(node.get_right(), data))
        if get_height(node.get_right()) - get_height(node.get_left()) == 2:
            right_child = node.get_right()
            assert right_child is not None
            if data < right_child.get_data():
                node = rl_rotation(node)
            else:
                node = left_rotation(node)
    h1 = my_max(get_height(node.get_right()), get_height(node.get_left())) + 1
    node.set_height(h1)
    return node


def get_right_most(root: MyNode) -> Any:
    while True:
        right_child = root.get_right()
        if right_child is None:
            break
        root = right_child
    return root.get_data()


def get_left_most(root: MyNode) -> Any:
    while True:
        left_child = root.get_left()
        if left_child is None:
            break
        root = left_child
    return root.get_data()


def get_balance(node: MyNode | None) -> int:
    if node is None:
        return 0
    return get_height(node.get_left()) - get_height(node.get_right())


def get_min_value_node(node: MyNode) -> MyNode:
    # Returns the node with the minimum value in the tree that is leftmost node
    # Function get_left_most is not used here because it returns the value of the node
    while True:
        left_child = node.get_left()
        if left_child is None:
            break
        node = left_child
    return node


def del_node(root: MyNode | None, data: Any) -> MyNode | None:
    if root is None:
        print(f"{data} not found in the tree")
        return None

    if root.get_data() > data:
        left_child = del_node(root.get_left(), data)
        root.set_left(left_child)
    elif root.get_data() < data:
        right_child = del_node(root.get_right(), data)
        root.set_right(right_child)
    else:
        if root.get_left() is None:
            return root.get_right()
        elif root.get_right() is None:
            return root.get_left()
        right_child = root.get_right()
        assert right_child is not None
        temp = get_min_value_node(right_child)
        root.set_data(temp.get_data())
        root.set_right(del_node(root.get_right(), temp.get_data()))

    root.set_height(
        1 + my_max(get_height(root.get_left()), get_height(root.get_right()))
    )

    balance = get_balance(root)

    if balance > 1:
        left_child = root.get_left()
        assert left_child is not None
        if get_balance(left_child) >= 0:
            return right_rotation(root)
        root.set_left(left_rotation(left_child))
        return right_rotation(root)

    if balance < -1:
        right_child = root.get_right()
        assert right_child is not None
        if get_balance(right_child) <= 0:
            return left_rotation(root)
        root.set_right(right_rotation(right_child))
        return left_rotation(root)

    return root


class AVLtree:
    """
    An AVL tree doctest
    Examples:
    >>> t = AVLtree()
    >>> t.insert(4)
    insert:4
    >>> print(str(t).replace(" \\n","\\n"))
     4
    *************************************
    >>> t.insert(2)
    insert:2
    >>> print(str(t).replace(" \\n","\\n").replace(" \\n","\\n"))
      4
     2  *
    *************************************
    >>> t.insert(3)
    insert:3
    right rotation node: 2
    left rotation node: 4
    >>> print(str(t).replace(" \\n","\\n").replace(" \\n","\\n"))
      3
     2  4
    *************************************
    >>> t.get_height()
    2
    >>> t.delete(3)
    delete:3
    >>> print(str(t).replace(" \\n","\\n").replace(" \\n","\\n"))
      4
     2  *
    *************************************
    """

    def __init__(self) -> None:
        self.root: MyNode | None = None

    def get_height(self) -> int:
        return get_height(self.root)

    def insert(self, data: Any) -> None:
        print("insert:" + str(data))
        self.root = insert_node(self.root, data)

    def delete(self, data: Any) -> None:
        print("delete:" + str(data))
        if self.root is None:
            print("Tree is empty!")
            return
        self.root = del_node(self.root, data)

    def __str__(
        self,
    ) -> str:  # a level traversale, gives a more intuitive look on the tree
        output = ""
        q = MyQueue()
        q.push(self.root)
        layer = self.get_height()
        if layer == 0:
            return output
        cnt = 0
        while not q.is_empty():
            node = q.pop()
            space = " " * int(math.pow(2, layer - 1))
            output += space
            if node is None:
                output += "*"
                q.push(None)
                q.push(None)
            else:
                output += str(node.get_data())
                q.push(node.get_left())
                q.push(node.get_right())
            output += space
            cnt = cnt + 1
            for i in range(100):
                if cnt == math.pow(2, i) - 1:
                    layer = layer - 1
                    if layer == 0:
                        output += "\n*************************************"
                        return output
                    output += "\n"
                    break
        output += "\n*************************************"
        return output


def _test() -> None:
    import doctest

    doctest.testmod()


if __name__ == "__main__":
    _test()
    t = AVLtree()
    lst = list(range(10))
    random.shuffle(lst)
    for i in lst:
        t.insert(i)
        print(str(t))
    random.shuffle(lst)
    for i in lst:
        t.delete(i)
        print(str(t))
