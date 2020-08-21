# https://en.wikipedia.org/wiki/Lowest_common_ancestor
# https://en.wikipedia.org/wiki/Breadth-first_search

import queue
from typing import Dict, List, Tuple


def swap(a: int, b: int) -> Tuple[int, int]:
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


def create_sparse(max_node: int, parent: List[List[int]]) -> List[List[int]]:
    """
    creating sparse table which saves each nodes 2^i-th parent
    """
    j = 1
    while (1 << j) < max_node:
        for i in range(1, max_node + 1):
            parent[j][i] = parent[j - 1][parent[j - 1][i]]
        j += 1
    return parent


# returns lca of node u,v
def lowest_common_ancestor(
    u: int, v: int, level: List[int], parent: List[List[int]]
) -> List[List[int]]:
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
        if parent[i][u] != 0 and parent[i][u] != parent[i][v]:
            u, v = parent[i][u], parent[i][v]
    # returning longest common ancestor of u,v
    return parent[0][u]


# runs a breadth first search from root node of the tree
def breadth_first_search(
    level: List[int],
    parent: List[List[int]],
    max_node: int,
    graph: Dict[int, int],
    root=1,
) -> Tuple[List[int], List[List[int]]]:
    """
    sets every nodes direct parent
    parent of root node is set to 0
    calculates depth of each node from root node
    """
    level[root] = 0
    q = queue.Queue(maxsize=max_node)
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
    graph = {
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
