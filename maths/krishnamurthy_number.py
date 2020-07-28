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
    function to calculate factorial of each digit
    """

    return 1 if (digit == 0 or digit == 1) else (digit * factorial(digit - 1))


def krishnamurthy(number: int) -> bool:
    """
    >>> krishnamurthy(145)
    True

    >>> krishnamurthy(240)
    False

    >>> krishnamurthy(1)
    True
    """

    factSum = 0
    duplicate = number
    while duplicate > 0:
        factSum += factorial(duplicate % 10)
        duplicate //= 10
    return factSum == number


if __name__ == "__main__":
    print("Program to check whether a number is a Krisnamurthy Number or not")
    number = int(input("Enter number: ").strip())
    print(
        f"{number} is {'' if krishnamurthy(number) else 'not '} a Krishnamurthy Number."
    )
