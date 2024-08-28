from typing import Optional, List, Tuple
from .kd_node import KDNode


def nearest_neighbour_search(
    root: Optional[KDNode], query_point: List[float]
) -> Tuple[Optional[List[float]], float, int]:
    """
    Performs a nearest neighbor search in a KD-Tree for a given query point.

    Args:
        root (Optional[KDNode]): The root node of the KD-Tree.
        query_point (List[float]): The point for which the nearest neighbor is being searched.

    Returns:
        Tuple[Optional[List[float]], float, int]:
            - The nearest point found in the KD-Tree to the query point.
            - The squared distance to the nearest point.
            - The number of nodes visited during the search.
    """
    nearest_point: Optional[List[float]] = None
    nearest_dist: float = float("inf")
    nodes_visited: int = 0

    def search(node: Optional[KDNode], depth: int = 0) -> None:
        nonlocal nearest_point, nearest_dist, nodes_visited
        if node is None:
            return

        nodes_visited += 1

        # Calculate the current distance (squared distance)
        current_point = node.point
        current_dist = sum(
            (query_coord - point_coord) ** 2
            for query_coord, point_coord in zip(query_point, current_point)
        )

        # Update nearest point if the current node is closer
        if nearest_point is None or current_dist < nearest_dist:
            nearest_point = current_point
            nearest_dist = current_dist

        # Determine which subtree to search first (based on axis and query point)
        k = len(query_point)  # dimensionality of points
        axis = depth % k

        if query_point[axis] <= current_point[axis]:
            nearer_subtree = node.left
            further_subtree = node.right
        else:
            nearer_subtree = node.right
            further_subtree = node.left

        # Search the nearer subtree first
        search(nearer_subtree, depth + 1)

        # If the further subtree has a closer point
        if (query_point[axis] - current_point[axis]) ** 2 < nearest_dist:
            search(further_subtree, depth + 1)

    search(root, 0)
    return nearest_point, nearest_dist, nodes_visited
