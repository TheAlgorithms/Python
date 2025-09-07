# https://en.wikipedia.org/wiki/Lowest_common_ancestor
# https://en.wikipedia.org/wiki/Breadth-first_search

from __future__ import annotations

from queue import Queue


def swap(a: int, b: int) -> tuple[int, int]:
    """
    Return a tuple (b, a) when given two integers a and b
    >>> swap(2,3)
    (3, 2)
    >>> swap(3,4)
    (4, 3)
    >>> swap(67, 12)
    (12, 67)
    >>> swap(3,-4)
    (-4, 3)
    """
    a ^= b
    b ^= a
    a ^= b
    return a, b


def create_sparse(max_node: int, parent: list[list[int]]) -> list[list[int]]:
    """
    creating sparse table which saves each nodes 2^i-th parent
    >>> max_node = 6
    >>> parent = [[0, 0, 1, 1, 2, 2, 3]] + [[0] * 7 for _ in range(19)]
    >>> parent = create_sparse(max_node=max_node, parent=parent)
    >>> parent[0]
    [0, 0, 1, 1, 2, 2, 3]
    >>> parent[1]
    [0, 0, 0, 0, 1, 1, 1]
    >>> parent[2]
    [0, 0, 0, 0, 0, 0, 0]

    >>> max_node = 1
    >>> parent = [[0, 0]] + [[0] * 2 for _ in range(19)]
    >>> parent = create_sparse(max_node=max_node, parent=parent)
    >>> parent[0]
    [0, 0]
    >>> parent[1]
    [0, 0]
    """
    j = 1
    while (1 << j) < max_node:
        for i in range(1, max_node + 1):
            parent[j][i] = parent[j - 1][parent[j - 1][i]]
        j += 1
    return parent


# returns lca of node u,v
def lowest_common_ancestor(
    u: int, v: int, level: list[int], parent: list[list[int]]
) -> int:
    """
    Return the lowest common ancestor between u and v

    >>> level = [-1, 0, 1, 1, 2, 2, 2]
    >>> parent = [[0, 0, 1, 1, 2, 2, 3],[0, 0, 0, 0, 1, 1, 1]] + \
                    [[0] * 7 for _ in range(17)]
    >>> lowest_common_ancestor(u=4, v=5, level=level, parent=parent)
    2
    >>> lowest_common_ancestor(u=4, v=6, level=level, parent=parent)
    1
    >>> lowest_common_ancestor(u=2, v=3, level=level, parent=parent)
    1
    >>> lowest_common_ancestor(u=6, v=6, level=level, parent=parent)
    6
    """
    # u must be deeper in the tree than v
    if level[u] < level[v]:
        u, v = swap(u, v)
    # making depth of u same as depth of v
    for i in range(18, -1, -1):
        if level[u] - (1 << i) >= level[v]:
            u = parent[i][u]
    # at the same depth if u==v that mean lca is found
    if u == v:
        return u
    # moving both nodes upwards till lca in found
    for i in range(18, -1, -1):
        if parent[i][u] not in [0, parent[i][v]]:
            u, v = parent[i][u], parent[i][v]
    # returning longest common ancestor of u,v
    return parent[0][u]


# runs a breadth first search from root node of the tree
def breadth_first_search(
    level: list[int],
    parent: list[list[int]],
    max_node: int,
    graph: dict[int, list[int]],
    root: int = 1,
) -> tuple[list[int], list[list[int]]]:
    """
    sets every nodes direct parent
    parent of root node is set to 0
    calculates depth of each node from root node
    >>> level = [-1] * 7
    >>> parent = [[0] * 7 for _ in range(20)]
    >>> graph = {1: [2, 3], 2: [4, 5], 3: [6], 4: [], 5: [], 6: []}
    >>> level, parent = breadth_first_search(
    ...     level=level, parent=parent, max_node=6, graph=graph, root=1)
    >>> level
    [-1, 0, 1, 1, 2, 2, 2]
    >>> parent[0]
    [0, 0, 1, 1, 2, 2, 3]


    >>> level = [-1] * 2
    >>> parent = [[0] * 2 for _ in range(20)]
    >>> graph = {1: []}
    >>> level, parent = breadth_first_search(
    ...     level=level, parent=parent, max_node=1, graph=graph, root=1)
    >>> level
    [-1, 0]
    >>> parent[0]
    [0, 0]
    """
    level[root] = 0
    q: Queue[int] = Queue(maxsize=max_node)
    q.put(root)
    while q.qsize() != 0:
        u = q.get()
        for v in graph[u]:
            if level[v] == -1:
                level[v] = level[u] + 1
                q.put(v)
                parent[0][v] = u
    return level, parent


def main() -> None:
    max_node = 13
    # initializing with 0
    parent = [[0 for _ in range(max_node + 10)] for _ in range(20)]
    # initializing with -1 which means every node is unvisited
    level = [-1 for _ in range(max_node + 10)]
    graph: dict[int, list[int]] = {
        1: [2, 3, 4],
        2: [5],
        3: [6, 7],
        4: [8],
        5: [9, 10],
        6: [11],
        7: [],
        8: [12, 13],
        9: [],
        10: [],
        11: [],
        12: [],
        13: [],
    }
    level, parent = breadth_first_search(level, parent, max_node, graph, 1)
    parent = create_sparse(max_node, parent)
    print("LCA of node 1 and 3 is: ", lowest_common_ancestor(1, 3, level, parent))
    print("LCA of node 5 and 6 is: ", lowest_common_ancestor(5, 6, level, parent))
    print("LCA of node 7 and 11 is: ", lowest_common_ancestor(7, 11, level, parent))
    print("LCA of node 6 and 7 is: ", lowest_common_ancestor(6, 7, level, parent))
    print("LCA of node 4 and 12 is: ", lowest_common_ancestor(4, 12, level, parent))
    print("LCA of node 8 and 8 is: ", lowest_common_ancestor(8, 8, level, parent))


if __name__ == "__main__":
    main()
