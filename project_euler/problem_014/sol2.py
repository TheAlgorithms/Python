"""
Problem 14: https://projecteuler.net/problem=14

Collatz conjecture: start with any positive integer n. Next term obtained from
the previous term as follows:

If the previous term is even, the next term is one half the previous term.
If the previous term is odd, the next term is 3 times the previous term plus 1.
The conjecture states the sequence will always reach 1 regardless of starting
n.

Problem Statement:
The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
"""
from __future__ import annotations

COLLATZ_SEQUENCE_LENGTHS = {1: 1}


def collatz_sequence_length(n: int) -> int:
    """Returns the Collatz sequence length for n."""
    if n in COLLATZ_SEQUENCE_LENGTHS:
        return COLLATZ_SEQUENCE_LENGTHS[n]
    next_n = n // 2 if n % 2 == 0 else 3 * n + 1
    sequence_length = collatz_sequence_length(next_n) + 1
    COLLATZ_SEQUENCE_LENGTHS[n] = sequence_length
    return sequence_length


def solution(n: int = 1000000) -> int:
    """Returns the number under n that generates the longest Collatz sequence.

    >>> solution(1000000)
    837799
    >>> solution(200)
    171
    >>> solution(5000)
    3711
    >>> solution(15000)
    13255
    """

    result = max((collatz_sequence_length(i), i) for i in range(1, n))
    return result[1]


if __name__ == "__main__":
    print(solution(int(input().strip())))
