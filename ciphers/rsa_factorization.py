"""
An RSA prime factor algorithm.

The program can efficiently factor RSA prime number given the private key d and
public key e.
Source: on page 3 of https://crypto.stanford.edu/~dabo/papers/RSA-survey.pdf
large number can take minutes to factor, therefore are not included in doctest.
"""
import math
import random
from typing import List


def rsafactor(d: int, e: int, N: int) -> List[int]:
    """
    This function returns the factors of N, where p*q=N
      Return: [p, q]
    
    We call N the RSA modulus, e the encryption exponent, and d the decryption exponent.
    The pair (N, e) is the public key. As its name suggests, it is public and is used to
        encrypt messages.
    The pair (N, d) is the secret key or private key and is known only to the recipient
        of encrypted messages.

    >>> rsafactor(3, 16971, 25777)
    [149, 173]
    >>> rsafactor(7331, 11, 27233)
    [113, 241]
    >>> rsafactor(4021, 13, 17711)
    [89, 199]
    """
    k = d * e - 1
    p = 0
    q = 0
    while p == 0:
        g = random.randint(2, N - 1)
        t = k
        if t % 2 == 0:
            t = t // 2
            x = (g ** t) % N
            y = math.gcd(x - 1, N)
            if x > 1 and y > 1:
                p = y
                q = N // y
    return sorted([p, q])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
