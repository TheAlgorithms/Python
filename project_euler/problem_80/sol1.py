"""
https://projecteuler.net/problem=80

It is well known that if the square root of a natural number is not an integer,
then it is irrational. The decimal expansion of such square roots is infinite
without any repeating pattern at all.

The square root of two is 1.41421356237309504880...,
and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital
sums of the first one hundred decimal digits for all the irrational square roots.
"""


from decimal import Decimal, getcontext


def digital_sum(num: int, accuracy: int) -> int:
    """
    Function to take the square root of a number with given accuracy.
    Returns string of answer without a dot.
    >>> digital_sum(2, 100)
    475
    >>> digital_sum(80, 100)
    500
    """
    getcontext().prec = accuracy + 5
    ans = str(Decimal(num).sqrt())
    ans = ans.replace(".", "")
    ans = ans[:accuracy]

    total_sum = 0

    for digit in ans:
        total_sum += int(digit)

    return total_sum


def solution():
    """Returns the total of the digital sum of the first one hundred
    decimal digits for all the irrational square roots of all the first
    one hundrer numbers.

    >>> solution()
    40886
    """

    numbers = list(range(1, 100))
    numbers = [num for num in numbers if num not in (1, 4, 9, 16, 25, 36, 49, 64, 81)]

    total_sum = 0
    accuracy = 100

    for num in numbers:
        total_sum += digital_sum(num, accuracy)

    return total_sum


if __name__ == "__main__":
    print(solution())
