"""
Binary Exponentiation
This is a method to find a^b in O(log b) time complexity
This is one of the most commonly used methods of exponentiation
It's also useful when the solution to (a^b) % c is required because a, b, c may be
over the computer's calculation limits

Let's say you need to calculate a ^ b
- RULE 1 : a ^ b = (a*a) ^ (b/2) ---- example : 4 ^ 4 = (4*4) ^ (4/2) = 16 ^ 2
- RULE 2 : IF b is odd, then a ^ b = a * (a ^ (b - 1)), where b - 1 is even
Once b is even, repeat the process until b = 1 or b = 0, because a^1 = a and a^0 = 1

For modular exponentiation, we use the fact that (a*b) % c = ((a%c) * (b%c)) % c
Now apply RULE 1 or 2 as required

@author chinmoy159
"""


def b_expo(a: int, b: int) -> int:
    """
    >>> b_expo(2, 10)
    1024
    >>> b_expo(9, 0)
    1
    >>> b_expo(0, 12)
    0
    >>> b_expo(4, 12)
    16777216
    """
    res = 1
    while b > 0:
        if b & 1:
            res *= a

        a *= a
        b >>= 1

    return res


def b_expo_mod(a: int, b: int, c: int) -> int:
    """
    >>> b_expo_mod(2, 10, 1000000007)
    1024
    >>> b_expo_mod(11, 13, 19)
    11
    >>> b_expo_mod(0, 19, 20)
    0
    >>> b_expo_mod(15, 5, 4)
    3
    """
    res = 1
    while b > 0:
        if b & 1:
            res = ((res % c) * (a % c)) % c

        a *= a
        b >>= 1

    return res
