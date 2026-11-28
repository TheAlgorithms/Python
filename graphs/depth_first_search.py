"""Iterative implementation of a Depth First Search algorithm."""

from __future__ import annotations


def depth_first_search(graph: dict[str, list[str]], start: str) -> set[str]:
    """Depth First Search on Graph

    :param graph: directed graph in dictionary format
    :param start: starting vertex as a string
    :returns: the trace of the search
    >>> input_G = { "A": ["B", "C", "D"], "B": ["A", "D", "E"],
    ... "C": ["A", "F"], "D": ["B", "D"], "E": ["B", "F"],
    ... "F": ["C", "E", "G"], "G": ["F"] }
    >>> output_G = list({'A', 'B', 'C', 'D', 'E', 'F', 'G'})
    >>> all(x in output_G for x in list(depth_first_search(input_G, "A")))
    True
    >>> all(x in output_G for x in list(depth_first_search(input_G, "G")))
    True
    """
    explored: set[str] = {start}
    stack: list[str] = [start]
    while stack:
        current = stack.pop()
        for neighbor in graph.get(current, []):
            if neighbor not in explored:
                explored.add(neighbor)
                stack.append(neighbor)
    return explored
