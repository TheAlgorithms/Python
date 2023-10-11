from __future__ import annotations


def modular_division(a: int, b: int, n: int) -> int:
    """
    Modular Division :
    An efficient algorithm for dividing b by a modulo n.

    GCD ( Greatest Common Divisor ) or HCF ( Highest Common Factor )

    Given three integers a, b, and n, such that gcd(a,n)=1 and n>1, the algorithm should
    return an integer x such that 0≤x≤n−1, and  b/a=x(modn) (that is, b=ax(modn)).

    Theorem:
    a has a multiplicative inverse modulo n iff gcd(a,n) = 1


    This find x = b*a^(-1) mod n
    Uses ExtendedEuclid to find the inverse of a

    >>> modular_division(4,8,5)
    2

    >>> modular_division(3,8,5)
    1

    >>> modular_division(4, 11, 5)
    4

    """
    assert n > 1
    assert a > 0
    assert greatest_common_divisor(a, n) == 1
    (d, t, s) = extended_gcd(n, a)  # Implemented below
    x = (b * s) % n
    return x


def invert_modulo(a: int, n: int) -> int:
    """
    This function find the inverses of a i.e., a^(-1)

    >>> invert_modulo(2, 5)
    3

    >>> invert_modulo(8,7)
    1

    """
    (b, x) = extended_euclid(a, n)  # Implemented below
    if b < 0:
        b = (b % n + n) % n
    return b


# ------------------ Finding Modular division using invert_modulo -------------------


def modular_division2(a: int, b: int, n: int) -> int:
    """
    This function used the above inversion of a to find x = (b*a^(-1))mod n

    >>> modular_division2(4,8,5)
    2

    >>> modular_division2(3,8,5)
    1

    >>> modular_division2(4, 11, 5)
    4

    """
    s = invert_modulo(a, n)
    x = (b * s) % n
    return x


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """
    Extended Euclid's Algorithm : If d divides a and b and d = a*x + b*y for integers x
    and y, then d = gcd(a,b)
    >>> extended_gcd(10, 6)
    (2, -1, 2)

    >>> extended_gcd(7, 5)
    (1, -2, 3)

    ** extended_gcd function is used when d = gcd(a,b) is required in output

    """
    assert a >= 0
    assert b >= 0

    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)

    assert a % d == 0
    assert b % d == 0
    assert d == a * x + b * y

    return (d, x, y)


def extended_euclid(a: int, b: int) -> tuple[int, int]:
    """
    Extended Euclid
    >>> extended_euclid(10, 6)
    (-1, 2)

    >>> extended_euclid(7, 5)
    (-2, 3)

    """
    if b == 0:
        return (1, 0)
    (x, y) = extended_euclid(b, a % b)
    k = a // b
    return (y, x - k * y)


def greatest_common_divisor(a: int, b: int) -> int:
    """
    Euclid's Lemma :  d divides a and b, if and only if d divides a-b and b
    Euclid's Algorithm

    >>> greatest_common_divisor(7,5)
    1

    Note : In number theory, two integers a and b are said to be relatively prime,
        mutually prime, or co-prime if the only positive integer (factor) that divides
        both of them is 1  i.e., gcd(a,b) = 1.

    >>> greatest_common_divisor(121, 11)
    11

    """
    if a < b:
        a, b = b, a

    while a % b != 0:
        a, b = b, a % b

    return b


if __name__ == "__main__":
    from doctest import testmod

    testmod(name="modular_division", verbose=True)
    testmod(name="modular_division2", verbose=True)
    testmod(name="invert_modulo", verbose=True)
    testmod(name="extended_gcd", verbose=True)
    testmod(name="extended_euclid", verbose=True)
    testmod(name="greatest_common_divisor", verbose=True)
