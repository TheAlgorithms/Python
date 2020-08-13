"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""


def factorial(n: int) -> int:
    """Return the factorial of n.
    >>> factorial(5)
    120
    >>> factorial(1)
    1
    >>> factorial(0)
    1
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0
    >>> factorial(1.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    """

    if not n >= 0:
        raise ValueError("n must be >= 0")
    if int(n) != n:
        raise ValueError("n must be exact integer")
    if n + 1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result


def sum_of_digit_factorial(n: int) -> int:
    """
    Returns the sum of the digits in n
    >>> sum_of_digit_factorial(15)
    121
    >>> sum_of_digit_factorial(0)
    1
    """
    return sum(factorial(int(digit)) for digit in str(n))


def compute() -> int:
    """
    Returns the sum of all numbers whose
    sum of the factorials of all digits
    add up to the number itself.
    >>> compute()
    40730
    """
    return sum(
        num
        for num in range(3, 7 * factorial(9) + 1)
        if sum_of_digit_factorial(num) == num
    )


if __name__ == "__main__":
    print(compute())
