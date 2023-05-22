def is_palindrome(num: int) -> bool:
    """
    Returns whether `num` is a palindrome or not
    (see for reference https://en.wikipedia.org/wiki/Palindromic_number).

    >>> is_palindrome(-121)
    False
    >>> is_palindrome(0)
    True
    >>> is_palindrome(10)
    False
    >>> is_palindrome(11)
    True
    >>> is_palindrome(101)
    True
    >>> is_palindrome(120)
    False
    """
    if num < 0:
        return False

    num_copy: int = num
    rev_num: int = 0
    while num > 0:
        rev_num = rev_num * 10 + (num % 10)
        num //= 10

    return num_copy == rev_num


if __name__ == "__main__":
    import doctest

    doctest.testmod()
