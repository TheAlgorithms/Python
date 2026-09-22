"""
Generalized Bresenham's Line Drawing Algorithm
----------------------------------------------

Handles all possible line slopes and directions.

Reference:
https://www.geeksforgeeks.org/dsa/bresenhams-line-generation-algorithm/

>>> generalized_bresenham_line((0, 0), (5, 3))
[(0, 0), (1, 1), (2, 1), (3, 2), (4, 2), (5, 3)]
>>> generalized_bresenham_line((5, 5), (2, 3))
[(5, 5), (4, 4), (3, 4), (2, 3)]
"""

import matplotlib.pyplot as plt


def generalized_bresenham_line(
    p1: tuple[int, int], p2: tuple[int, int]
) -> list[tuple[int, int]]:
    x1, y1 = p1
    x2, y2 = p2
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    points = []

    while True:
        points.append((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

    return points


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))

    points = generalized_bresenham_line((x1, y1), (x2, y2))
    print("Generated points:", points)

    xs, ys = zip(*points)
    plt.plot(xs, ys, marker="o")
    plt.title("Generalized Bresenham's Line Algorithm (All Slopes)")
    plt.grid()
    plt.show()
