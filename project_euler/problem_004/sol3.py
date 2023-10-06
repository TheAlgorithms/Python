"""
Palindrome Six-Digit Numbers

This program finds six-digit numbers that are palindromes and can be expressed as the product of two three-digit numbers.

References:
    - https://en.wikipedia.org/wiki/Palindrome
"""
import time


def is_palindrome(number: int) -> bool:
    """
    Checks if a given number is a palindrome.
    Returns boolean indicating if the number is a palindrome.

    >>> is_palindrome(121)
    True
    >>> is_palindrome(123)
    False
    >>> is_palindrome(999999)
    True
    >>> is_palindrome(100001)
    True
    >>> is_palindrome(123456)
    False
    """

    str_num = str(number)
    return str_num == str_num[::-1]


def find_palindrome_products() -> list:
    """
    Finds six-digit numbers that are palindromes and can be expressed as the product of two three-digit numbers.
    Returns a list of tuples where each tuple contains the palindrome number and its two three-digit factors.

    >>> find_palindrome_products()
    [(...), (...), ...]
    """

    results = []
    for i in range(100000, 999999):
        if is_palindrome(i):
            for j in range(100, 999):
                quotient = i // j
                if i % j == 0 and 100 <= quotient <= 999:
                    results.append((i, j, quotient))
    return results


if __name__ == "__main__":
    palindromes = find_palindrome_products()
    print("solution() =", max(palindromes)[0])
