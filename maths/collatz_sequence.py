from __future__ import annotations


def collatz_sequence(n: int) -> list[int]:
    """
    Collatz conjecture: start with any positive integer n. The next term is
    obtained as follows:
        If n term is even, the next term is: n / 2 .
        If n is odd, the next term is: 3 * n + 1.

    The conjecture states the sequence will always reach 1 for any starting value n.
    Example:
    >>> collatz_sequence(2.1)
    Traceback (most recent call last):
        ...
    Exception: Sequence only defined for natural numbers
    >>> collatz_sequence(0)
    Traceback (most recent call last):
        ...
    Exception: Sequence only defined for natural numbers
    >>> collatz_sequence(43)  # doctest: +NORMALIZE_WHITESPACE
    [43, 130, 65, 196, 98, 49, 148, 74, 37, 112, 56, 28, 14, 7,
     22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """

    if not isinstance(n, int) or n < 1:
        raise Exception("Sequence only defined for natural numbers")

    sequence = [n]
    while n != 1:
        n = 3 * n + 1 if n & 1 else n // 2
        sequence.append(n)
    return sequence


def main():
    n = 43
    sequence = collatz_sequence(n)
    print(sequence)
    print(f"collatz sequence from {n} took {len(sequence)} steps.")


if __name__ == "__main__":
    main()
