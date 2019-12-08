from typing import Generator


def primes(max: int) -> Generator[int, None, None]:
    """
    Return a list of all primes numbers up to max.
    >>> list(primes(0))
    []
    >>> list(primes(-1))
    []
    >>> list(primes(-10))
    []
    >>> list(primes(25))
    [2, 3, 5, 7, 11, 13, 17, 19, 23]
    >>> list(primes(11))
    [2, 3, 5, 7, 11]
    >>> list(primes(33))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    >>> list(primes(10000))[-1]
    9973
    """
    numbers: Generator = (i for i in range(1, (max + 1)))
    for i in (n for n in numbers if n > 1):
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            yield i


if __name__ == "__main__":
    number = int(input("Calculate primes up to:\n>> ").strip())
    for ret in primes(number):
        print(ret)
