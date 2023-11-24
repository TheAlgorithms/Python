def edit_distance(source: str, target: str) -> int:
    """
    Edit distance algorithm is a string metric, i.e., it is a way of quantifying how
    dissimilar two strings are to one another. It is measured by counting the minimum
    number of operations required to transform one string into another.

    This implementation assumes that the cost of operations (insertion, deletion and
    substitution) is always 1

    Args:
    source: the initial string with respect to which we are calculating the edit
        distance for the target
    target: the target string, formed after performing n operations on the source string

    >>> edit_distance("GATTIC", "GALTIC")
    1
    """
    m, n = len(source), len(target)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif source[i - 1] == target[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],  # Deletion
                    dp[i][j - 1],  # Insertion
                    dp[i - 1][j - 1],  # Substitution
                )

    return dp[m][n]


if __name__ == "__main__":
    print(edit_distance("ATCGCTG", "TAGCTAA"))  # Answer is 4
