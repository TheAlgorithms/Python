"""Dijkstra's shortest path algorithm.

This module provides a simple Dijkstra implementation that works on a
graph represented as an adjacency mapping: {node: [(neighbor, weight), ...], ...}.

Functions:
- dijkstra(graph, source) -> (dist, prev)
- shortest_path(prev, target) -> list

Doctests include a small example graph.
"""

from __future__ import annotations

import heapq
from typing import Dict, Iterable, List, Tuple, Any


def dijkstra(
    graph: Dict[Any, Iterable[Tuple[Any, float]]], source: Any
) -> Tuple[Dict[Any, float], Dict[Any, Any]]:
    """Compute shortest path distances from source to all reachable nodes.

    Args:
        graph: adjacency mapping where graph[u] yields (v, weight) pairs.
        source: start node.

    Returns:
        (dist, prev)
        - dist: mapping node -> distance (float). Unreachable nodes are absent.
        - prev: mapping node -> predecessor on shortest path (or None for source).

    Example:
    >>> graph = {
    ...     'A': [('B', 1), ('C', 4)],
    ...     'B': [('C', 2), ('D', 5)],
    ...     'C': [('D', 1)],
    ...     'D': []
    ... }
    >>> dist, prev = dijkstra(graph, 'A')
    >>> dist['D']
    4
    >>> shortest_path(prev, 'D')
    ['A', 'B', 'C', 'D']
    """
    dist: Dict[Any, float] = {}
    prev: Dict[Any, Any] = {}
    pq: List[Tuple[float, Any]] = []  # (distance, node)

    heapq.heappush(pq, (0.0, source))
    dist[source] = 0.0
    prev[source] = None

    while pq:
        d, u = heapq.heappop(pq)
        # Skip stale entries
        if d != dist.get(u, float("inf")):
            continue
        for v, w in graph.get(u, []):
            nd = d + float(w)
            if nd < dist.get(v, float("inf")):
                dist[v] = nd
                prev[v] = u
                heapq.heappush(pq, (nd, v))

    return dist, prev


def shortest_path(prev: Dict[Any, Any], target: Any) -> List[Any]:
    """Reconstruct path from source to target using predecessor map.

    If target is not in `prev`, returns an empty list.
    """
    if target not in prev:
        return []
    path: List[Any] = []
    cur = target
    while cur is not None:
        path.append(cur)
        cur = prev.get(cur)
    path.reverse()
    return path


if __name__ == "__main__":
    import doctest

    doctest.testmod()
