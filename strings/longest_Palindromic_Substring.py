"""
    Algorithm:
    1.	Maintain a variable ‘ longest_length = 1 ‘ (for storing longest palindromic substring length) and ‘ start =0 ‘ (for storing index of longest palindromic substring length).
    2.	The idea is very simple, we will traverse through the entire string with i=0 to i<(length of string) while traversing, initialize ‘start‘ and ‘end‘ pointer such that start= i-1 and end= i+1.
    3.	keep incrementing ‘end’ until str[end]==str[i]  similarly keep decrementing ‘start’ until str[start]==str[i].
    4.	Finally we will keep incrementing ‘end’ and decrementing ‘start’ until str[start]==str[end].
    5.	calculate length=end-start-1, if length > longest_length then longest_length = length and start = start+1 .
    6.	Return the longest palindromic substring.
    """


def longestPalindromicSubstring(string: str) -> str:
    """
    Returns the longest palindromic substring present in given string.
    >>> longestPalindromicSubstring("malayalam")
    'malayalam'
    >>> longestPalindromicSubstring("cabad")
    'aba'
    >>> longestPalindromicSubstring("zxyzzzx")
    'zzz'
    """
    length = len(string)  # calculating the length of string
    if length < 2:
        return length
    start_index = 0
    longest_length = 1
    for i in range(length):
        start = i - 1
        end = i + 1
        while end < length and string[end] == string[i]:
            end = end + 1
        while start >= 0 and string[start] == string[i]:
            start = start - 1
        while start >= 0 and end < length and string[start] == string[end]:
            start = start - 1
            end = end + 1
        curr_length = end - start - 1
        if longest_length < curr_length:
            longest_length = curr_length
            start_index = start + 1

    return string[start_index : start_index + longest_length]


if __name__ == "__main__":
    print("Longest Palindromic Substring is: " + longestPalindromicSubstring("cabad"))
    print("Longest Palindromic Substring is: " + longestPalindromicSubstring("zxyzzzx"))
    print(
        "Longest Palindromic Substring is: " + longestPalindromicSubstring("malayalam")
    )


# This program takes O(n^2) time complexity to find the longest palindromic substring
# This program takes O(1) space complexity to find the longest palindromic substring
