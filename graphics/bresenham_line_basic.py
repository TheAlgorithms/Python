"""
Classic Bresenham's Line Drawing Algorithm
------------------------------------------

Draws a line between two points (x1, y1) and (x2, y2)
for slope 0 ≤ m ≤ 1, without floating-point operations.

Reference : https://www.geeksforgeeks.org/dsa/bresenhams-line-generation-algorithm/

>>> classic_bresenham_line((0, 0), (5, 3))
[(0, 0), (1, 1), (2, 1), (3, 2), (4, 2), (5, 3)]
"""

import matplotlib.pyplot as plt


def classic_bresenham_line(
    p1: tuple[int, int], p2: tuple[int, int]
) -> list[tuple[int, int]]:
    x1, y1 = p1
    x2, y2 = p2

    dx = x2 - x1
    dy = y2 - y1
    p = 2 * dy - dx
    y = y1
    points = []

    for x in range(x1, x2 + 1):
        points.append((x, y))
        if p < 0:
            p += 2 * dy
        else:
            y += 1
            p += 2 * (dy - dx)
    return points


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))

    points = classic_bresenham_line((x1, y1), (x2, y2))
    print("Generated points:", points)

    xs, ys = zip(*points)
    plt.plot(xs, ys, marker="o")
    plt.title("Classic Bresenham's Line Algorithm")
    plt.grid()
    plt.show()
