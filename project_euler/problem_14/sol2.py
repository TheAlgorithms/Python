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
from typing import List


def collatz_sequence(n: int) -> List[int]:
    """Returns the Collatz sequence for n."""
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


def solution(n: int = 1000000) -> int:
    """Returns the number under n that generates the longest Collatz sequence.

    # The code below has been commented due to slow execution affecting Travis.
    # >>> solution(1000000)
    # 837799
    >>> solution(200)
    171
    >>> solution(5000)
    3711
    >>> solution(15000)
    13255
    """

    result = max([(len(collatz_sequence(i)), i) for i in range(1, n)])
    return result[1]


if __name__ == "__main__":
    print(solution(int(input().strip())))
