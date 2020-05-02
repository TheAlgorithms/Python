"""
    A Hamiltonian cycle (Hamiltonian circuit) is a graph cycle 
    through a graph that visits each node exactly once.
    Determining whether such paths and cycles exist in graphs 
    is the 'Hamiltonian path problem', which is NP-complete.
    
    Wikipedia: https://en.wikipedia.org/wiki/Hamiltonian_path
"""


def valid_connection(graph, next_vertex, curr_vertex, path):
    """
    Checks whether it is possible to add next_vertex into path by validating 2 statements
    1. There should be path between current and next vertex
    2. Next vertex should not be in path
    If both validations succeeds we return true saying that it is possible to connect this vertices
    either we return false    
    """

    # 1. Validate that path exists between current and next vertices
    if graph[path[curr_vertex - 1]][next_vertex] == 0:
        return False

    # 2. Validate that next vertex is not already in path
    return not any(vertex == next_vertex for vertex in path)


def util_hamilton_cycle(graph, path, curr_vertex):
    """
    Pseudo-Code
    Base Case:
    1. Chceck if we visited all of vertices
        1.1 If last visited vertex has path to starting vertex return True either return False
    Recursive Step:
    2. Iterate over each vertex
        Check if next vertex is valid for transiting from current vertex
            2.1 Remember next vertex as next transition 
            2.2 Do recursive call and check if going to this vertex solves problem
            2.3 if next vertex leads to solution return True
            2.4 else backtrack, delete remembered vertex
            
    Case 1: Use exact graph as in main function, with initialized values
    >>> graph = [[0, 1, 0, 1, 0],
    ...          [1, 0, 1, 1, 1],
    ...          [0, 1, 0, 0, 1],
    ...          [1, 1, 0, 0, 1],
    ...          [0, 1, 1, 1, 0]]
    >>> path = [0, -1, -1, -1, -1, 0]
    >>> curr_vertex = 1
    >>> util_hamilton_cycle(graph, path, curr_vertex)
    True
    >>> print(path)
    [0, 1, 2, 4, 3, 0]
    Case 2: Use exact graph as in previous case, but in the properties taken from middle of calculation
    >>> graph = [[0, 1, 0, 1, 0],
    ...          [1, 0, 1, 1, 1],
    ...          [0, 1, 0, 0, 1],
    ...          [1, 1, 0, 0, 1],
    ...          [0, 1, 1, 1, 0]]
    >>> path = [0, 1, 2, -1, -1, 0]
    >>> curr_vertex = 3
    >>> util_hamilton_cycle(graph, path, curr_vertex)
    True
    >>> print(path)
    [0, 1, 2, 4, 3, 0]
    """

    # Base Case
    if curr_vertex == len(graph):
        # return whether path exists between current and starting vertices
        return graph[path[curr_vertex - 1]][0] == 1

    # Recursive Step
    for next_vertex in range(len(graph)):
        if valid_connection(graph, next_vertex, curr_vertex, path):
            # Insert current vertex  into path as next transition
            path[curr_vertex] = next_vertex
            # Validate created path
            if util_hamilton_cycle(graph, path, curr_vertex + 1):
                return True
            # Backtrack
            path[curr_vertex] = -1
    return False


def hamilton_cycle(graph):
    """
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
    >>> hamilton_cycle(graph)
    []
    """

    # Initialize path with -1, indicating that we have not visited them yet
    path = [-1] * (len(graph) + 1)
    # initialize start and end of path with starting index
    path[0] = path[-1] = 0
    # evaluate and if we find answer return path either return empty array
    if util_hamilton_cycle(graph, path, 1):
        return path
    return []