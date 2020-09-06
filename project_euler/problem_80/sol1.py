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
    """Function to take the square root of a number with given accuracy.
    Returns the result as a string.

    >>> sqrt_with_accuracy(2, 100)
    '1.414213562373095048801688724209698078569671875376948073176679737990732478462107038850387534327641572'
    """
    getcontext().prec = accuracy + 5
    ans = str(Decimal(num).sqrt())
    return ans[: accuracy + 1]


def digital_sum(num: str) -> int:
    """Function to calculate the digital sum of a number.
    The digital sum is the sum of the digits of the representation of a number
    Returns the digital sum as an int.

    >>> digital_sum("1.414213562373095048801688724209698078569" \
    "671875376948073176679737990732478462107038850387534327641572")
    475
    """
    num = num.replace(".", "")

    total_sum = 0

    for digit in num:
        total_sum += int(digit)

    return total_sum


def solution():
    """Returns the total of the digital sum of the first one hundred
    decimal digits for all the irrational square roots of all the first
    one hundred numbers.

    >>> solution()
    40886
    """

    numbers = list(range(1, 100))
    numbers = [num for num in numbers if num not in (1, 4, 9, 16, 25, 36, 49, 64, 81)]

    total_sum = 0
    accuracy = 100

    for num in numbers:
        sqrt_num = sqrt_with_accuracy(num, accuracy)
        total_sum += digital_sum(sqrt_num)

    return total_sum


if __name__ == "__main__":
    print(solution())
