"""
Baby-step giant-step algorithm for discrete logarithms.

Solve for the smallest non-negative integer ``exponent`` such that
``base ** exponent ≡ target (mod modulus)``, assuming ``modulus`` is prime
and ``base`` is a primitive root (or at least generates ``target``).

Time and space complexity are O(sqrt(modulus)).

https://en.wikipedia.org/wiki/Baby-step_giant-step
"""

from __future__ import annotations

from math import ceil, isqrt


def baby_step_giant_step(base: int, target: int, modulus: int) -> int:
    """
    Return the discrete logarithm of ``target`` to ``base`` modulo ``modulus``.

    Finds the smallest non-negative ``exponent`` satisfying
    ``pow(base, exponent, modulus) == target % modulus``.

    Raises ValueError when no solution exists in ``0 .. modulus - 1``, or when
    the modulus is not a positive integer greater than 1.

    >>> baby_step_giant_step(2, 1, 5)
    0
    >>> baby_step_giant_step(2, 2, 5)
    1
    >>> baby_step_giant_step(2, 3, 5)
    3
    >>> pow(2, 3, 5)
    3
    >>> baby_step_giant_step(5, 8, 13)
    3
    >>> pow(5, 3, 13)
    8
    >>> baby_step_giant_step(7, 1, 11)
    0
    >>> baby_step_giant_step(3, 13, 17)
    4
    >>> baby_step_giant_step(2, 3, 1)
    Traceback (most recent call last):
        ...
    ValueError: modulus must be an integer greater than 1
    >>> baby_step_giant_step(2, 0, 7)
    Traceback (most recent call last):
        ...
    ValueError: no discrete logarithm for 0 base 2 modulo 7
    """
    if modulus <= 1:
        raise ValueError("modulus must be an integer greater than 1")

    base %= modulus
    target %= modulus

    if target == 1:
        return 0
    if base == 0:
        if target == 0:
            return 1
        raise ValueError(f"no discrete logarithm for {target} base 0 modulo {modulus}")

    # Baby steps: store base^j for j = 0 .. m-1
    step_count = ceil(isqrt(modulus - 1))
    baby_steps: dict[int, int] = {}
    value = 1
    for baby_index in range(step_count):
        if value not in baby_steps:
            baby_steps[value] = baby_index
        value = (value * base) % modulus

    # Giant step factor: base^{-m} mod modulus
    giant_factor = pow(base, -step_count, modulus)
    gamma = target
    for giant_index in range(step_count):
        if gamma in baby_steps:
            return giant_index * step_count + baby_steps[gamma]
        gamma = (gamma * giant_factor) % modulus

    raise ValueError(f"no discrete logarithm for {target} base {base} modulo {modulus}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
