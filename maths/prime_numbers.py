import math
from collections.abc import Generator


def slow_primes(max_n: int) -> Generator[int, None, None]:
    """
    Return a list of all primes numbers up to max.
    >>> list(slow_primes(0))
    []
    >>> list(slow_primes(-1))
    []
    >>> list(slow_primes(-10))
    []
    >>> list(slow_primes(25))
    [2, 3, 5, 7, 11, 13, 17, 19, 23]
    >>> list(slow_primes(11))
    [2, 3, 5, 7, 11]
    >>> list(slow_primes(33))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    >>> list(slow_primes(1000))[-1]
    997
    """
    numbers: Generator = (i for i in range(1, (max_n + 1)))
    for i in (n for n in numbers if n > 1):
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            yield i


def primes(max_n: int) -> Generator[int, None, None]:
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
    >>> list(primes(1000))[-1]
    997
    """
    numbers: Generator = (i for i in range(1, (max_n + 1)))
    for i in (n for n in numbers if n > 1):
        # only need to check for factors up to sqrt(i)
        bound = int(math.sqrt(i)) + 1
        for j in range(2, bound):
            if (i % j) == 0:
                break
        else:
            yield i


def fast_primes(max_n: int) -> Generator[int, None, None]:
    """
    Return a list of all primes numbers up to max.
    >>> list(fast_primes(0))
    []
    >>> list(fast_primes(-1))
    []
    >>> list(fast_primes(-10))
    []
    >>> list(fast_primes(25))
    [2, 3, 5, 7, 11, 13, 17, 19, 23]
    >>> list(fast_primes(11))
    [2, 3, 5, 7, 11]
    >>> list(fast_primes(33))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    >>> list(fast_primes(1000))[-1]
    997
    """
    numbers: Generator = (i for i in range(1, (max_n + 1), 2))
    # It's useless to test even numbers as they will not be prime
    if max_n > 2:
        yield 2  # Because 2 will not be tested, it's necessary to yield it now
    for i in (n for n in numbers if n > 1):
        bound = int(math.sqrt(i)) + 1
        for j in range(3, bound, 2):
            # As we removed the even numbers, we don't need them now
            if (i % j) == 0:
                break
        else:
            yield i


def benchmark():
    """
    Let's benchmark our functions side-by-side...
    """
    from timeit import timeit

    setup = "from __main__ import slow_primes, primes, fast_primes"
    print(timeit("slow_primes(1_000_000_000_000)", setup=setup, number=1_000_000))
    print(timeit("primes(1_000_000_000_000)", setup=setup, number=1_000_000))
    print(timeit("fast_primes(1_000_000_000_000)", setup=setup, number=1_000_000))


if __name__ == "__main__":
    number = int(input("Calculate primes up to:\n>> ").strip())
    for ret in primes(number):
        print(ret)
    benchmark()
