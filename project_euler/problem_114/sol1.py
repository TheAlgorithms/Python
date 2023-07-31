"""
Project Euler Problem 114: https://projecteuler.net/problem=114

A row measuring seven units in length has red blocks with a minimum length
of three units placed on it, such that any two red blocks
(which are allowed to be different lengths) are separated by at least one grey square.
There are exactly seventeen ways of doing this.

    |g|g|g|g|g|g|g|    |r,r,r|g|g|g|g|

    |g|r,r,r|g|g|g|    |g|g|r,r,r|g|g|

    |g|g|g|r,r,r|g|    |g|g|g|g|r,r,r|

    |r,r,r|g|r,r,r|    |r,r,r,r|g|g|g|

    |g|r,r,r,r|g|g|    |g|g|r,r,r,r|g|

    |g|g|g|r,r,r,r|    |r,r,r,r,r|g|g|

    |g|r,r,r,r,r|g|    |g|g|r,r,r,r,r|

    |r,r,r,r,r,r|g|    |g|r,r,r,r,r,r|

    |r,r,r,r,r,r,r|

How many ways can a row measuring fifty units in length be filled?

NOTE: Although the example above does not lend itself to the possibility,
in general it is permitted to mix block sizes. For example,
on a row measuring eight units in length you could use red (3), grey (1), and red (4).
"""


def solution(length: int = 50) -> int:
    """
    Returns the number of ways a row of the given length can be filled

    >>> solution(7)
    17
    """

    ways_number = [1] * (length + 1)

    for row_length in range(3, length + 1):
        for block_length in range(3, row_length + 1):
            for block_start in range(row_length - block_length):
                ways_number[row_length] += ways_number[
                    row_length - block_start - block_length - 1
                ]

            ways_number[row_length] += 1

    return ways_number[length]


if __name__ == "__main__":
    print(f"{solution() = }")
