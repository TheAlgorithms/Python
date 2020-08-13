"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.

"""


def factorial(n: int) -> int:
    """
    Returns the factorial of n
    >>> factorial(5)
    120
    >>> factorial(1)
    1
    >>> factorial(0)
    1
    """
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
    digits = list(map(int, str(n)))
    summ = sum(factorial(digit) for digit in digits)
    return summ


def compute() -> int:
    """
    Returns the sum of all numbers whose 
    sum of the factorials of all digits
    add up to the number itself.
    >>> compute()
    40730
    """
    summ = 0
    for num in range(3, 7 * factorial(9) + 1):
        if sum_of_digit_factorial(num) == num:
            summ += num
    return summ


if __name__ == "__main__":
    print(compute())