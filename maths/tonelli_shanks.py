"""
Tonelli-Shanks algorithm for modular square roots.

Given an odd prime modulus ``prime`` and an integer ``residue``, find an
integer ``root`` such that ``root ** 2 ≡ residue (mod prime)``, or report that
no square root exists.

The algorithm is efficient when ``prime ≡ 3 (mod 4)`` (a single
exponentiation) and uses the full Tonelli-Shanks procedure for
``prime ≡ 1 (mod 4)``.

https://en.wikipedia.org/wiki/Tonelli%E2%80%93Shanks_algorithm
"""

from __future__ import annotations


def legendre_symbol(residue: int, prime: int) -> int:
    """
    Compute the Legendre symbol (residue / prime).

    Returns 1 if residue is a quadratic residue modulo prime (and residue
    is not divisible by prime), -1 if it is a non-residue, and 0 if
    residue ≡ 0 (mod prime).

    >>> legendre_symbol(2, 7)
    1
    >>> legendre_symbol(3, 7)
    -1
    >>> legendre_symbol(14, 7)
    0
    >>> legendre_symbol(5, 11)
    1
    """
    if prime <= 2 or prime % 2 == 0:
        raise ValueError("prime must be an odd prime")
    symbol = pow(residue % prime, (prime - 1) // 2, prime)
    return -1 if symbol == prime - 1 else symbol


def tonelli_shanks(residue: int, prime: int) -> int:
    """
    Return a modular square root of ``residue`` modulo odd prime ``prime``.

    If both roots exist, the smaller non-negative representative is returned.
    Raises ValueError when ``residue`` is not a quadratic residue, or when
    ``prime`` is not a valid odd prime modulus for this routine.

    >>> tonelli_shanks(5, 41)
    13
    >>> pow(13, 2, 41)
    5
    >>> tonelli_shanks(2, 7)
    3
    >>> pow(3, 2, 7)
    2
    >>> tonelli_shanks(10, 13)
    6
    >>> tonelli_shanks(0, 11)
    0
    >>> tonelli_shanks(8, 17)
    5
    >>> pow(5, 2, 17)
    8
    >>> tonelli_shanks(3, 7)
    Traceback (most recent call last):
        ...
    ValueError: 3 is not a quadratic residue modulo 7
    >>> tonelli_shanks(5, 4)
    Traceback (most recent call last):
        ...
    ValueError: prime must be an odd prime
    >>> tonelli_shanks(5, 1)
    Traceback (most recent call last):
        ...
    ValueError: prime must be an odd prime
    """
    if prime <= 2 or prime % 2 == 0:
        raise ValueError("prime must be an odd prime")

    residue %= prime
    if residue == 0:
        return 0

    symbol = legendre_symbol(residue, prime)
    if symbol != 1:
        message = f"{residue} is not a quadratic residue modulo {prime}"
        raise ValueError(message)
    # Fast path: prime ≡ 3 (mod 4)
    if prime % 4 == 3:
        root = pow(residue, (prime + 1) // 4, prime)
        return min(root, prime - root)

    # Write prime - 1 = q * 2^s with q odd
    exponent_q = prime - 1
    power_of_two_s = 0
    while exponent_q % 2 == 0:
        exponent_q //= 2
        power_of_two_s += 1

    # Find a quadratic non-residue z
    non_residue = 2
    while legendre_symbol(non_residue, prime) != -1:
        non_residue += 1

    modular_c = pow(non_residue, exponent_q, prime)
    modular_r = pow(residue, (exponent_q + 1) // 2, prime)
    modular_t = pow(residue, exponent_q, prime)
    remaining_s = power_of_two_s

    while modular_t != 1:
        # Find the least i such that t^(2^i) ≡ 1 (mod prime)
        test_power = modular_t
        least_i = 0
        for candidate_i in range(1, remaining_s):
            test_power = pow(test_power, 2, prime)
            if test_power == 1:
                least_i = candidate_i
                break
        else:
            message = f"{residue} is not a quadratic residue modulo {prime}"
            raise ValueError(message)
        modular_b = pow(modular_c, 1 << (remaining_s - least_i - 1), prime)
        modular_r = (modular_r * modular_b) % prime
        modular_c = pow(modular_b, 2, prime)
        modular_t = (modular_t * modular_c) % prime
        remaining_s = least_i

    return min(modular_r, prime - modular_r)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
