"""
Mean Shift Clustering

A non-parametric, centroid-based clustering algorithm that does not require
specifying the number of clusters in advance. It works by iteratively shifting
each data point toward the mean of points within a given bandwidth (radius),
until convergence.

How it works:
    1. Each point starts as its own candidate centroid.
    2. For each candidate, compute the mean of all points within `bandwidth`
       distance (the "window").
    3. Shift the candidate to that mean.
    4. Repeat until candidates stop moving (convergence).
    5. Merge candidates that are closer than `bandwidth` to each other.
    6. Assign each original point to its nearest final centroid.

Key Properties:
    - No need to specify number of clusters (unlike K-Means)
    - Can find arbitrarily shaped clusters (like DBSCAN)
    - Sensitive to the `bandwidth` parameter
    - Deterministic (no random initialization)

Time Complexity:  O(n² * iterations) with brute-force window search
Space Complexity: O(n)

References:
    - https://en.wikipedia.org/wiki/Mean_shift
    - Comaniciu, D. & Meer, P. "Mean Shift: A Robust Approach Toward
      Feature Space Analysis." IEEE TPAMI, 2002.
      https://doi.org/10.1109/34.1000236
"""


def euclidean_distance(point_a: list[float], point_b: list[float]) -> float:
    """
    Compute the Euclidean distance between two n-dimensional points.

    >>> euclidean_distance([0.0, 0.0], [3.0, 4.0])
    5.0
    >>> euclidean_distance([1.0, 1.0], [1.0, 1.0])
    0.0
    >>> euclidean_distance([0.0], [5.0])
    5.0
    >>> euclidean_distance([0.0, 0.0], [1.0])
    Traceback (most recent call last):
        ...
    ValueError: Both points must have the same number of dimensions.
    """
    if len(point_a) != len(point_b):
        raise ValueError("Both points must have the same number of dimensions.")
    return sum((a - b) ** 2 for a, b in zip(point_a, point_b)) ** 0.5


def get_points_within_bandwidth(
    data: list[list[float]], center: list[float], bandwidth: float
) -> list[list[float]]:
    """
    Return all points in data that lie within `bandwidth` distance of `center`.

    >>> data = [[0.0, 0.0], [0.5, 0.5], [5.0, 5.0]]
    >>> get_points_within_bandwidth(data, [0.0, 0.0], 1.0)
    [[0.0, 0.0], [0.5, 0.5]]
    >>> get_points_within_bandwidth(data, [5.0, 5.0], 1.0)
    [[5.0, 5.0]]
    >>> get_points_within_bandwidth(data, [0.0, 0.0], 10.0)
    [[0.0, 0.0], [0.5, 0.5], [5.0, 5.0]]
    """
    return [point for point in data if euclidean_distance(point, center) <= bandwidth]


def compute_mean(points: list[list[float]]) -> list[float]:
    """
    Compute the element-wise mean of a list of points.

    >>> compute_mean([[1.0, 2.0], [3.0, 4.0]])
    [2.0, 3.0]
    >>> compute_mean([[0.0, 0.0, 0.0]])
    [0.0, 0.0, 0.0]
    >>> compute_mean([])
    Traceback (most recent call last):
        ...
    ValueError: Cannot compute mean of empty list.
    """
    if not points:
        raise ValueError("Cannot compute mean of empty list.")
    n_dims = len(points[0])
    return [sum(point[dim] for point in points) / len(points) for dim in range(n_dims)]


def shift_point(
    point: list[float], data: list[list[float]], bandwidth: float
) -> list[float]:
    """
    Shift a single point to the mean of all data points within `bandwidth`.

    If no points fall within the bandwidth, the point remains unchanged.

    >>> data = [[1.0, 1.0], [1.5, 1.5], [10.0, 10.0]]
    >>> shift_point([1.0, 1.0], data, 2.0)
    [1.25, 1.25]
    >>> shift_point([10.0, 10.0], data, 1.0)
    [10.0, 10.0]
    """
    neighbors = get_points_within_bandwidth(data, point, bandwidth)
    if not neighbors:
        return point
    return compute_mean(neighbors)


def has_converged(
    old_point: list[float], new_point: list[float], tolerance: float
) -> bool:
    """
    Check whether a point has converged (moved less than `tolerance`).

    >>> has_converged([1.0, 1.0], [1.0000001, 1.0000001], 1e-4)
    True
    >>> has_converged([1.0, 1.0], [1.5, 1.5], 1e-4)
    False
    """
    return euclidean_distance(old_point, new_point) < tolerance


