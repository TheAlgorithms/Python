from typing import Dict, Any
import heapq

def prim_mst(graph: Dict[Any, Dict[Any, int]]) -> Dict[Any, Any]:
    """
    Generate the Minimum Spanning Tree (MST) using Prim's algorithm.

    Args:
        graph (Dict[Any, Dict[Any, int]]): Adjacency dictionary of the graph where keys are nodes and
                                           values are dictionaries of neighbor nodes with edge weights.

    Returns:
        Dict[Any, Any]: A dictionary representing the MST with each node pointing to its parent in the MST.

    Example:
    >>> graph = {
    ...     'A': {'B': 2, 'C': 3},
    ...     'B': {'A': 2, 'C': 1},
    ...     'C': {'A': 3, 'B': 1}
    ... }
    >>> prim_mst(graph)
    {'A': 'B', 'B': 'C', 'C': 'B'}
    """
    if not graph:
        return {}

    start_node = next(iter(graph))
    visited = set([start_node])
    edges = [(weight, start_node, to) for to, weight in graph[start_node].items()]
    heapq.heapify(edges)
    mst = {}

    while edges:
        weight, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst[to] = frm
            for next_to, next_weight in graph[to].items():
                if next_to not in visited:
                    heapq.heappush(edges, (next_weight, to, next_to))

    return mst

if __name__ == "__main__":
    import doctest
    doctest.testmod()
