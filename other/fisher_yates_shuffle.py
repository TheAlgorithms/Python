#!/usr/bin/python
# encoding=utf8
"""
The Fisher–Yates shuffle is an algorithm for generating a random permutation of a finite sequence.
Time complexity: O(n)

For more details visit
https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
"""

import random


# The modern version of the Fisher–Yates shuffle,
# designed for computer use, was introduced by Richard Durstenfeld in 1964
def fisher_yates_shuffle(sequence: []) -> []:
    for i in range(len(sequence) - 1, 0, -1):
        j = random.randint(0, i)
        sequence[i], sequence[j] = sequence[j], sequence[i]

    return sequence


# was published in 1986 by Sandra Sattolo
# for generating uniformly distributed cycles of (maximal) length n
def sattoloCycle(sequence: []) -> []:
    for i in range(len(sequence) - 1, 0, -1):
        j = random.randint(0, i - 1)
        sequence[i], sequence[j] = sequence[j], sequence[i]

    return sequence


if __name__ == "__main__":
    integers = [0, 1, 2, 3, 4, 5, 6, 7]
    strings = ["python", "says", "hello", "!"]
    print("Fisher-Yates Shuffle:")
    print("List", integers, strings)
    print("FY Shuffle", fisher_yates_shuffle(integers), fisher_yates_shuffle(strings))
    print("Sattolo's algorithm", sattoloCycle(integers), sattoloCycle(strings))
