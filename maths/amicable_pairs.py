"""
https://en.wikipedia.org/wiki/Amicable_numbers

Amicable numbers are two different numbers related in such a way that the sum
of the proper divisors of each is equal to the other number.

Here we are given an array, and are required to find all amicable pairs in
the array.
"""

from typing import List
from math import sqrt


def sum_of_divisors(n: int) -> int:
    """
    Returns the sum of all proper divisors of n
    >>> sum_of_divisors(220)
    284
    >>> sum_of_divisors(7632)
    14130
    >>> sum_of_divisors(6)
    6
    """
    list_divisors = [1]
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            list_divisors.append(i)
            if i != n / i:
                list_divisors.append(n // i)
    return sum(list_divisors)


def is_amicable(a: int, b: int) -> bool:
    """
    Returns True if a and b form an amicable pair.
    >>> is_amicable(12,16)
    False
    >>> is_amicable(2924,2620)
    True
    >>> is_amicable(6368,6232)
    True
    """
    return sum_of_divisors(a) == b and sum_of_divisors(b) == a


def find_pairs(nums: List[int]) -> List[tuple]:
    """
    Returns a list with amicale pairs.
    >>> find_pairs([2620, 2924, 5020, 5564, 6232, 6368])
    [(2924, 2620), (5564, 5020), (6368, 6232)]
    >>> find_pairs([220,12,24,76,284])
    [(284, 220)]
    >>> find_pairs([220, 284, 1184, 1210, 2, 5])
    [(284, 220), (1210, 1184)]
    """
    set_nums = set(nums)
    pairs = []
    for i in range(len(nums)):
        a, b = sum_of_divisors(nums[i]), nums[i]
        if a in set_nums:
            if is_amicable(a, b):
                pairs.append((a, b))
                set_nums.remove(b)
    return pairs


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print(f"{find_pairs([220, 284, 1184, 1210, 2, 5, 6368, 6232])}")
