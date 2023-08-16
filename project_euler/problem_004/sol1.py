"""
Project Euler Problem 4: https://projecteuler.net/problem=4

Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

References:
    - https://en.wikipedia.org/wiki/Palindromic_number
"""


def solution(n: int = 998001) -> int:
    """
    Returns the largest palindrome made from the product of two 3-digit
    numbers which is less than n.

    >>> solution(20000)
    19591
    >>> solution(30000)
    29992
    >>> solution(40000)
    39893
    >>> solution(10000)
    Traceback (most recent call last):
        ...
    ValueError: That number is larger than our acceptable range.
    """

    # fetches the next number
    for number in range(n - 1, 9999, -1):
        str_number = str(number)

        # checks whether 'str_number' is a palindrome.
        if str_number == str_number[::-1]:
            divisor = 999

            # if 'number' is a product of two 3-digit numbers
            # then number is the answer otherwise fetch next number.
            while divisor != 99:
                if (number % divisor == 0) and (len(str(number // divisor)) == 3.0):
                    return number
                divisor -= 1
    raise ValueError("That number is larger than our acceptable range.")


if __name__ == "__main__":
    print(f"{solution() = }")
