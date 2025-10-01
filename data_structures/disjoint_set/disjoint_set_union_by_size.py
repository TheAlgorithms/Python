"""
Disjoint Set (Union by Size).
Reference: https://en.wikipedia.org/wiki/Disjoint-set_data_structure
"""

from __future__ import annotations


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.size: int
        self.parent: Node


def make_set(x: Node) -> None:
    """
    Make x as a set.

    >>> v = Node(1)
    >>> make_set(v)
    >>> v.size
    1
    >>> v.parent == v
    True
    """
    x.size = 1
    x.parent = x


def find_set(x: Node) -> Node:
    """
    Return the representative (parent) of the set containing x.

    >>> v = Node(1)
    >>> make_set(v)
    >>> find_set(v) == v
    True
    """
    if x != x.parent:
        x.parent = find_set(x.parent)  # Path compression
    return x.parent


def union_set(x: Node, y: Node) -> None:
    """
    Union of two sets by size.
    The root with the larger size becomes the parent.

    >>> v = [Node(i) for i in range(4)]
    >>> for node in v: make_set(node)
    >>> union_set(v[0], v[1])
    >>> union_set(v[2], v[3])
    >>> union_set(v[1], v[3])
    >>> find_set(v[0]) == find_set(v[2])
    True
    """
    x, y = find_set(x), find_set(y)
    if x == y:
        return

    if x.size < y.size:
        x, y = y, x
    y.parent = x
    x.size += y.size


def test_disjoint_set() -> None:
    """
    >>> test_disjoint_set()
    """
    vertex = [Node(i) for i in range(6)]
    for v in vertex:
        make_set(v)

    union_set(vertex[0], vertex[1])
    union_set(vertex[1], vertex[2])
    union_set(vertex[3], vertex[4])
    union_set(vertex[3], vertex[5])

    # After unions, sets should be {0,1,2} and {3,4,5}
    assert find_set(vertex[0]) == find_set(vertex[1])
    assert find_set(vertex[1]) == find_set(vertex[2])
    assert find_set(vertex[3]) == find_set(vertex[4])
    assert find_set(vertex[4]) == find_set(vertex[5])

    assert find_set(vertex[0]) != find_set(vertex[3])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    test_disjoint_set()
