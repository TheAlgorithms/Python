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
    """
    a ^= b
    b ^= a
    a ^= b
    return a, b


def create_sparse(max_node: int, parent: list[list[int]]) -> list[list[int]]:
    r"""
    Create a sparse table that saves each node's 2^i-th parent.

    The given ``parent`` table should have the direct parent of each node
    in row 0. This function fills in:

        parent[j][i] = parent[j - 1][parent[j - 1][i]]

    for each j where 2^j is less than max_node.

    For example, consider a small tree where:
      - Node 1 is the root (its parent is 0),
      - Nodes 2 and 3 have parent 1.

    We set up the parent table for only two levels (row 0 and row 1)
    for max_node = 3. (Note that in practice the table has many rows.)

    >>> parent0 = [0, 0, 1, 1]
    >>> parent1 = [0, 0, 0, 0]
    >>> parent = [parent0, parent1]
    >>> sparse = create_sparse(3, parent)
    >>> (sparse[1][1], sparse[1][2], sparse[1][3])
    (0, 0, 0)
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
    r"""
    Return the lowest common ancestor (LCA) of nodes u and v in a tree.

    The lists ``level`` and ``parent`` must be precomputed.

    >>> # Consider a simple tree:
    >>> #       1
    >>> #      / \\
    >>> #     2   3
    >>> # With levels: level[1]=0, level[2]=1, level[3]=1 and
    >>> # parent[0]=[0, 0, 1, 1]
    >>> level = [-1, 0, 1, 1]  # index 0 is dummy
    >>> parent = [[0, 0, 1, 1]] + [[0, 0, 0, 0] for _ in range(19)]
    >>> lowest_common_ancestor(2, 3, level, parent)
    1
    >>> lowest_common_ancestor(2, 2, level, parent)
    2
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
    r"""
    Run a breadth-first search (BFS) from the root node of the tree.

    This sets each node's direct parent (stored in parent[0]) and calculates the
    depth (level) of each node from the root.

    >>> # Consider a simple tree:
    >>> #    1
    >>> #   / \\
    >>> #  2   3
    >>> graph = {1: [2, 3], 2: [], 3: []}
    >>> level = [-1] * 4   # index 0 is unused; nodes 1 to 3.
    >>> parent = [[0] * 4 for _ in range(20)]
    >>> new_level, new_parent=breadth_first_search(level,parent,3,graph,root=1)
    >>> new_level[1:4]
    [0, 1, 1]
    >>> new_parent[0][1:4]
    [0, 1, 1]
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
    r"""
    Run a BFS to set node depths and parents in a sample tree, then create the
    sparse table and compute several lowest common ancestors.

    The sample tree used is:

                1
             /  |  \
            2   3   4
           /   / \\   \\
          5   6   7   8
         / \\   |    / \\
        9  10  11  12  13

    The expected lowest common ancestors are:
      - LCA(1, 3)  --> 1
      - LCA(5, 6)  --> 1
      - LCA(7, 11) --> 3
      - LCA(6, 7)  --> 3
      - LCA(4, 12) --> 4
      - LCA(8, 8)  --> 8

    To test main() without it printing to the console, we capture the output.

    >>> import sys
    >>> from io import StringIO
    >>> backup = sys.stdout
    >>> sys.stdout = StringIO()
    >>> main()
    >>> output = sys.stdout.getvalue()
    >>> sys.stdout = backup
    >>> 'LCA of node 1 and 3 is:  1' in output
    True
    >>> 'LCA of node 7 and 11 is:  3' in output
    True
    """
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
