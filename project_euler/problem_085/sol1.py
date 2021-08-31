"""
Project Euler Problem 85: https://projecteuler.net/problem=85

By counting carefully it can be seen that a rectangular grid measuring 3 by 2
contains eighteen rectangles.
￼
Although there exists no rectangular grid that contains exactly two million
rectangles, find the area of the grid with the nearest solution.

Solution:

    For a grid with side-lengths a and b, the number of rectangles contained in the grid
    is [a*(a+1)/2] * [b*(b+1)/2)], which happens to be the product of the a-th and b-th
    triangle numbers. So to find the solution grid (a,b), we need to find the two
    triangle numbers whose product is closest to two million.

    Denote these two triangle numbers Ta and Tb. We want their product Ta*Tb to be
    as close as possible to 2m. Assuming that the best solution is fairly close to 2m,
    We can assume that both Ta and Tb are roughly bounded by 2m. Since Ta = a(a+1)/2,
    we can assume that a (and similarly b) are roughly bounded by sqrt(2 * 2m) = 2000.
    Since this is a rough bound, to be on the safe side we add 10%. Therefore we start
    by generating all the triangle numbers Ta for 1 <= a <= 2200. This can be done
    iteratively since the ith triangle number is the sum of 1,2, ... ,i, and so
    T(i) = T(i-1) + i.

    We then search this list of triangle numbers for the two that give a product
    closest to our target of two million. Rather than testing every combination of 2
    elements of the list, which would find the result in quadratic time, we can find
    the best pair in linear time.

    We iterate through the list of triangle numbers using enumerate() so we have a
    and Ta. Since we want Ta * Tb to be as close as possible to 2m, we know that Tb
    needs to be roughly 2m / Ta. Using the formula Tb = b*(b+1)/2 as well as the
    quadratic formula, we can solve for b:
    b is roughly (-1 + sqrt(1 + 8 * 2m / Ta)) / 2.

    Since the closest integers to this estimate will give product closest to 2m,
    we only need to consider the integers above and below. It's then a simple matter
    to get the triangle numbers corresponding to those integers, calculate the product
    Ta * Tb, compare that product to our target 2m, and keep track of the (a,b) pair
    that comes the closest.


Reference: https://en.wikipedia.org/wiki/Triangular_number
           https://en.wikipedia.org/wiki/Quadratic_formula
"""


from math import ceil, floor, sqrt
from typing import List


def solution(target: int = 2000000) -> int:
    """
    Find the area of the grid which contains as close to two million rectangles
    as possible.
    >>> solution(20)
    6
    >>> solution(2000)
    72
    >>> solution(2000000000)
    86595
    """
    triangle_numbers: List[int] = [0]
    idx: int

    for idx in range(1, ceil(sqrt(target * 2) * 1.1)):
        triangle_numbers.append(triangle_numbers[-1] + idx)

    # we want this to be as close as possible to target
    best_product: int = 0
    # the area corresponding to the grid that gives the product closest to target
    area: int = 0
    # an estimate of b, using the quadratic formula
    b_estimate: float
    # the largest integer less than b_estimate
    b_floor: int
    # the largest integer less than b_estimate
    b_ceil: int
    # the triangle number corresponding to b_floor
    triangle_b_first_guess: int
    # the triangle number corresponding to b_ceil
    triangle_b_second_guess: int

    for idx_a, triangle_a in enumerate(triangle_numbers[1:], 1):
        b_estimate = (-1 + sqrt(1 + 8 * target / triangle_a)) / 2
        b_floor = floor(b_estimate)
        b_ceil = ceil(b_estimate)
        triangle_b_first_guess = triangle_numbers[b_floor]
        triangle_b_second_guess = triangle_numbers[b_ceil]

        if abs(target - triangle_b_first_guess * triangle_a) < abs(
            target - best_product
        ):
            best_product = triangle_b_first_guess * triangle_a
            area = idx_a * b_floor

        if abs(target - triangle_b_second_guess * triangle_a) < abs(
            target - best_product
        ):
            best_product = triangle_b_second_guess * triangle_a
            area = idx_a * b_ceil

    return area


if __name__ == "__main__":
    print(f"{solution() = }")
