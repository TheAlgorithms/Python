"""
Hilbert Curve

The Hilbert curve is a space-filling curve that recursively fills a square
with an intricate pattern. It is used in computer science, graphics, and various fields.

Reference:
https://en.wikipedia.org/wiki/Hilbert_curve

Requirements:
    - matplotlib
    - numpy
"""

import doctest

import matplotlib.pyplot as plt


def hilbert_curve(
    order: int,
    x0: float = 0,
    y0: float = 0,
    xi: float = 1,
    xj: float = 0,
    yi: float = 0,
    yj: float = 1,
) -> list[tuple[float, float]]:
    """
    Generates the points for the Hilbert curve of the specified order.

    The Hilbert curve is built using recursive rules. This function returns
    a list of (x, y) points.

    Parameters:
    - order: the recursion depth or order of the curve
    - x0, y0: the starting coordinates
    - xi, xj: the transformation matrix for x coordinates
    - yi, yj: the transformation matrix for y coordinates

    Returns:
    - A list of (x, y) coordinates representing the Hilbert curve.

    >>> len(hilbert_curve(1))
    4
    >>> len(hilbert_curve(2))
    16
    >>> len(hilbert_curve(3))
    64
    """
    if order == 0:
        return [(x0 + (xi + yi) / 2, y0 + (xj + yj) / 2)]

    points = []
    points += hilbert_curve(order - 1, x0, y0, yi / 2, yj / 2, xi / 2, xj / 2)
    points += hilbert_curve(
        order - 1, x0 + xi / 2, y0 + xj / 2, xi / 2, xj / 2, yi / 2, yj / 2
    )
    points += hilbert_curve(
        order - 1,
        x0 + xi / 2 + yi / 2,
        y0 + xj / 2 + yj / 2,
        xi / 2,
        xj / 2,
        yi / 2,
        yj / 2,
    )
    points += hilbert_curve(
        order - 1,
        x0 + xi / 2 + yi,
        y0 + xj / 2 + yj,
        -yi / 2,
        -yj / 2,
        -xi / 2,
        -xj / 2,
    )

    return points


def plot_hilbert_curve(points: list[tuple[float, float]]) -> None:
    """
    Plots the Hilbert curve using matplotlib.

    Parameters:
    - points: A list of (x, y) coordinates representing the Hilbert curve.

    Returns:
    - None
    """
    x, y = zip(*points)
    plt.plot(x, y)
    plt.title("Hilbert Curve")
    plt.gca().set_aspect("equal", adjustable="box")
    plt.show()


if __name__ == "__main__":
    doctest.testmod()

    order = 5  # Order of the Hilbert curve
    curve_points = hilbert_curve(order)
    plot_hilbert_curve(curve_points)
