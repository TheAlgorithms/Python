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

    while queue_forward and queue_backward:
        while not queue_forward.empty():
            _, v_fwd = queue_forward.get()

            if v_fwd not in visited_forward:
                break
        else:
            break
        visited_forward.add(v_fwd)

        while not queue_backward.empty():
            _, v_bwd = queue_backward.get()

            if v_bwd not in visited_backward:
                break
        else:
            break
        visited_backward.add(v_bwd)

        # forward pass and relaxation
        for nxt_fwd, d_forward in graph_forward[v_fwd]:
            if nxt_fwd in visited_forward:
                continue
            old_cost_f = cst_fwd.get(nxt_fwd, np.inf)
            new_cost_f = cst_fwd[v_fwd] + d_forward
            if new_cost_f < old_cost_f:
                queue_forward.put((new_cost_f, nxt_fwd))
                cst_fwd[nxt_fwd] = new_cost_f
                parent_forward[nxt_fwd] = v_fwd
            if nxt_fwd in visited_backward:
                if cst_fwd[v_fwd] + d_forward + cst_bwd[nxt_fwd] < shortest_distance:
                    shortest_distance = cst_fwd[v_fwd] + d_forward + cst_bwd[nxt_fwd]

        # backward pass and relaxation
        for nxt_bwd, d_backward in graph_backward[v_bwd]:
            if nxt_bwd in visited_backward:
                continue
            old_cost_b = cst_bwd.get(nxt_bwd, np.inf)
            new_cost_b = cst_bwd[v_bwd] + d_backward
            if new_cost_b < old_cost_b:
                queue_backward.put((new_cost_b, nxt_bwd))
                cst_bwd[nxt_bwd] = new_cost_b
                parent_backward[nxt_bwd] = v_bwd

            if nxt_bwd in visited_forward:
                if cst_bwd[v_bwd] + d_backward + cst_fwd[nxt_bwd] < shortest_distance:
                    shortest_distance = cst_bwd[v_bwd] + d_backward + cst_fwd[nxt_bwd]

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
