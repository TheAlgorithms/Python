#  Created by: Ramy-Badr-Ahmed (https://github.com/Ramy-Badr-Ahmed)
#  in Pull Request: #11532
#  https://github.com/TheAlgorithms/Python/pull/11532
#
#  Please mention me (@Ramy-Badr-Ahmed) in any issue or pull request
#  addressing bugs/corrections to this file.
#  Thank you!

from data_structures.kd_tree.kd_node import KDNode


def build_kdtree(points: list[list[float]], depth: int = 0) -> KDNode | None:
    """
    Builds a KD-Tree from a list of points.

    Args:
        points: The list of points to build the KD-Tree from.
        depth: The current depth in the tree
                     (used to determine axis for splitting).

    Returns:
        The root node of the KD-Tree,
                       or None if no points are provided.
    """
    if not points:
        return None

    k = len(points[0])  # Dimensionality of the points
    axis = depth % k

    # Sort point list and choose median as pivot element
    points.sort(key=lambda point: point[axis])
    median_idx = len(points) // 2

    # Create node and construct subtrees
    left_points = points[:median_idx]
    right_points = points[median_idx + 1 :]

    return KDNode(
        point=points[median_idx],
        left=build_kdtree(left_points, depth + 1),
        right=build_kdtree(right_points, depth + 1),
    )
