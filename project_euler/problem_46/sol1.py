"""
It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

9 = 7 + 2 × 12
15 = 7 + 2 × 22
21 = 3 + 2 × 32
25 = 7 + 2 × 32
27 = 19 + 2 × 22
33 = 31 + 2 × 12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a
prime and twice a square?
"""

from typing import List

seive = [True] * 100001
i = 2
while i * i <= 100000:
    if seive[i]:
        for j in range(i * i, 100001, i):
            seive[j] = False
    i += 1


def is_prime(n: int) -> bool:
    """
    Returns True if n is prime,
    False otherwise, for 2 <= n <= 100000
    >>> is_prime(87)
    False
    >>> is_prime(23)
    True
    >>> is_prime(25363)
    False
    """
    return seive[n]


odd_composites = [num for num in range(3, len(seive), 2) if not is_prime(num)]


def compute_nums(n: int) -> List[int]:
    """
    Returns a list of first n odd composite numbers which do
    not follow the conjecture.
    >>> compute_nums(1)
    [5777]
    >>> compute_nums(2)
    [5777, 5993]
    >>> compute_nums(0)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0
    >>> compute_nums("a")
    Traceback (most recent call last):
        ...
    ValueError: n must be an integer
    >>> compute_nums(1.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be an integer

    """
    if not isinstance(n, int):
        raise ValueError("n must be an integer")
    if n <= 0:
        raise ValueError("n must be >= 0")

    list_nums = []
    for num in range(len(odd_composites)):
        i = 0
        while 2 * i * i <= odd_composites[num]:
            rem = odd_composites[num] - 2 * i * i
            if is_prime(rem):
                break
            i += 1
        else:
            list_nums.append(odd_composites[num])
            if len(list_nums) == n:
                return list_nums


if __name__ == "__main__":
    print(f"{compute_nums(1) = }")
