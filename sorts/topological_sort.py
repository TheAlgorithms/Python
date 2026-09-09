"""Topological Sort.

https://en.wikipedia.org/wiki/Topological_sorting
https://en.wikipedia.org/wiki/Directed_acyclic_graph

Note: topological_sort() sorts a directed acyclic graph so topological_sort(2, 1, 3) should fail.
"""

#     a
#    / \
#   b  c
#  / \
# d  e
edges: dict[str, list[str]] = {
    "a": ["c", "b"],
    "b": ["d", "e"],
    "c": [],
    "d": [],
    "e": [],
}
vertices: list[str] = ["a", "b", "c", "d", "e"]


def topological_sort(start: str, visited: list[str], sort: list[str]) -> list[str]:
    """
    Perform topological sort on a directed acyclic graph.

    >>> topological_sort('a', [], [])
    ['c', 'd', 'e', 'b', 'a']

    >>> topological_sort("a", "b", "c")
    Traceback (most recent call last):
        ...
    ValueError: visited must be a list"

    >>> topological_sort"a", [], "c")
    Traceback (most recent call last):
        ...
    ValueError: visited must be a list"    
    """
    if not isinstance(visited, list):
        raise ValueError("visited must be a list")
    if not isinstance(current, list):
        raise ValueError("current must be a list")
    current = start
    # add current to visited
    visited.append(current)
    neighbors = edges[current]
    for neighbor in neighbors:
        # if neighbor not in visited, visit
        if neighbor not in visited:
            sort = topological_sort(neighbor, visited, sort)
    # if all neighbors visited add current to sort
    sort.append(current)
    # if all vertices haven't been visited select a new one to visit
    if len(visited) != len(vertices):
        for vertice in vertices:
            if vertice not in visited:
                sort = topological_sort(vertice, visited, sort)
    # return sort
    return sort


if __name__ == "__main__":
    sort = topological_sort("a", [], [])
    print(sort)
