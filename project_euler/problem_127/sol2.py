"""
Problem 127: https://projecteuler.net/problem=127

Description:

The radicalical of n, radical(n), is the product of distinct prime factors of
n. For example, 504 = 23 × 32 × 7, so radical(504) = 2 × 3 × 7 = 42.

We shall define the triplet of positive integers (a, b, c) to be an abc-hit if:

GCD(a, b) = GCD(a, c) = GCD(b, c) = 1
a < b
a + b = c
radical(abc) < c
For example, (5, 27, 32) is an abc-hit, because:

GCD(5, 27) = GCD(5, 32) = GCD(27, 32) = 1
5 < 27
5 + 27 = 32
radical(4320) = 30 < 32
It turns out that abc-hits are quite rare and there are only thirty-one
abc-hits for c < 1000, with ∑c = 12523.

Find ∑c for c < 120000.

Solution:

A Naive solution would be to generate all the triplets and check if they are
abc-hits:
    for c in range(2, LIMIT):
        for a in range(1, c):
            b = c - a
            if a < b and math.gcd(a, b) == 1 and math.gcd(a, c) == 1 and
            math.gcd(b, c) == 1 and radical(a * b * c) < c:
                ans += c

Observations:
2 <= radical(n) <= n (for all n > 1).
gcd(c,b) = gcd(a+b,b) = gcd(a,b) = gcd(a,a+b) = gcd(a,c)(Euclid's GCD
algorithm Source: https://en.wikipedia.org/wiki/Euclidean_algorithm).
radical(a * b * c) = radical(a) * radical(b) * radical(c) (Since {a, b, c}
are mutually coprime).

Idea:
We sort 'a' values in ascending order of radical(a) and stop when
radical(a) * radical(c) >= c instead of checking for all values of
a in the range [1,c). We only find gcd(a,b) instead of gcd(a,b), gcd(a,c)
and gcd(b,c) separately.
"""


def greatest_common_divisor(a: int, b: int) -> int:
    """
    Returns the greatest common divisor of a and b.
    >>> greatest_common_divisor(10, 15)
    5
    >>> greatest_common_divisor(3, 7)
    1
    >>> greatest_common_divisor(10, 10)
    10
    """
    while b != 0:
        a, b = b, a % b
    return a


def solution(limit: int = 120000) -> int:
    """
    Return the sum of all c < limit such that (a, b, c) is an abc-hit.
    >>> solution(1000)
    12523
    >>> solution(10000)
    441085
    >>> solution(100000)
    14125034
    >>> solution(120000)
    18407904
    """

    # Modified Sieve of Eratosthenes
    # (Source: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
    # to find Radicals.
    radicals = [0] + [1] * (limit - 1)
    for i in range(2, len(radicals)):
        if radicals[i] == 1:
            for j in range(i, len(radicals), i):
                radicals[j] *= i

    # Sort a values in ascending order of radical(a).
    sorted_radicals = sorted((radical, n) for (n, radical) in
                             enumerate(radicals))
    sorted_radicals = sorted_radicals[1:]  # Remove (0, 0) from the list.

    ans = 0
    for c in range(2, limit):
        for (radical, a) in sorted_radicals:
            radical *= radicals[c]
            if radical >= c:
                break
            b = c - a
            if (a < b and greatest_common_divisor(a, b) == 1
                    and radical * radicals[b] < c):
                ans += c
    return ans


if __name__ == "__main__":
    print(solution())
