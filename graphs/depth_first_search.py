"""The DFS function simply calls itself recursively for every unvisited child of
its argument. We can emulate that behaviour precisely using a stack of iterators.
Instead of recursively calling with a node, we'll push an iterator to the node's
children onto the iterator stack. When the iterator at the top of the stack
terminates, we'll pop it off the stack.

Pseudocode:
    all nodes initially unexplored
    mark s as explored
    for every edge (s, v):
        if v unexplored:
            DFS(G, v)
"""

from typing import Set, Dict


def depth_first_search(graph: Dict, start: str) -> Set[int]:
    """Depth First Search on Graph

       :param graph: directed graph in dictionary format
       :param vertex: starting vectex as a string
       :returns: the trace of the search
       >>> G = { "A": ["B", "C", "D"], "B": ["A", "D", "E"],
       ... "C": ["A", "F"], "D": ["B", "D"], "E": ["B", "F"],
       ... "F": ["C", "E", "G"], "G": ["F"] }
       >>> start = "A"
       >>> output_G = list({'A', 'B', 'C', 'D', 'E', 'F', 'G'})
       >>> all(x in output_G for x in list(depth_first_search(G, "A")))
       True
       >>> all(x in output_G for x in list(depth_first_search(G, "G")))
       True
    """
    explored, stack = set(start), [start]
    while stack:
        v = stack.pop()
        # one difference from BFS is to pop last element here instead of first one
        for w in graph[v]:
            if w not in explored:
                explored.add(w)
                stack.append(w)
    return explored


G = {
    "A": ["B", "C", "D"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B", "D"],
    "E": ["B", "F"],
    "F": ["C", "E", "G"],
    "G": ["F"],
}

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(depth_first_search(G, "A"))
