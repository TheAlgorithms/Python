def print_dist(dist, v):
    print("\nVertex Distance")
    for i in range(v):
        if dist[i] != float("inf"):
            print(i, "\t", int(dist[i]), end="\t")
        else:
            print(i, "\t", "INF", end="\t")
        print()


def min_dist(mdist, vset, v):
    min_val = float("inf")
    min_ind = -1
    for i in range(v):
        if (not vset[i]) and mdist[i] < min_val:
            min_ind = i
            min_val = mdist[i]
    return min_ind


def dijkstra(graph, v, src):
    mdist = [float("inf") for i in range(v)]
    vset = [False for i in range(v)]
    mdist[src] = 0.0

    for i in range(v - 1):
        u = min_dist(mdist, vset, v)
        vset[u] = True

        for v in range(v):
            if (
                (not vset[v])
                and graph[u][v] != float("inf")
                and mdist[u] + graph[u][v] < mdist[v]
            ):
                mdist[v] = mdist[u] + graph[u][v]

    print_dist(mdist, v)


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
