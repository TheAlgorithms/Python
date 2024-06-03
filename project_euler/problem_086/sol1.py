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

Solution:
    Label the 3 side-lengths of the cuboid a,b,c such that 1 <= a <= b <= c <= M.
    By conceptually "opening up" the cuboid and laying out its faces on a plane,
    it can be seen that the shortest distance between 2 opposite corners is
    sqrt((a+b)^2 + c^2). This distance is an integer if and only if (a+b),c make up
    the first 2 sides of a pythagorean triplet.

    The second useful insight is rather than calculate the number of cuboids
    with integral shortest distance for each maximum cuboid side-length M,
    we can calculate this number iteratively each time we increase M, as follows.
    The set of cuboids satisfying this property with maximum side-length M-1 is a
    subset of the cuboids satisfying the property with maximum side-length M
    (since any cuboids with side lengths <= M-1 are also <= M). To calculate the
    number of cuboids in the larger set (corresponding to M) we need only consider
    the cuboids which have at least one side of length M. Since we have ordered the
    side lengths a <= b <= c, we can assume that c = M. Then we just need to count
    the number of pairs a,b satisfying the conditions:
        sqrt((a+b)^2 + M^2) is integer
        1 <= a <= b <= M

    To count the number of pairs (a,b) satisfying these conditions, write d = a+b.
    Now we have:
        1 <= a <= b <= M  =>  2 <= d <= 2*M
                                   we can actually make the second equality strict,
                                   since d = 2*M => d^2 + M^2 = 5M^2
                                              => shortest distance = M * sqrt(5)
                                              => not integral.
        a + b = d => b = d - a
                 and a <= b
                  => a <= d/2
                also a <= M
                  => a <= min(M, d//2)

        a + b = d => a = d - b
                 and b <= M
                  => a >= d - M
                also a >= 1
                  => a >= max(1, d - M)

        So a is in range(max(1, d - M), min(M, d // 2) + 1)

    For a given d, the number of cuboids satisfying the required property with c = M
    and a + b = d is the length of this range, which is
        min(M, d // 2) + 1 - max(1, d - M).

    In the code below, d is sum_shortest_sides
                   and M is max_cuboid_size.


"""

from math import sqrt


def solution(limit: int = 1000000) -> int:
    """
    Return the least value of M such that there are more than one million cuboids
    of side lengths 1 <= a,b,c <= M such that the shortest distance between two
    opposite vertices of the cuboid is integral.
    >>> solution(100)
    24
    >>> solution(1000)
    72
    >>> solution(2000)
    100
    >>> solution(20000)
    288
    """
    num_cuboids: int = 0
    max_cuboid_size: int = 0
    sum_shortest_sides: int

    while num_cuboids <= limit:
        max_cuboid_size += 1
        for sum_shortest_sides in range(2, 2 * max_cuboid_size + 1):
            if sqrt(sum_shortest_sides**2 + max_cuboid_size**2).is_integer():
                num_cuboids += (
                    min(max_cuboid_size, sum_shortest_sides // 2)
                    - max(1, sum_shortest_sides - max_cuboid_size)
                    + 1
                )

    return max_cuboid_size


if __name__ == "__main__":
    print(f"{solution() = }")
