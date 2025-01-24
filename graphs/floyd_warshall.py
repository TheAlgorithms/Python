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


def floyd_warshall(graph, n):
    """
    Returns the shortest distance between all pairs of nodes

    >>> floyd_warshall(G1, 6)
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
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    return distance


if __name__ == "__main__":
    INF = 999999
    G1 = [
        [0, 2, INF, INF, INF, 3],
        [2, 0, 2, INF, INF, INF],
        [INF, 2, 0, 1, INF, INF],
        [INF, INF, 1, 0, 1, INF],
        [INF, INF, INF, 1, 0, 5],
        [3, INF, INF, INF, 5, 0],
    ]
    """
    Layout of G1:-
           2           2           1           1           5
    (1) <-----> (2) <-----> (3) <-----> (4) <-----> (5) <-----> (6)
    /\\                                                         /\\
    ||                                                          ||
    --------------------------------------------------------------
                              3
    """

    import doctest

    doctest.testmod()
