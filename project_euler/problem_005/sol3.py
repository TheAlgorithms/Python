"""
Project Euler Problem 5: https://projecteuler.net/problem=5

Smallest multiple

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is _evenly divisible_ by all
of the numbers from 1 to 20?
"""


def solution(n: int = 20) -> int:
    """
    Find the smallest number for 'n'.
    Iterate over each number up to n and add new factors
    that is not included in previous numbers.

    # >>> solution(10)
    # 2520
    # >>> solution(15)
    # 360360
    # >>> solution(22)
    # 232792560
    """

    # factors = {}
    factors = [0] * (n + 1)
    ans = 1
    for i in range(2, n + 1):
        if factors[i] == 0:
            f = i
            for j in range(2, i):
                if f == 1:
                    break
                power = factors[j]
                while power > 0:
                    if f % j == 0:
                        f //= j
                        power -= 1
                    else:
                        break
            if f != 1:
                factors[f] += 1
                ans *= f
    return ans


if __name__ == "__main__":
    print(f"{solution() = }")
