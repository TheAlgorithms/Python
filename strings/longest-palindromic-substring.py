def longest_palindromic_substring(s: str) -> str:
    if len(s) < 2 or s == s[::-1]:  # Quick check for a single character or an already palindromic string
        return s

    start, max_len = 0, 1

    for i in range(1, len(s)):
        # Odd-length palindrome (centered at s[i])
        odd = s[i - max_len - 1:i + 1]
        # Even-length palindrome (centered between s[i-1] and s[i])
        even = s[i - max_len:i + 1]

        # Check which palindrome is longer
        if i - max_len - 1 >= 0 and odd == odd[::-1]:
            start = i - max_len - 1
            max_len += 2
        elif even == even[::-1]:
            start = i - max_len
            max_len += 1

    return s[start:start + max_len]
