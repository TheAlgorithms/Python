import doctest


def get_palindrome(s: str) -> str:
    """
    Generates a palindrome by forming a mirror image of the string passed.

    - If the string contains spaces, All spaces will be removed to form the
    palindrome.
    - All letters will be converted to lower case.
    - All digits and special symbols will also be considered in the palindrome
    generation.

    >>> get_palindrome('Github')
    'githubuhtig'

    >>> get_palindrome("level")
    'level'

    >>> get_palindrome("firstlevel")
    'firstleveltsrif'

    >>> get_palindrome('The Third Level')
    'thethirdleveldrihteht'

    >>> get_palindrome('$99 for the coffee')
    '$99forthecoffeeffocehtrof99$'

    :param s: The string to generate the palindrome from
    :return: A mirror image palindrome of the string s
    """
    s = s.replace(" ", "").lower()
    for i, letter in enumerate(s):
        if s[i:][::-1] == s[i:]:
            return s + s[:i][::-1]


doctest.testmod()
