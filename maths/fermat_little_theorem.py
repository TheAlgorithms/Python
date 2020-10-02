"""
Python program to show the usage of Fermat's little theorem in a division

If p is a prime number, then given any integer a,
(a raised to the power of p) is congruent to (a) modulo the prime p.

Wikipedia reference: https://en.wikipedia.org/wiki/Fermat%27s_little_theorem
"""


def binary_exponentiation(a: int, n: int, mod: int) -> int:
    """
    Find a to the power of n, modulo mod.

    >>> binary_exponentiation(4, 3, 7)
    1

    >>> binary_exponentiation(2, 9, 9)
    8

    """
    if n == 0:
        return 1

    elif n % 2 == 1:
        return (binary_exponentiation(a, n - 1, mod) * a) % mod

    else:
        b = binary_exponentiation(a, n / 2, mod)
        return (b * b) % mod


def check_fermat_little_thm(a: int, p: int) -> bool:
    """
    Verifies the fermat little theorem

    # Example prime: 13
    >>> check_fermat_little_thm(400, 13)
    True

    >>> check_fermat_little_thm(22, 13)
    True

    # Example prime: 701
    >>> check_fermat_little_thm(13, 701)
    True

    >>> check_fermat_little_thm(22, 701)
    True
    """
    a_power_p = binary_exponentiation(a, p, p)
    a_mod_p = binary_exponentiation(a, 1, p)  # or just a % p

    return a_power_p == a_mod_p
