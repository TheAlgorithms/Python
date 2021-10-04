"""
Project Euler Problem 199: https://projecteuler.net/problem=199

Three circles of equal radius are placed inside a larger circle such that each pair of circles is tangent to one another and the inner circles do not overlap. There are four uncovered "gaps" which are to be filled iteratively with more tangent circles.
At each iteration, a maximally sized circle is placed in each gap, which creates more gaps for the next iteration. After 3 iterations (pictured), there are 108 gaps and the fraction of the area which is not covered by circles is 0.06790342, rounded to eight decimal places.

What fraction of the area is not covered by circles after 10 iterations?
Give your answer rounded to eight decimal places using the format x.xxxxxxxx .

References:
https://en.wikipedia.org/wiki/Descartes%27_theorem

"""

import math


def area(rad: float = 1.0) -> float:
    """
    return area of a circle

    >>> area(2.0)
    3.141592653589793
    >>> area(3.0)
    7.0685834705770345
    >>> area(4.0)
    12.566370614359172
    """
    return rad * rad * math.pi / 4


def descartes(k1: float = 1.0, k2: float = 1.0, k3: float = 1.0, depth: float = 1.0) -> float:
    """
    return sum of touching circles' areas including their children

    >>> descartes(1.0,2.0,3.0,4.0)
    0.00944483254632056
    >>> descartes(2.0,1.0,2.0,3.0)
    0.012188628633069158
    >>> descartes(4.0,5.0,3.0,6.0)
    0.0024359771569779304
    """
    k4 = k1 + k2 + k3 + 2 * math.sqrt(k1 * k2 + k2 * k3 + k1 * k3)
    r = 1 / k4
    ar = area(r)
    if depth == 1:
        return ar
    return ar + descartes(k1, k2, k4, depth - 1) + descartes(k2, k3, k4, depth - 1) + descartes(k1, k3, k4, depth - 1)


def solution(dep: int = 10) -> float:
    """
    returns the fraction of the area which is not covered by circles after 'n' iterations

    >>> solution(3)
    0.0679034
    >>> solution(4)
    0.0416773
    >>> solution(9)
    0.00550538
    """
    depth = dep
    outerk = 3 - 2 * math.sqrt(3)
    outerradius = -1 / outerk
    innerradius = 1.0
    innerk = 1 / innerradius
    initial = 3 * area(innerradius)
    vshaped = descartes(outerk, innerk, innerk, depth)
    middle = descartes(innerk, innerk, innerk, depth)
    result = initial + 3 * vshaped + middle
    result /= area(outerradius)
    print(round(1 - result, 8))


if __name__ == "__main__":
    print(f"{solution() = }")
