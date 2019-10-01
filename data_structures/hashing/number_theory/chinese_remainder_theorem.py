# Chinese Remainder Theorem:

# If GCD(a,b) = 1, then for any remainder ra modulo a and any remainder rb modulo b there exists integer n,
# such that n = ra (mod a) and n = ra(mod b).  If n1 and n2 are two such integers, then n1=n2(mod ab)

# Algorithm :

# 1. Use extended euclid algorithm to find x,y such that a*x + b*y = 1
# 2. Take n = ra*by + rb*ax

# import testmod for testing our function
from doctest import testmod


# Extended Euclid
def ExtendedEuclid(a, b):
    if b == 0:
        return (1, 0)
    (x, y) = ExtendedEuclid(b, a % b)
    k = a // b
    return (y, x - k * y)


# Uses ExtendedEuclid to find inverses
def ChineseRemainderTheorem(n1, r1, n2, r2):
    """
    >>> ChineseRemainderTheorem(5,1,7,3)
    31

    Explanation : 31 is the smallest number such that
                (i)  When we divide it by 5, we get remainder 1
                (ii) When we divide it by 7, we get remainder 3

    >>> ChineseRemainderTheorem(6,1,4,3)
    14
    """
    (x, y) = ExtendedEuclid(n1, n2)
    m = n1 * n2
    n = r2 * x * n1 + r1 * y * n2
    return ((n % m + m) % m)


# ----------SAME SOLUTION USING InvertModulo instead ExtendedEuclid----------------

# This function find the inverses of a i.e., a^(-1)
def InvertModulo(a, n):
    (b, x) = ExtendedEuclid(a, n)
    if b < 0:
        b = (b % n + n) % n
    return b


# Same a above using InvertingModulo
def ChineseRemainderTheorem2(n1, r1, n2, r2):
    """
    >>> ChineseRemainderTheorem2(5,1,7,3)
    31

    >>> ChineseRemainderTheorem2(6,1,4,3)
    14
    """
    x, y = InvertModulo(n1, n2), InvertModulo(n2, n1)
    m = n1 * n2
    n = r2 * x * n1 + r1 * y * n2
    return (n % m + m) % m


if __name__ == '__main__':
    testmod(name='ChineseRemainderTheorem', verbose=True)
    testmod(name='ChineseRemainderTheorem2', verbose=True)
