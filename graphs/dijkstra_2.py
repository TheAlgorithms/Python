def print_dist(dist, v):
    print("\nVertex Distance")
    for i in range(v):
        if dist[i] != float("inf"):
            print(i, "\t", int(dist[i]), end="\t")
        else:
            print(i, "\t", "INF", end="\t")
        print()


def min_dist(mdist, vset, v):
     """
    Finds the vertex with minimum distance that hasn't been visited yet.
    >>> min_dist([0, 4, 2, float('inf')], [True, False, False, False], 4)
    2
    >>> min_dist([0, 4, 2, 1], [True, False, True, False], 4)
    3
    >>> min_dist([0, 4, 2, 1], [True, True, True, True], 4)
    -1
    >>> min_dist([float('inf'), float('inf')], [False, False], 2)
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
