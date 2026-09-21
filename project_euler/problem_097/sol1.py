"""
The first known prime found to exceed one million digits was discovered in 1999,
and is a Mersenne prime of the form 2**6972593 - 1; it contains exactly 2,098,960
digits. Subsequently other Mersenne primes, of the form 2**p - 1, have been found
which contain more digits.
However, in 2004 there was found a massive non-Mersenne prime which contains
2,357,207 digits: (28433 * (2 ** 7830457 + 1)).

Find the last ten digits of this prime number.
"""


def solution(n: int = 10) -> str:
    """
    Returns the last n digits of NUMBER.
    >>> solution()
    '8739992577'
    >>> solution(8)
    '39992577'
    >>> solution(1)
    '7'
    >>> solution(-1)
    Traceback (most recent call last):
        ...
    ValueError: Invalid input
    >>> solution(8.3)
    Traceback (most recent call last):
        ...
    ValueError: Invalid input
    >>> solution("a")
    Traceback (most recent call last):
        ...
    ValueError: Invalid input
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Invalid input")
    modulus = 10**n
    number = 28433 * (pow(2, 7830457, modulus)) + 1
    return str(number % modulus)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print(f"{solution(10) = }")
