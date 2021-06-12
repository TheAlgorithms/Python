from typing import Dict, List


def print_distance(distance: List[float], src):
    print(f"Vertex\tShortest Distance from vertex {src}")
    for i, d in enumerate(distance):
        print(f"{i}\t\t{d}")


def bellman_ford(
    graph: List[Dict[str, int]], vertex_count: int, edge_count: int, src: int
) -> List[float]:
    """
    Returns shortest paths from a vertex src to all
    other vertices.
    >>> edges = [(2, 1, -10), (3, 2, 3), (0, 3, 5), (0, 1, 4)]
    >>> g = [{"src": s, "dst": d, "weight": w} for s, d, w in edges]
    >>> bellman_ford(g, 4, 4, 0)
    [0.0, -2.0, 8.0, 5.0]
    >>> g = [{"src": s, "dst": d, "weight": w} for s, d, w in edges + [(1, 3, 5)]]
    >>> bellman_ford(g, 4, 5, 0)
    Traceback (most recent call last):
     ...
    Exception: Negative cycle found
    """
    distance = [float("inf")] * vertex_count
    distance[src] = 0.0

    for i in range(vertex_count - 1):
        for j in range(edge_count):
            u, v, w = graph[j]["src"], graph[j]["dst"], graph[j]["weight"]

            if distance[u] != float("inf") and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    for j in range(edge_count):
        u, v, w = graph[j]["src"], graph[j]["dst"], graph[j]["weight"]

        if distance[u] != float("inf") and distance[u] + w < distance[v]:
            raise Exception("Negative cycle found")

    return distance


if __name__ == "__main__":
    edges = [(2, 1, -10), (3, 2, 3), (0, 3, 5), (0, 1, 4)]
    g = [{"src": s, "dst": d, "weight": w} for s, d, w in edges]
    shortest_distance = bellman_ford(g, 4, 4, 0)
    print_distance(shortest_distance, 0)

    import doctest

    doctest.testmod()
