from queue import PriorityQueue
import numpy as np

"""
Bi-directional Dijkstra's algorithm.

A bi-directional approach is an efficient and less time consuming optimization for Dijkstra's searching algorithm
Link for reference: https://www.homepages.ucl.ac.uk/~ucahmto/math/2020/05/30/bidirectional-dijkstra.html
"""

# Author: Swayam Singh (https://github.com/practice404)

def bidirectional_dij(source, destination, graph_forward, graph_backward) -> int:
    """
    Bi-directional Dijkstra's algorithm.
    Link for reference: https://www.homepages.ucl.ac.uk/~ucahmto/math/2020/05/30/bidirectional-dijkstra.html
    Args:
        source : Source stop id
        destination: destination stop id
        graph_forward: forward flow of graph
        graph_backward: backward flow of graph

    Returns:
        shortest_path_distance (int): length of the shortest path.

    Warnings:
        If the destination is not reachable, function returns -1
    """
    shortest_path_distance = -1

    visited_forward = set()
    visited_backward = set()
    cost_forward = {source: 0}
    cost_backward = {destination: 0}
    parent_forward = {source: None}
    parent_backward = {destination: None}
    queue_forward = PriorityQueue()
    queue_backward = PriorityQueue()

    shortest_distance = np.inf

    queue_forward.put((0, source))
    queue_backward.put((0, destination))

    if source == destination:
        return 0

    while queue_forward and queue_backward:
        while not queue_forward.empty():
            _, vertex_forward = queue_forward.get()

            if vertex_forward not in visited_forward:
                break
        else:
            break
        visited_forward.add(vertex_forward)

        while not queue_backward.empty():
            _, vertex_backward = queue_backward.get()

            if vertex_backward not in visited_backward:
                break
        else:
            break
        visited_backward.add(vertex_backward)

        # forward pass and relaxation
        for next_forward, d_forward in graph_forward[vertex_forward]:
            if next_forward in visited_forward:
                continue
            old_cost_f = cost_forward.get(next_forward, np.inf)
            new_cost_f = cost_forward[vertex_forward] + d_forward
            if new_cost_f < old_cost_f:
                queue_forward.put((new_cost_f, next_forward))
                cost_forward[next_forward] = new_cost_f
                parent_forward[next_forward] = vertex_forward
            if next_forward in visited_backward and cost_forward[vertex_forward] + d_forward + \
                    cost_backward[next_forward] < shortest_distance:
                shortest_distance = cost_forward[vertex_forward] + d_forward + cost_backward[next_forward]

        # backward pass and relaxation
        for next_backward, d_backward in graph_backward[vertex_backward]:
            if next_backward in visited_backward:
                continue
            old_cost_b = cost_backward.get(next_backward, np.inf)
            new_cost_b = cost_backward[vertex_backward] + d_backward
            if new_cost_b < old_cost_b:
                queue_backward.put((new_cost_b, next_backward))
                cost_backward[next_backward] = new_cost_b
                parent_backward[next_backward] = vertex_backward

            if next_backward in visited_forward and cost_backward[vertex_backward] + d_backward + \
                    cost_forward[next_backward] < shortest_distance:
                shortest_distance = cost_backward[vertex_backward] + d_backward + cost_forward[next_backward]

        if cost_forward[vertex_forward] + cost_backward[vertex_backward] >= shortest_distance:
            break

    if shortest_distance == np.inf:
        return shortest_path_distance
    shortest_path_distance = shortest_distance
    return shortest_path_distance


if __name__ == "__main__":
    r"""
    Layout of input Graph:
    E -- 1 --> B -- 1 --> C -- 1 --> D -- 1 --> F
     \                                         /\
      \                                        ||
        -------- 2 ---------> G ------- 1 ------
    """

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
        "G": [["E", 2]]
    }
    print(bidirectional_dij("E", "F", graph_fwd, graph_bwd))
    # E -- 2 --> G -- 1 --> F == 3
