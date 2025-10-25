"""
Simon's Algorithm (Classical Simulation)

Simon's algorithm finds a hidden bitstring s such that
f(x) = f(y) if and only if x XOR y = s.

Here we simulate the mapping behavior classically to
illustrate how the hidden period can be discovered by
analyzing collisions in f(x).

References:
https://en.wikipedia.org/wiki/Simon's_problem
"""

from collections.abc import Callable
from itertools import product


def xor_bits(a: list[int], b: list[int]) -> list[int]:
    """
    Return the bitwise XOR of two equal-length bit lists.

    >>> xor_bits([1, 0, 1], [1, 1, 0])
    [0, 1, 1]
    """
    if len(a) != len(b):
        raise ValueError("Bit lists must be of equal length.")
    return [x ^ y for x, y in zip(a, b)]


def simons_algorithm(f: Callable[[list[int]], list[int]], n: int) -> list[int]:

    """
    Simulate Simon's algorithm classically to find the hidden bitstring s.

    Args:
        f: A function mapping n-bit input to n-bit output.
        n: Number of bits in the input.

    Returns:
        The hidden bitstring s as a list of bits.

    >>> # Example with hidden bitstring s = [1, 0, 1]
    >>> s = [1, 0, 1]
    >>> def f(x):
    ...     mapping = {
    ...         (0,0,0): (1,1,0),
    ...         (1,0,1): (1,1,0),
    ...         (0,0,1): (0,1,1),
    ...         (1,0,0): (0,1,1),
    ...         (0,1,0): (1,0,1),
    ...         (1,1,1): (1,0,1),
    ...         (0,1,1): (0,0,0),
    ...         (1,1,0): (0,0,0),
    ...     }
    ...     return mapping[tuple(x)]
    >>> simons_algorithm(f, 3)
    [1, 0, 1]
    """
    mapping: dict[tuple[int, ...], tuple[int, ...]] = {}
    inputs = list(product([0, 1], repeat=n))

    for x in inputs:
        fx = tuple(f(list(x)))
        if fx in mapping:
            y = mapping[fx]
            return xor_bits(list(x), list(y))
        mapping[fx] = x

    # If no collision found, function might be constant
    return [0] * n


if __name__ == "__main__":
    import doctest

    doctest.testmod()
