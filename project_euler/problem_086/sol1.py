"""
Project Euler Problem 86: https://projecteuler.net/problem=86

A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F,
sits in the opposite corner. By travelling on the surfaces of the room the shortest
"straight line" distance from S to F is 10 and the path is shown on the diagram.
￼
However, there are up to three "shortest" path candidates for any given cuboid and the
shortest route doesn't always have integer length.

It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, with
integer dimensions, up to a maximum size of M by M by M, for which the shortest route
has integer length when M = 100. This is the least value of M for which the number of
solutions first exceeds two thousand; the number of solutions when M = 99 is 1975.

Find the least value of M such that the number of solutions first exceeds one million.
"""


from math import sqrt


def is_int(n: float) -> bool:
    """
    Checks whether n is an integer.
    >>> is_int(1.9)
    False
    >>> is_int(2.0)
    True
    """
    return int(n) == n


def solution(limit: int = 1000000) -> int:
    """
    Return the least value of M such that there are more than one million cuboids
    of side lengths 1 <= a,b,c <= M such that the shortest distance between two
    opposite vertices of the cuboid is integral.
    >>> solution(2000)
    100
    """
    num_cuboids = 0
    M = 0
    while num_cuboids <= limit:
        M += 1
        for d in range(2, 2 * M):
            if is_int(sqrt(d * d + M * M)):
                num_cuboids += min(M, d // 2) - max(1, d - M) + 1

    return M


if __name__ == "__main__":
    print(f"{solution() = }")
