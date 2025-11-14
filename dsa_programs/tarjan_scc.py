"""Tarjan's algorithm for strongly connected components."""

from typing import Dict, Iterable, List, Set, TypeVar

T = TypeVar("T")
Graph = Dict[T, Iterable[T]]


def tarjan_strongly_connected_components(graph: Graph) -> List[List[T]]:
    index = 0
    indices: Dict[T, int] = {}
    lowlink: Dict[T, int] = {}
    stack: List[T] = []
    on_stack: Set[T] = set()
    components: List[List[T]] = []

    def strong_connect(node: T) -> None:
        nonlocal index
        indices[node] = lowlink[node] = index
        index += 1
        stack.append(node)
        on_stack.add(node)
        for neighbor in graph.get(node, ()):  # default to empty for missing keys
            if neighbor not in indices:
                strong_connect(neighbor)
                lowlink[node] = min(lowlink[node], lowlink[neighbor])
            elif neighbor in on_stack:
                lowlink[node] = min(lowlink[node], indices[neighbor])
        if lowlink[node] == indices[node]:
            component: List[T] = []
            while True:
                w = stack.pop()
                on_stack.remove(w)
                component.append(w)
                if w == node:
                    break
            components.append(component)

    for node in set(graph) | {
        neighbor for neighbors in graph.values() for neighbor in neighbors
    }:
        if node not in indices:
            strong_connect(node)
    return components
