def is_number_palindromic(num: int) -> bool:
    """
    This function checks if given number is palindromic or not.
    >>> is_number_palindromic(121)
    True
    >>> is_number_palindromic(1231)
    False
    >>> is_number_palindromic(12321)
    True
    >>> is_number_palindromic(1211)
    False
    """
    num_rev = str(num)[::-1]
    num_rev = int(num_rev)
    if num == num_rev:
        return True
    else:
        return False


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
