from typing import List, Generator


def primes(max: int) -> Generator[int]:
    """
    Return a list of all primes numbers up to max.
    >>> primes(10)
    [2, 3, 5, 7]
    >>> primes(11)
    [2, 3, 5, 7, 11]
    >>> primes(25)
    [2, 3, 5, 7, 11, 13, 17, 19, 23]
    >>> primes(1_000_000)[-1]
    999983
    """
    numbers: Generator = (i for i in range(1, (max + 1)))
    for i in filter(lambda x: x > 1, numbers):
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            yield i


if __name__ == "__main__":
    number = int(input("Calculate primes up to:\n>> "))
    for ret in primes(number):
        print(ret)
