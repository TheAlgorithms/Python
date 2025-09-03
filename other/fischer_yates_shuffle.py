#!/usr/bin/python
"""
The Fisher-Yates shuffle is an algorithm for generating a random permutation of a
finite sequence.
For more details visit
wikipedia/Fischer-Yates-Shuffle.
"""

import random
from typing import Any


def fisher_yates_shuffle(data: list) -> list[Any]:
    """
    In-place random shuffle of a list using the Fisher–Yates algorithm.

    The output is a permutation of the input. Since the operation is random,
    we assert permutation properties rather than exact order in doctests.

    >>> data = [1, 2, 3, 4]
    >>> shuffled = fisher_yates_shuffle(data.copy())
    >>> sorted(shuffled) == [1, 2, 3, 4]
    True
    >>> len(shuffled) == len(set(shuffled))
    True
    """
    for _ in range(len(data)):
        a = random.randint(0, len(data) - 1)
        b = random.randint(0, len(data) - 1)
        data[a], data[b] = data[b], data[a]
    return data


if __name__ == "__main__":
    integers = [0, 1, 2, 3, 4, 5, 6, 7]
    strings = ["python", "says", "hello", "!"]
    print("Fisher-Yates Shuffle:")
    print("List", integers, strings)
    print("FY Shuffle", fisher_yates_shuffle(integers), fisher_yates_shuffle(strings))
