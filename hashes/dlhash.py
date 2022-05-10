"""
This simple hash algorithm that is strongly collision resistant.
It works by taking a prime p such that q = p - 1 / 2 is also prime.
Alpha1 and alpha2 must be primitive roots mod p.
The hash function is as follows:
    h(num) = h((Quotient)q + Remainder) = alpha1^Remainder + alpha2^Quotient mod p.
source: https://www.mathcs.emory.edu/~whalen/Hash/Hash_Articles/IEEE/Discrete%20logarithm%20hash%20function%20that%20is%20collision%20free%20and%20one%20way.pdf
"""

def dlhash(p, alpha1, alpha2, num):
    """
    Implementation of the discrete log hash
    >>>dlhash(47, 5, 11, 5)
    h(0*23 + 5) = 5^5 * 11^0 mod 47 -> 23
    """
    q = (p-1) / 2
    quotient = 0
    remainder = 0
    flag = True
    while flag:
        remainder = int(num - (quotient * q))
        if remainder >= q:
            quotient += 1
        elif remainder == 0:
            flag = False
        else:
            flag = False
    hash = pow(alpha1, remainder, p) * pow(alpha2, quotient, p)
    hash = hash % p
    return hash