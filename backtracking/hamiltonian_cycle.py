"""
    A Hamiltonian cycle (Hamiltonian circuit) is a graph cycle 
    through a graph that visits each node exactly once.
    Determining whether such paths and cycles exist in graphs 
    is the 'Hamiltonian path problem', which is NP-complete.
    
    Wikipedia: https://en.wikipedia.org/wiki/Hamiltonian_path
"""


def util_hamilton_cycle(graph):
    pass


def hamilton_cycle(graph):
    """
    Wrapper function to call subroutine called util_hamilton_cycle,
    which will either return array of vertices indicating hamiltonian cycle
    or an empty list indicating that hamiltonian cycle was not found.
    Test 1: 
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
    Test 2:
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
    return []