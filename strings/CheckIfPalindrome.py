def palindrome(s: str) -> str:
    """
    Determines whether the given word is a palindrome
    :param s: the string
    :return: string being "YES" if it is a palindrome and "NO" if it is not a palindrome:
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
        return 'Yes'
    else:
        return 'No'

if __name__ == "__main__":
    s = input() # String
    print(palindrome(s))
