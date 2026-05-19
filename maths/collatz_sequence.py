"""
The Collatz conjecture is a famous unsolved problem in mathematics. Given a starting
positive integer, define the following sequence:
- If the current term n is even, then the next term is n/2.
- If the current term n is odd, then the next term is 3n + 1.
The conjecture claims that this sequence will always reach 1 for any starting number.

Other names for this problem include the 3n + 1 problem, the Ulam conjecture, Kakutani's
problem, the Thwaites conjecture, Hasse's algorithm, the Syracuse problem, and the
hailstone sequence.

Reference: https://en.wikipedia.org/wiki/Collatz_conjecture
"""

from __future__ import annotations

from collections.abc import Generator


def collatz_sequence(n: int) -> Generator[int]:
    """
    Generate the Collatz sequence starting at n.
    >>> tuple(collatz_sequence(2.1))
    Traceback (most recent call last):
        ...
    Exception: Sequence only defined for positive integers
    >>> tuple(collatz_sequence(0))
    Traceback (most recent call last):
        ...
    Exception: Sequence only defined for positive integers
    >>> tuple(collatz_sequence(4))
    (4, 2, 1)
    >>> tuple(collatz_sequence(11))
    (11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1)
    >>> tuple(collatz_sequence(31))     # doctest: +NORMALIZE_WHITESPACE
    (31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137,
    412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593,
    1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425,
    1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644,
    1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732,
    866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53,
    160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1)
    >>> tuple(collatz_sequence(43))     # doctest: +NORMALIZE_WHITESPACE
    (43, 130, 65, 196, 98, 49, 148, 74, 37, 112, 56, 28, 14, 7, 22, 11, 34, 17, 52, 26,
    13, 40, 20, 10, 5, 16, 8, 4, 2, 1)
    """
    if not isinstance(n, int) or n < 1:
        raise Exception("Sequence only defined for positive integers")

    yield n
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        yield n


def main():
    n = int(input("Your number: "))
    sequence = tuple(collatz_sequence(n))
    print(sequence)
    print(f"Collatz sequence from {n} took {len(sequence)} steps.")


if __name__ == "__main__":
    main()
