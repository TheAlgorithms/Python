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
        # pop from forward queue
        v_fwd = add_visited(queue_forward, visited_forward)
        if v_fwd is None:
            break
        
        # pop from backward queue
        v_bwd = add_visited(queue_backward, visited_backward)
        if v_bwd is None:
            break
        
        # forward pass and relaxation
        shortest_distance = forward_pass(graph_forward, v_fwd, queue_forward, visited_forward, visited_backward, parent_forward, cst_fwd, cst_bwd, shortest_distance)
        
        # backward pass and relaxation
        shortest_distance = backward_pass(graph_backward, v_bwd, queue_backward, visited_forward, visited_backward, parent_backward, cst_bwd, cst_bwd, shortest_distance)

        if cst_fwd[v_fwd] + cst_bwd[v_bwd] >= shortest_distance:
            break

    if shortest_distance != np.inf:
        shortest_path_distance = shortest_distance
    return shortest_path_distance

def add_visited(queue, visited) -> int:
    """
    pop a node from the queue and add it to visited nodes
    
    Args:
        queue (PriorityQueue): priority queue of forward/backward search
        visited (set): visited set of nodes of forward/backward search

    Returns:
        int: popped node
    """
    while not queue.empty():
        _, v_fwd = queue.get()

        if v_fwd not in visited:
            break
    else:
        return None
    visited.add(v_fwd)
    return v_fwd

def forward_pass(graph_forward, v_fwd, queue_forward, visited_forward, visited_backward, parent_forward, cst_fwd, cst_bwd, shortest_distance):
    """
    Forward pass and relaxation.

    Args:
        graph_forward (dict): graph structure used for forward pass
        v_fwd (int): popped node from forward queue
        queue_forward (PriorityQueue): forward queue
        visited_forward (set): visited nodes during forward pass
        visited_backward (set): visited nodes during backward pass
        parent_forward (dict): dict of node and its predecessor for forward pass
        cst_fwd (dict): dict of node and shortest distance for forward pass
        cst_bwd (dict): dict of node and shortest distance for backward pass
        shortest_distance (float): current shortest distance

    Returns:
        float: updated shortest distance
    """
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
    return shortest_distance

def backward_pass(graph_backward, v_bwd, queue_backward, visited_forward, visited_backward, parent_backward, cst_fwd, cst_bwd, shortest_distance):
    """
    Backward pass and relaxation.

    Args:
        graph_backward (dict): graph structure used for backward pass
        v_bwd (int): popped node from backward queue
        queue_backward (PriorityQueue): backward queue
        visited_forward (set): visited nodes during forward pass
        visited_backward (set): visited nodes during backward pass
        parent_backward (dict): dict of node and its predecessor for backward pass
        cst_fwd (dict): dict of node and shortest distance for forward pass
        cst_bwd (dict): dict of node and shortest distance for backward pass
        shortest_distance (float): current shortest distance

    Returns:
        float: updated shortest distance
    """
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
    return shortest_distance


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
