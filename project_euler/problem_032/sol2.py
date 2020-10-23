"""
Project Euler problem 32: https://projecteuler.net/problem=32

We shall say that an n-digit number is pandigital if it makes use of all the digits
1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand,
multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be
written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include
it once in your sum.
"""


from math import ceil
from typing import Iterator, List, Set, Tuple


def is_pandigital(m: int, max_dig: int) -> bool:
    """
    Check if integer m is pandigital 1 though max_dig.
    >>> is_pandigital(123,3)
    True
    >>> is_pandigital(12345,6)
    False
    >>> is_pandigital(764851392,9)
    True
    >>> is_pandigital(7648510392,9)
    False
    """
    digs: List[bool] = [False for _ in range(max_dig + 1)]
    n: int
    while m:
        n = m % 10
        if n == 0 or n > max_dig:
            return False
        if digs[n]:
            return False
        digs[n] = True
        m //= 10

    return all(digs[1:])


def get_abc_lengths(max_dig: int) -> Iterator[Tuple[int, int, int]]:
    """
    Return an iterator of tuples (t,u,v) where solutions (a,b,c) to the problem
    have t, u and v digits respectively.

    Explanation:
    let t = len(a), u = len(b), v = len(c)
    then 10^(t-1) <= a < 10^t,
         10^(u-1) <= b < 10^u,
         10^(v-1) <= c < 10^v.

    so 10^((t-1)(u-1)) <= a*b = c < 10^(t*u)
    so we need the windows [10^((t-1)(u-1)), 10^(t*u))
                       and [10^(v-1),        10^v)
    to overlap.
    This gives us (t-1)*(u-1) <= v <= t*u  + 1
    Furthermore, if we assume w.l.o.g that a <= b <= c then t <= u <= v
    so t + u + v = max_dig,
       t <= max_dig / 3,
       t <= v = max_dig - t - u ==> u >= 2*t - max_dig,
       v >= 1 ==> max_dig - t - u >= 1 ==> u <= max_dig - t + 1,
       u <= v = max_dig - t - u ==> u <= (max_dig - t) / 2

    >>> list(get_abc_lengths(5))
    [(1, 2, 2)]
    >>> list(get_abc_lengths(7))
    [(1, 3, 3), (2, 2, 3)]
    >>> list(get_abc_lengths(9))
    [(1, 4, 4), (2, 3, 4)]
    """
    t: int
    u: int
    v: int

    for t in range(1, int(max_dig / 3) + 1):
        for u in range(
            max(t, 2 * t - max_dig), min(max_dig + 1 - t, 1 + (max_dig - t) // 2)
        ):
            v = max_dig - t - u
            if v >= max(u, t):
                if (t - 1) * (u - 1) < v < t * u + 1:
                    yield t, u, v


def general_solution(max_dig: int = 9) -> int:
    """
    Return the sum of all products a*b=c where abc gives a 1 through max_dig
    pandigital number.
    >>> general_solution(5)
    52
    >>> general_solution(8)
    8994
    """
    s: Set[int] = set()
    t: int
    u: int
    v: int
    a: int
    b: int
    c: int

    for t, u, v in get_abc_lengths(max_dig):
        for a in range(10 ** (t - 1), 10 ** t):
            for b in range(10 ** (u - 1), 10 ** u):
                c = a * b
                if is_pandigital(a + b * (10 ** t) + c * (10 ** (u + t)), max_dig):
                    s.add(c)

    return sum(s)


def solution() -> int:
    """
    Return the sum of all products a*b=c where abc gives a 1 through 9
    pandigital number.
    This is an explicit specialisation of general_solution for max_dig = 9,
    since it can be shown the lengths to check (as given by get_abc_lengths)
    are (1,4,4) and (2,3,4). [skipping the generation of the tuples saves some
    execution time]
    """

    s = set()
    a: int
    b: int
    c: int

    # 1, 4, 4:
    for a in range(1, 10):
        for b in range(1000, min(10000, ceil(10000 / a))):
            c = a * b
            if is_pandigital(a + b * 10 + c * 100000, 9):
                s.add(c)

    # 2, 3, 4
    for a in range(10, 100):
        for b in range(ceil(1000 / a), 1000):
            c = a * b
            if is_pandigital(a + b * 100 + c * 100000, 9):
                s.add(c)

    return sum(s)


if __name__ == "__main__":
    print(f"{solution() = }")
