"""Depth-first search using recursion to record visitation order."""

from typing import Dict, Iterable, List, Set, TypeVar

T = TypeVar("T")


def depth_first_search(graph: Dict[T, Iterable[T]], start: T) -> List[T]:
    visited: Set[T] = set()
    order: List[T] = []

    def _dfs(node: T) -> None:
        visited.add(node)
        order.append(node)
        for neighbor in graph.get(node, ()):  # support sparse adjacency
            if neighbor not in visited:
                _dfs(neighbor)

    _dfs(start)
    return order
