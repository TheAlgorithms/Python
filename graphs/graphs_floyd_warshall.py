# floyd_warshall.py
"""
The problem is to find the shortest distance between all pairs of vertices in a
weighted directed graph that can have negative edge weights.
"""


def _print_dist(dist, v):
    print("\nThe shortest path matrix using Floyd Warshall algorithm\n")
    for i in range(v):
        for j in range(v):
            if dist[i][j] != float("inf"):
                print(int(dist[i][j]), end="\t")
            else:
                print("INF", end="\t")
        print()


def floyd_warshall(graph, v):
    """
    Computes the shortest paths in a weighted graph.

    :param graph: 2D list where each element represents the weight from i to j.
    :type graph: List[List[float]]
    :param v: Number of vertices in the graph.
    :type v: int
    :return: A tuple containing the distances matrix and number of vertices.

    Example:
    >>> v = 3
    >>> inf = float('inf')
    >>> graph = [
    ...     [0, 1, inf],
    ...     [inf, 0, 1],
    ...     [1, inf, 0]
    ... ]
    >>> dist, _ = floyd_warshall(graph, v)  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    <BLANKLINE>
    The shortest path matrix using Floyd Warshall algorithm
    <BLANKLINE>
    0   1   2
    2   0   1
    1   2   0
    >>> [int(x) if x != inf else 'INF' for row in dist for x in row]
    [0, 1, 2, 2, 0, 1, 1, 2, 0]

    Handling a graph with no edges:
    >>> v = 3
    >>> graph = [[inf]*3 for _ in range(3)]
    >>> for i in range(3): graph[i][i] = 0
    >>> dist, _ = floyd_warshall(graph, v)  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    <BLANKLINE>
    The shortest path matrix using Floyd Warshall algorithm
    <BLANKLINE>
    0   INF     INF
    INF 0       INF
    INF INF     0
    >>> [int(x) if x != inf else 'INF' for row in dist for x in row]
    [0, 'INF', 'INF', 'INF', 0, 'INF', 'INF', 'INF', 0]

    """
    dist = [[float("inf") for _ in range(v)] for _ in range(v)]

    for i in range(v):
        for j in range(v):
            dist[i][j] = graph[i][j]

    for k in range(v):
        for i in range(v):
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
    import doctest

    doctest.testmod()
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
