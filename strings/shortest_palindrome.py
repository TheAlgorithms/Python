"""
Program to find the shortest palindrome in the given string
"""

def shortestpalindrome(s: str) -> str:
    
    """
    >>> shortestPalindrome("aacecaaa")
    'aaacecaaa'
    >>> shortestPalindrome("abcd")
    'dcbabcd'
    """

    # Reverse the input string 's' and store it in 'r'.
    r = s[::-1]

    # Check if the original string 's' is already a palindrome.
    if s == s[::-1]:
        return s
    
    # Iterate through the characters of 's'.
    for i in range(len(s) + 1):
        # Check if the substring of 's' starting from index 'i' matches with the reversed string 'r'.
        if s.startswith(r[i:]):
            # If palindrome found, construct shortest palindrome by concatenating reversed prefix 'r[:i]' with original string 's'.
            return r[:i] + s

if __name__ == "__main__":
    from doctest import testmod

    testmod()          