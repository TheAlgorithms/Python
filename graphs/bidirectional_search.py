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
        >>> bidirectional_search(graph, 0, 11)
        [0, 1, 3, 7, 11]
        >>> bidirectional_search(graph, 5, 5)
        [5]
        >>> disconnected_graph = {
        ...     0: [1, 2],
        ...     1: [0],
        ...     2: [0],
        ...     3: [4],
        ...     4: [3],
        ... }
        >>> bidirectional_search(disconnected_graph, 0, 3) is None
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
        if forward_queue:
            current = forward_queue.popleft()
            for neighbor in graph[current]:
                if neighbor not in forward_parents:
                    forward_parents[neighbor] = current
                    forward_queue.append(neighbor)

                    # Check if this creates an intersection
                    if neighbor in backward_parents:
                        intersection = neighbor
                        break

        # If no intersection found, expand backward search
        if intersection is None and backward_queue:
            current = backward_queue.popleft()
            for neighbor in graph[current]:
                if neighbor not in backward_parents:
                    backward_parents[neighbor] = current
                    backward_queue.append(neighbor)

                    # Check if this creates an intersection
                    if neighbor in forward_parents:
                        intersection = neighbor
                        break

    # If no intersection found, there's no path
    if intersection is None:
        return None

    # Construct path from start to intersection
    forward_path: list[int] = []
    current_forward: int | None = intersection
    while current_forward is not None:
        forward_path.append(current_forward)
        current_forward = forward_parents[current_forward]
    forward_path.reverse()

    # Construct path from intersection to goal
    backward_path: list[int] = []
    current_backward: int | None = backward_parents[intersection]
    while current_backward is not None:
        backward_path.append(current_backward)
        current_backward = backward_parents[current_backward]

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
    path = bidirectional_search(example_graph, start, goal)
    print(f"Path from {start} to {goal}: {path}")

    # Test case 2: Start and goal are the same
    start, goal = 5, 5
    path = bidirectional_search(example_graph, start, goal)
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
    path = bidirectional_search(disconnected_graph, start, goal)
    print(f"Path from {start} to {goal}: {path}")


if __name__ == "__main__":
    main()
