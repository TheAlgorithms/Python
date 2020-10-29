"""
    A Hamiltonian cycle (Hamiltonian circuit) is a graph cycle
    through a graph that visits each node exactly once.
    Determining whether such paths and cycles exist in graphs
    is the 'Hamiltonian path problem', which is NP-complete.

    Wikipedia: https://en.wikipedia.org/wiki/Hamiltonian_path
"""
from __future__ import annotations


def valid_connection(
    graph: list[list[int]], next_ver: int, curr_ind: int, path: list[int]
) -> bool:
    """
    Checks whether it is possible to add next into path by validating 2 statements
    1. There should be path between current and next vertex
    2. Next vertex should not be in path
    If both validations succeeds we return True saying that it is possible to connect
    this vertices either we return False

    Case 1:Use exact graph as in main function, with initialized values
    >>> graph = [[0, 1, 0, 1, 0],
    ...          [1, 0, 1, 1, 1],
    ...          [0, 1, 0, 0, 1],
    ...          [1, 1, 0, 0, 1],
    ...          [0, 1, 1, 1, 0]]
    >>> path = [0, -1, -1, -1, -1, 0]
    >>> curr_ind = 1
    >>> next_ver = 1
    >>> valid_connection(graph, next_ver, curr_ind, path)
    True

    Case 2: Same graph, but trying to connect to node that is already in path
    >>> path = [0, 1, 2, 4, -1, 0]
    >>> curr_ind = 4
    >>> next_ver = 1
    >>> valid_connection(graph, next_ver, curr_ind, path)
    False
    """

    # 1. Validate that path exists between current and next vertices
    if graph[path[curr_ind - 1]][next_ver] == 0:
        return False

    # 2. Validate that next vertex is not already in path
    return not any(vertex == next_ver for vertex in path)


def util_hamilton_cycle(graph: list[list[int]], path: list[int], curr_ind: int) -> bool:
    """
    Pseudo-Code
    Base Case:
    1. Check if we visited all of vertices
        1.1 If last visited vertex has path to starting vertex return True either
            return False
    Recursive Step:
    2. Iterate over each vertex
        Check if next vertex is valid for transiting from current vertex
            2.1 Remember next vertex as next transition
            2.2 Do recursive call and check if going to this vertex solves problem
            2.3 If next vertex leads to solution return True
            2.4 Else backtrack, delete remembered vertex

    Case 1: Use exact graph as in main function, with initialized values
    >>> graph = [[0, 1, 0, 1, 0],
    ...          [1, 0, 1, 1, 1],
    ...          [0, 1, 0, 0, 1],
    ...          [1, 1, 0, 0, 1],
    ...          [0, 1, 1, 1, 0]]
    >>> path = [0, -1, -1, -1, -1, 0]
    >>> curr_ind = 1
    >>> util_hamilton_cycle(graph, path, curr_ind)
    True
    >>> print(path)
    [0, 1, 2, 4, 3, 0]

    Case 2: Use exact graph as in previous case, but in the properties taken from
        middle of calculation
    >>> graph = [[0, 1, 0, 1, 0],
    ...          [1, 0, 1, 1, 1],
    ...          [0, 1, 0, 0, 1],
    ...          [1, 1, 0, 0, 1],
    ...          [0, 1, 1, 1, 0]]
    >>> path = [0, 1, 2, -1, -1, 0]
    >>> curr_ind = 3
    >>> util_hamilton_cycle(graph, path, curr_ind)
    True
    >>> print(path)
    [0, 1, 2, 4, 3, 0]
    """

    # Base Case
    if curr_ind == len(graph):
        # return whether path exists between current and starting vertices
        return graph[path[curr_ind - 1]][path[0]] == 1

    # Recursive Step
    for next in range(0, len(graph)):
        if valid_connection(graph, next, curr_ind, path):
            # Insert current vertex  into path as next transition
            path[curr_ind] = next
            # Validate created path
            if util_hamilton_cycle(graph, path, curr_ind + 1):
                return True
            # Backtrack
            path[curr_ind] = -1
    return False


def hamilton_cycle(graph: list[list[int]], start_index: int = 0) -> list[int]:
    r"""
    Wrapper function to call subroutine called util_hamilton_cycle,
    which will either return array of vertices indicating hamiltonian cycle
    or an empty list indicating that hamiltonian cycle was not found.
    Case 1:
    Following graph consists of 5 edges.
    If we look closely, we can see that there are multiple Hamiltonian cycles.
    For example one result is when we iterate like:
    (0)->(1)->(2)->(4)->(3)->(0)

    (0)---(1)---(2)
     |   /   \   |
     |  /     \  |
     | /       \ |
     |/         \|
    (3)---------(4)
    >>> graph = [[0, 1, 0, 1, 0],
    ...          [1, 0, 1, 1, 1],
    ...          [0, 1, 0, 0, 1],
    ...          [1, 1, 0, 0, 1],
    ...          [0, 1, 1, 1, 0]]
    >>> hamilton_cycle(graph)
    [0, 1, 2, 4, 3, 0]

    Case 2:
    Same Graph as it was in Case 1, changed starting index from default to 3

    (0)---(1)---(2)
     |   /   \   |
     |  /     \  |
     | /       \ |
     |/         \|
    (3)---------(4)
    >>> graph = [[0, 1, 0, 1, 0],
    ...          [1, 0, 1, 1, 1],
    ...          [0, 1, 0, 0, 1],
    ...          [1, 1, 0, 0, 1],
    ...          [0, 1, 1, 1, 0]]
    >>> hamilton_cycle(graph, 3)
    [3, 0, 1, 2, 4, 3]

    Case 3:
    Following Graph is exactly what it was before, but edge 3-4 is removed.
    Result is that there is no Hamiltonian Cycle anymore.

    (0)---(1)---(2)
     |   /   \   |
     |  /     \  |
     | /       \ |
     |/         \|
    (3)         (4)
    >>> graph = [[0, 1, 0, 1, 0],
    ...          [1, 0, 1, 1, 1],
    ...          [0, 1, 0, 0, 1],
    ...          [1, 1, 0, 0, 0],
    ...          [0, 1, 1, 0, 0]]
    >>> hamilton_cycle(graph,4)
    []
    """

    # Initialize path with -1, indicating that we have not visited them yet
    path = [-1] * (len(graph) + 1)
    # initialize start and end of path with starting index
    path[0] = path[-1] = start_index
    # evaluate and if we find answer return path either return empty array
    return path if util_hamilton_cycle(graph, path, 1) else []
