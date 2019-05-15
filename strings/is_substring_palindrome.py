"""
This is a Python implementation for checking whether a substring is palindromic or not.

For testing run:
python3 is_substring_palindrome.py
"""

def preprocess_all_substrings(text):
    """Find all palindromic substrings of a string, using dynamic programming, with O(n^2) time complexity.
    
    Args:
        text: the string to be preprocessed.
    Returns:
        A 2-dimentional matrix called ret.
        ret[i][j] is True, if and only if the substring text[i:j+1] is palindromic.
    """
    n = len(text)
    ret = [[False for i in range(n)] for j in range(n)]

    for i in range(n):
        ret[i][i] = True
        if i + 1 < n:
            ret[i][i + 1] = (text[i] == text[i + 1]) 

    for substr_len in range(2, n + 1):
        for i in range(n - substr_len + 1):
            j = i + substr_len - 1
            ret[i][j] = (text[i] == text[j] and ret[i + 1][j - 1])

    return ret


def is_substring_palindrome(dp, l, r):
    """Check whether a substring is palindromic or not, with O(1) time complexity.

    Args:
        dp: a preprocessed 2-dimentional matrix.
            dp[i][j] has been set to True, if and only if the substring text[i:j+1] is palindromic.
        l: left most character of the substring index
        r: right most character of the substring index
    Returns:
        True, if and only if text[l:r+1] substring is palindromic.
        False, if and only if text[l:r+1] substring is not palindromic.
    """
    n = len(dp)
    if l >= r or l < 0 or r > n:
        return False
    else:
        return dp[l][r - 1]


if __name__ == '__main__':
    s = "'nursesrun' and 'racecar' are some palindromes."

    dp = preprocess_all_substrings(s)

    # Answering some queries:
    if is_substring_palindrome(dp, 1, 10):
        print(s[1:10], "is a palindrome.")
    else:
        print(s[1:10], "is not a palindrome.")

    if is_substring_palindrome(dp, 17, 24):
        print(s[17:24], "is a palindrome.")
    else:
        print(s[17:24], "is not a palindrome.")

    if is_substring_palindrome(dp, 35, 45):
        print(s[35:45], "is a palindrome.")
    else:
        print(s[35:45], "is not a palindrome.")
