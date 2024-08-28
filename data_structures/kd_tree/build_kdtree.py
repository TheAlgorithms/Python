from .kd_node import KDNode

def build_kdtree(points, depth=0):
    if not points:
        return None

    k = len(points[0])  # dimensionality of the points
    axis = depth % k

    # Sort point list and choose median as pivot element
    points.sort(key=lambda x: x[axis])
    median_idx = len(points) // 2

    # Create node and construct subtrees
    return KDNode(
        point = points[median_idx],
        left = build_kdtree(points[:median_idx], depth + 1),
        right = build_kdtree(points[median_idx + 1:], depth + 1)
    )
