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


def sqrt_with_accuracy(num: int, accuracy: int) -> str:
    """
    Function to take the square root of a number with given accuracy.
    Returns string of answer without a dot.
    >>> sqrt_with_accuracy(2, 30)
    '141421356237309504880168872420'
    >>> sqrt_with_accuracy(80, 100)
    '8944271909999158785636694674925104941762473438446102897083588981642083702551219597657657633515129099'
    """
    getcontext().prec = accuracy + 5
    ans = str(Decimal(num).sqrt())
    ans = ans.replace(".", "")
    return ans[:accuracy]


def solution():
    """Returns the total of the digital sum of the first one hundred
    decimal digits for all the irrational square roots of all the first
    one hundrer numbers.

    >>> solution()
    40886
    """

    numbers = list(range(2, 100))
    numbers = [num for num in numbers if num not in (4, 9, 16, 25, 36, 49, 64, 81)]

    total_sum = 0

    for num in numbers:
        num_sqrt = sqrt_with_accuracy(num, 100)
        for digit in num_sqrt:
            total_sum += int(digit)

    return total_sum


if __name__ == "__main__":
    print(solution())
