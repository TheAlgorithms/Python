def longest_palindromic_substring(string: str) -> str:
    """
    Given a string, returns the longest palindromic substring in the string.

    :param string: The input string.
    :return: The longest palindromic substring.

    Examples:
    >>> result = longest_palindromic_substring("babad")
    >>> result in ['bab', 'aba']
    True
    >>> longest_palindromic_substring("cbbd")
    'bb'
    >>> longest_palindromic_substring("a")
    'a'
    >>> longest_palindromic_substring("")
    ''
    """
    if len(string) < 2:
        return string

    start = 0
    end = 0

    for i in range(len(string)):
        len1 = expand_around_center(string, i, i)
        len2 = expand_around_center(string, i, i + 1)
        max_len = max(len1, len2)

        if max_len > end - start + 1:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return string[start : end + 1]


def expand_around_center(string: str, left: int, right: int) -> int:
    """
    Expands around the center and returns the length of the palindrome.

    :param string: The input string.
    :param left: The left index.
    :param right: The right index.
    :return: The length of the palindrome.

    Examples:
    >>> expand_around_center("babad", 0, 0)
    1
    >>> expand_around_center("babad", 2, 2)
    3
    >>> expand_around_center("cbbd", 1, 2)
    2
    >>> expand_around_center("a", 0, 0)
    1
    """
    while left >= 0 and right < len(string) and string[left] == string[right]:
        left -= 1
        right += 1
    return right - left - 1


# Run the doctests
if __name__ == "__main__":
    import doctest

    doctest.testmod()
