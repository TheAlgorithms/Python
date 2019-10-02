# Modular Division
# An efficient algorithm for dividing b by a modulo n.

# Given three integers a, b, and n, such that gcd(a,n)=1 and n>1, the algorithm should return an integer x such that
#        0≤x≤n−1, and  b/a=x(modn) (that is, b=ax(modn)).

# Theorem:
# a has a multiplicative inverse modulo n iff gcd(a,n) = 1


# This find x = b*a^(-1) mod n
# Uses ExtendedEuclid to find the inverse of a

# Import testmod for testing our function
from doctest import testmod


def modular_division(a, b, n):
    """
    >>> modular_division(4,8,5)
    2

    >>> modular_division(3,8,5)
    1

    >>> modular_division(4, 11, 5)
    4

    """
    assert n > 1 and a > 0 and gcd(a, n) == 1
    (d, t, s) = extended_gcd(n, a)  # Implemented below
    x = (b * s) % n
    return x


# This function find the inverses of a i.e., a^(-1)
def invert_modulo(a, n):
    (b, x) = extended_euclid(a, n)  # Implemented below
    if b < 0:
        b = (b % n + n) % n
    return b


# ------------------ Finding Modular division using invert_modulo -------------------

# This function used the above inversion of a to find x = (b*a^(-1))mod n
def modular_division2(a, b, n):
    """
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


# Extended Euclid's Algorithm : If d divides a and b and d = a*x + b*y for integers x and y, then d = gcd(a,b)


def extended_gcd(a, b):
    assert a >= 0 and b >= 0

    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)

    assert a % d == 0 and b % d == 0
    assert d == a * x + b * y

    return (d, x, y)


# Extended Euclid
def extended_euclid(a, b):
    if b == 0:
        return (1, 0)
    (x, y) = extended_euclid(b, a % b)
    k = a // b
    return (y, x - k * y)

# Euclid's Lemma :  d divides a and b, if and only if d divides a-b and b
# Euclid's Algorithm

def gcd(a, b):
    if a < b:
        a, b = b, a

    while a % b != 0:
        a, b = b, a % b

    return b


if __name__ == '__main__':
    testmod(name='modular_division', verbose=True)
    testmod(name='modular_division2', verbose=True)
