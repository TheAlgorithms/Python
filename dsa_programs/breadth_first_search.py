"""Breadth-first search returning discovery order from a starting node."""

from collections import deque
from typing import Deque, Dict, Iterable, List, Set, TypeVar

T = TypeVar("T")


def breadth_first_search(graph: Dict[T, Iterable[T]], start: T) -> List[T]:
    visited: Set[T] = set()
    order: List[T] = []
    queue: Deque[T] = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, ()):  # gracefully handle missing keys
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order
