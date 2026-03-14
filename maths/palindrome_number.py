def is_palindrome(number: int) -> bool:
    """
    Determines if an integer is a palindrome without using string conversion.

    Logic:
    1. Negative numbers are not palindromes.
    2. Numbers ending in 0 (except 0 itself) are not palindromes.
    3. Reverse half of the number and compare.

    Examples:
    >>> is_palindrome(121)
    True
    >>> is_palindrome(12321)
    True
    >>> is_palindrome(10)
    False
    >>> is_palindrome(-121)
    False
    >>> is_palindrome(0)
    True
    """
    if number < 0 or (number % 10 == 0 and number != 0):
        return False

    reversed_half = 0
    while number > reversed_half:
        reversed_half = (reversed_half * 10) + (number % 10)
        number //= 10

    return number == reversed_half or number == reversed_half // 10
