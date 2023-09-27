"""
Bi-directional Dijkstra's algorithm.

A bi-directional approach is an efficient and
less time consuming optimization for Dijkstra's
searching algorithm

Reference: shorturl.at/exHM7
"""

# Author: Swayam Singh (https://github.com/practice404)


from queue import PriorityQueue
from typing import Any

import numpy as np


def pass_and_relaxation(
    graph: dict,
    v: str,
    visited_forward: set,
    visited_backward: set,
    cst_fwd: dict,
    cst_bwd: dict,
    queue: PriorityQueue,
    parent: dict,
    shortest_distance: float,
) -> float:
    for nxt, d in graph[v]:
        if nxt in visited_forward:
            continue
        old_cost_f = cst_fwd.get(nxt, np.inf)
        new_cost_f = cst_fwd[v] + d
        if new_cost_f < old_cost_f:
            queue.put((new_cost_f, nxt))
            cst_fwd[nxt] = new_cost_f
            parent[nxt] = v
        if nxt in visited_backward:
            if cst_fwd[v] + d + cst_bwd[nxt] < shortest_distance:
                shortest_distance = cst_fwd[v] + d + cst_bwd[nxt]
    return shortest_distance


def bidirectional_dij(
    source: str, destination: str, graph_forward: dict, graph_backward: dict
) -> int:
    """
    Bi-directional Dijkstra's algorithm.

    Returns:
        shortest_path_distance (int): length of the shortest path.

    Warnings:
        If the destination is not reachable, function returns -1

    >>> bidirectional_dij("E", "F", graph_fwd, graph_bwd)
    3
    """
    shortest_path_distance = -1

    visited_forward = set()
    visited_backward = set()
    cst_fwd = {source: 0}
    cst_bwd = {destination: 0}
    parent_forward = {source: None}
    parent_backward = {destination: None}
    queue_forward: PriorityQueue[Any] = PriorityQueue()
    queue_backward: PriorityQueue[Any] = PriorityQueue()

    shortest_distance = np.inf

    queue_forward.put((0, source))
    queue_backward.put((0, destination))

    if source == destination:
        return 0

    while not queue_forward.empty() and not queue_backward.empty():
        _, v_fwd = queue_forward.get()
        visited_forward.add(v_fwd)

        _, v_bwd = queue_backward.get()
        visited_backward.add(v_bwd)

        shortest_distance = pass_and_relaxation(
            graph_forward,
            v_fwd,
            visited_forward,
            visited_backward,
            cst_fwd,
            cst_bwd,
            queue_forward,
            parent_forward,
            shortest_distance,
        )

        shortest_distance = pass_and_relaxation(
            graph_backward,
            v_bwd,
            visited_backward,
            visited_forward,
            cst_bwd,
            cst_fwd,
            queue_backward,
            parent_backward,
            shortest_distance,
        )

        if cst_fwd[v_fwd] + cst_bwd[v_bwd] >= shortest_distance:
            break

    if shortest_distance != np.inf:
        shortest_path_distance = shortest_distance
    return shortest_path_distance


graph_fwd = {
    "B": [["C", 1]],
    "C": [["D", 1]],
    "D": [["F", 1]],
    "E": [["B", 1], ["G", 2]],
    "F": [],
    "G": [["F", 1]],
}
graph_bwd = {
    "B": [["E", 1]],
    "C": [["B", 1]],
    "D": [["C", 1]],
    "F": [["D", 1], ["G", 1]],
    "E": [[None, np.inf]],
    "G": [["E", 2]],
}

if __name__ == "__main__":
    import doctest

    doctest.testmod()
