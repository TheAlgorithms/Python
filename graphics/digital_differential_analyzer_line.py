import matplotlib.pyplot as plt


def digital_differential_analyzer_line(
    p1: tuple[int, int], p2: tuple[int, int]
) -> list[tuple[int, int]]:
    """
    Draws a line between two points using the Digital Differential Analyzer (DDA)
    algorithm.

    The DDA algorithm works by calculating dx and dy and then iteratively stepping
    along the dominant axis while incrementing the other axis by a fractional
    amount, rounding at each step to determine the next pixel.

    This approach relies on floating-point arithmetic and rounding at every step,
    which can be slower and less accurate than integer-only methods. In practice
    it is generally outperformed by the Bresenham line algorithm, which uses
    only integer arithmetic.

    More details: https://en.wikipedia.org/wiki/Digital_differential_analyzer_(graphics_algorithm)

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
