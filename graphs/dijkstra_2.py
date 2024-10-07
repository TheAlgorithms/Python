def print_dist(dist, v):
    """
    Print vertex distance

    Examples:
    >>> print_dist([float('inf'),float('inf'),float('inf')], 3)
    <BLANKLINE>
    Vertex Distance
    0   INF
    1   INF
    2   INF
    >>> print_dist([2.0,6.0,10.0,3.0], 4)
    <BLANKLINE>
    Vertex Distance
    0   2
    1   6
    2   10
    3   3
    >>> print_dist([], 4)
    Traceback (most recent call last):
     ...
    IndexError: list index out of range
    """
    print("\nVertex Distance")
    for i in range(v):
        if dist[i] != float("inf"):
            print(i, " ", int(dist[i]), end="")
        else:
            print(i, " ", "INF", end="")
        print()


def min_dist(mdist, vset, v):
    """
    Finds the index of the node with the minimum distance between no-visited nodes

    Examples:
    >>> dist = [0.0, float('inf'), float('inf'), float('inf')]
    >>> set = [False, False, False, False]
    >>> min_dist(dist, set, 4)
    0
    >>> min_dist([], [], 0)
    -1
    """
    min_val = float("inf")
    min_ind = -1
    for i in range(v):
        if (not vset[i]) and mdist[i] < min_val:
            min_ind = i
            min_val = mdist[i]
    return min_ind


def dijkstra(graph, v, src):
    """
    Dijkstra's algorithm to calculate the shortest distances from the src source node
    to all other nodes in a graph represented as an adjacency matrix.

    Examples:
    >>> G1 = [[0.0, 6.0, 2.0, float('inf')],
    ... [float('inf'), 0.0, 9.0, 1.0],
    ... [float('inf'), float('inf'), 0.0, 3.0],
    ... [float('inf'), float('inf'), float('inf'), 0.0]]
    >>> dijkstra(G1, 4, 5)
    Traceback (most recent call last):
    ...
    IndexError: list assignment index out of range
    >>> G2 = [[0.0, 6.0, 2.0, float('inf')],
    ... [float('inf'), 0.0, 9.0, 1.0],
    ... [float('inf'), float('inf'), 0.0, 3.0],
    ... [float('inf'), float('inf'), float('inf'), 0.0]]
    >>> dijkstra(G2, 4, 0)
    <BLANKLINE>
    Vertex Distance
    0   0
    1   6
    2   2
    """
    mdist = [float("inf") for _ in range(v)]
    vset = [False for _ in range(v)]
    mdist[src] = 0.0

    for _ in range(v - 1):
        u = min_dist(mdist, vset, v)
        vset[u] = True

        for i in range(v):
            if (
                (not vset[i])
                and graph[u][i] != float("inf")
                and mdist[u] + graph[u][i] < mdist[i]
            ):
                mdist[i] = mdist[u] + graph[u][i]

    print_dist(mdist, i)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

    V = int(input("Enter number of vertices: ").strip())
    E = int(input("Enter number of edges: ").strip())

    graph = [[float("inf") for i in range(V)] for j in range(V)]

    for i in range(V):
        graph[i][i] = 0.0

    for i in range(E):
        print("\nEdge ", i + 1)
        src = int(input("Enter source:").strip())
        dst = int(input("Enter destination:").strip())
        weight = float(input("Enter weight:").strip())
        graph[src][dst] = weight

    gsrc = int(input("\nEnter shortest path source:").strip())
    dijkstra(graph, V, gsrc)
