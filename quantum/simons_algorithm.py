"""
Simon's Algorithm (Classical Simulation)

Simon's algorithm finds a hidden bitstring s such that
f(input_bits) = f(other_bits) if and only if input_bits XOR other_bits = s.

Here we simulate the mapping behavior classically to
illustrate how the hidden period can be discovered by
analyzing collisions in f(input_bits).

References:
https://en.wikipedia.org/wiki/Simon's_problem
"""

from collections.abc import Callable
from itertools import product


def xor_bits(bits1: list[int], bits2: list[int]) -> list[int]:
    """
    Return the bitwise XOR of two equal-length bit lists.

    >>> xor_bits([1, 0, 1], [1, 1, 0])
    [0, 1, 1]
    """
    if len(bits1) != len(bits2):
        raise ValueError("Bit lists must be of equal length.")
    return [x ^ y for x, y in zip(bits1, bits2)]


def simons_algorithm(f: Callable[[list[int]], list[int]], num_bits: int) -> list[int]:
    """
    Simulate Simon's algorithm classically to find the hidden bitstring s.

    Args:
        f: A function mapping n-bit input to n-bit output.
        num_bits: Number of bits in the input.

    Returns:
        The hidden bitstring s as a list of bits.

    >>> # Example with hidden bitstring s = [1, 0, 1]
    >>> s = [1, 0, 1]
    >>> def f(input_bits):
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
    ...     return mapping[tuple(input_bits)]
    >>> simons_algorithm(f, 3)
    [1, 0, 1]
    """
    mapping: dict[tuple[int, ...], tuple[int, ...]] = {}
    inputs = list(product([0, 1], repeat=num_bits))

    for bits in inputs:
        fx = tuple(f(list(bits)))
        if fx in mapping:
            prev_bits = mapping[fx]
            return xor_bits(list(bits), list(prev_bits))
        mapping[fx] = bits

    # If no collision found, function might be constant
    return [0] * num_bits


if __name__ == "__main__":
    import doctest

    doctest.testmod()
