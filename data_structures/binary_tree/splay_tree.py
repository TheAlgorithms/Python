"""
Splay tree
Reference: https://en.wikipedia.org/wiki/Splay_tree
"""
from __future__ import annotations
from typing import Any, Optional


class Node:
    """
    Implementation of tree node.
    >>> root = Node(1)
    >>> root.left = Node(2)
    >>> root.right = Node(3)
    >>> root.left.parent = root
    >>> root.right.parent = root
    >>> print(root.get_data())
    1
    >>> print(root.get_left().get_data())
    2
    >>> print(root.get_right().get_data())
    3
    >>> print(root.get_right().get_parent().get_data())
    1
    """

    def __init__(self, data: Any) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def get_data(self) -> Any:
        return self.data

    def get_left(self) -> Optional[Node]:
        return self.left

    def get_right(self) -> Optional[Node]:
        return self.right

    def get_parent(self) -> Optional[Node]:
        return self.parent


class SplayTree:
    """
    Implementation of splay tree.
    >>> tree = SplayTree()
    >>> tree.insert(30)
    >>> tree.insert(40)
    >>> tree.insert(67)
    >>> tree.insert(8)
    >>> tree.insert(70)
    >>> tree.insert(35)
    >>> tree.insert(96)
    >>> tree.print()
    [96]
    [70, '*']
    [35, '*', '*', '*']
    [8, 67, '*', '*', '*', '*', '*', '*']
    ['*', 30, 40, '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
    ----------------------------------------------------------------------------------------------------
    >>> tree.delete(35)
    >>> tree.delete(70)
    >>> tree.print()
    [67]
    [30, 96]
    [8, 40, '*', '*']
    ----------------------------------------------------------------------------------------------------
    """

    def __init__(self) -> None:
        self.root = None

    def left_rotate(self, node: Node) -> None:
        r"""
          P              x
         / \            / \
        A   x    -->   p   c
           / \        / \
          B   C      A   B
        """
        y = node.right
        if y:
            node.right = y.left
            if y.left:
                y.left.parent = node
            y.parent = node.parent
        if node.parent is None:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        if y:
            y.left = node
        node.parent = y

    def right_rotate(self, node: Node) -> None:
        r"""
            P            x
           / \          / \
          x   C   -->  A   p
         / \              / \
        A   B            B   C
        """
        y = node.left
        if y:
            node.left = y.right
            if y.right:
                y.right.parent = node
            y.parent = node.parent
        if node.parent is None:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        if y:
            y.right = node
        node.parent = y

    def splay(self, node: Node) -> None:
        while node.parent:
            if node.parent.parent:
                if (
                    node == node.parent.left and node.parent == node.parent.parent.left
                ):  # zig-zig
                    self.right_rotate(node.parent.parent)
                    self.right_rotate(node.parent)
                elif (
                    node == node.parent.right and node.parent == node.parent.parent.left
                ):  # zig-zag
                    self.left_rotate(node.parent)
                    self.right_rotate(node.parent)
                elif (
                    node == node.parent.right
                    and node.parent == node.parent.parent.right
                ):  # zag-zag
                    self.left_rotate(node.parent.parent)
                    self.left_rotate(node.parent)
                else:  # zag-zig
                    self.right_rotate(node.parent)
                    self.left_rotate(node.parent)
            else:
                if node == node.parent.left:  # zig
                    self.right_rotate(node.parent)
                else:  # zag
                    self.left_rotate(node.parent)

    def empty(self) -> bool:
        return self.root is None

    def find_min(self, node: Node) -> Node:
        while node.left:
            node = node.left
        return node

    def find_max(self, node: Node) -> Node:
        while node.right:
            node = node.right
        return node

    def join(
        self, left_tree_root: Optional[Node], right_tree_root: Optional[Node]
    ) -> Optional[Node]:
        if left_tree_root is None:
            return right_tree_root
        if right_tree_root is None:
            return left_tree_root
        x = self.find_max(left_tree_root)
        self.splay(x)
        x.right = right_tree_root
        right_tree_root.parent = x
        return x

    def find(self, data: Any) -> Optional[Node]:
        x = self.root
        while x:
            if x.data == data:
                return x
            elif data < x.data:
                x = x.left
            else:
                x = x.right
        return None

    def insert(self, data: Any) -> None:
        x = self.root
        y = None
        while x:
            y = x
            if data < x.data:
                x = x.left
            else:
                x = x.right

        node = Node(data)
        node.parent = y
        if y is None:
            self.root = node
        elif data < y.data:
            y.left = node
        else:
            y.right = node

        self.splay(node)

    def delete(self, data: Any) -> None:
        x = self.find(data)
        if x is None:
            print("data not found")
            return

        self.splay(x)
        s = None
        if x.left:
            s = x.left
            s.parent = None
            x.left = None
        t = None
        if x.right:
            t = x.right
            t.parent = None
            x.right = None
        self.root = self.join(s, t)

    def preorder(self, node: Node) -> list:
        if node is None:
            return []
        return [node.data] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node: Node) -> list:
        if node is None:
            return []
        return self.inorder(node.left) + [node.data] + self.inorder(node.right)

    def postorder(self, node: Node) -> list:
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.data]

    def print(self) -> None:
        if self.root is None:
            return
        queue = [(self.root, 1, 1)]
        d = {}
        while queue:
            node, height, idx = queue.pop(0)
            if height not in d:
                d[height] = []
            d[height].append((node.data, idx))
            if node.left:
                queue.append((node.left, height + 1, idx * 2))
            if node.right:
                queue.append((node.right, height + 1, idx * 2 + 1))
        for h in range(1, max(d.keys()) + 1):
            line = []
            k = 0
            for j in range(2 ** (h - 1), 2 ** h):
                if k < len(d[h]) and d[h][k][1] == j:
                    line.append(d[h][k][0])
                    k += 1
                else:
                    line.append("*")
            print(line)
        print("-" * 100)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
