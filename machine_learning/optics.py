"""
OPTICS (Ordering Points To Identify the Clustering Structure).

OPTICS is a density-based clustering algorithm that creates an ordering
of data points and calculates their reachability distances. Unlike DBSCAN,
it can help identify clusters with different density levels.

Reference:
    https://en.wikipedia.org/wiki/OPTICS_algorithm
"""

from heapq import heappop, heappush
from math import dist, inf, isfinite, isnan

point_type = list[float]


def _calculate_core_distances(
    data: list[point_type],
    min_samples: int,
    max_eps: float,
) -> list[float]:
    """
    Calculate the core distance for every point.

    >>> _calculate_core_distances([[0.0], [1.0], [5.0]], 2, 2.0)
    [1.0, 1.0, inf]
    """
    core_distances = [inf] * len(data)

    for index, point in enumerate(data):
        distances = [
            dist(point, other) for other in data if dist(point, other) <= max_eps
        ]

        if len(distances) >= min_samples:
            core_distances[index] = sorted(distances)[min_samples - 1]

    return core_distances


def _get_neighbors(
    data: list[point_type],
    point_index: int,
    max_eps: float,
) -> list[int]:
    """
    Return indices of points within max_eps.

    >>> _get_neighbors([[0.0], [1.0], [5.0]], 0, 1.0)
    [0, 1]
    """
    return [
        index
        for index, point in enumerate(data)
        if dist(data[point_index], point) <= max_eps
    ]


def _update_seeds(
    data: list[point_type],
    point_index: int,
    core_distances: list[float],
    reachability: list[float],
    processed: list[bool],
    max_eps: float,
    seeds: list[tuple[float, int]],
) -> None:
    """
    Update the priority queue with improved reachability distances.

    >>> data = [[0.0], [1.0], [5.0]]
    >>> core = [1.0, 1.0, inf]
    >>> reachability = [inf, inf, inf]
    >>> processed = [True, False, False]
    >>> seeds = []
    >>> _update_seeds(data, 0, core, reachability, processed, 2.0, seeds)
    >>> seeds
    [(1.0, 1)]
    >>> reachability
    [inf, 1.0, inf]
    """
    core_distance = core_distances[point_index]

    for neighbor in _get_neighbors(data, point_index, max_eps):
        if processed[neighbor]:
            continue

        new_distance = max(
            core_distance,
            dist(data[point_index], data[neighbor]),
        )

        if new_distance < reachability[neighbor]:
            reachability[neighbor] = new_distance
            heappush(seeds, (new_distance, neighbor))


def _expand_cluster_order(
    data: list[point_type],
    point_index: int,
    core_distances: list[float],
    reachability: list[float],
    processed: list[bool],
    ordering: list[int],
    max_eps: float,
) -> None:
    """
    Expand the ordering from a core point.

    >>> data = [[0.0], [1.0], [5.0]]
    >>> core = [1.0, 1.0, inf]
    >>> reachability = [inf, inf, inf]
    >>> processed = [True, False, False]
    >>> ordering = [0]
    >>> _expand_cluster_order(data, 0, core, reachability, processed, ordering, 2.0)
    >>> ordering
    [0, 1]
    >>> reachability
    [inf, 1.0, inf]
    """
    if core_distances[point_index] == inf:
        return

    seeds = []

    _update_seeds(
        data,
        point_index,
        core_distances,
        reachability,
        processed,
        max_eps,
        seeds,
    )

    while seeds:
        candidate_distance, current_index = heappop(seeds)

        if processed[current_index]:
            continue

        if candidate_distance != reachability[current_index]:
            continue

        processed[current_index] = True
        ordering.append(current_index)

        if core_distances[current_index] == inf:
            continue

        _update_seeds(
            data,
            current_index,
            core_distances,
            reachability,
            processed,
            max_eps,
            seeds,
        )


