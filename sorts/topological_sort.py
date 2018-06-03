from __future__ import print_function
#     a
#    / \
#   b  c
#  / \
# d  e
edges = {'a': ['c', 'b'], 'b': ['d', 'e'], 'c': [], 'd': [], 'e': []}
vertices = ['a', 'b', 'c', 'd', 'e']


def topological_sort(start, visited, sort):
    """Perform topolical sort on a directed acyclic graph."""
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


sort = topological_sort('a', [], [])
print(sort)
