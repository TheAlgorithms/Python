#!/usr/bin/python
"""
The Fisher–Yates shuffle is an algorithm for generating a random permutation of a finite sequence.
For more details visit
wikipedia/Fischer-Yates-Shuffle.
"""
import random


def FYshuffle(list):
    for i in range(len(list)):
        a = random.randint(0, len(list) - 1)
        b = random.randint(0, len(list) - 1)
        list[a], list[b] = list[b], list[a]
    return list


if __name__ == "__main__":
    integers = [0, 1, 2, 3, 4, 5, 6, 7]
    strings = ["python", "says", "hello", "!"]
    print("Fisher-Yates Shuffle:")
    print("List", integers, strings)
    print("FY Shuffle", FYshuffle(integers), FYshuffle(strings))
