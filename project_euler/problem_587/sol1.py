"""
Project Euler Problem 587: https://projecteuler.net/problem=587

A square is drawn around a circle as shown in the diagram below on the left.
We shall call the blue shaded region the L-section.
A line is drawn from the bottom left of the square to the top right
as shown in the diagram on the right.
We shall call the orange shaded region a concave triangle.

It should be clear that the concave triangle occupies exactly half of the L-section.

Two circles are placed next to each other horizontally,
a rectangle is drawn around both circles, and
a line is drawn from the bottom left to the top right as shown in the diagram below.

This time the concave triangle occupies approximately 36.46% of the L-section.

If n circles are placed next to each other horizontally,
a rectangle is drawn around the n circles, and
a line is drawn from the bottom left to the top right,
then it can be shown that the least value of n
for which the concave triangle occupies less than 10% of the L-section is n = 15.

What is the least value of n
for which the concave triangle occupies less than 0.1% of the L-section?
"""

from itertools import count
from math import asin, pi, sqrt


def circle_bottom_arc_integral(point: float) -> float:
    """
    Returns integral of circle bottom arc y = 1 / 2 - sqrt(1 / 4 - (x - 1 / 2) ^ 2)

    >>> circle_bottom_arc_integral(0)
    0.39269908169872414

    >>> circle_bottom_arc_integral(1 / 2)
    0.44634954084936207

    >>> circle_bottom_arc_integral(1)
    0.5
    """

    return (
        (1 - 2 * point) * sqrt(point - point**2) + 2 * point + asin(sqrt(1 - point))
    ) / 4


def concave_triangle_area(circles_number: int) -> float:
    """
    Returns area of concave triangle

    >>> concave_triangle_area(1)
    0.026825229575318944

    >>> concave_triangle_area(2)
    0.01956236140083944
    """

    intersection_y = (circles_number + 1 - sqrt(2 * circles_number)) / (
        2 * (circles_number**2 + 1)
    )
    intersection_x = circles_number * intersection_y

    triangle_area = intersection_x * intersection_y / 2
    concave_region_area = circle_bottom_arc_integral(
        1 / 2
    ) - circle_bottom_arc_integral(intersection_x)

    return triangle_area + concave_region_area


def solution(fraction: float = 1 / 1000) -> int:
    """
    Returns least value of n
    for which the concave triangle occupies less than fraction of the L-section

    >>> solution(1 / 10)
    15
    """

    l_section_area = (1 - pi / 4) / 4

    for n in count(1):
        if concave_triangle_area(n) / l_section_area < fraction:
            return n

    return -1


if __name__ == "__main__":
    print(f"{solution() = }")
