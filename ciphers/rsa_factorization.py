"""
An RSA prime factor algorithm.

The program can efficiently factor RSA prime number given the private key d and
public key e.
Source: on page 3 of https://crypto.stanford.edu/~dabo/papers/RSA-survey.pdf
More readable source: https://www.di-mgt.com.au/rsa_factorize_n.html
"""
from __future__ import annotations

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
    >>> rsafactor(0x123c5b61ba36edb1d3679904199a89ea80c09b9122e1400c09adcf7784676d01d23356a7d44d6bd8bd50e94bfc723fa87d8862b75177691c11d757692df8881, 0x10001, 0xa66791dc6988168de7ab77419bb7fb0c001c62710270075142942e19a8d8c51d053b3e3782a1de5dc5af4ebe99468170114a1dfe67cdc9a9af55d655620bbab)
    [23234950162188993388155927630085331316851060055334470382368804331834850828939, 23443439767333138692938389505422341860387525814723848738690073331642118819681]
    >>> rsafactor(4, 3, 13)
    Traceback (most recent call last):
    ...
    ValueError: e and d are not valid RSA exponents
    """
    k = d * e - 1
    if k & 1 == 1:
        raise ValueError("e and d are not valid RSA exponents")

    while True:
        g = random.randint(2, N - 1)
        t = k
        while t & 1 == 0:
            t >>= 1
            x = pow(g, t, N)
            y = math.gcd(x - 1, N)
            if x > 1 and y > 1:
                # we found the correct factors
                p = y
                q = N // y
                return sorted([p, q])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
