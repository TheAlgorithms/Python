"""Topological sorting for a directed acyclic graph using Kahn's algorithm."""

from collections import deque
from typing import Deque, Dict, Iterable, List, TypeVar

T = TypeVar("T")


def topological_sort(graph: Dict[T, Iterable[T]]) -> List[T]:
    indegree: Dict[T, int] = {}
    for node, neighbors in graph.items():
        indegree.setdefault(node, 0)
        for neighbor in neighbors:
            indegree[neighbor] = indegree.get(neighbor, 0) + 1
    queue: Deque[T] = deque(node for node, count in indegree.items() if count == 0)
    order: List[T] = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, ()):  # skip nodes without outgoing edges
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    if len(order) != len(indegree):
        raise ValueError("Graph contains a cycle")
    return order
