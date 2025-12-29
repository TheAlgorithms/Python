"""
Check whether a number is a palindrome.

A palindrome number reads the same forward and backward.
Example:
    121 -> True
    123 -> False
"""

def is_palindrome(number: int) -> bool:
    """
    Check if a number is a palindrome.

    :param number: Integer to check
    :return: True if palindrome, False otherwise
    """
    original = number
    reverse = 0

    while number > 0:
        reverse = reverse * 10 + number % 10
        number //= 10

    return original == reverse


if __name__ == "__main__":
    print(is_palindrome(121))   # True
    print(is_palindrome(123))   # False
