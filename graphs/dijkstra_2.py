def print_dist(dist, v):
    """
    Print vertex distances.

    Parameters:
    dist (list): A list of distances.
    v (int): The number of vertices.

    Example:
    >>> print_dist([0.0, 2.0, 3.0, float('inf')], 4)
    Vertex Distance
    0 0
    1 2
    2 3
    3 INF
    """
    print("\nVertex Distance")
    for i in range(v):
        if dist[i] != float("inf"):
            print(i, int(dist[i]), end=" ")
        else:
            print(i, "INF", end=" ")
        print()


def min_dist(mdist, vset, v):
    """
    Find the vertex with the minimum distance.

    Parameters:
    mdist (list): A list of distances.
    vset (list): A list of boolean values indicating visited vertices.
    v (int): The number of vertices.

    Example:
    >>> min_dist([0.0, 2.0, 3.0, float('inf')], [False, True, False, False], 4)
    0
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
    Implement Dijkstra's algorithm to find the shortest path.

    Parameters:
    graph (list): The graph represented as an adjacency matrix.
    v (int): The number of vertices.
    src (int): The source vertex.

    Example:
    >>> graph = [[0.0, 2.0, float('inf'), 1.0],
    ...          [2.0, 0.0, 4.0, float('inf')],
    ...          [float('inf'), 4.0, 0.0, 3.0],
    ...          [1.0, float('inf'), 3.0, 0.0]]
    >>> dijkstra(graph, 4, 0)
    Vertex Distance
    0 	 0
    1 	 2
    2 	 3
    3 	 1
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

    print_dist(mdist, v)


if __name__ == "__main__":
    V = int(input("Enter the number of vertices: ").strip())
    E = int(input("Enter the number of edges: ").strip())

    graph = [[float("inf") for i in range(V)] for j in range(V)]

    for i in range(V):
        graph[i][i] = 0.0

    for i in range(E):
        print("\nEdge ", i + 1)
        src = int(input("Enter source:").strip())
        dst = int(input("Enter destination:").strip())
        weight = float(input("Enter weight:").strip())
        graph[src][dst] = weight

    gsrc = int(input("\nEnter the shortest path source:").strip())
    dijkstra(graph, V, gsrc)
