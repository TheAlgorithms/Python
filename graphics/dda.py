from typing import Tuple

Point2D = Tuple[int, int]


def dda(first_point: Point2D, second_point: Point2D) -> list:

    """A Python implementation of digital differential analyzer (DDA) algorithm.
    It is used for rasterization of lines, and interpolates variables over an
    interval between two different points.

    https://en.wikipedia.org/wiki/Digital_differential_analyzer_(graphics_algorithm)

    Examples:
    >>> dda((2, 1), (5, 1))
    [(2, 1), (3, 1), (4, 1), (5, 1)]

    >>> dda((-1, 4), (3, 8))
    [(-1, 4), (0, 5), (1, 6), (2, 7), (3, 8)]

    >>> dda((4, 6), (2, 2))
    [(4, 6), (4, 5), (3, 4), (2, 3), (2, 2)]
    """

    delta_x = second_point[0] - first_point[0]
    delta_y = second_point[1] - first_point[1]

    if abs(delta_x) > abs(delta_y):
        steps = abs(delta_x)
    else:
        steps = abs(delta_y)

    if steps == 0:
        raise ValueError("first_point and second_point are equals")

    final_pixels = []

    x_incr = delta_x / steps
    y_incr = delta_y / steps

    x = first_point[0]
    y = first_point[1]

    for _ in range(steps + 1):
        new_pixel = (round(x), round(y))
        final_pixels.append(new_pixel)

        x += x_incr
        y += y_incr

    return final_pixels


if __name__ == "__main__":
    import doctest

    doctest.testmod()
