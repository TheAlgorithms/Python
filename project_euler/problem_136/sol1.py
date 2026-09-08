"""
Project Euler Problem 136: https://projecteuler.net/problem=136

Singleton Difference

The positive integers, x, y, and z, are consecutive terms of an arithmetic progression.
Given that n is a positive integer, the equation, x^2 - y^2 - z^2 = n,
has exactly one solution when n = 20:
                              13^2 - 10^2 - 7^2 = 20.

In fact there are twenty-five values of n below one hundred for which
the equation has a unique solution.

How many values of n less than fifty million have exactly one solution?

By change of variables

x = y + delta
z = y - delta

The expression can be rewritten:

x^2 - y^2 - z^2 = y * (4 * delta - y) = n

The algorithm loops over delta and y, which is restricted in upper and lower limits,
to count how many solutions each n has.
In the end it is counted how many n's have one solution.
"""


def solution(n_limit: int = 50 * 10**6) -> int:
    """
    Define n count list and loop over delta, y to get the counts, then check
    which n has count == 1.

    >>> solution(3)
    0
    >>> solution(10)
    3
    >>> solution(100)
    25
    >>> solution(110)
    27
    """
    n_sol = [0] * n_limit

    for delta in range(1, (n_limit + 1) // 4 + 1):
        for y in range(4 * delta - 1, delta, -1):
            n = y * (4 * delta - y)
            if n >= n_limit:
                break
            n_sol[n] += 1

    ans = 0
    for i in range(n_limit):
        if n_sol[i] == 1:
            ans += 1

    return ans


if __name__ == "__main__":
    print(f"{solution() = }")
