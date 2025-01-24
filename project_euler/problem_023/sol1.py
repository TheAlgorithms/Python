"""
A perfect number is a number for which the sum of its proper divisors is exactly
equal to the number. For example, the sum of the proper divisors of 28 would be
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers
is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum
of two abundant numbers.
"""


def solution(limit=28123):
    """
    Finds the sum of all the positive integers which cannot be written as
    the sum of two abundant numbers
    as described by the statement above.

    >>> solution()
    4179871
    """
    sum_divs = [1] * (limit + 1)

    for i in range(2, int(limit**0.5) + 1):
        sum_divs[i * i] += i
        for k in range(i + 1, limit // i + 1):
            sum_divs[k * i] += k + i

    abundants = set()
    res = 0

    for n in range(1, limit + 1):
        if sum_divs[n] > n:
            abundants.add(n)

        if not any((n - a in abundants) for a in abundants):
            res += n

    return res


if __name__ == "__main__":
    print(solution())
