"""
Project Euler Problem 5: https://projecteuler.net/problem=5

Smallest multiple

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is _evenly divisible_ by all
of the numbers from 1 to 20?

References:
    - https://en.wiktionary.org/wiki/evenly_divisible
"""

from math import ceil, sqrt


def isprime(p_num):
    """
    Returns boolean value corresponding to whether a number is prime or not

    >>> isprime(3)
    True
    >>> isprime(18)
    False
    >>> isprime(97)
    True
    """
    if (p_num == 2) or (p_num == 3):
        return True
    elif p_num % 2 == 0:
        return False
    else:
        lock = int(ceil(sqrt(p_num)))
        for k in range(3, lock + 1, 2):
            if p_num % k == 0:
                return False
        return True


def lcm(num):
    """
    Finds all the prime factors of a number and returns it in a list

    >>> lcm(5)
    [5]
    >>> lcm(10)
    [2, 5]
    >>> lcm(20)
    [2, 2, 5]
    """
    p_list = list()
    fact = 2
    while fact <= num:
        if isprime(fact):
            if num % fact == 0:
                num /= fact
                p_list.append(fact)
            else:
                fact += 1
        else:
            fact += 1
    return p_list


def smallest_multiple(y: int = 20) -> int:
    """
        Returns the number which is evenly divisible from 1 to y.

        >>> smallest_multiple(10)
        2520
        >>> smallest_multiple(15)
        360360
        >>> smallest_multiple(22)
        232792560
        >>> smallest_multiple(25)
        26771144400
    """
    def kick(num):
        for k in prime_list:
            try:
                k.remove(num)
            except ValueError:
                pass

    prime_list = list()

    for i in range(1, y+1):
        prime_list.append(lcm(i))

    final_list = list()

    for i in prime_list:
        for j in i:
            final_list.append(j)
            kick(j)

    result = 1

    for r in final_list:
        result *= r

    return result


if __name__ == "__main__":
    print(f"{smallest_multiple() = }")
