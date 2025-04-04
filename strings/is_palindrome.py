def is_palindrome(txt):
    """
    Checks if a given text is a palindrome.

    A palindrome is a word or phrase that reads the same forwards and backwards.

    Parameters:
    txt (str): The text to check.

    Returns:
    bool: True if the text is a palindrome, False otherwise.
    """
    return txt == txt[::-1]


print(is_palindrome("radar"))
