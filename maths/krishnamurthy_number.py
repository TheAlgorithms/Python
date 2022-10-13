"""
 == Krishnamurthy Number ==
It is also known as Peterson Number
A Krishnamurthy Number is a number whose sum of the
factorial of the digits equals to the original
number itself.

For example: 145 = 1! + 4! + 5!
    So, 145 is a Krishnamurthy Number
"""


def factorial(digit: int) -> int:
    """
    >>> factorial(3)
    6
    >>> factorial(0)
    1
    >>> factorial(5)
    120
    """

    return 1 if digit in (0, 1) else (digit * factorial(digit - 1))


def krishnamurthy(number: int) -> bool:
    """
    >>> krishnamurthy(145)
    True
    >>> krishnamurthy(240)
    False
    >>> krishnamurthy(1)
    True
    """

    fact_sum = 0
    duplicate = number
    while duplicate > 0:
        duplicate, digit = divmod(duplicate, 10)
        fact_sum += factorial(digit)
    return fact_sum == number


if __name__ == "__main__":
    print("Program to check whether a number is a Krisnamurthy Number or not.")
    number = int(input("Enter number: ").strip())
    print(
        f"{number} is {'' if krishnamurthy(number) else 'not '}a Krishnamurthy Number."
    )
