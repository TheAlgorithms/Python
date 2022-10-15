"""
We all know that Breadth First Search works for unweighted graphs.
However, it doesn't work for Weighted Graphs. Sometimes all we need
is a 0 or 1 weight on all edges, rather than any given number.

In such cases we can use this simple 0-1 BFS (Zero One Breadth First Search)
as it is much simpler than the usual algorithm for such kind of a problem, a dijkstra.

Requirement:
Each edge of the graph must be either ZERO or ONE

Refer this link: https://cp-algorithms.com/graph/01_bfs.html for more details
"""

import collections
import math


def zero_one_bfs(graph: dict, n: int, start: int, goal: int) -> None:
    """
    Shortest weighted path for a ZERO - ONE weighted graph

    The graph (dict) must have all keys from 0 to n - 1
    The values of each key must be a list of lists of length 2,
            the first element being the next node and
            the second elements being the weight of the edge connecting them

    This function implements the zero_one_bfs. Programmers can just add print
    statements or modify the data_types as per the applications of this.

    """

    # d[i] is the distance from the node 'start' to the node i
    d = [math.inf for i in range(n)]

    # The distance of a node from itself is ZERO
    d[start] = 0

    q: collections.deque = collections.deque([])

    q.appendleft(start)

    while len(q) != 0:
        v = q[0]
        q.popleft()
        for edge in graph[v]:
            u = edge[0]
            w = edge[1]
            if d[v] + w < d[u]:
                d[u] = d[v] + w
                if w == 1:
                    q.append(u)
                else:
                    q.appendleft(u)


def main() -> None:
    print("This function implements the zero_one_bfs.")
    print("Programmers can just add print statements or ", end="")
    print("modify the data_types as per the applications of this.")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()