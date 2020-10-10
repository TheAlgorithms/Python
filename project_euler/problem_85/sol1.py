"""
By counting carefully it can be seen that a rectangular grid measuring 3 by 2
contains eighteen rectangles.
￼
Although there exists no rectangular grid that contains exactly two million
rectangles, find the area of the grid with the nearest solution.
"""


from math import ceil, floor, sqrt


def solution(target: int = 2000000) -> int:
    """
    Find the area of the grid which contains as close to two million rectangles
    as possible.
    >>> solution(2000)
    72
    """
    triangle_numbers = [0]
    for i in range(1, ceil(sqrt(target * 2) * 1.1)):
        triangle_numbers.append(triangle_numbers[-1] + i)

    best = 0
    area = 0

    for a, tri_a in enumerate(triangle_numbers[1:], 1):
        hit = (-1 + sqrt(1 + 8 * target / tri_a)) / 2
        b_floor = floor(hit)
        b_ceil = ceil(hit)
        first = triangle_numbers[b_floor]
        second = triangle_numbers[b_ceil]
        if abs(target - first * tri_a) < abs(target - best):
            best = first * tri_a
            area = a * b_floor
        if abs(target - second * tri_a) < abs(target - best):
            best = second * tri_a
            area = a * b_ceil

    return area


if __name__ == "__main__":
    print(solution())
