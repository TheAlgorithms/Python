from random import random
from typing import Tuple


class Node:
    """
    Treap's node
    Treap is a binary tree by key and heap by priority
    """
    def __init__(self, key: int):
        self.key = key
        self.prior = random()
        self.l = None
        self.r = None


def split(root: Node, key: int) -> Tuple[Node, Node]:
    """
    We split current tree into 2 trees with key:

    Left tree contains all keys less than split key.
    Right tree contains all keys greater or equal, than split key
    """
    if root is None:  # None tree is split into 2 Nones
        return (None, None)
    if root.key >= key:
        """
        Right tree's root will be current node.
        Now we split(with the same key) current node's left son
        Left tree: left part of that split
        Right tree's left son: right part of that split
        """
        l, root.l = split(root.l, key)
        return (l, root)
    else:
        """
        Just symmetric to previous case
        """
        root.r, r = split(root.r, key)
        return (root, r)


def merge(left: Node, right: Node) -> Node:
    """
    We merge 2 trees into one.
    Note: all left tree's keys must be less than all right tree's
    """
    if (not left) or (not right):
        """
        If one node is None, return the other
        """
        return left or right
    if left.key > right.key:
        """
        Left will be root because it has more priority
        Now we need to merge left's right son and right tree
        """
        left.r = merge(left.r, right)
        return left
    else:
        """
        Symmetric as well
        """
        right.l = merge(left, right.l)
        return right


def insert(root: Node, key: int) -> Node:
    """
    Insert element

    Split current tree with a key into l, r,
    Insert new node into the middle
    Merge l, node, r into root
    """
    node = Node(key)
    l, r = split(root, key)
    root = merge(l, node)
    root = merge(root, r)
    return root


def erase(root: Node, key: int) -> Node:
    """
    Erase element

    Split all nodes with keys less into l,
    Split all nodes with keys greater into r.
    Merge l, r
    """
    l, r = split(root, key)
    _, r = split(r, key + 1)
    return merge(l, r)


def node_print(root: Node):
    """
    Just recursive print of a tree
    """
    if not root:
        return
    node_print(root.l)
    print(root.key, end=" ")
    node_print(root.r)


def interactTreap():
    """
    Commands:
    + key to add key into treap
    - key to erase all nodes with key

    After each command, program prints treap
    """
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
