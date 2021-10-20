"""
Program to check if a cycle is present in a given graph
"""


def chk_cycle(graph: dict) -> bool:
    """
    Returns True if graph is cyclic else False

    >>> chk_cycle({0:[], 1:[0, 3], 2:[0, 4], 3:[5], 4:[5], 5:[]})
    False
    >>> chk_cycle({0:[1, 2], 1:[2], 2:[0, 3], 3:[3]})
    True
    """
    # Keep track of visited nodes
    visited = set()
    # To detect a back edge, keep track of vertices currently in the recursion stack
    rec_stk = set()
    for node in graph:
        if node not in visited:
            if depth_first_search(graph, node, visited, rec_stk):
                return True
    return False


def depth_first_search(graph: dict, vertex: int, visited: set, rec_stk: set) -> bool:
    # Mark current node as visited and add to recursion stack
    visited.add(vertex)
    rec_stk.add(vertex)

    # Recur for all neighbours
    # If any neighbour is visited and in rec_stk then graph is cyclic
    for node in graph[vertex]:
        if node not in visited:
            if depth_first_search(graph, node, visited, rec_stk):
                return True
        elif node in rec_stk:
            return True

    # The node needs to be removed from recursion stack before function ends
    rec_stk.remove(vertex)
    return False


if __name__ == "__main__":
    from doctest import testmod

    testmod()
