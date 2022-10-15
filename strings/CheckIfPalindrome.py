def palindrome(s: str) -> str:
    """
    Determines whether the given word is a palindrome
    :param str:
    :return: string:
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
    n_inp = int(input()) #Numbers of case test
    for item in range(n_inp):
        size = int(input()) # Size of string
        n = input() # String
        if len(n) > size:
            print("Oversized or is different.")
        else:
            print(palindrome(n))
