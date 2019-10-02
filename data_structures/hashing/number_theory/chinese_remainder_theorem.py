# Chinese Remainder Theorem:
# GCD ( Greatest Common Divisor ) or HCF ( Highest Common Factor )

# If GCD(a,b) = 1, then for any remainder ra modulo a and any remainder rb modulo b there exists integer n,
# such that n = ra (mod a) and n = ra(mod b).  If n1 and n2 are two such integers, then n1=n2(mod ab)

# Algorithm :

# 1. Use extended euclid algorithm to find x,y such that a*x + b*y = 1
# 2. Take n = ra*by + rb*ax


# Extended Euclid
def extended_euclid(a, b):
    """
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


# Uses ExtendedEuclid to find inverses
def chinese_remainder_theorem(n1, r1, n2, r2):
    """
    >>> chinese_remainder_theorem(5,1,7,3)
    31

    Explanation : 31 is the smallest number such that
                (i)  When we divide it by 5, we get remainder 1
                (ii) When we divide it by 7, we get remainder 3

    >>> chinese_remainder_theorem(6,1,4,3)
    14

    """
    (x, y) = extended_euclid(n1, n2)
    m = n1 * n2
    n = r2 * x * n1 + r1 * y * n2
    return ((n % m + m) % m)


# ----------SAME SOLUTION USING InvertModulo instead ExtendedEuclid----------------

# This function find the inverses of a i.e., a^(-1)
def invert_modulo(a, n):
    """
    >>> invert_modulo(2, 5)
    3

    >>> invert_modulo(8,7)
    1

    """
    (b, x) = extended_euclid(a, n)
    if b < 0:
        b = (b % n + n) % n
    return b


# Same a above using InvertingModulo
def chinese_remainder_theorem2(n1, r1, n2, r2):
    """
    >>> chinese_remainder_theorem2(5,1,7,3)
    31

    >>> chinese_remainder_theorem2(6,1,4,3)
    14

    """
    x, y = invert_modulo(n1, n2), invert_modulo(n2, n1)
    m = n1 * n2
    n = r2 * x * n1 + r1 * y * n2
    return (n % m + m) % m


# import testmod for testing our function
from doctest import testmod

if __name__ == '__main__':
    testmod(name='chinese_remainder_theorem', verbose=True)
    testmod(name='chinese_remainder_theorem2', verbose=True)
    testmod(name='invert_modulo', verbose=True)
    testmod(name='extended_euclid', verbose=True)
