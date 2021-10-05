import math
from typing import Generator

"""
Naive implementation of finding primes by checking if each number
is divisible by 2 or any odd number up to its root.

For a fast implementation see Sieve of Eratosthenes.
"""


def slow_primes(max: int) -> Generator[int, None, None]:
    """
    Return a list of all primes numbers up to max.
    >>> list(slow_primes(0))
    []
    >>> list(slow_primes(-1))
    []
    >>> list(slow_primes(2))
    [2]
    >>> list(slow_primes(25))
    [2, 3, 5, 7, 11, 13, 17, 19, 23]
    >>> list(slow_primes(11))
    [2, 3, 5, 7, 11]
    >>> list(slow_primes(33))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    >>> list(slow_primes(10000))[-1]
    9973
    """
    numbers: Generator = (i for i in range(1, (max + 1)))
    for i in (n for n in numbers if n > 1):
        if i % 2 == 0:
            if i == 2:
                yield 2
            continue
        # only need to check for factors up to sqrt(i)
        bound = int(math.sqrt(i)) + 1
        for j in range(3, bound, 2):
            if i % j == 0:
                break
        else:
            yield i


if __name__ == "__main__":
    number = int(input("Calculate primes up to:\n>> ").strip())
    for ret in slow_primes(number):
        print(ret)