def optics(
    data: list[point_type],
    min_samples: int = 5,
    max_eps: float = inf,
) -> tuple[list[int], list[float], list[float]]:
    """
    Perform OPTICS clustering on a dataset.

    Args:
        data: List of numerical data points.
        min_samples: Minimum number of points required for a core point.
        max_eps: Maximum neighborhood distance. Defaults to infinity.

    Returns:
        A tuple containing:
        - ordering: Points arranged in OPTICS processing order.
        - reachability: Reachability distance for each original point.
        - core_distances: Core distance for each original point.

    Raises:
        ValueError: If the dataset or parameters are invalid.

    Example:
        >>> data = [
        ...     [0.0, 0.0], [0.0, 0.1], [0.1, 0.0],
        ...     [5.0, 5.0], [5.0, 5.1], [5.1, 5.0],
        ... ]
        >>> ordering, reachability, core = optics(data, min_samples=2)
        >>> sorted(ordering) == list(range(len(data)))
        True
        >>> len(reachability) == len(data)
        True
        >>> len(core) == len(data)
        True
        >>> optics([], min_samples=2)
        Traceback (most recent call last):
            ...
        ValueError: Data must not be empty.
        >>> optics([[1.0, 2.0]], min_samples=1)
        Traceback (most recent call last):
            ...
        ValueError: min_samples must be at least 2.
    """
    if not data:
        raise ValueError("Data must not be empty.")

    if isinstance(min_samples, bool) or not isinstance(min_samples, int):
        raise ValueError("min_samples must be an integer.")

    if min_samples < 2:
        raise ValueError("min_samples must be at least 2.")

    if (
        isinstance(max_eps, bool)
        or not isinstance(max_eps, (int, float))
        or max_eps <= 0
        or isnan(max_eps)
    ):
        raise ValueError("max_eps must be positive.")

    if not data[0]:
        raise ValueError("Points must have at least one dimension.")

    dimensions = len(data[0])

    for point in data:
        if len(point) != dimensions:
            raise ValueError("All points must have the same dimensions.")

        if not all(isfinite(value) for value in point):
            raise ValueError("All coordinates must be finite numbers.")

    point_count = len(data)
    processed = [False] * point_count
    reachability = [inf] * point_count

    core_distances = _calculate_core_distances(
        data,
        min_samples,
        max_eps,
    )

    ordering = []

    for point_index in range(point_count):
        if processed[point_index]:
            continue

        processed[point_index] = True
        ordering.append(point_index)

        _expand_cluster_order(
            data,
            point_index,
            core_distances,
            reachability,
            processed,
            ordering,
            max_eps,
        )

    return ordering, reachability, core_distances


def extract_clusters(
    ordering: list[int],
    reachability: list[float],
    core_distances: list[float],
    epsilon: float,
) -> list[int]:
    """
    Extract DBSCAN-style clusters from an OPTICS ordering.

    Points that do not belong to a cluster receive label -1.

    >>> ordering = [0, 1, 2, 3]
    >>> reachability = [float("inf"), 0.2, 0.3, float("inf")]
    >>> core = [0.3, 0.3, 0.3, float("inf")]
    >>> extract_clusters(ordering, reachability, core, 0.5)
    [0, 0, 0, -1]
    >>> extract_clusters([], [], [], 0.5)
    []
    >>> extract_clusters([0], [0.0], [0.0], 0.0)
    Traceback (most recent call last):
        ...
    ValueError: epsilon must be positive.
    """
    if (
        isinstance(epsilon, bool)
        or not isinstance(epsilon, (int, float))
        or epsilon <= 0
        or not isfinite(epsilon)
    ):
        raise ValueError("epsilon must be positive.")

    if not (len(ordering) == len(reachability) == len(core_distances)):
        raise ValueError("All input lists must have equal lengths.")

    point_count = len(ordering)

    if sorted(ordering) != list(range(point_count)):
        raise ValueError("Ordering must contain each point index exactly once.")

    labels = [-1] * point_count
    cluster_id = -1

    for point_index in ordering:
        if reachability[point_index] > epsilon:
            if core_distances[point_index] <= epsilon:
                cluster_id += 1
                labels[point_index] = cluster_id
        else:
            labels[point_index] = cluster_id

    return labels
