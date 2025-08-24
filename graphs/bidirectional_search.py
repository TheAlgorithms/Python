"""
Bidirectional Search Algorithm.

This algorithm searches from both the source and target nodes simultaneously,
meeting somewhere in the middle. This approach can significantly reduce the
search space compared to a traditional one-directional search.

Time Complexity: O(b^(d/2)) where b is the branching factor and d is the depth
Space Complexity: O(b^(d/2))

https://en.wikipedia.org/wiki/Bidirectional_search
"""

from collections import deque


def expand_search(
    graph: dict[int, list[int]],
    queue: deque[int],
    parents: dict[int, int | None],
    opposite_direction_parents: dict[int, int | None],
) -> int | None:
    if not queue:
        return None

    current = queue.popleft()
    for neighbor in graph[current]:
        if neighbor in parents:
            continue

        parents[neighbor] = current
        queue.append(neighbor)

        # Check if this creates an intersection
        if neighbor in opposite_direction_parents:
            return neighbor

    return None


def construct_path(current: int | None, parents: dict[int, int | None]) -> list[int]:
    path: list[int] = []
    while current is not None:
        path.append(current)
        current = parents[current]
    return path


def bidirectional_search(
    graph: dict[int, list[int]], start: int, goal: int
) -> list[int] | None:
    """
    Perform bidirectional search on a graph to find the shortest path.

    Args:
        graph: A dictionary where keys are nodes and values are lists of adjacent nodes
        start: The starting node
        goal: The target node

    Returns:
        A list representing the path from start to goal, or None if no path exists

    Examples:
        >>> graph = {
        ...     0: [1, 2],
        ...     1: [0, 3, 4],
        ...     2: [0, 5, 6],
        ...     3: [1, 7],
        ...     4: [1, 8],
        ...     5: [2, 9],
        ...     6: [2, 10],
        ...     7: [3, 11],
        ...     8: [4, 11],
        ...     9: [5, 11],
        ...     10: [6, 11],
        ...     11: [7, 8, 9, 10],
        ... }
        >>> bidirectional_search(graph=graph, start=0, goal=11)
        [0, 1, 3, 7, 11]
        >>> bidirectional_search(graph=graph, start=5, goal=5)
        [5]
        >>> disconnected_graph = {
        ...     0: [1, 2],
        ...     1: [0],
        ...     2: [0],
        ...     3: [4],
        ...     4: [3],
        ... }
        >>> bidirectional_search(graph=disconnected_graph, start=0, goal=3) is None
        True
    """
    if start == goal:
        return [start]

    # Check if start and goal are in the graph
    if start not in graph or goal not in graph:
        return None

    # Initialize forward and backward search dictionaries
    # Each maps a node to its parent in the search
    forward_parents: dict[int, int | None] = {start: None}
    backward_parents: dict[int, int | None] = {goal: None}

    # Initialize forward and backward search queues
    forward_queue = deque([start])
    backward_queue = deque([goal])

    # Intersection node (where the two searches meet)
    intersection = None

    # Continue until both queues are empty or an intersection is found
    while forward_queue and backward_queue and intersection is None:
        # Expand forward search
        intersection = expand_search(
            graph=graph,
            queue=forward_queue,
            parents=forward_parents,
            opposite_direction_parents=backward_parents,
        )

        # If no intersection found, expand backward search
        if intersection is not None:
            break

        intersection = expand_search(
            graph=graph,
            queue=backward_queue,
            parents=backward_parents,
            opposite_direction_parents=forward_parents,
        )

    # If no intersection found, there's no path
    if intersection is None:
        return None

    # Construct path from start to intersection
    forward_path: list[int] = construct_path(
        current=intersection, parents=forward_parents
    )
    forward_path.reverse()

    # Construct path from intersection to goal
    backward_path: list[int] = construct_path(
        current=backward_parents[intersection], parents=backward_parents
    )

    # Return the complete path
    return forward_path + backward_path


def main() -> None:
    """
    Run example of bidirectional search algorithm.

    Examples:
        >>> main()  # doctest: +NORMALIZE_WHITESPACE
        Path from 0 to 11: [0, 1, 3, 7, 11]
        Path from 5 to 5: [5]
        Path from 0 to 3: None
    """
    # Example graph represented as an adjacency list
    example_graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5, 6],
        3: [1, 7],
        4: [1, 8],
        5: [2, 9],
        6: [2, 10],
        7: [3, 11],
        8: [4, 11],
        9: [5, 11],
        10: [6, 11],
        11: [7, 8, 9, 10],
    }

    # Test case 1: Path exists
    start, goal = 0, 11
    path = bidirectional_search(graph=example_graph, start=start, goal=goal)
    print(f"Path from {start} to {goal}: {path}")

    # Test case 2: Start and goal are the same
    start, goal = 5, 5
    path = bidirectional_search(graph=example_graph, start=start, goal=goal)
    print(f"Path from {start} to {goal}: {path}")

    # Test case 3: No path exists (disconnected graph)
    disconnected_graph = {
        0: [1, 2],
        1: [0],
        2: [0],
        3: [4],
        4: [3],
    }
    start, goal = 0, 3
    path = bidirectional_search(graph=disconnected_graph, start=start, goal=goal)
    print(f"Path from {start} to {goal}: {path}")


if __name__ == "__main__":
    main()
