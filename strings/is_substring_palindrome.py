MAX_LEN = 1000

text = ""
dp = [[False for i in range(MAX_LEN)] for i in range(MAX_LEN)]

def preprocess(s):
    """
        Preprocesses a string using dynamic programming.
        Time complexity: O(n^2)
    """
    global text
    global dp
    text = s
    dp = [[False for i in range(MAX_LEN)] for i in range(MAX_LEN)]
    n = len(s)

    for i in range(n):
        dp[i][i] = True

    for i in range(n - 1):
        dp[i][i + 1] = (text[i] == text[i + 1]) 

    for substr_len in range(2, n + 1):
        for i in range(n - substr_len + 1):
            j = i + substr_len - 1
            dp[i][j] = (text[i] == text[j] and dp[i + 1][j - 1])


def is_substring_palindrome(l, r):
    """
        Returns True if and only if the substring text[l:r] is a palindrome.
        Time complexity: O(1)
        Call preprocess function at least once, before calling this function.
    """
    n = len(text)
    if l >= r or l < 0 or r > n:
        return False
    else:
        return dp[l][r - 1]


if __name__ == '__main__':
    s = "'nursesrun' and 'racecar' are some palindromes."

    preprocess(s)

    # Answering some queries:
    if is_substring_palindrome(1, 10):
        print(s[1:10], "is a palindrome.")
    else:
        print(s[1:10], "is not a palindrome.")

    if is_substring_palindrome(17, 24):
        print(s[17:24], "is a palindrome.")
    else:
        print(s[17:24], "is not a palindrome.")

    if is_substring_palindrome(35, 45):
        print(s[35:45], "is a palindrome.")
    else:
        print(s[35:45], "is not a palindrome.")
