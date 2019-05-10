from random import random
from typing import Tuple


class Node:
    def __init__(self, key: int):
        self.key = key
        self.prior = random()
        self.l = None
        self.r = None


def split(root: Node, key: int) -> Tuple[Node, Node]:
    if root is None:
        return (None, None)
    if root.key >= key:
        l, root.l = split(root.l, key)
        return (l, root)
    else:
        root.r, r = split(root.r, key)
        return (root, r)


def merge(left: Node, right: Node) -> Node:
    if (not left) or (not right):
        return left or right
    if left.key > right.key:
        left.r = merge(left.r, right)
        return left
    else:
        right.l = merge(left, right.l)
        return right


def insert(root: Node, key: int) -> Node:
    node = Node(key)
    l, r = split(root, key)
    root = merge(l, node)
    root = merge(root, r)
    return root


def erase(root: Node, key: int) -> Node:
    l, r = split(root, key)
    _, r = split(r, key + 1)
    return merge(l, r)


def node_print(root: Node):
    if not root:
        return
    node_print(root.l)
    print(root.key, end=" ")
    node_print(root.r)


def interactTreap():
    root = None
    while True:
        cmd = input().split()
        cmd[1] = int(cmd[1])
        if cmd[0] == "+":
            root = insert(root, cmd[1])
        elif cmd[0] == "-":
            root = erase(root, cmd[1])
        else:
            print("Unknown command")
        node_print(root)


if __name__ == "__main__":
    interactTreap()
