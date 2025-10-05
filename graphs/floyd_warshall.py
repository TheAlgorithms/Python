# Algorithm to find shortest paths between all pairs of vertices in a weighted graph.

def floyd_warshall(graph):
    """
    graph: adjacency matrix (2D list)
    returns: distance matrix (shortest path between all pairs)
    """
    n = len(graph)
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


if __name__ == "__main__":
    INF = 99999
    graph = [
        [0, 5, INF, 10],
        [INF, 0, 3, INF],
        [INF, INF, 0, 1],
        [INF, INF, INF, 0]
    ]

    result = floyd_warshall(graph)
    print("All-Pairs Shortest Paths:")
    for row in result:
        print(row)
