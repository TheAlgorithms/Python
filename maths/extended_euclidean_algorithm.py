"""
Extended Euclidean Algorithm.

Finds 2 numbers a and b such that it satisfies
the equation am + bn = gcd(m, n) (a.k.a Bezout's Identity)
"""

# @Author: S. Sharma <silentcat>
# @Date:   2019-02-25T12:08:53-06:00
# @Email:  silentcat@protonmail.com
# @Last modified by:   PatOnTheBack
# @Last modified time: 2019-07-05

import sys


def extended_euclidean_algorithm(m, n):
    """
    Extended Euclidean Algorithm.

    Finds 2 numbers a and b such that it satisfies
    the equation am + bn = gcd(m, n) (a.k.a Bezout's Identity)
    """
    a = 0
    a_prime = 1
    b = 1
    b_prime = 0
    q = 0
    r = 0
    if m > n:
        c = m
        d = n
    else:
        c = n
        d = m

    while True:
        q = int(c / d)
        r = c % d
        if r == 0:
            break
        c = d
        d = r

        t = a_prime
        a_prime = a
        a = t - q * a

        t = b_prime
        b_prime = b
        b = t - q * b

    pair = None
    if m > n:
        pair = (a, b)
    else:
        pair = (b, a)
    return pair


def main():
    """Call Extended Euclidean Algorithm."""
    if len(sys.argv) < 3:
        print("2 integer arguments required")
        exit(1)
    m = int(sys.argv[1])
    n = int(sys.argv[2])
    print(extended_euclidean_algorithm(m, n))


if __name__ == "__main__":
    main()
