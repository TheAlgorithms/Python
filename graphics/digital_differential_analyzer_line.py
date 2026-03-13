import matplotlib.pyplot as plt


def digital_differential_analyzer_line(
    p1: tuple[int, int], p2: tuple[int, int]
) -> list[tuple[int, int]]:
    """
    Draw a line between two points using the Digital Differential Analyzer (DDA) algorithm.

    The DDA algorithm works by calculating dx and dy and incrementally stepping
    along the dominant axis while updating the other axis using fractional values.

    Advantages:
    - Simple and easy to understand implementation.

    Disadvantages:
    - Uses floating-point arithmetic, which can introduce rounding errors.
    - Generally slower and less efficient than Bresenham's line algorithm,
      which relies only on integer calculations.

    Reference:
    https://en.wikipedia.org/wiki/Digital_differential_analyzer_(graphics_algorithm)
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
