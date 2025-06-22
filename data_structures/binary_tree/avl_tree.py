from __future__ import annotations

import math
import random
import doctest
from typing import Any

class MyQueue:
    def __init__(self) -> None:
        self.data: list[Any] = []
        self.head = self.tail = 0

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
        self.left = self.right = None
        self.height = 1

    def get_data(self) -> Any: return self.data
    def get_left(self) -> MyNode | None: return self.left
    def get_right(self) -> MyNode | None: return self.right
    def get_height(self) -> int: return self.height
    def set_data(self, data: Any) -> None: self.data = data
    def set_left(self, node: MyNode | None) -> None: self.left = node
    def set_right(self, node: MyNode | None) -> None: self.right = node
    def set_height(self, height: int) -> None: self.height = height

def get_height(node: MyNode | None) -> int:
    return node.height if node else 0

def my_max(a: int, b: int) -> int:
    return a if a > b else b

def right_rotation(node: MyNode) -> MyNode:
    print("left rotation node:", node.data)
    ret = node.left
    node.left = ret.right
    ret.right = node
    node.height = my_max(get_height(node.right), get_height(node.left)) + 1
    ret.height = my_max(get_height(ret.right), get_height(ret.left)) + 1
    return ret
    def left_rotation(node: MyNode) -> MyNode:
    print("right rotation node:", node.data)
    ret = node.right
    node.right = ret.left
    ret.left = node
    node.height = my_max(get_height(node.right), get_height(node.left)) + 1
    ret.height = my_max(get_height(ret.right), get_height(ret.left)) + 1
    return ret

def lr_rotation(node: MyNode) -> MyNode:
    node.left = left_rotation(node.left)
    return right_rotation(node)

def rl_rotation(node: MyNode) -> MyNode:
    node.right = right_rotation(node.right)
    return left_rotation(node)

def insert_node(node: MyNode | None, data: Any) -> MyNode | None:
    if not node: return MyNode(data)

    if data < node.data:
        node.left = insert_node(node.left, data)
        if get_height(node.left) - get_height(node.right) == 2:
            node = right_rotation(node) if data < node.left.data else lr_rotation(node)
    else:
        node.right = insert_node(node.right, data)
        if get_height(node.right) - get_height(node.left) == 2:
            node = rl_rotation(node) if data < node.right.data else left_rotation(node)

    node.height = my_max(get_height(node.right), get_height(node.left)) + 1
    return node

def get_extreme(root: MyNode, is_right: bool) -> Any:
    while (child := root.right if is_right else root.left):
        root = child
    return root.data

def del_node(root: MyNode, data: Any) -> MyNode | None:
    if root.data == data:
        if root.left and root.right:
            root.data = get_extreme(root.right, False)
            root.right = del_node(root.right, root.data)
        else: return root.left or root.right
    elif root.data > data:
        if not root.left: return root
        root.left = del_node(root.left, data)
    else: root.right = del_node(root.right, data)

    if get_height(root.right) - get_height(root.left) == 2:
        root = left_rotation(root) if get_height(root.right.right) > get_height(root.right.left) else rl_rotation(root)
    elif get_height(root.right) - get_height(root.left) == -2:
        root = right_rotation(root) if get_height(root.left.left) > get_height(root.left.right) else lr_rotation(root)

    root.height = my_max(get_height(root.right), get_height(root.left)) + 1
    return root
    class AVLtree:
    def __init__(self) -> None: self.root = None
    def get_height(self) -> int: return get_height(self.root)

    def insert(self, data: Any) -> None:
        print(f"insert:{data}")
        self.root = insert_node(self.root, data)

    def del_node(self, data: Any) -> None:
        print(f"delete:{data}")
        if not self.root: return
        self.root = del_node(self.root, data)

    def __str__(self) -> str:
        if not self.root: return ""
        q, output, layer, cnt = MyQueue(), "", self.get_height(), 0
        q.push(self.root)

        while not q.is_empty():
            node = q.pop()
            space = " " * int(2**(layer-1))
            output += space + (str(node.data) if node else "*") + space
            cnt += 1

            if node:
                q.push(node.left)
                q.push(node.right)
            else:
                q.push(None)
                q.push(None)

            if any(cnt == 2**i - 1 for i in range(10)):
                layer -= 1
                output += "\n"
                if layer == 0: break

        return output + "\n" + "*"*36
        def _test() -> None: doctest.testmod()

if __name__ == "__main__":
    _test()
    t = AVLtree()
    lst = list(range(10))
    random.shuffle(lst)

    for i in lst:
        t.insert(i)
        print(t)

    random.shuffle(lst)
    for i in lst:
        t.del_node(i)
        print(t)
