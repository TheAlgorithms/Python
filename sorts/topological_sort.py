"""Topological Sort on Directed Acyclic Graph(DAG)"""

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
        for vertice in vertices:
            if vertice not in visited:
                sort = topological_sort(vertice, visited, sort)

    # Return sorted list
    return sort


if __name__ == "__main__":
    # Topological Sorting from node "a" (Returns the order in bottom up approach)
    sort = topological_sort("a", [], [])

    # Reversing the list to get the correct topological order (Top down approach)
    sort.reverse()

    print(sort)
