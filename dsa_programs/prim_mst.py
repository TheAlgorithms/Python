"""Prim's algorithm for minimum spanning tree using a priority queue."""

from heapq import heappop, heappush
from typing import Dict, Iterable, List, Optional, Set, Tuple, TypeVar

T = TypeVar("T")
Edge = Tuple[T, T, float]
Graph = Dict[T, Iterable[Tuple[T, float]]]


def prim_mst(graph: Graph, start: Optional[T] = None) -> List[Edge]:
    if not graph:
        return []
    nodes: Set[T] = set(graph)
    for adjacency in graph.values():
        for neighbor, _ in adjacency:
            nodes.add(neighbor)
    current_start = start if start is not None else next(iter(nodes))
    nodes.add(current_start)
    visited: Set[T] = {current_start}
    heap: List[Tuple[float, T, T]] = []
    for neighbor, weight in graph.get(current_start, []):
        heappush(heap, (weight, current_start, neighbor))
    mst: List[Edge] = []
    while heap and len(visited) < len(nodes):
        weight, u, v = heappop(heap)
        if v in visited:
            continue
        visited.add(v)
        mst.append((u, v, weight))
        for neighbor, w in graph.get(v, []):
            if neighbor not in visited:
                heappush(heap, (w, v, neighbor))
    return mst
