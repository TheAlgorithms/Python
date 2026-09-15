from maths.greatest_common_divisor import gcd_by_iterative


def find_mod_inverse(a: int, m: int) -> int:
    """
    Find the modular multiplicative inverse of a modulo m.

    The modular multiplicative inverse of a modulo m is an integer x such that:
    (a * x) % m = 1

    This function uses the Extended Euclidean Algorithm to find the inverse.
    An inverse exists if and only if a and m are coprime (gcd(a, m) = 1).

    Args:
        a: The integer to find the inverse of
        m: The modulus

    Returns:
        The modular multiplicative inverse of a modulo m

    Raises:
        ValueError: If gcd(a, m) != 1 (inverse does not exist)

    Reference:
        https://en.wikipedia.org/wiki/Modular_multiplicative_inverse

    Examples:
    >>> find_mod_inverse(3, 7)
    5
    >>> (3 * 5) % 7  # Verify: 3 * 5 ≡ 1 (mod 7)
    1
    >>> find_mod_inverse(3, 10)
    7
    >>> (3 * 7) % 10  # Verify: 3 * 7 ≡ 1 (mod 10)
    1
    >>> find_mod_inverse(4, 11)
    3
    >>> (4 * 3) % 11  # Verify: 4 * 3 ≡ 1 (mod 11)
    1
    >>> find_mod_inverse(7, 26)
    15
    >>> (7 * 15) % 26  # Verify: 7 * 15 ≡ 1 (mod 26)
    1
    >>> find_mod_inverse(1, 5)
    1
    >>> find_mod_inverse(5, 11)
    9
    >>> find_mod_inverse(2, 4)
    Traceback (most recent call last):
        ...
    ValueError: mod inverse of 2 and 4 does not exist
    >>> find_mod_inverse(6, 9)
    Traceback (most recent call last):
        ...
    ValueError: mod inverse of 6 and 9 does not exist
    >>> find_mod_inverse(10, 20)
    Traceback (most recent call last):
        ...
    ValueError: mod inverse of 10 and 20 does not exist
    """
    if gcd_by_iterative(a, m) != 1:
        msg = f"mod inverse of {a!r} and {m!r} does not exist"
        raise ValueError(msg)
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m
