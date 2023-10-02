import heapq
from typing import Dict, Union


def dijkstra(
    graph: Dict[str, Dict[str, int]], start: str
) -> Dict[str, Union[int, float]]:
    """
    Find the shortest path from a starting node to all other nodes in a weighted graph.

    Args:
        graph (dict): Representing the weighted graph in {node: {neighbor: weight}}.
        start (str): The starting node.

    Returns:
        dict: Containing the shortest distance from the start node to all other nodes.
        For unreachable nodes, the distance is set to float('inf').

    Example:
        >>> graph = {
        ...     'A': {'B': 1, 'C': 4},
        ...     'B': {'A': 1, 'C': 2, 'D': 5},
        ...     'C': {'A': 4, 'B': 2, 'D': 1},
        ...     'D': {'B': 5, 'C': 1},
        ... }
        >>> dijkstra(graph, 'A')
        {'A': 0, 'B': 1, 'C': 3, 'D': 4}
    """
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


if __name__ == "__main__":
    import doctest

    result = doctest.testmod()

    if result.failed == 0:
        print("All tests passed!")
    else:
        print(f"{result.failed} test(s) failed.")
