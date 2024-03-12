"""
Project Euler Problem 38: https://projecteuler.net/problem=38

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call
192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?

Solution:
Since n>1, the largest candidate for the solution will be a concactenation of
a 4-digit number and its double, a 5-digit number.
Let a be the 4-digit number.
a  has 4 digits  =>  1000 <=  a  < 10000
2a has 5 digits  => 10000 <= 2a  < 100000
=>  5000 <= a < 10000

The concatenation of a with 2a = a * 10^5 + 2a
so our candidate for a given a is 100002 * a.
We iterate through the search space 5000 <= a < 10000 in reverse order,
calculating the candidates for each a and checking if they are 1-9 pandigital.

In case there are no 4-digit numbers that satisfy this property, we check
the 3-digit numbers with a similar formula (the example a=192 gives a lower
bound on the length of a):
a has 3 digits, etc...
=>  100 <= a < 334, candidate = a * 10^6 + 2a * 10^3 + 3a
                              = 1002003 * a
"""

from __future__ import annotations


def is_9_pandigital(n: int) -> bool:
    """
    Checks whether n is a 9-digit 1 to 9 pandigital number.
    >>> is_9_pandigital(12345)
    False
    >>> is_9_pandigital(156284973)
    True
    >>> is_9_pandigital(1562849733)
    False
    """
    s = str(n)
    return len(s) == 9 and set(s) == set("123456789")


def solution() -> int | None:
    """
    Return the largest 1 to 9 pandigital 9-digital number that can be formed as the
    concatenated product of an integer with (1,2,...,n) where n > 1.
    """
    for base_num in range(9999, 4999, -1):
        candidate = 100002 * base_num
        if is_9_pandigital(candidate):
            return candidate

    for base_num in range(333, 99, -1):
        candidate = 1002003 * base_num
        if is_9_pandigital(candidate):
            return candidate

    return None


if __name__ == "__main__":
    print(f"{solution() = }")
