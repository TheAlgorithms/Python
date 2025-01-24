"""
Author:- Sanjay Muthu <https://github.com/XenoBytesX>

The Algorithm:
    The Floyd Warshall algorithm is a All Pairs Shortest Path algorithm (APSP)
    which finds the shortest path between all the pairs of nodes.

Complexity:
    Time Complexity:- O(n^3)
    Space Complexity:- O(n^2)

Wiki page:- <https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm>
"""


def floyd_warshall(graph: list[list], num_nodes: int) -> list[list]:
    """
    Returns the shortest distance between all pairs of nodes

    >>> INF = 999999
    >>> G = []
    >>> G.append([0, 2, INF, INF, INF, 3])
    >>> G.append([2, 0, 2, INF, INF, INF])
    >>> G.append([INF, 2, 0, 1, INF, INF])
    >>> G.append([INF, INF, 1, 0, 1, INF])
    >>> G.append([INF, INF, INF, 1, 0, 5])
    >>> G.append([3, INF, INF, INF, 5, 0])
    >>> floyd_warshall(G, 6)
    [\
[0, 2, 4, 5, 6, 3], \
[2, 0, 2, 3, 4, 5], \
[4, 2, 0, 1, 2, 7], \
[5, 3, 1, 0, 1, 6], \
[6, 4, 2, 1, 0, 5], \
[3, 5, 7, 6, 5, 0]\
]
    """
    # The graph is a Adjancecy matrix (see <https://en.wikipedia.org/wiki/Adjacency_matrix>)
    distance: list[list] = graph
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    return distance


if __name__ == "__main__":
    """
    Layout of G:-
           2           2           1           1           5
    (1) <-----> (2) <-----> (3) <-----> (4) <-----> (5) <-----> (6)
    /\\                                                         /\\
    ||                                                          ||
    --------------------------------------------------------------
                              3
    """

    import doctest

    doctest.testmod()
