"""Needleman-Wunsch algorithm for global sequence alignment.

Reference:
    https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm

The Needleman-Wunsch algorithm (1970) is a dynamic programming algorithm
used in bioinformatics and computational biology to find the optimal global
alignment between two sequences (such as DNA, RNA, or protein sequences).

Unlike local alignment algorithms (e.g., Smith-Waterman), which find the
highest-scoring local sub-regions, Needleman-Wunsch aligns both sequences across
their entire lengths from start to finish.

Algorithm:
1. Initialization:
   - Construct a matrix of size (m + 1) x (n + 1) where m and n are sequence lengths.
   - Initialize boundary conditions:
     score_matrix[i][0] = i * gap_score
     score_matrix[0][j] = j * gap_score

2. Matrix Filling (Recurrence Relation):
   For each cell (i, j):
     diagonal = score_matrix[i - 1][j - 1] + (match_score if seq1[i-1] == seq2[j-1]
                                              else mismatch_score)
     deletion = score_matrix[i - 1][j] + gap_score
     insertion = score_matrix[i][j - 1] + gap_score
     score_matrix[i][j] = max(diagonal, deletion, insertion)

3. Traceback:
   - Start from the bottom-right cell (m, n) and trace back to (0, 0).
   - At each step, determine which direction (diagonal, up, or left) produced the
     maximum score, assembling the aligned sequences in reverse order.

Complexity:
    Time Complexity:  O(m * n) where m and n are the lengths of the sequences.
    Space Complexity: O(m * n) to store the score matrix for traceback.
"""

from __future__ import annotations


def needleman_wunsch(
    sequence1: str,
    sequence2: str,
    match_score: int = 1,
    mismatch_score: int = -1,
    gap_score: int = -1,
) -> tuple[str, str, int]:
    """Compute the optimal global sequence alignment using Needleman-Wunsch.

    Parameters:
        sequence1: The first input sequence to align.
        sequence2: The second input sequence to align.
        match_score: Score awarded when two characters match (default: 1).
        mismatch_score: Penalty score when characters do not match (default: -1).
        gap_score: Penalty score for introducing a gap '-' (default: -1).

    Returns:
        A tuple containing:
        - aligned_sequence1: The first aligned sequence with inserted gaps.
        - aligned_sequence2: The second aligned sequence with inserted gaps.
        - alignment_score: The total optimal alignment score.

    Raises:
        ValueError: If gap_score is positive (gap must be neutral or a penalty).

    Examples:
        >>> # Wikipedia classic example
        >>> needleman_wunsch(
        ...     "GCATGCG", "GATTACA", match_score=1, mismatch_score=-1, gap_score=-1
        ... )
        ('GCA-TGCG', 'G-ATTACA', 0)

        >>> # Identical sequences
        >>> needleman_wunsch(
        ...     "ACGT", "ACGT", match_score=2, mismatch_score=-1, gap_score=-2
        ... )
        ('ACGT', 'ACGT', 8)

        >>> # Completely mismatched sequences
        >>> needleman_wunsch(
        ...     "AAAA", "TTTT", match_score=1, mismatch_score=-1, gap_score=-2
        ... )
        ('AAAA', 'TTTT', -4)

        >>> # One sequence is empty
        >>> needleman_wunsch("AGTC", "", match_score=1, mismatch_score=-1, gap_score=-1)
        ('AGTC', '----', -4)

        >>> # Both sequences are empty
        >>> needleman_wunsch("", "")
        ('', '', 0)

        >>> # Protein sequence example
        >>> needleman_wunsch(
        ...     "HEAGAWGHEE", "PAWHEAE", match_score=2, mismatch_score=-1, gap_score=-2
        ... )
        ('HEAGAWGHE-E', '---PAW-HEAE', -1)

        >>> # Invalid gap score
        >>> needleman_wunsch("A", "C", gap_score=5)
        Traceback (most recent call last):
            ...
        ValueError: gap_score must be non-positive (<= 0)
    """
    if gap_score > 0:
        msg = "gap_score must be non-positive (<= 0)"
        raise ValueError(msg)

    first_sequence_length = len(sequence1)
    second_sequence_length = len(sequence2)

    # Initialize the (m + 1) x (n + 1) dynamic programming score matrix
    score_matrix = [
        [0] * (second_sequence_length + 1) for _ in range(first_sequence_length + 1)
    ]

    # Fill base-case boundary penalties
    for row_index in range(first_sequence_length + 1):
        score_matrix[row_index][0] = row_index * gap_score
    for col_index in range(second_sequence_length + 1):
        score_matrix[0][col_index] = col_index * gap_score

    # Populate the score matrix using dynamic programming
    for row_index in range(1, first_sequence_length + 1):
        for col_index in range(1, second_sequence_length + 1):
            char1 = sequence1[row_index - 1]
            char2 = sequence2[col_index - 1]
            substitution = match_score if char1 == char2 else mismatch_score

            diagonal_score = score_matrix[row_index - 1][col_index - 1] + substitution
            deletion_score = score_matrix[row_index - 1][col_index] + gap_score
            insertion_score = score_matrix[row_index][col_index - 1] + gap_score

            score_matrix[row_index][col_index] = max(
                diagonal_score, deletion_score, insertion_score
            )

    # Traceback from bottom-right (m, n) to top-left (0, 0)
    aligned_chars_first: list[str] = []
    aligned_chars_second: list[str] = []
    curr_row = first_sequence_length
    curr_col = second_sequence_length

    while curr_row > 0 or curr_col > 0:
        if curr_row > 0 and curr_col > 0:
            char1 = sequence1[curr_row - 1]
            char2 = sequence2[curr_col - 1]
            substitution = match_score if char1 == char2 else mismatch_score

            # Check if diagonal step was optimal
            if (
                score_matrix[curr_row][curr_col]
                == score_matrix[curr_row - 1][curr_col - 1] + substitution
            ):
                aligned_chars_first.append(char1)
                aligned_chars_second.append(char2)
                curr_row -= 1
                curr_col -= 1
                continue

        # Check if vertical step (gap in second sequence) was optimal
        if (
            curr_row > 0
            and score_matrix[curr_row][curr_col]
            == score_matrix[curr_row - 1][curr_col] + gap_score
        ):
            aligned_chars_first.append(sequence1[curr_row - 1])
            aligned_chars_second.append("-")
            curr_row -= 1
        else:
            # Horizontal step (gap in first sequence)
            aligned_chars_first.append("-")
            aligned_chars_second.append(sequence2[curr_col - 1])
            curr_col -= 1

    aligned_sequence1 = "".join(reversed(aligned_chars_first))
    aligned_sequence2 = "".join(reversed(aligned_chars_second))
    final_score = score_matrix[first_sequence_length][second_sequence_length]

    return aligned_sequence1, aligned_sequence2, final_score


if __name__ == "__main__":
    import doctest

    doctest.testmod()
