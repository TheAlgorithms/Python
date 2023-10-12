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
    Calculate the Jacobi symbol. The Jacobi symbol is a mathematical function
    used to determine whether an integer is a quadratic residue modulo
    another integer (usually prime) or not.

    Parameters:
        random_a (int): A randomly chosen integer from 2 to n-2 (inclusive)
        number (int): The number that is tested for primality

    Returns:
        jocobi_symbol (int): The jacobi symbol

    >>> jacobi_symbol(2, 13)
    -1
    >>> jacobi_symbol(5, 19)
    1
    >>> jacobi_symbol(7, 14)
    0
    """

    if random_a == 0:
        return 0
    if random_a == 1:
        return 1

    random_a = random_a % number
    t = 1

    while random_a != 0:
        while random_a % 2 == 0:
            random_a = random_a // 2
            r = number % 8
            if r in (3, 5):
                t = -t

        random_a, number = number, random_a

        if random_a % 4 == number % 4 == 3:
            t = -t

        random_a = random_a % number

    if number == 1:
        return t
    else:
        return 0


def solovay_strassen(number: int, accuracy: int) -> bool:
    """
    Check whether the input number is prime or not using
    the Solovay-Strassen Primality test

    Parameters:
        number (int): The number that is tested for primality
        accuracy (int): The accuracy for the test

    Returns:
        result (bool): True if number is probably prime and false
        if composite

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

    for _ in range(accuracy):
        a = random.randint(2, number - 2)
        x = jacobi_symbol(a, number)
        y = pow(a, (number - 1) // 2, number)

        if x == 0 or y != x % number:
            return False

    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
