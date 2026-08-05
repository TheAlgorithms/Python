"""
Johnson's Algorithm for All-Pairs Shortest Paths

More efficient than Floyd-Warshall for sparse graphs.
Uses Bellman-Ford + Dijkstra with reweighting.

Time Complexity: O(V² log V + VE) - better than O(V³) for sparse graphs
Space Complexity: O(V²)
"""

import heapq


def bellman_ford(
    graph: dict[int, list[tuple[int, int]]], source: int, n: int
) -> tuple[list[float], bool]:
    """
    Bellman-Ford to detect negative cycles and compute potentials.

    Returns:
        Tuple of (distances, has_negative_cycle)
    """
    dist = [float("inf")] * n
    dist[source] = 0

    # Relax edges V-1 times
    for _ in range(n - 1):
        updated = False
        for u in range(n):
            if dist[u] == float("inf"):
                continue
            for v, w in graph.get(u, []):
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
        if not updated:
            break

    # Check for negative cycles
    for u in range(n):
        if dist[u] == float("inf"):
            continue
        for v, w in graph.get(u, []):
            if dist[u] + w < dist[v]:
                return dist, True  # Negative cycle detected

    return dist, False


def dijkstra_with_potential(
    graph: dict[int, list[tuple[int, int]]], source: int, n: int, potential: list[float]
) -> list[float]:
    """
    Dijkstra with reweighted edges using Johnson's potential.
    """
    dist = [float("inf")] * n
    dist[source] = 0
    pq = [(0, source)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue

        for v, w in graph.get(u, []):
            # Reweighted edge: w + potential[u] - potential[v]
            new_dist = dist[u] + w + potential[u] - potential[v]
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

    # Convert back to original weights
    for i in range(n):
        if dist[i] != float("inf"):
            dist[i] = dist[i] - potential[source] + potential[i]

    return dist


def johnsons_algorithm(
    graph: dict[int, list[tuple[int, int]]], n: int
) -> list[list[float]]:
    """
    Johnson's algorithm for all-pairs shortest paths.

    Args:
        graph: Adjacency list {u: [(v, weight), ...]}
        n: Number of vertices (0 to n-1)

    Returns:
        Distance matrix where result[i][j] is shortest path i->j

    Raises:
        ValueError: If graph contains negative weight cycle

    """
    # Add dummy node connected to all vertices with 0-weight edges
    # Create copy to avoid modifying original
    modified_graph = {v: edges[:] for v, edges in graph.items()}
    modified_graph[n] = [(v, 0) for v in range(n)]

    # Run Bellman-Ford from dummy node to get potentials
    potential, has_negative = bellman_ford(modified_graph, n, n + 1)

    if has_negative:
        raise ValueError("Graph contains negative weight cycle")

    potential = potential[:-1]  # Remove dummy node

    # Run Dijkstra from each vertex with reweighting
    result = []
    for source in range(n):
        dist = dijkstra_with_potential(graph, source, n, potential)
        result.append(dist)

    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
