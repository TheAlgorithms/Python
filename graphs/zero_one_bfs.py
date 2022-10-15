"""
We all know that Breadth First Search works for unweighted graphs.
However, it doesn't work for Weighted Graphs. Sometimes all we need
is a 0 or 1 weight on all edges, rather than any given number.

In such cases we can use this simple 0-1 BFS (Zero One Breadth First Search)
as it is much simpler than the usual algorithm for such kind of a problem, a dijkstra.

Requirement:
Each edge of the graph must be either ZERO or ONE

Refer this link: https://cp-algorithms.com/graph/01_bfs.html for more details
"""

import collections
import math


def zero_one_bfs(graph: dict, number_of_nodes: int, start: int, goal: int) -> None:
    """
    Shortest weighted path for a ZERO - ONE weighted graph

    The graph (dict) must have all keys from 0 to number_of_nodes - 1
    The values of each key must be a list of lists of length 2,
            the first element being the next node and
            the second elements being the weight of the edge connecting them

    This function implements the zero_one_bfs. Programmers can just add print
    statements or modify the data_types as per the applications of this.

    """

    # d[i] is the distance from the node 'start' to the node i
    distance_from_start = [math.inf for i in range(number_of_nodes)]

    # The distance of a node from itself is ZERO
    distance_from_start[start] = 0

    queuee: collections.deque = collections.deque([])

    queuee.appendleft(start)

    while len(queuee) != 0:
        node_to_check = queuee[0]
        queuee.popleft()
        for edge in graph[node_to_check]:
            next_node = edge[0]
            weight_of_node = edge[1]
            if (
                distance_from_start[node_to_check] + weight_of_node
                < distance_from_start[next_node]
            ):
                distance_from_start[next_node] = (
                    distance_from_start[node_to_check] + weight_of_node
                )
                if weight_of_node == 1:
                    queuee.append(next_node)
                else:
                    queuee.appendleft(next_node)


def main() -> None:
    print("This function implements the zero_one_bfs.")
    print("Programmers can just add print statements or ", end="")
    print("modify the data_types as per the applications of this.")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
