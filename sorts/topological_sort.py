"""Topological Sort on Directed Acyclic Graph(DAG)

https://en.wikipedia.org/wiki/Topological_sorting
https://en.wikipedia.org/wiki/Directed_acyclic_graph

Note: topological_sort() sorts a directed acyclic graph so topological_sort(2, 1, 3)
    should fail.
"""

#     a
#    / \
#   b   c
#  / \
# d   e

edges: dict[str, list[str]] = {
    "a": ["c", "b"],
    "b": ["d", "e"],
    "c": [],
    "d": [],
    "e": [],
}

vertices: list[str] = ["a", "b", "c", "d", "e"]


# Perform topological sort on a DAG starting from the specified node
def topological_sort(start: str, visited: list[str], sort: list[str]) -> list[str]:
    """
    Perform topological sort on a directed acyclic graph.

    >>> topological_sort('a', [], [])
    ['c', 'd', 'e', 'b', 'a']

    >>> topological_sort("a", "b", "c")
    Traceback (most recent call last):
        ...
    ValueError: visited must be a list

    >>> topological_sort("a", [], "c")
    Traceback (most recent call last):
        ...
    ValueError: sort must be a list
    """
    if not isinstance(visited, list):
        raise ValueError("visited must be a list")
    if not isinstance(sort, list):
        raise ValueError("sort must be a list")
    current = start
    # Mark the current node as visited
    visited.append(current)
    # List of all neighbors of current node
    neighbors = edges[current]

    # Traverse all neighbors of the current node
    for neighbor in neighbors:
        # Recursively visit each unvisited neighbor
        if neighbor not in visited:
            sort = topological_sort(neighbor, visited, sort)

    # After visiting all neighbors, add the current node to the sorted list
    sort.append(current)

    # If there are some nodes that were not visited (disconnected components)
    if len(visited) != len(vertices):
        for vertex in vertices:
            if vertex not in visited:
                sort = topological_sort(vertex, visited, sort)

    # Return sorted list
    return sort


if __name__ == "__main__":
    # Topological Sorting from node "a" (Returns the order in bottom up approach)
    sort = topological_sort("a", [], [])

    # Reversing the list to get the correct topological order (Top down approach)
    sort.reverse()
    print(sort)
