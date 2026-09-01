"""
Tonelli-Shanks Algorithm for Modular Square Roots.

Reference: https://en.wikipedia.org/wiki/Tonelli%E2%80%93Shanks_algorithm
Reference: https://cp-algorithms.com/algebra/tonelli-shanks.html

Given an integer residue and an odd prime modulus, the Tonelli-Shanks algorithm
computes an integer root such that:
    root^2 = residue (mod modulus)
If residue is a quadratic residue modulo modulus, it returns two solutions (r1, r2)
where r1 <= r2 and r1 + r2 = modulus (or (0, 0) if residue = 0 mod modulus).
"""

from __future__ import annotations


def legendre_symbol(number: int, modulus: int) -> int:
    """
    Compute the Legendre Symbol (number / modulus) modulo an odd prime modulus.

    Euler's Criterion states that:
        (number / modulus) = number^((modulus - 1) / 2) (mod modulus)

    Returns:
         1 if number is a quadratic residue modulo modulus and number != 0 (mod modulus)
        -1 if number is a quadratic non-residue modulo modulus
         0 if number = 0 (mod modulus)

    >>> legendre_symbol(5, 11)
    1
    >>> legendre_symbol(2, 7)
    1
    >>> legendre_symbol(3, 7)
    -1
    >>> legendre_symbol(0, 7)
    0
    >>> legendre_symbol(14, 7)
    0
    """
    symbol = pow(number % modulus, (modulus - 1) // 2, modulus)
    return symbol if symbol <= 1 else -1


def tonelli_shanks(residue: int, modulus: int) -> tuple[int, int]:
    """
    Find solutions to root^2 = residue (mod modulus) for an odd prime modulus
    using the Tonelli-Shanks algorithm.

    Time Complexity: O(log^2 modulus) on average.

    Parameters:
        residue: The integer whose square root modulo modulus is to be found.
        modulus: An odd prime modulus.

    Returns:
        A tuple (r1, r2) containing the two square roots modulo modulus (r1 <= r2).

    Raises:
        ValueError: If modulus is not an odd prime >= 3.
        ValueError: If residue is not a quadratic residue modulo modulus.

    >>> tonelli_shanks(5, 11)
    (4, 7)
    >>> tonelli_shanks(10, 13)
    (6, 7)
    >>> tonelli_shanks(0, 7)
    (0, 0)
    >>> tonelli_shanks(2, 7)
    (3, 4)
    >>> tonelli_shanks(28, 7)
    (0, 0)
    >>> tonelli_shanks(3, 7)
    Traceback (most recent call last):
        ...
    ValueError: 3 is not a quadratic residue modulo 7.
    >>> tonelli_shanks(5, 4)
    Traceback (most recent call last):
        ...
    ValueError: Modulus p must be an odd prime (got 4).
    >>> tonelli_shanks(5, 1)
    Traceback (most recent call last):
        ...
    ValueError: Modulus p must be an odd prime (got 1).
    """
    if modulus <= 2 or modulus % 2 == 0:
        msg = f"Modulus p must be an odd prime (got {modulus})."
        raise ValueError(msg)

    residue = residue % modulus
    if residue == 0:
        return 0, 0

    if legendre_symbol(residue, modulus) != 1:
        msg = f"{residue} is not a quadratic residue modulo {modulus}."
        raise ValueError(msg)

    # Factor out powers of 2 from modulus - 1: modulus - 1 = odd_factor * 2^two_power
    odd_factor = modulus - 1
    two_power = 0
    while odd_factor % 2 == 0:
        odd_factor //= 2
        two_power += 1

    # Case 1: modulus = 3 (mod 4), two_power = 1
    if two_power == 1:
        root = pow(residue, (modulus + 1) // 4, modulus)
        return min(root, modulus - root), max(root, modulus - root)

    # Case 2: Search for a quadratic non-residue non_residue modulo modulus
    non_residue = 2
    while legendre_symbol(non_residue, modulus) != -1:
        non_residue += 1

    multiplier = pow(non_residue, odd_factor, modulus)
    root = pow(residue, (odd_factor + 1) // 2, modulus)
    reduced_residue = pow(residue, odd_factor, modulus)
    exponent = two_power

    while reduced_residue != 1:
        # Find the smallest power_step (0 < power_step < exponent)
        # such that reduced_residue^(2^power_step) = 1 (mod modulus)
        power_step = 0
        temp_residue = reduced_residue
        while temp_residue != 1 and power_step < exponent:
            temp_residue = pow(temp_residue, 2, modulus)
            power_step += 1

        if power_step == exponent:
            msg = f"Failed to find square root for {residue} mod {modulus}."
            raise ValueError(msg)

        step_multiplier = pow(multiplier, 1 << (exponent - power_step - 1), modulus)
        step_multiplier_squared = (step_multiplier * step_multiplier) % modulus
        root = (root * step_multiplier) % modulus
        reduced_residue = (reduced_residue * step_multiplier_squared) % modulus
        multiplier = step_multiplier_squared
        exponent = power_step

    return min(root, modulus - root), max(root, modulus - root)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
