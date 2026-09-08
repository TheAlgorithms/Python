"""
This script implements the Solovay-Strassen Primality test.

This probabilistic primality test is based on Euler's criterion. It is similar
to the Fermat test but uses quadratic residues. It can quickly identify
composite numbers but may occasionally classify composite numbers as prime.

More details and concepts about this can be found on:
https://en.wikipedia.org/wiki/Solovay%E2%80%93Strassen_primality_test
"""

import random


def jacobi_symbol(random_a: int, number: int) -> int:
    """
    Calculate the Jacobi symbol. The Jacobi symbol is a generalization
    of the Legendre symbol, which can be used to simplify computations involving
    quadratic residues. The Jacobi symbol is used in primality tests, like the
    Solovay-Strassen test, because it helps determine if an integer is a
    quadratic residue modulo a given modulus, providing valuable information
    about the number's potential primality or compositeness.

    Parameters:
        random_a: A randomly chosen integer from 2 to n-2 (inclusive)
        number: The number that is tested for primality

    Returns:
        jacobi_symbol: The Jacobi symbol is a mathematical function
        used to determine whether an integer is a quadratic residue modulo
        another integer (usually prime) or not.

    >>> jacobi_symbol(2, 13)
    -1
    >>> jacobi_symbol(5, 19)
    1
    >>> jacobi_symbol(7, 14)
    0
    """

    if random_a in (0, 1):
        return random_a

    random_a %= number
    t = 1

    while random_a != 0:
        while random_a % 2 == 0:
            random_a //= 2
            r = number % 8
            if r in (3, 5):
                t = -t

        random_a, number = number, random_a

        if random_a % 4 == number % 4 == 3:
            t = -t

        random_a %= number

    return t if number == 1 else 0


def solovay_strassen(number: int, iterations: int) -> bool:
    """
    Check whether the input number is prime or not using
    the Solovay-Strassen Primality test

    Parameters:
        number: The number that is tested for primality
        iterations: The number of times that the test is run
        which effects the accuracy

    Returns:
        result: True if number is probably prime and false
        if not

    >>> random.seed(10)
    >>> solovay_strassen(13, 5)
    True
    >>> solovay_strassen(9, 10)
    False
    >>> solovay_strassen(17, 15)
    True
    """

    if number <= 1:
        return False
    if number <= 3:
        return True

    for _ in range(iterations):
        a = random.randint(2, number - 2)
        x = jacobi_symbol(a, number)
        y = pow(a, (number - 1) // 2, number)

        if x == 0 or y != x % number:
            return False

    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