def merge_centroids(
    centroids: list[list[float]], bandwidth: float
) -> list[list[float]]:
    """
    Merge centroids that are within `bandwidth` distance of each other.

    Iterates through centroids and greedily merges any that are close enough,
    keeping the first encountered as the representative.

    >>> centroids = [[1.0, 1.0], [1.1, 1.1], [10.0, 10.0]]
    >>> merged = merge_centroids(centroids, 1.0)
    >>> len(merged)
    2
    >>> centroids = [[0.0, 0.0], [5.0, 5.0], [10.0, 10.0]]
    >>> len(merge_centroids(centroids, 1.0))
    3
    """
    merged: list[list[float]] = []
    for centroid in centroids:
        if all(
            euclidean_distance(centroid, existing) >= bandwidth for existing in merged
        ):
            merged.append(centroid)
    return merged


def mean_shift(
    data: list[list[float]],
    bandwidth: float,
    max_iterations: int = 300,
    tolerance: float = 1e-4,
) -> list[int]:
    """
    Perform Mean Shift clustering on a dataset.

    Args:
        data:           List of n-dimensional data points.
        bandwidth:      Radius of the window used to compute the mean.
                        Must be greater than 0.
        max_iterations: Maximum number of shift iterations per point.
                        Must be at least 1.
        tolerance:      Convergence threshold — stop shifting when movement
                        is smaller than this value. Must be greater than 0.

    Returns:
        A list of integer cluster labels, one per input point.
        Cluster IDs start from 0.

    Raises:
        ValueError: If data is empty.
        ValueError: If bandwidth is not positive.
        ValueError: If max_iterations is less than 1.
        ValueError: If tolerance is not positive.

    Example — two well-separated clusters:
    >>> data = [
    ...     [1.0, 1.0], [1.2, 1.0], [1.0, 1.2],
    ...     [9.0, 9.0], [9.2, 9.0], [9.0, 9.2],
    ... ]
    >>> labels = mean_shift(data, bandwidth=2.0)
    >>> len(set(labels))  # two clusters
    2
    >>> labels[0] == labels[1] == labels[2]  # first group same cluster
    True
    >>> labels[3] == labels[4] == labels[5]  # second group same cluster
    True
    >>> labels[0] != labels[3]               # different clusters
    True

    Example — single cluster (all points close together):
    >>> data = [[0.0, 0.0], [0.1, 0.0], [0.0, 0.1], [0.1, 0.1]]
    >>> labels = mean_shift(data, bandwidth=2.0)
    >>> len(set(labels))
    1

    Example — invalid inputs:
    >>> mean_shift([], bandwidth=1.0)
    Traceback (most recent call last):
        ...
    ValueError: Data must not be empty.
    >>> mean_shift([[1.0, 2.0]], bandwidth=0.0)
    Traceback (most recent call last):
        ...
    ValueError: Bandwidth must be greater than 0.
    >>> mean_shift([[1.0, 2.0]], bandwidth=1.0, max_iterations=0)
    Traceback (most recent call last):
        ...
    ValueError: max_iterations must be at least 1.
    >>> mean_shift([[1.0, 2.0]], bandwidth=1.0, tolerance=0.0)
    Traceback (most recent call last):
        ...
    ValueError: Tolerance must be greater than 0.
    """
    if not data:
        raise ValueError("Data must not be empty.")
    if bandwidth <= 0:
        raise ValueError("Bandwidth must be greater than 0.")
    if max_iterations < 1:
        raise ValueError("max_iterations must be at least 1.")
    if tolerance <= 0:
        raise ValueError("Tolerance must be greater than 0.")

    # each point starts as its own candidate centroid
    candidates = [point[:] for point in data]

    for _ in range(max_iterations):
        new_candidates = [
            shift_point(candidate, data, bandwidth) for candidate in candidates
        ]
        if all(
            has_converged(old, new, tolerance)
            for old, new in zip(candidates, new_candidates)
        ):
            break
        candidates = new_candidates

    centroids = merge_centroids(candidates, bandwidth)

    # assign each original point to its nearest centroid
    labels = [
        min(
            range(len(centroids)),
            key=lambda centroid_index: euclidean_distance(
                point, centroids[centroid_index]
            ),
        )
        for point in data
    ]

    return labels


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
