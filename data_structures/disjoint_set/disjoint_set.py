"""
Disjoint set.
Reference: https://en.wikipedia.org/wiki/Disjoint-set_data_structure
"""


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.rank: int
        self.parent: Node


def make_set(x: Node) -> None:
    """
    Make x as a set.

    >>> node = Node(1)
    >>> make_set(node)
    >>> node.parent == node
    True
    >>> node.rank
    0
    >>> node.data
    1
    """
    # rank is the distance from x to its' parent
    # root's rank is 0
    x.rank = 0
    x.parent = x


def union_set(x: Node, y: Node) -> None:
    """
    Union of two sets.
    set with bigger rank should be parent, so that the
    disjoint set tree will be more flat.

    >>> node1 = Node(1)
    >>> node2 = Node(2)
    >>> make_set(node1)
    >>> make_set(node2)
    >>> union_set(node1, node2)
    >>> find_set(node1) == find_set(node2)
    True
    >>> # Test union of already connected nodes
    >>> node3 = Node(3)
    >>> make_set(node3)
    >>> union_set(node1, node3)
    >>> find_set(node1) == find_set(node3)
    True
    >>> find_set(node2) == find_set(node3)
    True
    """
    x, y = find_set(x), find_set(y)
    if x == y:
        return

    elif x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def find_set(x: Node) -> Node:
    """
    Return the parent of x

    >>> node = Node(1)
    >>> make_set(node)
    >>> find_set(node) == node
    True
    >>> node1 = Node(1)
    >>> node2 = Node(2)
    >>> make_set(node1)
    >>> make_set(node2)
    >>> union_set(node1, node2)
    >>> find_set(node1) == find_set(node2)
    True
    >>> # Test path compression
    >>> node3 = Node(3)
    >>> make_set(node3)
    >>> union_set(node1, node3)
    >>> find_set(node1) == find_set(node3)
    True
    """
    if x != x.parent:
        x.parent = find_set(x.parent)
    return x.parent


def find_python_set(node: Node) -> set:
    """
    Return a Python Standard Library set that contains i.

    >>> node = Node(1)
    >>> find_python_set(node)
    {0, 1, 2}
    >>> node = Node(4)
    >>> find_python_set(node)
    {3, 4, 5}
    >>> node = Node(6)
    >>> find_python_set(node)
    Traceback (most recent call last):
       ...
    ValueError: 6 is not in ({0, 1, 2}, {3, 4, 5})
    """
    sets = ({0, 1, 2}, {3, 4, 5})
    for s in sets:
        if node.data in s:
            return s
    msg = f"{node.data} is not in {sets}"
    raise ValueError(msg)


def test_disjoint_set() -> None:
    """
    Test the disjoint set operations with a comprehensive example.
    Creates two disjoint sets: {0, 1, 2} and {3, 4, 5}

    >>> test_disjoint_set()
    """
    vertex = [Node(i) for i in range(6)]
    for v in vertex:
        make_set(v)

    union_set(vertex[0], vertex[1])
    union_set(vertex[1], vertex[2])
    union_set(vertex[3], vertex[4])
    union_set(vertex[3], vertex[5])

    for node0 in vertex:
        for node1 in vertex:
            if find_python_set(node0).isdisjoint(find_python_set(node1)):
                assert find_set(node0) != find_set(node1)
            else:
                assert find_set(node0) == find_set(node1)


if __name__ == "__main__":
    test_disjoint_set()
