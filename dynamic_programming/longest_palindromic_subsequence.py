"""
The longest palindromic subsequence (LPS) is the longest
subsequence in a string that is the same when reversed.
A subsequence is not the same as a substring.
Unlike substrings, the characters of subsequences are not required
to occupy consecutive positions.

Explanation:
https://www.techiedelight.com/longest-palindromic-subsequence-using-dynamic-programming/
"""


def longest_palindromic_subsequence(sequence: str, i: int, j: int, memo: dict) -> int:
    """Find the longest palindromic subsequence in a given string

    :param sequence: The sequence to search in
    :type sequence: str
    :param i: The initial lower index bounding the search area
    :type i: int
    :param j: The initial upper index bounding the search area
    :type j: int
    :param memo: The memoization table used to optimize this algorithm
    :type memo: dict
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
    if i == j:
        return 1

    # Base case: If i is greater than j you have gone too far
    if i > j:
        return 0

    # Each subproblem can be identified by the substring it works on.
    # So, we can identify whether a subproblem has been solved by
    # checking if it is in the memo table.
    key = (i, j)

    if key not in memo:

        # If the first character of the current string equals the last
        if sequence[i] == sequence[j]:
            # Recur with the remaining substring and put the result in the memo table
            memo[key] = (
                longest_palindromic_subsequence(sequence, i + 1, j - 1, memo) + 2
            )

        # If the first and last characters are NOT equal, find the larger LPS between:
        #   a.) the substring formed by removing the first character
        #   b.) the substring formed by removing the last character
        # Then, store in the memo table
        else:
            memo[key] = max(
                longest_palindromic_subsequence(sequence, i + 1, j, memo),
                longest_palindromic_subsequence(sequence, i, j - 1, memo),
            )

    return memo[key]


if __name__ == "__main__":
    sequence = input("Enter sequence string: ")
    len_lps = longest_palindromic_subsequence(sequence, 0, len(sequence) - 1, {})
    print(f'The length of the LPS in "{sequence}" is {len_lps}')
