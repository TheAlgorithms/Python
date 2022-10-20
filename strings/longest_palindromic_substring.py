"""
1. Maintain a variable ‘ longest_length = 1 ‘
(for storing longest palindromic substring length) and ‘ start =0 ‘.
2.	The idea is very simple, we will traverse through the entire
string with i=0 to i<(length of string) while traversing, initialize
’start‘ and ‘end‘ pointer such that start= i-1 and end= i+1.
3.	keep incrementing ‘end’ until str[end]==str[i]  similarly
keep decrementing ‘start’ until str[start]==str[i].
4.	Finally we will keep incrementing ‘end’ and decrementing
‘start’ until str[start]==str[end].
5.	calculate length=end-start-1, if length > longest_length
then longest_length = length and start = start+1 .
6.	Return the longest palindromic substring.
"""

import doctest


def longest_palindromic_substring(string: str) -> str:
    """
    This program takes O(n^2) time complexity to find the longest palindromic substring
    This program takes O(1) space complexity to find the longest palindromic substring
    Returns the longest palindromic substring present in given string.

    >>> longest_palindromic_substring("malayalam")
    'malayalam'
    >>> longest_palindromic_substring("cabad")
    'aba'
    >>> longest_palindromic_substring("zxyzzzx")
    'zzz'
    """
    length = len(string)
    if length < 2:
        return string
    start_index = 0
    longest_length = 1
    for i, char in enumerate(string):
        start = i - 1
        end = i + 1
        while end < length and string[end] == char:
            end += 1
        while start >= 0 and string[start] == char:
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
    doctest.testmod()
