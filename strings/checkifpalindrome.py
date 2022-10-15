def checkifpalindrome(s: str) -> bool:
    """
    Determine whether the given word is a palindrome
    :param s:
    :return: string being "YES" if it is a palindrome and "NO" if it is not a palindrome:
    >>> palindrome(Bib)
    Yes
    >>>palindrome(Nun)
    Yes
    >>>palindrome(A man)
    No
    >>>palindrome(Hello)
    No
    >>>palindrome(Madam)
    Yes
    """

    s = s.lower()
    string_rev = s[::-1]
    if string_rev == s:
        return True
    else:
        return False


if __name__ == "__main__":
    s = input()
    if checkifpalindrome(s):
        print("Yes")
    else:
        print("No")
