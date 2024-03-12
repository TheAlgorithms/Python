"""Breadth-first search shortest path implementations.
doctest:
python -m doctest -v bfs_shortest_path.py
Manual test:
python bfs_shortest_path.py
"""

demo_graph = {
    "A": ["B", "C", "E"],
    "B": ["A", "D", "E"],
    "C": ["A", "F", "G"],
    "D": ["B"],
    "E": ["A", "B", "D"],
    "F": ["C"],
    "G": ["C"],
}


def bfs_shortest_path(graph: dict, start, goal) -> list[str]:
    """Find shortest path between `start` and `goal` nodes.
    Args:
        graph (dict): node/list of neighboring nodes key/value pairs.
        start: start node.
        goal: target node.
    Returns:
        Shortest path between `start` and `goal` nodes as a string of nodes.
        'Not found' string if no path found.
    Example:
        >>> bfs_shortest_path(demo_graph, "G", "D")
        ['G', 'C', 'A', 'B', 'D']
        >>> bfs_shortest_path(demo_graph, "G", "G")
        ['G']
        >>> bfs_shortest_path(demo_graph, "G", "Unknown")
        []
    """
    # keep track of explored nodes
    explored = set()
    # keep track of all the paths to be checked
    queue = [[start]]

    # return path if start is goal
    if start == goal:
        return [start]

    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path

            # mark node as explored
            explored.add(node)

    # in case there's no path between the 2 nodes
    return []


def bfs_shortest_path_distance(graph: dict, start, target) -> int:
    """Find shortest path distance between `start` and `target` nodes.
    Args:
        graph: node/list of neighboring nodes key/value pairs.
        start: node to start search from.
        target: node to search for.
    Returns:
        Number of edges in shortest path between `start` and `target` nodes.
        -1 if no path exists.
    Example:
        >>> bfs_shortest_path_distance(demo_graph, "G", "D")
        4
        >>> bfs_shortest_path_distance(demo_graph, "A", "A")
        0
        >>> bfs_shortest_path_distance(demo_graph, "A", "Unknown")
        -1
    """
    if not graph or start not in graph or target not in graph:
        return -1
    if start == target:
        return 0
    queue = [start]
    visited = set(start)
    # Keep tab on distances from `start` node.
    dist = {start: 0, target: -1}
    while queue:
        node = queue.pop(0)
        if node == target:
            dist[target] = (
                dist[node] if dist[target] == -1 else min(dist[target], dist[node])
            )
        for adjacent in graph[node]:
            if adjacent not in visited:
                visited.add(adjacent)
                queue.append(adjacent)
                dist[adjacent] = dist[node] + 1
    return dist[target]


if __name__ == "__main__":
    print(bfs_shortest_path(demo_graph, "G", "D"))  # returns ['G', 'C', 'A', 'B', 'D']
    print(bfs_shortest_path_distance(demo_graph, "G", "D"))  # returns 4
