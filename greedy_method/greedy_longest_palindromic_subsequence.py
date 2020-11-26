"""
The longest palindromic subsequence (LPS) is the longest
subsequence in a string that is the same when reversed.
A subsequence is not the same as a substring.
Unlike substrings, the characters of subsequences are not required
to occupy consecutive positions.

Explanation:
https://www.techiedelight.com/longest-palindromic-subsequence-using-dynamic-programming/
"""


def longest_palindromic_subsequence(
    sequence: str, begin_substring: int, end_substring: int
) -> int:
    """Find the longest palindromic subsequence in a given string

    :param sequence: The sequence to search in
    :type sequence: str
    :param i: The initial lower index bounding the search area
    :type i: int
    :param j: The initial upper index bounding the search area
    :type j: int
    :return: The length of the longest palindromic subsequence
    :rtype: int

    >>> longest_palindromic_subsequence("ABBDCACB", 0, 7)
    5
    >>> longest_palindromic_subsequence("nurses run", 0, 9)
    9
    >>> longest_palindromic_subsequence("Z", 0, 0)
    1
    """
    # If the sequence only has one character, it is a palindrome
    # This prevents a one-letter palindrome from being counted as 2
    if begin_substring == end_substring:
        return 1

    # Base case: If i is greater than j you have gone too far
    if begin_substring > end_substring:
        return 0

    # If the first character of the current string equals the last
    if sequence[begin_substring] == sequence[end_substring]:
        # Recur with the remaining substring
        return (
            longest_palindromic_subsequence(
                sequence, begin_substring + 1, end_substring - 1
            )
            + 2
        )

    # If the first and last characters are NOT equal, then find the larger LPS between:
    #   a.) the substring formed by removing the first character
    #   b.) the substring formed by removing the last character
    return max(
        longest_palindromic_subsequence(sequence, begin_substring + 1, end_substring),
        longest_palindromic_subsequence(sequence, begin_substring, end_substring - 1),
    )


if __name__ == "__main__":
    sequence = input("Enter sequence string: ")
    len_lps = longest_palindromic_subsequence(sequence, 0, len(sequence) - 1)
    print(f'The length of the LPS in "{sequence}" is {len_lps}')
