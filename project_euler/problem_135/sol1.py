"""
Project Euler Problem 135: https://projecteuler.net/problem=135

Given the positive integers, x, y, and z, are consecutive terms of an arithmetic
progression, the least value of the positive integer, n, for which the equation,
x2 − y2 − z2 = n, has exactly two solutions is n = 27:

342 − 272 − 202 = 122 − 92 − 62 = 27

It turns out that n = 1155 is the least value which has exactly ten solutions.

How many values of n less than one million have exactly ten distinct solutions?


Taking x, y, z of the form a + d, a, a - d respectively, the given equation reduces to
a * (4d - a) = n.
Calculating no of solutions for every n till 1 million by fixing a, and n must be a
multiple of a. Total no of steps = n * (1/1 + 1/2 + 1/3 + 1/4 + ... + 1/n), so roughly
O(nlogn) time complexity.
"""


def solution(limit: int = 1000000) -> int:
    """
    returns the values of n less than or equal to the limit
    have exactly ten distinct solutions.
    >>> solution(100)
    0
    >>> solution(10000)
    45
    >>> solution(50050)
    292
    """
    limit = limit + 1
    frequency = [0] * limit
    for first_term in range(1, limit):
        for n in range(first_term, limit, first_term):
            common_difference = first_term + n / first_term
            if common_difference % 4:  # d must be divisible by 4
                continue
            else:
                common_difference /= 4
                if (
                    first_term > common_difference
                    and first_term < 4 * common_difference
                ):  # since x, y, z are positive integers
                    frequency[n] += 1  # so z > 0, a > d and 4d < a

    count = sum(1 for x in frequency[1:limit] if x == 10)

    return count


if __name__ == "__main__":
    print(f"{solution() = }")
