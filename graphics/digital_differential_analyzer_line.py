from typing import List, Tuple


def digital_differential_analyzer_line(
    p1: Tuple[int, int], p2: Tuple[int, int]
) -> List[Tuple[int, int]]:
    """
    Draw a line between two points using the Digital Differential Analyzer (DDA)
    algorithm.

    The DDA algorithm increments the dominant axis in unit steps and updates the
    other axis proportionally. After each step coordinates are rounded to the
    nearest integer to obtain pixel coordinates.

    Args:
        p1: Starting coordinate (x1, y1).
        p2: Ending coordinate (x2, y2).

    Returns:
        A list of integer coordinate tuples representing the rasterized line.
        The list includes the end point and excludes the start point.

    Examples:
    >>> digital_differential_analyzer_line((1, 1), (4, 4))
    [(2, 2), (3, 3), (4, 4)]

    >>> digital_differential_analyzer_line((0, 0), (0, 5))
    [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5)]

    >>> digital_differential_analyzer_line((5, 5), (2, 5))
    [(4, 5), (3, 5), (2, 5)]

    >>> digital_differential_analyzer_line((3, 3), (3, 3))
    [(3, 3)]
    """
    x1, y1 = p1
    x2, y2 = p2
    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))
    if steps == 0:
        return [p1]

    x_inc = dx / float(steps)
    y_inc = dy / float(steps)

    x, y = float(x1), float(y1)
    points: List[Tuple[int, int]] = []

    for _ in range(steps):
        x += x_inc
        y += y_inc
        points.append((round(x), round(y)))

    return points
