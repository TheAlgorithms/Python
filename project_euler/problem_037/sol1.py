"""
The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each stage:
3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right
and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from __future__ import annotations

seive = [True] * 1000001
seive[1] = False
i = 2
while i * i <= 1000000:
    if seive[i]:
        for j in range(i * i, 1000001, i):
            seive[j] = False
    i += 1


def is_prime(n: int) -> bool:
    """
    Returns True if n is prime,
    False otherwise, for 1 <= n <= 1000000
    >>> is_prime(87)
    False
    >>> is_prime(1)
    False
    >>> is_prime(25363)
    False
    """
    return seive[n]


def list_truncated_nums(n: int) -> list[int]:
    """
    Returns a list of all left and right truncated numbers of n
    >>> list_truncated_nums(927628)
    [927628, 27628, 92762, 7628, 9276, 628, 927, 28, 92, 8, 9]
    >>> list_truncated_nums(467)
    [467, 67, 46, 7, 4]
    >>> list_truncated_nums(58)
    [58, 8, 5]
    """
    str_num = str(n)
    list_nums = [n]
    for i in range(1, len(str_num)):
        list_nums.append(int(str_num[i:]))
        list_nums.append(int(str_num[:-i]))
    return list_nums


def validate(n: int) -> bool:
    """
    To optimize the approach, we will rule out the numbers above 1000,
    whose first or last three digits are not prime
    >>> validate(74679)
    False
    >>> validate(235693)
    False
    >>> validate(3797)
    True
    """
    if len(str(n)) > 3:
        if not is_prime(int(str(n)[-3:])) or not is_prime(int(str(n)[:3])):
            return False
    return True


def compute_truncated_primes(count: int = 11) -> list[int]:
    """
    Returns the list of truncated primes
    >>> compute_truncated_primes(11)
    [23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]
    """
    list_truncated_primes: list[int] = []
    num = 13
    while len(list_truncated_primes) != count:
        if validate(num):
            list_nums = list_truncated_nums(num)
            if all(is_prime(i) for i in list_nums):
                list_truncated_primes.append(num)
        num += 2
    return list_truncated_primes


def solution() -> int:
    """
    Returns the sum of truncated primes
    """
    return sum(compute_truncated_primes(11))


if __name__ == "__main__":
    print(f"{sum(compute_truncated_primes(11)) = }")
