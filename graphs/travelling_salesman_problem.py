"""
Author:- Sanjay Muthu <https://github.com/XenoBytesX>

The Problem:
    In the travelling salesman problem you have to find the path
    in which a salesman can start from a source node and visit all the other nodes
    ONCE and return to the source node in the shortest possible way

Complexity:
    There are n! permutations of all the nodes in the graph and
    for each permutation we have to go through all the nodes
    which will take O(n) time per permutation.
    So the total time complexity will be O(n * n!).

    Time Complexity:- O(n * n!)

    It takes O(n) space to store the list of nodes.

    Space Complexity:- O(n)

Wiki page:- <https://en.wikipedia.org/wiki/Travelling_salesman_problem>
"""

from itertools import permutations


def floyd_warshall(graph, v):
    dist = graph
    for k in range(v):
        for i in range(v):
            for j in range(v):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


def travelling_salesman_problem(graph, v):
    """
    Returns the shortest path that a salesman can take to visit all the nodes
    in the graph and return to the source node

    The graph in the below testcase looks something like this:-
                                    2
                        _________________________
                        |                       |
              2         ^                 6     ^
    (0) <------------> (1)          (2)<------>(3)
     ^                               ^
     |              3                |
     |_______________________________|

    >>> graph = []
    >>> graph.append([0, 2, 3, float('inf')])
    >>> graph.append([2, 0, float('inf'), 2])
    >>> graph.append([3, float('inf'), 0, 6])
    >>> graph.append([float('inf'), 2, 6, 0])
    >>> travelling_salesman_problem(graph, 4)
    13
    """

    # See graphs_floyd_warshall.py for implementation
    shortest_distance_matrix = floyd_warshall(graph, v)
    nodes = list(range(v))

    min_distance = float("inf")

    # Go through all the permutations of the nodes to find out
    # which of the order of nodes lead to the shortest distance
    # Permutations(nodes) returns a list of all permutations of the list
    # Permutations are all the possible ways to arrange the elements of the list
    for permutation in permutations(nodes):
        current_dist = 0
        current_node = 0

        # Find the distance of the current permutation by going through all the nodes
        # in order and add the distance between the nodes to the current_dist
        for node in permutation:
            current_dist += shortest_distance_matrix[current_node][node]
            current_node = node

        # Add the distance to come back to the source node
        current_dist += shortest_distance_matrix[current_node][0]

        # If the current distance is less than the minimum distance found so far,
        # update the minimum distance
        # print(permutation, current_dist)
        min_distance = min(min_distance, current_dist)

    # NOTE: We are assuming 0 is the source node here.

    return min_distance


if __name__ == "__main__":
    import doctest

    doctest.testmod()
