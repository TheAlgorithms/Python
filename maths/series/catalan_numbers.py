"""
Catalan Numbers
Reference: https://en.wikipedia.org/wiki/Catalan_number

Catalan numbers C_n are a sequence of natural numbers that occur in
various counting problems, often recursively defined.
They can be computed directly using binomial coefficients:
C_n = 1/(n+1) * C(2n, n)
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
    if not isinstance(count, int) or count < 0:
        raise ValueError("Count must be a non-negative integer.")

    if count == 0:
        return []

    sequence: list[int] = []

    for n in range(count):
        # Calculate C_n using the formula: C_n = (1 / (n + 1)) * (2n choose n)
        # Using math.comb for direct, efficient calculation of binomial coefficient
        # math.comb(N, K) computes N! / (K! * (N - K)!)
        try:
            binomial_coeff = math.comb(2 * n, n)
            c_n = binomial_coeff // (n + 1)
            sequence.append(c_n)
        except AttributeError:
            # Fallback for older Python versions (< 3.8) without math.comb
            # This uses the factorial-based formula: (2n)! / ((n+1)! n!)
            if n == 0:
                sequence.append(1)
            else:
                numerator = math.factorial(2 * n)
                denominator = math.factorial(n + 1) * math.factorial(n)
                sequence.append(numerator // denominator)

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
