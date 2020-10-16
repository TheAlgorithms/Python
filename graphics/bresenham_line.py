from typing import Tuple

Point2D = Tuple[int, int]


def bresenham_line(first_point: Point2D, second_point: Point2D) -> list:

    """A Python implementation of Bresenham's line algorithm.
    It is used for rasterization of lines, and interpolates variables over an
    interval between two different points, where the coordinates are integers.

    https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm

    Examples:
    >>> bresenham_line((2, 1), (5, 1))
    [(2, 1), (3, 1), (4, 1), (5, 1)]
    >>> bresenham_line((-1, 4), (3, 8))
    [(-1, 4), (0, 5), (1, 6), (2, 7), (3, 8)]
    >>> bresenham_line((0, 1), (6, 4))
    [(0, 1), (1, 1), (2, 2), (3, 2), (4, 3), (5, 3), (6, 4)]
    """

    delta_x = abs(first_point[0] - second_point[0])
    delta_y = abs(first_point[1] - second_point[1])

    p = (2 * delta_y) - delta_x

    if first_point[0] == second_point[0]:
        steps = abs(first_point[1] - second_point[1])
    else:
        steps = abs(first_point[0] - second_point[0])

    if second_point[0] - first_point[0] > 0:
        x_incr = 1
    elif second_point[0] - first_point[0] < 0:
        x_incr = -1
    else:
        x_incr = 0

    if second_point[1] - first_point[1] > 0:
        y_incr = 1
    elif second_point[1] - first_point[1] < 0:
        y_incr = -1
    else:
        y_incr = 0

    if x_incr == 0 and y_incr == 0:
        raise ValueError("first_point and second_point are equals")

    final_pixels = []

    x = first_point[0]
    y = first_point[1]

    for _ in range(steps + 1):
        new_pixel = (x, y)
        final_pixels.append(new_pixel)

        x += x_incr
        if p <= 0:
            p += 2 * delta_y
        else:
            y += y_incr
            p += (2 * delta_y) - (2 * delta_x)

    return final_pixels


if __name__ == "__main__":
    import doctest

    doctest.testmod()
