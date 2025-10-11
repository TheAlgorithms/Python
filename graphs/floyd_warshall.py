"""
Floyd-Warshall Algorithm
Solves the all-pairs shortest path problem for a weighted graph.
"""

def floyd_warshall(dist):
    """
    Updates the distance matrix to contain the shortest distances
    between all pairs of vertices.
    
    Args:
        dist: 2D list, adjacency matrix where dist[i][j] is the weight
              from vertex i to vertex j (use a large number for infinity)
    """
    V = len(dist)

    # Consider each vertex as an intermediate point
    for k in range(V):
        for i in range(V):
            for j in range(V):
                # Update dist[i][j] if a shorter path is found through k
                if dist[i][k] != INF and dist[k][j] != INF:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


if __name__ == "__main__":
    INF = 100000000  # Representation of "infinity"
    
    # New example adjacency matrix
    dist = [
        [0, 3, INF, 7, INF],
        [8, 0, 2, INF, INF],
        [5, INF, 0, 1, INF],
        [2, INF, INF, 0, 1],
        [INF, INF, INF, INF, 0]
    ]

    floyd_warshall(dist)

    print("Shortest distances between all pairs of vertices:")
    for row in dist:
        print(row)
