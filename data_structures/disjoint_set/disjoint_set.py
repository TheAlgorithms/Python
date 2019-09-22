class node:
    def __init__(self, data):
        self.data = data


def makeSet(x):
    """
    make x as a set.
    """
    # rank is the distance from x to its' parent
    # root's rank is 0
    x.rank = 0
    # p is x's parent
    x.p = x


def unionSet(x, y):
    """
    union two sets.
    set with bigger rank should be parent, so that the
    disjoint set tree will be more flat.
    """
    x, y = findSet(x), findSet(y)
    if x.rank > y.rank:
        y.p = x
    else:
        x.p = y
        if x.rank == y.rank:
            y.rank += 1


def findSet(x):
    """
    return the parent of x
    """
    if x != x.p:
        x.p = findSet(x.p)
    return x.p


def test_disjoint_set():
    vertex = [node(i) for i in range(6)]
    for v in vertex:
        makeSet(v)
    unionSet(vertex[0], vertex[1])
    unionSet(vertex[1], vertex[2])
    unionSet(vertex[3], vertex[4])
    unionSet(vertex[3], vertex[5])
    # now there are two sets: {1, 2, 3}, {4, 5, 6}
    assert findSet(vertex[0]) == findSet(vertex[1])
    assert findSet(vertex[1]) == findSet(vertex[2])
    assert findSet(vertex[2]) != findSet(vertex[3])
    assert findSet(vertex[3]) == findSet(vertex[4])
    assert findSet(vertex[4]) == findSet(vertex[5])


def main():
    test_disjoint_set()


if __name__ == "__main__":
    main()
