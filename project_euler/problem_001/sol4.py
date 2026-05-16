"""
Project Euler Problem 1: https://projecteuler.net/problem=1

Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def solution(n: int = 1000) -> int:
    """
    Returns the sum of all the multiples of 3 or 5 below n.

    >>> solution(3)
    0
    >>> solution(4)
    3
    >>> solution(10)
    23
    >>> solution(600)
    83700
    """

    xmulti = []
    zmulti = []
    z = 3
    x = 5
    temp = 1
    while True:
        result = z * temp
        if result < n:
            zmulti.append(result)
            temp += 1
        else:
            temp = 1
            break
    while True:
        result = x * temp
        if result < n:
            xmulti.append(result)
            temp += 1
        else:
            break
    collection = list(set(xmulti + zmulti))
    return sum(collection)


if __name__ == "__main__":
    print(f"{solution() = }")
