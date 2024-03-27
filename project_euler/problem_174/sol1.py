"""
Project Euler Problem 174: https://projecteuler.net/problem=174

We shall define a square lamina to be a square outline with a square "hole" so that
the shape possesses vertical and horizontal symmetry.

Given eight tiles it is possible to form a lamina in only one way: 3x3 square with a
1x1 hole in the middle. However, using thirty-two tiles it is possible to form two
distinct laminae.

If t represents the number of tiles used, we shall say that t = 8 is type L(1) and
t = 32 is type L(2).

Let N(n) be the number of t ≤ 1000000 such that t is type L(n); for example,
N(15) = 832.

What is ∑ N(n) for 1 ≤ n ≤ 10?
"""

from collections import defaultdict
from math import ceil, sqrt


def solution(t_limit: int = 1000000, n_limit: int = 10) -> int:
    """
    Return the sum of N(n) for 1 <= n <= n_limit.

    >>> solution(1000,5)
    222
    >>> solution(1000,10)
    249
    >>> solution(10000,10)
    2383
    """
    count: defaultdict = defaultdict(int)

    for outer_width in range(3, (t_limit // 4) + 2):
        if outer_width * outer_width > t_limit:
            hole_width_lower_bound = max(
                ceil(sqrt(outer_width * outer_width - t_limit)), 1
            )
        else:
            hole_width_lower_bound = 1

        hole_width_lower_bound += (outer_width - hole_width_lower_bound) % 2

        for hole_width in range(hole_width_lower_bound, outer_width - 1, 2):
            count[outer_width * outer_width - hole_width * hole_width] += 1

    return sum(1 for n in count.values() if 1 <= n <= n_limit)


if __name__ == "__main__":
    print(f"{solution() = }")
