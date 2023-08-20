# https://en.wikipedia.org/wiki/Smith%E2%80%93Waterman_algorithm
# Score constants
"""
Score constants used in the Smith-Waterman algorithm. Matches are given a positive
score while mismatches are given a negative score. Gaps are also penalized.
"""
MATCH = 1
MISMATCH = -1
GAP = -2


def score_function(a: str, b: str) -> int:
    """
    Calculate the score for a character pair based on whether they match or mismatch.
    Returns 1 if the characters match, -1 if they mismatch.
    >>> score_function('A', 'A')
    1
    >>> score_function('A', 'C')
    -1
    """
    if a == b:
        return MATCH
    else:
        return MISMATCH


def smith_waterman(query: str, subject: str) -> list[list[int]]:
    """
    Perform the Smith-Waterman local sequence alignment algorithm.
    Returns a 2D list representing the score matrix. Each value in the matrix
    corresponds to the score of the best local alignment ending at that point.
    >>> smith_waterman('ACAC', 'CA')
    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 2], [0, 1, 0]]
    """

    # Initialize score matrix
    m = len(query)
    n = len(subject)
    score = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Calculate scores for each cell
            match = score[i - 1][j - 1] + score_function(query[i - 1], subject[j - 1])
            delete = score[i - 1][j] + GAP
            insert = score[i][j - 1] + GAP

            # Take maximum score
            score[i][j] = max(0, match, delete, insert)

    return score


def traceback(score: list[list[int]], query: str, subject: str) -> str:
    r"""
    Perform traceback to find the optimal local alignment.
    Starts from the highest scoring cell in the matrix and traces back recursively
    until a 0 score is found. Returns the alignment strings.
    >>> traceback([[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 2], [0, 1, 0]], 'ACAC', 'CA')
    'CAC\nCA-'
    """

    # Traceback logic to find optimal alignment
    i = len(query)
    j = len(subject)
    align1 = ""
    align2 = ""

    while i > 0 and j > 0:
        if score[i][j] == score[i - 1][j - 1] + score_function(
            query[i - 1], subject[j - 1]
        ):
            # optimal path is a diagonal take both letters
            align1 = query[i - 1] + align1
            align2 = subject[j - 1] + align2
            i -= 1
            j -= 1
        elif score[i][j] == score[i - 1][j] + GAP:
            # optimal path is a vertical
            align1 = query[i - 1] + align1
            align2 = "-" + align2
            i -= 1
        else:
            # optimal path is a horizontal
            align1 = "-" + align1
            align2 = subject[j - 1] + align2
            j -= 1

    return f"{align1}\n{align2}"


if __name__ == "__main__":
    query = "HEAGAWGHEE"
    subject = "PAWHEAE"

    score = smith_waterman(query, subject)
    print(traceback(score, query, subject))
