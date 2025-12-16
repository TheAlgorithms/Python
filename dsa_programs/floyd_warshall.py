"""Floyd-Warshall all-pairs shortest path algorithm."""

from typing import Dict, TypeVar

T = TypeVar("T")


def floyd_warshall(graph: Dict[T, Dict[T, float]]) -> Dict[T, Dict[T, float]]:
    nodes: set[T] = set(graph)
    for adjacency in graph.values():
        nodes.update(adjacency)
    distances: Dict[T, Dict[T, float]] = {
        u: {v: float("inf") for v in nodes} for u in nodes
    }
    for node in nodes:
        distances[node][node] = 0.0
    for u, adjacency in graph.items():
        for v, weight in adjacency.items():
            if weight < distances[u][v]:
                distances[u][v] = weight
    for k in nodes:
        for i in nodes:
            for j in nodes:
                via = distances[i][k] + distances[k][j]
                if via < distances[i][j]:
                    distances[i][j] = via
    return distances
