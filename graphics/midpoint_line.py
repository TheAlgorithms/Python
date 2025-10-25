"""
Midpoint Line Drawing Algorithm
-------------------------------

Handles all lines with arbitrary slopes using the midpoint method.

Referece:
https://www.geeksforgeeks.org/dsa/mid-point-line-generation-algorithm/

>>> midpoint_line((0, 0), (5, 3))
[(0, 0), (1, 1), (2, 1), (3, 2), (4, 2), (5, 3)]
>>> midpoint_line((5, 5), (2, 3))
[(5, 5), (4, 4), (3, 4), (2, 3)]
"""

import matplotlib.pyplot as plt


def midpoint_line(p1: tuple[int, int], p2: tuple[int, int]) -> list[tuple[int, int]]:
    x1, y1 = p1
    x2, y2 = p2

    points = []

    dx = x2 - x1
    dy = y2 - y1

    # Determine the direction of the step
    sx = 1 if dx >= 0 else -1
    sy = 1 if dy >= 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        # Shallow slope: iterate over x
        d = dy - dx / 2
        x, y = x1, y1
        while x != x2 + sx:
            points.append((x, y))
            if d >= 0:
                y += sy
                d -= dx
            x += sx
            d += dy
    else:
        # Steep slope: iterate over y
        d = dx - dy / 2
        x, y = x1, y1
        while y != y2 + sy:
            points.append((x, y))
            if d >= 0:
                x += sx
                d -= dy
            y += sy
            d += dx

    return points


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))

    points = midpoint_line((x1, y1), (x2, y2))
    print("Generated points:", points)

    xs, ys = zip(*points)
    plt.plot(xs, ys, marker="o")
    plt.title("Midpoint Line Drawing Algorithm")
    plt.grid()
    plt.show()
