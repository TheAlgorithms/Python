# -*- coding: utf-8 -*-
"""
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
from __future__ import print_function

try:
    raw_input  # Python 2
except NameError:
    raw_input = input  # Python 3


def solution(n):
    """Returns the number under n that generates the longest sequence using the
    formula:
    n → n/2 (n is even)
    n → 3n + 1 (n is odd)
 
    >>> solution(1000000)
    {'counter': 525, 'largest_number': 837799}
    >>> solution(200)
    {'counter': 125, 'largest_number': 171}
    >>> solution(5000)
    {'counter': 238, 'largest_number': 3711}
    >>> solution(15000)
    {'counter': 276, 'largest_number': 13255}
    """
    largest_number = 0
    pre_counter = 0

    for input1 in range(n):
        counter = 1
        number = input1

        while number > 1:
            if number % 2 == 0:
                number /= 2
                counter += 1
            else:
                number = (3 * number) + 1
                counter += 1

        if counter > pre_counter:
            largest_number = input1
            pre_counter = counter
    return {"counter": pre_counter, "largest_number": largest_number}


if __name__ == "__main__":
    result = solution(int(raw_input().strip()))
    print(
        (
            "Largest Number:",
            result["largest_number"],
            "->",
            result["counter"],
            "digits",
        )
    )
