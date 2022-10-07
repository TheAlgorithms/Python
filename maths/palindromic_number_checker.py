def isNumberPalindromic(num : int) -> bool:
    """
    This function checks if given number is palindromic or not.
    >>> isNumberPalindromic(121)
    True
    >>> isNumberPalindromic(1231)
    False
    >>> isNumberPalindromic(12321)
    True
    >>> isNumberPalindromic(1211)
    False
    """
    numRev = str(num)[::-1]
    numRev = int(numRev)
    if (num == numRev):
        return True
    else:
        return False


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
