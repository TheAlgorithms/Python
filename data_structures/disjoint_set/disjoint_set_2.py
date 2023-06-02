n = 9

parent = list(range(n))

rank = [0] * n


def union_set(x: int, y: int) -> None:
    """
    Union of two sets.
    set with bigger rank should be parent, so that the
    disjoint set tree will be more flat.
    """
    x, y = find_set(x), find_set(y)
    if x == y:
        return

    if rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y
        if rank[x] == rank[y]:
            rank[x] += 1


def find_set(x: int) -> int:
    """
    Return the parent of x
    """
    if x != parent[x]:
        parent[x] = find_set(parent[x])
    return parent[x]


def find_python_set(node: int) -> set:
    """
    Return a Python Standard Library set that contains i.
    """
    sets = ({0, 1, 6, 7, 8}, {2, 3, 4, 5})
    for s in sets:
        if node in s:
            return s
    msg = f"{node} is not in {sets}"
    raise ValueError(msg)


def test_disjoint_set() -> None:
    """
    >>> test_disjoint_set()
    parent: [8, 8, 5, 5, 5, 5, 8, 8, 8]
    rank: [1, 1, 1, 1, 1, 0, 1, 1, 0]
    """
    # set(0, 1)
    #
    # root(1) -> 0
    for i in range(1):
        union_set(i, i + 1)

    # set(2, 3, 4, 5)
    #
    # root(5) -> 4 -> 3 -> 2
    for i in range(2, 5):
        union_set(i, i + 1)

    # set(6, 7, 8)
    #
    # root(8) -> 7 -> 6
    for i in range(6, 8):
        union_set(i, i + 1)

    # set(0, 1) | set(6, 7, 8) = set(0, 1, 6, 7, 8)
    #
    #         / 6
    # root(8) - 7
    #         \ 1 -> 0
    union_set(1, 6)

    for node0 in range(n):
        for node1 in range(n):
            if find_python_set(node0).isdisjoint(find_python_set(node1)):
                assert find_set(node0) != find_set(node1)
            else:
                assert find_set(node0) == find_set(node1)

    # compressed path
    print("parent:", parent)
    print("rank:", rank)


if __name__ == "__main__":
    test_disjoint_set()
