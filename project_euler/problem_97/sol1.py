"""
The first known prime found to exceed one million digits was discovered in 1999,
and is a Mersenne prime of the form 2**6972593 − 1; it contains exactly 2,098,960
digits. Subsequently other Mersenne primes, of the form 2**p − 1, have been found
which contain more digits.
However, in 2004 there was found a massive non-Mersenne prime which contains
2,357,207 digits: (28433 * (2 ** 7830457 + 1)).

Find the last ten digits of this prime number.
"""


def compute_digits(n: int) -> str:
    """
    Returns the last n digits of NUMBER.
    >>> compute_digits(10)
    '8740021009'
    >>> compute_digits(8)
    '40021009'
    >>> compute_digits(1)
    '9'
    >>> compute_digits(-1)
    ''
    >>> compute_digits(8.3)
    ''
    """
    if n < 0 or not isinstance(n, int):
        return ""
    MODULUS = 10 ** n
    NUMBER = 28433 * (pow(2, 7830457, MODULUS) + 1)
    return str(NUMBER % MODULUS)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print(f"{compute_digits(10)}")
