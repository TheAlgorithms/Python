from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass


@dataclass
class Node:
    """
    A node in a binary tree.
    >>> Node(0)
    Node(data=0, left=None, right=None)
    >>> Node(0, Node(1), Node(2))  # doctest: +NORMALIZE_WHITESPACE
    Node(data=0,
         left=Node(data=1, left=None, right=None),
         right=Node(data=2, left=None, right=None))
    """

    data: int
    left: Node | None = None
    right: Node | None = None

    def __iter__(self) -> Iterator[int]:
        """
        >>> list(Node(0))
        [0]
        >>> tuple(Node(1, Node(0), Node(2)))
        (0, 1, 2)
        """
        if self.left:
            yield from self.left
        yield self.data
        if self.right:
            yield from self.right

    def __len__(self) -> int:
        """
        >>> len(Node(0))
        1
        >>> len(Node(1, Node(0), Node(2)))
        3
        """
        return sum(1 for _ in self)


def insert(temp, data):
    """
    Insert a node into a binary tree.
    >>> root = Node(1)
    >>> insert(root, 0)
    >>> tuple(root)
    (0, 1)
    >>> insert(root, 2)
    >>> tuple(root)
    (0, 1, 2)
    """
    que = [temp]
    while len(que):
        temp = que[0]
        que.pop(0)
        if not temp.left:
            if data is not None:
                temp.left = Node(data)
            else:
                temp.left = Node(0)
            break
        else:
            que.append(temp.left)
            if not temp.right:
                if data is not None:
                    temp.right = Node(data)
                else:
                    temp.right = Node(0)
                break
            else:
                que.append(temp.right)


def make_tree(elements):
    """
    Insert nodes into a binary tree.
    >>> tuple(make_tree(range(10)))
    (7, 3, 8, 1, 9, 4, 0, 5, 2, 6)
    """
    tr = Node(elements[0])
    for element in elements[1:]:
        insert(tr, element)
    return tr


def lowest_common_ancestor(root, p, q):
    """
    >>> tree = make_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    >>> lowest_common_ancestor(tree, 5, 1).data
    3
    """
    if not root:
        return None
    if root.data in (p, q):
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if right and left:
        return root
    return right or left


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    tree = make_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    print(f"{tuple(tree) = }")
    print(f"{lowest_common_ancestor(tree, 5, 1).data = }")
