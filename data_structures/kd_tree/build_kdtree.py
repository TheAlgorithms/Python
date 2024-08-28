from typing import Optional
from .kd_node import KDNode


def build_kdtree(points: list[list[float]], depth: int = 0) -> Optional[KDNode]:
    """
    Builds a KD-Tree from a list of points.

    Args:
        points (list[list[float]]): The list of points to build the KD-Tree from.
        depth (int): The current depth in the tree (used to determine axis for splitting).

    Returns:
        Optional[KDNode]: The root node of the KD-Tree.
    """
    if not points:
        return None

    k = len(points[0])  # Dimensionality of the points
    axis = depth % k

    # Sort point list and choose median as pivot element
    points.sort(key=lambda point: point[axis])
    median_idx = len(points) // 2

    # Create node and construct subtrees
    return KDNode(
        point=points[median_idx],
        left=build_kdtree(points[:median_idx], depth + 1),
        right=build_kdtree(points[median_idx + 1 :], depth + 1),
    )
