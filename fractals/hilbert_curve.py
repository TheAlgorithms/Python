"""
Author Atharva Date | atharvad931@gmail.com | git/Atharva9621

The Hilbert Curve (also known as the Hilbert Space Filling Curve) is a continuous
fractal space-filling curve and is a variant of the space-filling Peano curves.

Because it is space-filling, its Hausdorff dimension is 2. Precisely, its image
is the unit square, whose dimension is 2 in any definition of dimension. Its
graph is a compact set homeomorphic to the closed unit interval, with Hausdorff
dimension 1.

Credits:
    description adapted from
    https://en.wikipedia.org/wiki/Hilbert_curve

    also see
    https://youtu.be/3s7h2MHQtxc?si=_qIusAJFHYfXIOKn
        (3b1b - Hilbert's Curve: Is infinite math useful?)
    https://dl.acm.org/doi/pdf/10.1145/290200.290219

Requirements (pip):
    - matplotlib
"""

import matplotlib.pyplot as plt


def rotate_pnts(
    pnts: list[tuple[float, float]], angle: int
) -> list[tuple[float, float]]:
    """
    Rotates a list of points by a given angle (in multiples of 90 degrees).

    Since the rotation is limited to multiples of 90 degrees (90, 180, 270, 360),
    this function simply reorders the list of points accordingly. The rotation in
    each quadrant is achieved  by adjusting the starting index of the list
    and wrapping around.

    Parameters:
    -----------
    pnts : List[Tuple[float, float]]
        A list of tuples, where each tuple represents a point (x, y).
    angle : int
        The angle of rotation, should be a multiple of 90 degrees
        (e.g., 90, 180, 270, 360).

    Returns:
    --------
    List[Tuple[float, float]]
        A reordered list of points, rotated by the specified angle.

    Example:
    --------
    >>> rotate_pnts([(1, 1), (0, 1), (0, 0), (1, 0)], 90)
    [(0, 1), (0, 0), (1, 0), (1, 1)]
    """
    start_index = angle // 90 % 4
    return pnts[start_index:] + pnts[:start_index]


def hilbert_curve(
    center: tuple[float, float], level: int, side: float = 1, angle: int = 90
) -> list[tuple[float, float]]:
    """
    Params:
    ------
        center: Tuple[float, float]- The (x, y) center coordinate of the subsection.
        level: int- The recursion depth or subdivision level of the Hilbert curve.
        side : float, optional
                The length of the side of the square region in which the curve is drawn.
        angle : int, optional
                The initial rotation angle of the curve in degrees.
                It should be a multiple of 90 degrees. (default=90)

    Returns:
    ------
        pts: List[Tuple[float, float]] -
            A list of points (x, y) representing the Hilbert curve for the given level.

    Example:
    --------
    >>> hilbert_curve((0, 0), 1, angle=0)
    [(0.25, 0.25), (-0.25, 0.25), (-0.25, -0.25), (0.25, -0.25)]
    """
    x, y = center
    angle = angle % 360
    pnts = [
        (x + side / 4, y + side / 4),
        (x - side / 4, y + side / 4),
        (x - side / 4, y - side / 4),
        (x + side / 4, y - side / 4),
    ]
    pnts = rotate_pnts(pnts, angle)

    if level == 1:
        return pnts
    else:
        return (
            hilbert_curve(pnts[0], level - 1, side / 2, angle=angle + 90)[::-1]
            + hilbert_curve(pnts[1], level - 1, side / 2, angle=angle)
            + hilbert_curve(pnts[2], level - 1, side / 2, angle=angle)
            + hilbert_curve(pnts[3], level - 1, side / 2, angle=angle - 90)[::-1]
        )


def plot_hilbert_curve(points: list[tuple[float, float]]) -> None:
    """
    Plots the hilbert curve using mtplotlib

    Example
    --------
    >>> plot_hilbert_curve([(-0.25, 0.25), (-0.25, -0.25), (0.25, -0.25), (0.25, 0.25)])
    """
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]

    plt.plot(x_coords, y_coords, marker="o", linestyle="-")
    plt.gca().set_aspect("equal", adjustable="box")  # Make the plot square
    plt.title("Hilbert Curve")
    plt.show()


if __name__ == "__main__":
    import doctest

    # Run doctests
    doctest.testmod()

    # Plotting Hilbert Curve
    plot_hilbert_curve(hilbert_curve((0, 0), 4))
