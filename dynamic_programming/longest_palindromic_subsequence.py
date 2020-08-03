"""
Longest Palindromic Subsequence Problem:
Find the longest sequence of characters from a given input string that
is the same backwards and forwards
https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
"""


def longest_palindromic_subsequence(s: str, length: int) -> int:

    """
    Computes the longest Palindromic sequence of a string

    :param s: str, the string we provide
    :param length: int, the length of the string
    :return L[0][n - 1]: int, the length of the longest Palindromic subsequence



    >>> longest_palindromic_subsequence("ABBCDABBC",9)
    5
    >>> longest_palindromic_subsequence("ABACCG",6)
    3
    >>> longest_palindromic_subsequence("55055901565109",14)
    9
    """

    # creating an array to store the values generated
    dp_table = [[1 for i in range(length)] for i in range(length)]

    # Filling in the array created
    for x in range(2, length + 1):
        for y in range(length + 1 - x):
            z = y + x - 1
            if s[y] == s[z] and x == 2:
                dp_table[y][z] = 2
            elif s[y] == s[z]:
                dp_table[y][z] = dp_table[y + 1][z - 1] + 2
            else:
                dp_table[y][z] = max(dp_table[y][z - 1], dp_table[y + 1][z])

    return dp_table[0][length - 1]


if __name__ == "__main__":
    test_case = "ABAC"

    len_of_test_case = len(test_case)
    print(
        "The longest palindromic subsequence is: "
        + str(longest_palindromic_subsequence(test_case, len_of_test_case))
    )

    import doctest

    doctest.testmod()
