"""Topological Sort."""

#     a
#    / \
#   b  c
#  / \
# d  e
edges = {"a": ["c", "b"], "b": ["d", "e"], "c": [], "d": [], "e": []}
vertices = ["a", "b", "c", "d", "e"]

# sort stores the topological sort of graph
sort = []
# visited dictionary keep tracks of which nodes of graph are visited
visited = {}


def topological_sort(start: str, visited: list, sort: list) -> list:
    """Perform topological sort on a directed acyclic graph."""
    current = start
    # add current to visited
    visited[current] = 1
    neighbors = edges[current]
    for neighbor in neighbors:
        # if neighbor not in visited, visit
        if visited[neighbor] == 0:
            sort = topological_sort(neighbor, visited, sort)
    # if all neighbors visited add current to sort
    sort.append(current)
    # return sort
    return sort


if __name__ == "__main__":
    # Adding vertices to visited and mark them as 0
    # 0 value indicates that vertex is unvisited
    # 1 value indicates that vertex is visited
    for vertex in vertices:
        visited.update({vertex: 0})

    for vertex in visited:
        if visited[vertex] == 0:
            sort = topological_sort(vertex, visited, sort)

    # reverse the sort
    sort = sort[::-1]
    print(sort)
