"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""

from math import factorial


def sum_of_digit_factorial(n: int) -> int:
    """
    Returns the sum of the digits in n
    >>> sum_of_digit_factorial(15)
    121
    >>> sum_of_digit_factorial(0)
    1
    """
    return sum(factorial(int(char)) for char in str(n))


def compute() -> int:
    """
    Returns the sum of all numbers whose
    sum of the factorials of all digits
    add up to the number itself.
    >>> compute()
    40730
    """
    limit = 7 * factorial(9) + 1
    return sum(i for i in range(3, limit) if sum_of_digit_factorial(i) == i)


if __name__ == "__main__":
    print(f"{compute()} = ")
