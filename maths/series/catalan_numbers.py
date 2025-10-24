"""
Catalan Numbers
Reference: https://en.wikipedia.org/wiki/Catalan_number

Catalan numbers C_n are a sequence of natural numbers that occur in
various counting problems, often recursively defined.
This implementation uses the dynamic programming approach based on the
recursive definition: C_{n+1} = sum_{i=0}^{n} C_i C_{n-i}
"""

from __future__ import annotations

def catalan_numbers(count: int) -> list[int]:
    """
    Generates the first 'count' Catalan numbers (C_0, C_1, ..., C_{count-1}).

    :param count: The number of Catalan numbers to generate.
    :return: A list of integers representing the Catalan numbers.

    Examples:
    >>> catalan_numbers(0)
    []
    >>> catalan_numbers(1)
    [1]
    >>> catalan_numbers(5)
    [1, 1, 2, 5, 14]
    >>> # C_6 = 42, C_7 = 132
    >>> catalan_numbers(8)
    [1, 1, 2, 5, 14, 42, 132, 429]
    >>> catalan_numbers(-5)
    Traceback (most recent call last):
        ...
    ValueError: Count must be a non-negative integer.
    """
    if not isinstance(count, int):
        raise ValueError("Count must be a non-negative integer.")
    if count < 0:
        raise ValueError("Count must be a non-negative integer.")

    if count == 0:
        return []

    # Initialize the sequence with the base case C_0 = 1
    sequence: list[int] = [1]

    # Dynamically compute C_n for n from 1 up to count - 1
    # We already have C_0, so we need 'count - 1' more elements.
    for n in range(1, count):
        c_n = 0
        # The recursive formula is C_n = sum_{i=0}^{n-1} C_i * C_{n-1-i}
        # C_n is the sum of products of previously computed Catalan numbers.
        # sequence currently holds [C_0, C_1, ..., C_{n-1}]
        # The length of 'sequence' is 'n'
        for i in range(n):
            # C_i * C_{n-1-i}
            c_n += sequence[i] * sequence[n - 1 - i]

        sequence.append(c_n)

    return sequence


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    try:
        num = int(input("Enter the number of Catalan numbers to generate: "))
        if num < 0:
            print("Please enter a non-negative integer.")
        else:
            print(f"The first {num} Catalan numbers are: {catalan_numbers(num)}")
    except ValueError:
        print("Invalid input. Please enter an integer.")