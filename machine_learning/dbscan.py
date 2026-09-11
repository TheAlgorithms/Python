"""
DBSCAN (Density-Based Spatial Clustering of Applications with Noise)

A density-based clustering algorithm that groups together points that are
closely packed together, while marking points in low-density regions as outliers.

Unlike K-Means, DBSCAN:
- Does NOT require specifying the number of clusters in advance
- Can find clusters of arbitrary shapes
- Is robust to outliers (labels them as noise, cluster id = -1)

Key Parameters:
    epsilon (eps): The maximum distance between two points to be considered neighbors
    min_points: Minimum number of points to form a dense region (core point)

Point Types:
    - Core point:    Has at least `min_points` neighbors within `epsilon` distance
    - Border point:  Within `epsilon` of a core point, but has fewer than
                     `min_points` neighbors
    - Noise point:   Neither core nor border — labeled as -1

Time Complexity:  O(n²) with brute-force neighbor search
Space Complexity: O(n)

References:
    - https://en.wikipedia.org/wiki/DBSCAN
    - Ester, M., et al. "A density-based algorithm for discovering clusters."
      KDD 1996. https://dl.acm.org/doi/10.5555/3001460.3001507
"""


def euclidean_distance(point_a: list[float], point_b: list[float]) -> float:
    """
    Compute the Euclidean distance between two points in n-dimensional space.

    >>> euclidean_distance([0.0, 0.0], [3.0, 4.0])
    5.0
    >>> euclidean_distance([1.0, 2.0, 3.0], [1.0, 2.0, 3.0])
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


def get_neighbors(
    data: list[list[float]], point_index: int, epsilon: float
) -> list[int]:
    """
    Return indices of all points within epsilon distance of data[point_index].

    >>> data = [[0.0, 0.0], [0.1, 0.1], [5.0, 5.0]]
    >>> get_neighbors(data, 0, 0.5)
    [0, 1]
    >>> get_neighbors(data, 2, 0.5)
    [2]
    >>> get_neighbors(data, 0, 10.0)
    [0, 1, 2]
    """
    return [
        index
        for index, point in enumerate(data)
        if euclidean_distance(data[point_index], point) <= epsilon
    ]


def dbscan(
    data: list[list[float]],
    epsilon: float,
    min_points: int,
) -> list[int]:
    """
    Perform DBSCAN clustering on a dataset.

    Args:
        data:       List of n-dimensional data points, e.g. [[x1,y1], [x2,y2], ...]
        epsilon:    Maximum distance between two points to be considered neighbors.
                    Must be greater than 0.
        min_points: Minimum number of neighbors (including self) to be a core point.
                    Must be at least 1.

    Returns:
        A list of integer cluster labels, one per input point.
        Noise points are labeled -1.
        Cluster IDs start from 0.

    Raises:
        ValueError: If data is empty.
        ValueError: If epsilon is not positive.
        ValueError: If min_points is less than 1.

    Example — two well-separated clusters:
    >>> data = [
    ...     [1.0, 1.0], [1.1, 1.0], [1.0, 1.1],
    ...     [9.0, 9.0], [9.1, 9.0], [9.0, 9.1],
    ... ]
    >>> labels = dbscan(data, epsilon=0.5, min_points=2)
    >>> len(set(labels))  # two clusters
    2
    >>> labels[0] == labels[1] == labels[2]  # first three in same cluster
    True
    >>> labels[3] == labels[4] == labels[5]  # last three in same cluster
    True
    >>> labels[0] != labels[3]               # different clusters
    True

    Example — isolated noise point:
    >>> data = [[0.0, 0.0], [0.1, 0.0], [0.0, 0.1], [99.0, 99.0]]
    >>> labels = dbscan(data, epsilon=0.5, min_points=2)
    >>> labels[3]  # noise
    -1
    >>> labels[0] == labels[1] == labels[2]  # one cluster
    True

    Example — all points are noise (min_points too high):
    >>> data = [[0.0, 0.0], [5.0, 5.0]]
    >>> dbscan(data, epsilon=0.3, min_points=5)
    [-1, -1]

    Example — single cluster (all points close together):
    >>> data = [[0.0, 0.0], [0.1, 0.0], [0.0, 0.1], [0.1, 0.1]]
    >>> labels = dbscan(data, epsilon=0.5, min_points=2)
    >>> len(set(labels))
    1
    >>> -1 not in labels
    True

    Example — invalid inputs:
    >>> dbscan([], epsilon=0.5, min_points=2)
    Traceback (most recent call last):
        ...
    ValueError: Data must not be empty.
    >>> dbscan([[1.0, 2.0]], epsilon=0.0, min_points=2)
    Traceback (most recent call last):
        ...
    ValueError: Epsilon must be greater than 0.
    >>> dbscan([[1.0, 2.0]], epsilon=0.5, min_points=0)
    Traceback (most recent call last):
        ...
    ValueError: min_points must be at least 1.
    """
    if not data:
        raise ValueError("Data must not be empty.")
    if epsilon <= 0:
        raise ValueError("Epsilon must be greater than 0.")
    if min_points < 1:
        raise ValueError("min_points must be at least 1.")

    labels = [-1] * len(data)  # all points start as noise
    current_cluster_id = 0

    for point_index in range(len(data)):
        if labels[point_index] != -1:
            continue  # already assigned

        neighbors = get_neighbors(data, point_index, epsilon)

        if len(neighbors) < min_points:
            continue  # not a core point — remains noise for now

        # point_index is a core point — start a new cluster
        labels[point_index] = current_cluster_id
        seeds = [n for n in neighbors if n != point_index]

        while seeds:
            current_point = seeds.pop()

            # skip points already claimed by a different cluster
            if (
                labels[current_point] != -1
                and labels[current_point] != current_cluster_id
            ):
                continue

            # assign noise points and unvisited points to this cluster
            labels[current_point] = current_cluster_id
            current_neighbors = get_neighbors(data, current_point, epsilon)

            if len(current_neighbors) >= min_points:
                # current_point is also a core point — expand cluster
                for neighbor in current_neighbors:
                    if labels[neighbor] == -1:
                        seeds.append(neighbor)

        current_cluster_id += 1

    return labels


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
