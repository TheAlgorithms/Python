from typing import List, Optional
from .kd_node import KDNode

def build_kdtree(points: List[List[float]], depth: int = 0) -> Optional[KDNode]:
    """
    Builds a KD-Tree from a set of k-dimensional points.

    Args:
        points (List[List[float]]): A list of k-dimensional points (each point is a list of floats).
        depth (int): The current depth in the tree. Used to determine the splitting axis. Defaults to 0.

    Returns:
        Optional[KDNode]: The root of the KD-Tree or None if the input list is empty.
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
        right=build_kdtree(points[median_idx + 1:], depth + 1),
    )
