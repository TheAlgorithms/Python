def edit_distance(source: str, target: str) -> int:
    """
    Calculate the edit distance between two strings using dynamic programming.
    Edit distance is the minimum number of operations (insertions, deletions, or
    substitutions) required to transform one string into another.

    Args:
    source (str): The original string.
    target (str): The string to transform into.

    Returns:
    int: The minimum number of operations required.

    Examples:
    >>> edit_distance("GATTIC", "GALTIC")
    1
    >>> edit_distance("ATCGCTG", "TAGCTAA")
    4
    """

    dp = [[0 for _ in range(len(target) + 1)] for _ in range(len(source) + 1)]

    # Populate the matrix
    for i in range(len(source) + 1):
        for j in range(len(target) + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif source[i - 1] == target[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]  # Remove  # Insert
                )  # Replace

    return dp[len(source)][len(target)]


if __name__ == "__main__":
    print(edit_distance("GATTIC", "GALTIC"))  # Output: 1
    print(edit_distance("ATCGCTG", "TAGCTAA"))  # Output: 4

