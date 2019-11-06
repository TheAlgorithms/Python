from typing import List


def primes(max: int) -> List[int]:
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
    max += 1
    numbers = [False] * max
    ret = []
    for i in range(2, max):
        if not numbers[i]:
            for j in range(i, max, i):
                numbers[j] = True
            ret.append(i)
    return ret


if __name__ == "__main__":
    print(primes(int(input("Calculate primes up to:\n>> "))))
