def is_palindrome_number(number: int) -> bool:
    """
    Checks if a given integer is a palindrome without converting it to a string.
    A palindrome is a number that reads the same backward as forward.
    Negative numbers are not considered palindromes by this definition.

    Args:
        number: The integer to check.

    Returns:
        True if the number is a palindrome, False otherwise.

    Examples:
    >>> is_palindrome_number(121)
    True
    >>> is_palindrome_number(123)
    False
    >>> is_palindrome_number(10)
    False
    >>> is_palindrome_number(12321)
    True
    >>> is_palindrome_number(7)
    True
    >>> is_palindrome_number(0)
    True
    >>> is_palindrome_number(-121)
    False
    """
    # Negative numbers are not considered palindromes
    if number < 0:
        return False

    original_number = number
    reversed_number = 0

    while number > 0:
        # Get the last digit
        digit = number % 10
        
        # Build the reversed number
        reversed_number = (reversed_number * 10) + digit
        
        # Remove the last digit from the original number
        number //= 10

    # Compare the original with the reversed number
    return original_number == reversed_number
