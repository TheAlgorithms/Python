#!/usr/bin/python
"""
The Fisher–Yates shuffle is an algorithm for generating a random permutation of a
finite sequence.
For more details visit
wikipedia/Fischer-Yates-Shuffle.
"""
import random


def fisher_yates_shuffle(data: list) -> list:
    for datum in data:
        a = random.randint(0, len(data) - 1)
        b = random.randint(0, len(data) - 1)
        [a], [b] = [b], [a]
    return data


if __name__ == "__main__":
    integers = [0, 1, 2, 3, 4, 5, 6, 7]
    strings = ["python", "says", "hello", "!"]
    print("Fisher-Yates Shuffle:")
    print("List", integers, strings)
    print("FY Shuffle", fisher_yates_shuffle(integers), fisher_yates_shuffle(strings))
