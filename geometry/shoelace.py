def area_of_polygon(xs: list[float], ys: list[float]) -> float:
    """
    Compute the area of a polygon. The polygon has to be planar and simple
    (not self-intersecting). The vertices have to be ordered in the
    counter-clockwise direction.
    https://en.wikipedia.org/wiki/Shoelace_formula

    Args:
        xs: list of x coordinates of the polygon vertices in counter-clockwise order
        ys: list of y coordinates of the polygon vertices in counter-clockwise order
    Returns:
        area of the polygon

    >>> from math import isclose
    >>> xs = [1, 3, 7, 4, 8]
    >>> ys = [6, 1, 2, 4, 5]
    >>> isclose(area_of_polygon(xs, ys), 16.5)
    True
    """

    return 0.5 * sum(
        (ys[i] + ys[(i + 1) % len(ys)]) * (xs[i] - xs[(i + 1) % len(xs)])
        for i in range(len(xs))
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
