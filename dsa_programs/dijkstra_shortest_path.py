"""Dijkstra's shortest path algorithm with a min-heap."""

from heapq import heappop, heappush
from typing import Dict, Iterable, List, Tuple, TypeVar

T = TypeVar("T")

Graph = Dict[T, Iterable[Tuple[T, float]]]


def dijkstra_shortest_path(graph: Graph, source: T) -> Dict[T, float]:
    distances: Dict[T, float] = {source: 0.0}
    heap: List[Tuple[float, T]] = [(0.0, source)]
    while heap:
        current_dist, node = heappop(heap)
        if current_dist > distances.get(node, float("inf")):
            continue
        for neighbor, weight in graph.get(node, ()):  # missing key means no outgoing edges
            cost = current_dist + weight
            if cost < distances.get(neighbor, float("inf")):
                distances[neighbor] = cost
                heappush(heap, (cost, neighbor))
    return distances
