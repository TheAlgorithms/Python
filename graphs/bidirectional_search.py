"""
Bidirectional Search Algorithm

A bidirectional search algorithm searches from both the source and the target
simultaneously, meeting somewhere in the middle. This can significantly reduce
the search space and improve performance compared to a single-direction search
in many scenarios.

Time Complexity: O(b^(d/2)) where b is the branching factor and d is the depth
Space Complexity: O(b^(d/2))
"""

from collections import deque
from typing import Dict, List, Optional, Set, Tuple


def bidirectional_search(
    graph: Dict[int, List[int]], start: int, goal: int
) -> Optional[List[int]]:
    """
    Perform bidirectional search on a graph to find the shortest path
    between start and goal nodes.

    Args:
        graph: A dictionary where keys are nodes and values are lists of adjacent nodes
        start: The starting node
        goal: The target node

    Returns:
        A list representing the path from start to goal, or None if no path exists
    """
    if start == goal:
        return [start]

    # Check if start and goal are in the graph
    if start not in graph or goal not in graph:
        return None

    # Initialize forward and backward search queues
    forward_queue = deque([(start, [start])])
    backward_queue = deque([(goal, [goal])])

    # Initialize visited sets for both directions
    forward_visited: Set[int] = {start}
    backward_visited: Set[int] = {goal}

    # Dictionary to store paths
    forward_paths: Dict[int, List[int]] = {start: [start]}
    backward_paths: Dict[int, List[int]] = {goal: [goal]}

    while forward_queue and backward_queue:
        # Expand forward search
        intersection = expand_search(
            graph, forward_queue, forward_visited, forward_paths, backward_visited
        )
        if intersection:
            return construct_path(intersection, forward_paths, backward_paths)

        # Expand backward search
        intersection = expand_search(
            graph, backward_queue, backward_visited, backward_paths, forward_visited
        )
        if intersection:
            return construct_path(intersection, forward_paths, backward_paths)

    # No path found
    return None


def expand_search(
    graph: Dict[int, List[int]],
    queue: deque,
    visited: Set[int],
    paths: Dict[int, List[int]],
    other_visited: Set[int],
) -> Optional[int]:
    """
    Expand the search in one direction and check for intersection.

    Args:
        graph: The graph
        queue: The queue for this direction
        visited: Set of visited nodes for this direction
        paths: Dictionary to store paths for this direction
        other_visited: Set of visited nodes for the other direction

    Returns:
        The intersection node if found, None otherwise
    """
    if not queue:
        return None

    current, path = queue.popleft()

    for neighbor in graph[current]:
        if neighbor not in visited:
            visited.add(neighbor)
            new_path = path + [neighbor]
            paths[neighbor] = new_path
            queue.append((neighbor, new_path))

            # Check if the neighbor is in the other visited set (intersection)
            if neighbor in other_visited:
                return neighbor

    return None


def construct_path(
    intersection: int,
    forward_paths: Dict[int, List[int]],
    backward_paths: Dict[int, List[int]],
) -> List[int]:
    """
    Construct the full path from the intersection point.

    Args:
        intersection: The node where the two searches met
        forward_paths: Paths from start to intersection
        backward_paths: Paths from goal to intersection

    Returns:
        The complete path from start to goal
    """
    # Get the path from start to intersection
    forward_path = forward_paths[intersection]

    # Get the path from goal to intersection and reverse it
    backward_path = backward_paths[intersection]
    backward_path.reverse()

    # Combine the paths (remove the duplicate intersection node)
    return forward_path + backward_path[1:]


def main():
    """
    Example usage and test cases for bidirectional search
    """
    # Example graph represented as an adjacency list
    graph = {
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
    path = bidirectional_search(graph, start, goal)
    print(f"Path from {start} to {goal}: {path}")
    # Expected: Path from 0 to 11: [0, 1, 3, 7, 11] or similar valid shortest path

    # Test case 2: Start and goal are the same
    start, goal = 5, 5
    path = bidirectional_search(graph, start, goal)
    print(f"Path from {start} to {goal}: {path}")
    # Expected: Path from 5 to 5: [5]

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
    # Expected: Path from 0 to 3: None


if __name__ == "__main__":
    main()
