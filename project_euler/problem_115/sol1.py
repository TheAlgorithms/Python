"""
Project Euler Problem 115: https://projecteuler.net/problem=115

NOTE: This is a more difficult version of Problem 114
(https://projecteuler.net/problem=114).

A row measuring n units in length has red blocks
with a minimum length of m units placed on it, such that any two red blocks
(which are allowed to be different lengths) are separated by at least one black square.

Let the fill-count function, F(m, n),
represent the number of ways that a row can be filled.

For example, F(3, 29) = 673135 and F(3, 30) = 1089155.

That is, for m = 3, it can be seen that n = 30 is the smallest value
for which the fill-count function first exceeds one million.

In the same way, for m = 10, it can be verified that
F(10, 56) = 880711 and F(10, 57) = 1148904, so n = 57 is the least value
for which the fill-count function first exceeds one million.

For m = 50, find the least value of n
for which the fill-count function first exceeds one million.
"""

from itertools import count


def solution(min_block_length: int = 50) -> int:
    """
    Returns for given minimum block length the least value of n
    for which the fill-count function first exceeds one million

    >>> solution(3)
    30

    >>> solution(10)
    57
    """

    fill_count_functions = [1] * min_block_length

    for n in count(min_block_length):
        fill_count_functions.append(1)

        for block_length in range(min_block_length, n + 1):
            for block_start in range(n - block_length):
                fill_count_functions[n] += fill_count_functions[
                    n - block_start - block_length - 1
                ]

            fill_count_functions[n] += 1

        if fill_count_functions[n] > 1_000_000:
            break

    return n


if __name__ == "__main__":
    print(f"{solution() = }")
