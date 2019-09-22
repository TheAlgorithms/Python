class Node:
    def __init__(self, data):
        self.data = data


def make_set(x):
    """
    make x as a set.
    """
    # rank is the distance from x to its' parent
    # root's rank is 0
    x.rank = 0
    # p is x's parent
    x.p = x


def union_set(x, y):
    """
    union two sets.
    set with bigger rank should be parent, so that the
    disjoint set tree will be more flat.
    """
    x, y = find_set(x), find_set(y)
    if x.rank > y.rank:
        y.p = x
    else:
        x.p = y
        if x.rank == y.rank:
            y.rank += 1


def find_set(x):
    """
    return the parent of x
    """
    if x != x.p:
        x.p = find_set(x.p)
    return x.p


def test_disjoint_set():
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

    # now there are two sets: {1, 2, 3}, {4, 5, 6}
    assert find_set(vertex[0]) == find_set(vertex[1])
    assert find_set(vertex[1]) == find_set(vertex[2])
    assert find_set(vertex[0]) == find_set(vertex[2])

    assert find_set(vertex[2]) != find_set(vertex[3])

    assert find_set(vertex[3]) == find_set(vertex[4])
    assert find_set(vertex[4]) == find_set(vertex[5])
    assert find_set(vertex[3]) == find_set(vertex[5])


if __name__ == "__main__":
    test_disjoint_set()
