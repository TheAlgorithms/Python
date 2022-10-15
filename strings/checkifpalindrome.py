def checkifpalindrome(s: str) -> str:
    """
    Determine whether the given word is a palindrome
    :param s:
    :return: string being "YES" or "NO":
    >>> palindrome(bib)
    Yes
    >>>palindrome(nun)
    Yes
    >>>palindrome(a man)
    No
    >>>palindrome(pedro)
    No
    >>>palindrome(madam)
    Yes
    """

    string_rev = s[::-1]
    if string_rev == s:
        return "Yes"
    else:
        return "No"


if __name__ == "__main__":
    s = input()
    print(checkifpalindrome(s))
