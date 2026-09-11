"""
The Barnsley fern is a fractal that resembles the black spleenwort fern.  It was
described by the British mathematician Michael Barnsley in his 1988 book
*Fractals Everywhere* and is a classic example of an iterated function system
(IFS).

An IFS builds a fractal by repeatedly applying a small set of affine
transformations, each chosen at random with a fixed probability.  Starting from
the point ``(0, 0)`` the fern uses four transformations:

===============  ===========================================  ============
Transformation   Effect                                       Probability
===============  ===========================================  ============
Stem             collapse onto the y-axis                     1%
Successive leaf  the main self-similar copy of the fern       85%
Left leaflet     a smaller rotated/reflected copy             7%
Right leaflet    another smaller rotated/reflected copy       7%
===============  ===========================================  ============

Because the whole picture is produced by chance the doctests below seed Python's
random generator so that the results are reproducible.  Plotting the points with
matplotlib is optional and only happens when the module is run directly.

Reference: https://en.wikipedia.org/wiki/Barnsley_fern
"""

import random

# Each row is (a, b, c, d, e, f) for the affine map
#   x' = a*x + b*y + e
#   y' = c*x + d*y + f
# and the running cumulative probabilities used to pick a transformation.
TRANSFORMATIONS: tuple[tuple[float, float, float, float, float, float], ...] = (
    (0.00, 0.00, 0.00, 0.16, 0.00, 0.00),  # stem
    (0.85, 0.04, -0.04, 0.85, 0.00, 1.60),  # successive smaller leaflets
    (0.20, -0.26, 0.23, 0.22, 0.00, 1.60),  # left-hand leaflet
    (-0.15, 0.28, 0.26, 0.24, 0.00, 0.44),  # right-hand leaflet
)
CUMULATIVE_PROBABILITIES: tuple[float, ...] = (0.01, 0.86, 0.93, 1.00)


def transform(point: tuple[float, float], index: int) -> tuple[float, float]:
    """
    Apply the affine transformation ``index`` to ``point`` and return the image.

    >>> transform((0.0, 0.0), 0)
    (0.0, 0.0)
    >>> transform((1.0, 1.0), 1)
    (0.89, 2.41)
    >>> transform((2.0, 3.0), 3)
    (0.54, 1.68)
    >>> transform((0.0, 0.0), 4)
    Traceback (most recent call last):
        ...
    IndexError: index must be in range 0..3, got 4
    """
    if not 0 <= index < len(TRANSFORMATIONS):
        msg = f"index must be in range 0..3, got {index}"
        raise IndexError(msg)
    a, b, c, d, e, f = TRANSFORMATIONS[index]
    x, y = point
    new_x = round(a * x + b * y + e, 12)
    new_y = round(c * x + d * y + f, 12)
    return (new_x, new_y)


def choose_transformation(sample: float) -> int:
    """
    Map a value ``sample`` from ``[0, 1)`` to a transformation index using the
    cumulative probabilities of the fern.

    >>> choose_transformation(0.0)
    0
    >>> choose_transformation(0.5)
    1
    >>> choose_transformation(0.9)
    2
    >>> choose_transformation(0.97)
    3
    """
    for index, threshold in enumerate(CUMULATIVE_PROBABILITIES):
        if sample < threshold:
            return index
    return len(CUMULATIVE_PROBABILITIES) - 1


def generate_fern(
    iterations: int, seed: int | None = None
) -> list[tuple[float, float]]:
    """
    Generate ``iterations`` points of the Barnsley fern, starting at ``(0, 0)``.

    Passing a ``seed`` makes the (otherwise random) output reproducible, which is
    what keeps the doctests deterministic.

    >>> points = generate_fern(5, seed=0)
    >>> len(points)
    5
    >>> points[0]
    (0.0, 0.0)
    >>> points  # doctest: +NORMALIZE_WHITESPACE
    [(0.0, 0.0), (0.0, 1.6), (0.064, 2.96),
     (0.1728, 4.11344), (0.3114176, 5.089512)]

    Every fern point lives inside the well known bounding box.

    >>> cloud = generate_fern(2000, seed=42)
    >>> all(-2.182 <= x <= 2.6558 for x, _ in cloud)
    True
    >>> all(0.0 <= y <= 9.9984 for _, y in cloud)
    True
    >>> generate_fern(0)
    Traceback (most recent call last):
        ...
    ValueError: iterations must be positive, got 0
    """
    if iterations <= 0:
        msg = f"iterations must be positive, got {iterations}"
        raise ValueError(msg)
    rng = random.Random(seed)
    point = (0.0, 0.0)
    points = [point]
    for _ in range(iterations - 1):
        index = choose_transformation(rng.random())
        point = transform(point, index)
        points.append(point)
    return points


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib is required to plot the fern (pip install matplotlib).")
    else:
        fern_points = generate_fern(100_000, seed=0)
        xs = [x for x, _ in fern_points]
        ys = [y for _, y in fern_points]
        plt.figure(figsize=(4, 8))
        plt.scatter(xs, ys, s=0.2, color="forestgreen")
        plt.axis("off")
        plt.title("Barnsley fern")
        plt.show()
