def printDist(dist, V):
    print("\nVertex Distance")
    for i in range(V):
        if dist[i] != float("inf"):
            print(i, "\t", int(dist[i]), end="\t")
        else:
            print(i, "\t", "INF", end="\t")
        print()


def BellmanFord(graph, V, E, src):
    mdist = [float("inf") for i in range(V)]
    mdist[src] = 0.0

    for i in range(V - 1):
        for j in range(E):
            u = graph[j]["src"]
            v = graph[j]["dst"]
            w = graph[j]["weight"]

            if mdist[u] != float("inf") and mdist[u] + w < mdist[v]:
                mdist[v] = mdist[u] + w
    for j in range(E):
        u = graph[j]["src"]
        v = graph[j]["dst"]
        w = graph[j]["weight"]

        if mdist[u] != float("inf") and mdist[u] + w < mdist[v]:
            print("Negative cycle found. Solution not possible.")
            return

    printDist(mdist, V)


if __name__ == "__main__":
    V = int(input("Enter number of vertices: ").strip())
    E = int(input("Enter number of edges: ").strip())

    graph = [dict() for j in range(E)]

    for i in range(V):
        graph[i][i] = 0.0

    for i in range(E):
        print("\nEdge ", i + 1)
        src = int(input("Enter source:").strip())
        dst = int(input("Enter destination:").strip())
        weight = float(input("Enter weight:").strip())
        graph[i] = {"src": src, "dst": dst, "weight": weight}

    gsrc = int(input("\nEnter shortest path source:").strip())
    BellmanFord(graph, V, E, gsrc)
