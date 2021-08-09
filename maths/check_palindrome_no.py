"""
Checking Palindrome number.

A number is a Palindrome if it remains unchanged when reversed
for example: 101, 131, 454, 616 are Palindrome numbers.
             123, 199, 342, 453 are not Palindrome numbers.
"""


def check_palindrome(number: int) -> bool:
    """
    return True if number is palindrome
    or
    return false if number is not palindrome

    >>> check_palindrome(101)
    True
    >>> check_palindrome(434)
    True
    >>> check_palindrome(9531)
    False
    >>> check_palindrome(12321)
    True

    """
    if number == 0:
        return True
    if number:
        number = abs(number)
        tmp = number
        same = 0
        while number > 0:
            digit = number % 10
            same = same * 10 + digit
            number = number // 10
    return same == tmp


if __name__ == "__main__":
    print(check_palindrome(int(input())))
