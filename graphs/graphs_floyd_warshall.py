# floyd_warshall.py
"""
The problem is to find the shortest distance between all pairs of vertices in a
weighted directed graph that can have negative edge weights.
"""


def _print_dist(dist, v):
    print("The shortest path matrix using Floyd Warshall algorithm\n")
    for i in range(v):
        for j in range(v):
            end_char = "" if j == v - 1 else "  "
            if dist[i][j] != float("inf"):
                print(int(dist[i][j]), end=end_char)
            else:
                print("INF", end=end_char)
        print()


def floyd_warshall(graph, v):
    """
    :param graph: 2D array calculated from weight[edge[i, j]]
    :type graph: List[List[float]]
    :param v: number of vertices
    :type v: int
    :return: shortest distance between all vertex pairs
    distance[u][v] will contain the shortest distance from vertex u to v.

    1. For all edges from v to n, distance[i][j] = weight(edge(i, j)).
    3. The algorithm then performs distance[i][j] = min(distance[i][j], distance[i][k] +
        distance[k][j]) for each possible pair i, j of vertices.
    4. The above is repeated for each vertex k in the graph.
    5. Whenever distance[i][j] is given a new minimum value, next vertex[i][j] is
        updated to the next vertex[i][k].


    >>> graph = [
    ...     [0, 3, float('inf')],
    ...     [2, 0, float('inf')],
    ...     [float('inf'), 7, 0]
    ... ]

    >>> expected = [
    ...     [0, 3, float('inf')],
    ...     [2, 0, float('inf')],
    ...     [9, 7, 0]
    ... ]
    >>> dist, _ = floyd_warshall(graph, 3)
    The shortest path matrix using Floyd Warshall algorithm
    <BLANKLINE>
    0  3  INF
    2  0  INF
    9  7  0
    >>> dist == expected
    True
    """

    dist = [[float("inf") for _ in range(v)] for _ in range(v)]

    for i in range(v):
        for j in range(v):
            dist[i][j] = graph[i][j]

            # check vertex k against all other vertices (i, j)
    for k in range(v):
        # looping through rows of graph array
        for i in range(v):
            # looping through columns of graph array
            for j in range(v):
                if (
                    dist[i][k] != float("inf")
                    and dist[k][j] != float("inf")
                    and dist[i][k] + dist[k][j] < dist[i][j]
                ):
                    dist[i][j] = dist[i][k] + dist[k][j]

    _print_dist(dist, v)
    return dist, v


if __name__ == "__main__":
    v = int(input("Enter number of vertices: "))
    e = int(input("Enter number of edges: "))

    graph = [[float("inf") for i in range(v)] for j in range(v)]

    for i in range(v):
        graph[i][i] = 0.0

        # src and dst are indices that must be within the array size graph[e][v]
        # failure to follow this will result in an error
    for i in range(e):
        print("\nEdge ", i + 1)
        src = int(input("Enter source:"))
        dst = int(input("Enter destination:"))
        weight = float(input("Enter weight:"))
        graph[src][dst] = weight

    floyd_warshall(graph, v)

    # Example Input
    # Enter number of vertices: 3
    # Enter number of edges: 2

    # # generated graph from vertex and edge inputs
    # [[inf, inf, inf], [inf, inf, inf], [inf, inf, inf]]
    # [[0.0, inf, inf], [inf, 0.0, inf], [inf, inf, 0.0]]

    # specify source, destination and weight for edge #1
    # Edge  1
    # Enter source:1
    # Enter destination:2
    # Enter weight:2

    # specify source, destination and weight for edge #2
    # Edge  2
    # Enter source:2
    # Enter destination:1
    # Enter weight:1

    # # Expected Output from the vertice, edge and src, dst, weight inputs!!
    # 0		INF	INF
    # INF	0	2
    # INF	1	0
