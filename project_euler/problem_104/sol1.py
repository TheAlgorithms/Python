"""
Project Euler Problem 104: https://projecteuler.net/problem=104

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

It turns out that F541, which contains 113 digits, is the first Fibonacci
number for which the last nine digits are 1-9 pandigital (contain all
the digits 1 to 9, but not necessarily in order). And F2749, which
contains 575 digits, is the first Fibonacci number for which the
first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits AND
the last nine digits are 1-9 pandigital, find k.
"""
from typing import List

base = [[1, 1], [1, 0]]


def matrix_product(a: List[list], b: List[list], mod: int = None) -> List[list]:
    """
    Return product of two matrices a and b, modulo mod.

    >>> matrix_product(base, base)
    [[2, 1], [1, 1]]
    >>> matrix_product([[2, 1], [1, 1]], base, 2)
    [[1, 0], [0, 1]]
    """
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += a[i][k] * b[k][j]
                if mod is not None:
                    result[i][j] %= mod
    return result


def matrix_power(n: int, mod: int = None) -> List[list]:
    """
    Return resutl of matrix base power n modulo mod.

    >>> matrix_power(1)
    [[1, 1], [1, 0]]
    >>> matrix_power(2)
    [[2, 1], [1, 1]]
    >>> matrix_power(3, 2)
    [[1, 0], [0, 1]]
    """
    if n == 1:
        return base

    tmp = matrix_power(n // 2, mod)
    tmp = matrix_product(tmp, tmp, mod)
    if n % 2 != 0:
        tmp = matrix_product(tmp, base, mod)
    return tmp


def fib(k: int, mod: int = None) -> int:
    """
    Return the k-th fibonacci number modulo mod.

    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    >>> fib(7)
    13
    >>> fib(541, 10 ** 9)
    839725641
    """
    if k <= 2:
        return 1
    tmp = matrix_power(k - 2, mod)
    ans = tmp[0][0] + tmp[0][1]
    if mod is not None:
        ans %= mod
    return ans


def is_pandigital(string: str) -> bool:
    """
    Checks if a string is a permutation of 9.

    >>> is_pandigital('789456123')
    True
    >>> is_pandigital('789456127')
    False
    >>> is_pandigital('839725641')
    True
    """
    occ = [0] * 10
    for i in string:
        occ[int(i)] += 1

    return all(map(lambda x: x == 1, occ[1:]))


def solution() -> int:
    """
    Return the first Fibonacci number for which
    the first nine digits AND the last nine digits are 1-9 pandigital.

    >>> solution()
    329468
    """
    mod = 10 ** 9
    k = 3 * 10 ** 5
    while True:
        res = fib(k, mod)
        if is_pandigital(str(res)):
            res = str(fib(k))
            first = res[:9]
            if is_pandigital(first):
                break
        k += 1
    return k


if __name__ == "__main__":
    print(f"{solution() = }")
