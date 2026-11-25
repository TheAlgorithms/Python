"""Generate permutations in Steinhaus-Johnson-Trotter order."""

from collections.abc import Iterator


def steinhaus_johnson_trotter(size: int) -> Iterator[tuple[int, ...]]:
    """Yield permutations of 1 through size in adjacent-swap order.

    Each step takes O(size) time and the iterator uses O(size) working space.
    Iteration raises ValueError if size is not a non-negative integer.

    Source: https://doi.org/10.1090/S0025-5718-1963-0159764-2

    >>> list(steinhaus_johnson_trotter(3))
    [(1, 2, 3), (1, 3, 2), (3, 1, 2), (3, 2, 1), (2, 3, 1), (2, 1, 3)]
    >>> list(steinhaus_johnson_trotter(0))
    [()]
    >>> list(steinhaus_johnson_trotter(-1))
    Traceback (most recent call last):
    ...
    ValueError: size must be a non-negative integer
    >>> list(steinhaus_johnson_trotter(True))
    Traceback (most recent call last):
    ...
    ValueError: size must be a non-negative integer
    """
    if isinstance(size, bool) or not isinstance(size, int) or size < 0:
        raise ValueError("size must be a non-negative integer")

    values = list(range(1, size + 1))
    directions = [-1] * (size + 1)

    while True:
        yield tuple(values)

        # Find the largest value pointing toward a smaller neighbor.
        mobile = 0
        source = target = 0
        for index, value in enumerate(values):
            neighbor = index + directions[value]
            if 0 <= neighbor < size and values[neighbor] < value and value > mobile:
                mobile = value
                source = index
                target = neighbor

        if mobile == 0:
            return

        values[source], values[target] = values[target], values[source]
        for value in range(mobile + 1, size + 1):
            directions[value] *= -1
