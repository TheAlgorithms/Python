def is_string_palindrome(words: str) -> bool:
    """
    Returns whether `num` is a palindrome or not
    (see for reference https://en.wikipedia.org/wiki/Palindromic_number).

    >>> is_string_palindrome("-121")
    False
    >>> is_string_palindrome("0")
    True
    >>> is_string_palindrome("10")
    False
    >>> is_string_palindrome("11")
    True
    >>> is_string_palindrome("101")
    True
    >>> is_string_palindrome("120")
    False
    >>> is_string_palindrome(120)
    False
    >>> is_string_palindrome("madam")
    True
    >>> is_string_palindrome("racecar")
    True
    >>> is_string_palindrome("hello")
    False
    >>> is_string_palindrome("A man a plan a canal Panama")
    True
    >>> is_string_palindrome(120)
    False
    >>> is_string_palindrome("")
    True
    >>> is_string_palindrome("noon")
    True
    >>> is_string_palindrome("Was it a car or a cat I saw")
    True
    >>> is_string_palindrome("Python")
    False
    >>> is_string_palindrome(" ")
    True
    """
    cleaned_phrase = ''.join(words.split()).lower()
    return cleaned_phrase == cleaned_phrase[::-1]

if __name__ == "__main__":
    import doctest

    doctest.testmod()
