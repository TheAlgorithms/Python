import typing


def check_all_edges_marked(
    graph: dict[int, list[int]],
    marked_edges: dict[int, list[int]],
) -> bool:
    """
        >>> check_all_edges_marked(
        ... {0:[1], 1:[0]},
        ... {1:[0], 0:[1]}
        ... )
        True
    """
    for vertex, neighbours in graph.items():
        for neighbour in neighbours:
            if neighbour not in marked_edges[vertex]:
                return False
    return True


def hierholzer(graph: dict[int, list[int]]) -> list[int]:
    """
    Returns an eulerian circuit in a graph if there is one

    >>> hierholzer(
    ...    {0:[1,2], 1:[0,2,3,4],
    ...     2:[0,1,3,4], 3:[1,2,4,5],
    ...     4:[1,2,3,5], 5:[3,4]}
    ... )
    [3, 2, 4, 1, 2, 0, 1, 3, 4, 5, 3]
    """
    current_vertex = next(iter(graph))
    marked_edges = {vertex: [] for vertex in graph.keys()}
    path = [current_vertex]
    while not check_all_edges_marked(graph, marked_edges):
        old_vertex = current_vertex
        # Check if the current vertex has an unmarked edge,
        # if so use this edge to continue the circuit
        for neighbour in graph[current_vertex]:
            if neighbour not in marked_edges[current_vertex]:
                marked_edges[current_vertex].append(neighbour)
                marked_edges[neighbour].append(current_vertex)
                current_vertex = neighbour
                break
        # If the the current vertex has no unmarked edge,
        # find a vertex with an unmarked edge in the path and
        # continue by inserting the new sub-circuit into the current path
        if old_vertex == current_vertex:
            for vertex in path:
                for neighbour in graph[vertex]:
                    if neighbour not in marked_edges[vertex]:
                        path.pop()
                        while path[0] != vertex:
                            path.append(path.pop(0))
                        path.append(vertex)
                        marked_edges[vertex].append(neighbour)
                        marked_edges[neighbour].append(vertex)
                        current_vertex = neighbour
                        break
                if old_vertex != current_vertex:
                    break
        path.append(current_vertex)
    return path


if __name__ == "__main__":
    g1 = {0: [1, 3], 1: [0, 2], 2: [1, 4], 3: [0, 4], 4: [2, 3]}
    print(hierholzer(g1))
