"""
This script is a implementation of the Damerau-Levenshtein distance algorithm.

It's an algorithm that measures the edit distance between two string sequences

More information about this algorithm can be found in this wikipedia article:
https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance
"""


def damerau_levenshtein_distance(first_string: str, second_string: str) -> int:
    """
    Implements the Damerau-Levenshtein distance algorithm that measures
    the edit distance between two strings.

    Parameters:
        first_string: The first string to compare
        second_string: The second string to compare

    Returns:
        distance: The edit distance between the first and second strings

    >>> damerau_levenshtein_distance("cat", "cut")
    1
    >>> damerau_levenshtein_distance("kitten", "sitting")
    3
    >>> damerau_levenshtein_distance("hello", "world")
    4
    >>> damerau_levenshtein_distance("book", "back")
    2
    >>> damerau_levenshtein_distance("container", "containment")
    3
    >>> damerau_levenshtein_distance("container", "containment")
    3
    """
    # Create a dynamic programming matrix to store the distances
    dp_matrix = [[0] * (len(second_string) + 1) for _ in range(len(first_string) + 1)]

    # Initialize the matrix
    for i in range(len(first_string) + 1):
        dp_matrix[i][0] = i
    for j in range(len(second_string) + 1):
        dp_matrix[0][j] = j

    # Fill the matrix
    for i, first_char in enumerate(first_string, start=1):
        for j, second_char in enumerate(second_string, start=1):
            cost = int(first_char != second_char)

            dp_matrix[i][j] = min(
                dp_matrix[i - 1][j] + 1,  # Deletion
                dp_matrix[i][j - 1] + 1,  # Insertion
                dp_matrix[i - 1][j - 1] + cost,  # Substitution
            )

            if (
                i > 1
                and j > 1
                and first_string[i - 1] == second_string[j - 2]
                and first_string[i - 2] == second_string[j - 1]
            ):
                # Transposition
                dp_matrix[i][j] = min(dp_matrix[i][j], dp_matrix[i - 2][j - 2] + cost)

    return dp_matrix[-1][-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
