"""
Tonelli-Shanks Algorithm for Modular Square Roots.

Reference: https://en.wikipedia.org/wiki/Tonelli%E2%80%93Shanks_algorithm
Reference: https://cp-algorithms.com/algebra/tonelli-shanks.html

Given an integer n and an odd prime p, the Tonelli-Shanks algorithm computes
an integer x such that:
    x^2 = n (mod p)
If n is a quadratic residue modulo p, it returns two solutions (r1, r2)
where r1 <= r2 and r1 + r2 = p (or (0, 0) if n = 0 mod p).
"""

from __future__ import annotations


def legendre_symbol(n: int, p: int) -> int:
    """
    Compute the Legendre Symbol (n / p) modulo an odd prime p.

    Euler's Criterion states that:
        (n / p) = n^((p - 1) / 2) (mod p)

    Returns:
         1 if n is a quadratic residue modulo p and n != 0 (mod p)
        -1 if n is a quadratic non-residue modulo p
         0 if n = 0 (mod p)

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
    ls = pow(n % p, (p - 1) // 2, p)
    return ls if ls <= 1 else -1


def tonelli_shanks(n: int, p: int) -> tuple[int, int]:
    """
    Find solutions to x^2 = n (mod p) for an odd prime p using Tonelli-Shanks algorithm.

    Time Complexity: O(log^2 p) on average.

    Parameters:
        n: The integer whose square root modulo p is to be found.
        p: An odd prime modulus.

    Returns:
        A tuple (r1, r2) containing the two square roots modulo p such that r1 <= r2.

    Raises:
        ValueError: If p is not an odd prime >= 3.
        ValueError: If n is not a quadratic residue modulo p.

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
    if p <= 2 or p % 2 == 0:
        msg = f"Modulus p must be an odd prime (got {p})."
        raise ValueError(msg)

    n = n % p
    if n == 0:
        return 0, 0

    if legendre_symbol(n, p) != 1:
        msg = f"{n} is not a quadratic residue modulo {p}."
        raise ValueError(msg)

    # Factor out powers of 2 from p - 1: p - 1 = q * 2^s, with q odd
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1

    # Case 1: p = 3 (mod 4), s = 1
    if s == 1:
        root = pow(n, (p + 1) // 4, p)
        return min(root, p - root), max(root, p - root)

    # Case 2: Search for a quadratic non-residue z modulo p
    z = 2
    while legendre_symbol(z, p) != -1:
        z += 1

    c = pow(z, q, p)
    x = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s

    while t != 1:
        # Find the smallest i (0 < i < m) such that t^(2^i) = 1 (mod p)
        i = 0
        t2i = t
        while t2i != 1 and i < m:
            t2i = pow(t2i, 2, p)
            i += 1

        if i == m:
            msg = f"Failed to find square root for {n} mod {p}."
            raise ValueError(msg)

        b = pow(c, 1 << (m - i - 1), p)
        x = (x * b) % p
        t = (t * b * b) % p
        c = (b * b) % p
        m = i

    return min(x, p - x), max(x, p - x)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
