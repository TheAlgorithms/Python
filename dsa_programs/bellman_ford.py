"""Bellman-Ford shortest paths with negative cycle detection."""

from typing import Dict, Iterable, List, Set, Tuple, TypeVar

T = TypeVar("T")
Edge = Tuple[T, T, float]


def bellman_ford(
    vertices: Iterable[T], edges: Iterable[Edge], source: T
) -> Dict[T, float]:
    edge_list: List[Edge] = list(edges)
    vertex_set: Set[T] = set(vertices)
    for u, v, _ in edge_list:
        vertex_set.add(u)
        vertex_set.add(v)
    vertex_set.add(source)
    distances: Dict[T, float] = {vertex: float("inf") for vertex in vertex_set}
    distances[source] = 0.0
    for _ in range(len(vertex_set) - 1):
        updated = False
        for u, v, weight in edge_list:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                updated = True
        if not updated:
            break
    for u, v, weight in edge_list:
        if distances[u] + weight < distances[v]:
            raise ValueError("Graph contains a negative-weight cycle")
    return distances
