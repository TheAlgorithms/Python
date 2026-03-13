"""
AO* (And-Or) Graph Search Algorithm
===================================

This module implements the AO* (And-Or Star) search algorithm for solving
AND-OR graphs — a generalization of search trees where nodes can represent
either OR decisions or AND decompositions.

Each node in the graph maps to a list of *options*, where each option is a
list of child nodes. This naturally encodes the AND/OR structure:

- The outer list represents OR options (choices).
- Each inner list represents AND sets (all must be solved).

This implementation follows the GeeksforGeeks explanation:
https://www.geeksforgeeks.org/artificial-intelligence/ao-algorithm-artificial-intelligence/

Time Complexity:
    Exponential in worst case (depends on branching factor).

"""

from __future__ import annotations

from typing import Any


def _update_node(
    graph: dict[Any, list[list[Any]]],
    node: Any,
    h: dict[Any, float],
    solved: dict[Any, list[Any]],
    weight: float = 1.0,
) -> None:
    """
    Update the heuristic value and solved status of a node.

    Uses the AO* rule:
        value(node) = min_{option in options(node)}
            (sum(value(child) + weight) for child in option)
    """
    if not graph.get(node):
        solved[node] = []
        return

    best_cost = float("inf")
    best_option: list[Any] | None = None
    best_all_solved = False

    for option in graph[node]:
        # option cost is sum of (child value + edge weight)
        total = sum(h[child] + weight for child in option)
        all_solved = all(child in solved for child in option)
        if total < best_cost:
            best_cost = total
            best_option = option
            best_all_solved = all_solved

    h[node] = best_cost
    # mark node solved only if best option's children are solved
    if best_option and best_all_solved:
        solved[node] = best_option


def _ao_star(
    graph: dict[Any, list[list[Any]]],
    node: Any,
    h: dict[Any, float],
    solved: dict[Any, list[Any]],
    weight: float = 1.0,
) -> float:
    """
    Recursive AO* solver.

    Returns the updated heuristic value of the node.
    """
    # terminal node
    if not graph.get(node):
        solved[node] = []
        return h[node]

    # initial estimate/update using current child heuristics
    _update_node(graph, node, h, solved, weight)

    # continue expanding the currently best AND-set until node becomes solved
    while node not in solved:
        # choose best option under current estimates (sum(child + weight))
        best_option = min(
            graph[node],
            key=lambda option: sum(h[child] + weight for child in option),
        )

        # expand (refine) each child in that best option
        for child in best_option:
            # recursively refine child; this will explore child's best options
            _ao_star(graph, child, h, solved, weight)

        # after expanding, update this node again (propagate refinements upward)
        prev = h[node]
        _update_node(graph, node, h, solved, weight)

        # if no meaningful change, we can break to avoid infinite loops on cycles
        if abs(h[node] - prev) < 1e-9:
            break

    return h[node]


def ao_star(
    graph: dict[Any, list[list[Any]]],
    start: Any,
    h: dict[Any, float],
    weight: float = 1.0,
) -> tuple[dict[Any, list[Any]], float]:
    """
    Perform AO* (And-Or Star) search on a given AND-OR graph.

    Args:
     graph: Mapping of node → list of AND-options.
         Each option is a list of child nodes.
        start: Start node key.
        h: dictionary of heuristic values. Updated in-place.
        weight: edge cost (g(n)) to add per child (default 1.0).

    Returns:
        A tuple (solution, value):
        - solution: dict mapping solved nodes to their chosen AND-children.
        - value: final value (cost) of the start node.

    Example:
        >>> g = {'A': [['B', 'C'], ['D']], 'B': [], 'C': [], 'D': []}
        >>> h = {'A': 2.0, 'B': 1.0, 'C': 1.0, 'D': 5.0}
        >>> sol, val = ao_star(g, 'A', h)
        >>> val
        4.0
        >>> sol['A']
        ['B', 'C']

    Chain example:
        >>> g = {'A': [['B']], 'B': [['C']], 'C': []}
        >>> h = {'A': 10.0, 'B': 5.0, 'C': 1.0}
        >>> sol, val = ao_star(g, 'A', h)
        >>> val
        3.0
        >>> sol['A']
        ['B']
        >>> sol['B']
        ['C']

    Example (the case you described; note edge cost = 1 by default):
        >>> graph = {
        ...     'A': [['B'], ['C', 'D']],
        ...     'B': [['E'], ['F']],
        ...     'C': [['G'], ['H', 'I']],
        ...     'D': [['J']],
        ...     'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': []
        ... }
        >>> h = {
        ...     'A': 100.0, 'B': 5.0, 'C': 2.0, 'D': 4.0,
        ...     'E': 7.0, 'F': 9.0, 'G': 3.0, 'H': 0.0, 'I': 0.0, 'J': 0.0
        ... }
        >>> sol, v = ao_star(graph, 'A', h)
        >>> v
        5.0
        >>> sol['C'] == ['H', 'I']
        True
        >>> sol['D'] == ['J']
        True
    """
    if start not in graph:
        raise ValueError("Start node must exist in graph.")

    solved: dict[Any, list[Any]] = {}
    final_value = _ao_star(graph, start, h, solved, weight)
    return solved, final_value


if __name__ == "__main__":
    demo_graph = {
        "S": [["A", "B"], ["C", "D"]],
        "A": [["E"], ["F", "G"]],
        "B": [],
        "C": [["H"]],
        "D": [],
        "E": [],
        "F": [],
        "G": [],
        "H": [],
    }

    heuristics = {
        "S": 100.0,
        "A": 50.0,
        "B": 3.0,
        "C": 20.0,
        "D": 4.0,
        "E": 1.0,
        "F": 2.0,
        "G": 2.0,
        "H": 1.0,
    }

    sol, val = ao_star(demo_graph, "S", heuristics)
    print("Solution graph:", sol)
    print("Final cost of start node:", val)
