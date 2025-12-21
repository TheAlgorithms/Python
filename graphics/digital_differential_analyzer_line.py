import matplotlib.pyplot as plt


def digital_differential_analyzer_line(
    p1: tuple[int, int], p2: tuple[int, int]
) -> list[tuple[int, int]]:
    """

    Digital Differential Analyzer (DDA) Line Drawing Algorithm.

    This algorithm draws a straight line between two points by calculating
    the difference in x (dx) and y (dy) coordinates and incrementally stepping
    through the dominant axis while updating the other axis using fractional
    increments.

    One of the main disadvantages of the DDA algorithm is its reliance on
    floating-point arithmetic, which can introduce rounding errors at each step.
    Because of this, it is generally slower and less accurate than the
    Bresenham line drawing algorithm, which uses only integer arithmetic.

    Despite this, DDA is useful for educational purposes as it is simple
    to understand and demonstrates the basic idea of incremental line generation.

    For more details, see:
    https://en.wikipedia.org/wiki/Digital_differential_analyzer_(graphics_algorithm)




        Args:
        - p1: Coordinates of the starting point.
        - p2: Coordinates of the ending point.
        Returns:
        - List of coordinate points that form the line.

        >>> digital_differential_analyzer_line((1, 1), (4, 4))
        [(2, 2), (3, 3), (4, 4)]
    """
    x1, y1 = p1
    x2, y2 = p2
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    x_increment = dx / float(steps)
    y_increment = dy / float(steps)
    coordinates = []
    x: float = x1
    y: float = y1
    for _ in range(steps):
        x += x_increment
        y += y_increment
        coordinates.append((round(x), round(y)))
    return coordinates


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    x1 = int(input("Enter the x-coordinate of the starting point: "))
    y1 = int(input("Enter the y-coordinate of the starting point: "))
    x2 = int(input("Enter the x-coordinate of the ending point: "))
    y2 = int(input("Enter the y-coordinate of the ending point: "))
    coordinates = digital_differential_analyzer_line((x1, y1), (x2, y2))
    x_points, y_points = zip(*coordinates)
    plt.plot(x_points, y_points, marker="o")
    plt.title("Digital Differential Analyzer Line Drawing Algorithm")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid()
    plt.show()
