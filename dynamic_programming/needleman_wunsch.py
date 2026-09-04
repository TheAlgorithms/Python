"""
Needleman-Wunsch Global Sequence Alignment Algorithm
=====================================================

Reference:
    Needleman, S.B. and Wunsch, C.D. (1970).
    "A general method applicable to the search for similarities in the
    amino acid sequence of two proteins."
    Journal of Molecular Biology, 48(3), 443-453.
    https://doi.org/10.1016/0022-2836(70)90057-4

Overview:
    The Needleman-Wunsch algorithm finds the OPTIMAL GLOBAL ALIGNMENT
    between two biological sequences (DNA, RNA, or protein).

    "Global" means we align the sequences from end to end : every
    character in both sequences must be placed somewhere in the alignment.

    It works in three distinct phases:
        1. Initialization  : Set up a 2D scoring grid with gap penalties.
        2. Matrix Filling  : Fill the grid using dynamic programming.
        3. Traceback       : Walk back through the grid to find the best alignment.

Scoring Convention used here:
    - Match   : +1  (same character in both sequences)
    - Mismatch: -1  (different characters)
    - Gap     : -2  (inserting a gap '-' into one of the sequences)
"""


# SECTION 1 : SCORING HELPERS


def get_match_score(
    char_a: str, char_b: str, match: int = 1, mismatch: int = -1
) -> int:
    """Return +match if the two characters are identical, else -mismatch.

    This is the substitution score used when comparing two aligned residues.
    It answers: "How good is it to pair these two characters together?"

    Args:
        char_a:    A single character from sequence 1 (e.g. 'A').
        char_b:    A single character from sequence 2 (e.g. 'T').
        match:     Score awarded for identical characters (default 1).
        mismatch:  Penalty applied for differing characters (default -1).

    Returns:
        match score if char_a == char_b, else the negative of mismatch.

    Examples:
        >>> get_match_score('A', 'A')
        1
        >>> get_match_score('A', 'T')
        -1
        >>> get_match_score('G', 'G', match=2, mismatch=0)
        2
    """
    # Same letter -> reward; different letter -> negate the mismatch value.
    # Because mismatch is passed as a positive penalty (e.g. 1), we negate it
    # to produce a negative score (e.g. -1).
    if char_a == char_b:
        return match
    return -abs(mismatch)  # always produce a non-positive penalty


# SECTION 2 : PHASE 1: INITIALIZATION


def initialize_score_matrix(rows: int, cols: int, gap_penalty: int = -2) -> list:
    """Build the empty (rows x cols) scoring grid and fill the border cells.

    Why do we need a border?
    -
    Think of the grid as having sequence 1 along the top and sequence 2
    down the left side.  The very first row represents aligning each prefix
    of sequence 1 against an *empty* sequence 2 : which requires inserting
    gaps for every character.  Same logic applies to the first column.

    So:
        score_matrix[0][col] = col * gap_penalty   (gaps to cover seq1's prefix)
        score_matrix[row][0] = row * gap_penalty   (gaps to cover seq2's prefix)

    The interior cells start at 0 and will be filled in Phase 2.

    Args:
        rows:         Number of rows    = len(seq2) + 1.
        cols:         Number of columns = len(seq1) + 1.
        gap_penalty:  Score for opening/extending a gap (default -2).

    Returns:
        A 2D list (list of lists) with border cells pre-filled.

    Examples:
        >>> initialize_score_matrix(3, 4, gap_penalty=-2)
        [[0, -2, -4, -6], [-2, 0, 0, 0], [-4, 0, 0, 0]]
    """
    #  Create an all-zero grid of size (rows x cols)
    # We use a list comprehension: for each row, create a list of `cols` zeros.
    score_matrix = [
        [0] * cols  # One row = a list of `cols` zeros
        for _ in range(rows)  # Repeat this for every row
    ]

    #  Fill the first ROW (row index 0)
    # score_matrix[0][col] represents aligning col characters of seq1
    # against zero characters of seq2, so we need `col` gaps.
    for col in range(cols):
        score_matrix[0][col] = col * gap_penalty
        # Example: col=3, gap=-2 -> score = 3 * -2 = -6

    #  Fill the first COLUMN (col index 0)
    # score_matrix[row][0] represents aligning zero characters of seq1
    # against `row` characters of seq2, so we need `row` gaps.
    for row in range(rows):
        score_matrix[row][0] = row * gap_penalty
        # Example: row=2, gap=-2 -> score = 2 * -2 = -4

    return score_matrix


def initialize_traceback_matrix(rows: int, cols: int) -> list:
    """Build the companion direction grid used during traceback.

    Every cell in the score_matrix will eventually be filled by choosing
    the best of three options (diagonal / up / left).  We record WHICH
    option was chosen here so the traceback can retrace the decision path.

    Direction codes:
        'D' -> Diagonal  (char from seq1 paired with char from seq2)
        'U' -> Up        (gap inserted into seq1)
        'L' -> Left      (gap inserted into seq2)
        'X' -> Start     (the top-left origin cell, no predecessor)

    Args:
        rows:  Number of rows    = len(seq2) + 1.
        cols:  Number of columns = len(seq1) + 1.

    Returns:
        A 2D list of strings, borders pre-labelled with 'L' / 'U' / 'X'.

    Examples:
        >>> tb = initialize_traceback_matrix(3, 3)
        >>> tb[0]
        ['X', 'L', 'L']
        >>> [tb[r][0] for r in range(3)]
        ['X', 'U', 'U']
    """
    #  Create a grid filled with empty strings
    traceback_matrix = [[""] * cols for _ in range(rows)]

    #  First cell is the origin: no predecessor
    traceback_matrix[0][0] = "X"

    #  First row: to get here we always came from the LEFT
    for col in range(1, cols):
        traceback_matrix[0][col] = "L"

    #  First column: to get here we always came from ABOVE (Up)
    for row in range(1, rows):
        traceback_matrix[row][0] = "U"

    return traceback_matrix


# SECTION 3 : PHASE 2: MATRIX FILLING (Core Dynamic Programming)


def fill_score_matrix(
    score_matrix: list,
    traceback_matrix: list,
    sequence_1: str,
    sequence_2: str,
    gap_penalty: int = -2,
    match: int = 1,
    mismatch: int = -1,
) -> tuple:
    """Fill every interior cell of the scoring grid using DP recurrence.

    The Recurrence Relation
    --
    For each cell (row, col), the alignment score is the MAXIMUM of:

        diagonal_score = score_matrix[row-1][col-1] + substitution_score
            -> We aligned seq2[row-1] with seq1[col-1]  (match or mismatch)

        up_score       = score_matrix[row-1][col]   + gap_penalty
            -> We inserted a gap into seq1 at this position

        left_score     = score_matrix[row][col-1]   + gap_penalty
            -> We inserted a gap into seq2 at this position

    We also record which direction gave the maximum in traceback_matrix
    so that Phase 3 can reconstruct the aligned sequences.

    Note on indexing:
        sequence_1[col-1] and sequence_2[row-1] because the grid has an
        extra row and column for the border (representing empty prefixes).

    Args:
        score_matrix:      The initialised 2D scoring grid.
        traceback_matrix:  The initialised 2D direction grid.
        sequence_1:        First input sequence (runs along columns).
        sequence_2:        Second input sequence (runs along rows).
        gap_penalty:       Score for each gap (default -2).
        match:             Score for a matching character pair (default 1).
        mismatch:          Penalty for a mismatching pair (default -1).

    Returns:
        A tuple of (filled score_matrix, filled traceback_matrix).

    Examples:
        >>> sm = initialize_score_matrix(3, 4, gap_penalty=-2)
        >>> tm = initialize_traceback_matrix(3, 4)
        >>> sm, tm = fill_score_matrix(sm, tm, 'ACG', 'AC', gap_penalty=-2)
        >>> sm[2][3]
        0
    """
    total_rows = len(score_matrix)  # = len(sequence_2) + 1
    total_cols = len(score_matrix[0])  # = len(sequence_1) + 1

    # Iterate over every interior cell (skip row 0 and col 0, already filled)
    for row in range(1, total_rows):
        for col in range(1, total_cols):
            # - Identify which characters we are comparing -
            # Subtract 1 because row 0 / col 0 are the "empty prefix" border.
            char_from_seq2 = sequence_2[row - 1]  # character on the left axis
            char_from_seq1 = sequence_1[col - 1]  # character on the top axis

            # - Compute score for each of the three possible moves -

            # Option A : DIAGONAL: pair the two characters (match or mismatch)
            substitution_score = get_match_score(
                char_from_seq1, char_from_seq2, match=match, mismatch=mismatch
            )
            diagonal_score = score_matrix[row - 1][col - 1] + substitution_score

            # Option B : UP: place a gap in sequence_1 (seq2 char is unmatched)
            up_score = score_matrix[row - 1][col] + gap_penalty

            # Option C : LEFT: place a gap in sequence_2 (seq1 char is unmatched)
            left_score = score_matrix[row][col - 1] + gap_penalty

            # - Choose the best (maximum) score -
            best_score = max(diagonal_score, up_score, left_score)
            score_matrix[row][col] = best_score

            # - Record which direction produced the best score -
            # Priority order when tied: Diagonal > Up > Left
            # (tie-breaking affects which of equally-optimal paths is returned)
            if best_score == diagonal_score:
                traceback_matrix[row][col] = "D"
            elif best_score == up_score:
                traceback_matrix[row][col] = "U"
            else:
                traceback_matrix[row][col] = "L"

    return score_matrix, traceback_matrix


# SECTION 4 : PHASE 3: TRACEBACK


def traceback_alignment(
    traceback_matrix: list,
    sequence_1: str,
    sequence_2: str,
) -> tuple:
    """Walk back through the direction grid to reconstruct the aligned sequences.

    How traceback works
    -
    We start at the BOTTOM-RIGHT cell (the final alignment score) and
    follow the arrows recorded in traceback_matrix until we reach the
    top-left origin cell ('X').

    At each step:
        'D' (Diagonal) -> both sequences contribute a character.
                          prepend seq1[col-1] and seq2[row-1]
        'U' (Up)        -> seq2 contributes a character; seq1 gets a gap '-'.
                          prepend '-'         and seq2[row-1]
        'L' (Left)      -> seq1 contributes a character; seq2 gets a gap '-'.
                          prepend seq1[col-1] and '-'

    Because we build the aligned strings in reverse (bottom-right -> top-left),
    we collect characters in lists and reverse at the end.

    Args:
        traceback_matrix:  Filled direction grid from fill_score_matrix.
        sequence_1:        Original first sequence.
        sequence_2:        Original second sequence.

    Returns:
        A tuple (aligned_seq1, aligned_seq2) as strings with '-' for gaps.

    Examples:
        >>> sm = initialize_score_matrix(4, 4, gap_penalty=-2)
        >>> tm = initialize_traceback_matrix(4, 4)
        >>> sm, tm = fill_score_matrix(sm, tm, 'ACG', 'ACT', gap_penalty=-2)
        >>> a1, a2 = traceback_alignment(tm, 'ACG', 'ACT')
        >>> a1
        'ACG'
        >>> a2
        'ACT'
    """
    # Build the alignment character by character (in reverse, then flip)
    aligned_seq1_reversed = []
    aligned_seq2_reversed = []

    #  Start at the bottom-right corner of the grid
    current_row = len(traceback_matrix) - 1  # last row index
    current_col = len(traceback_matrix[0]) - 1  # last column index

    #  Follow arrows until we reach the origin cell 'X'
    while traceback_matrix[current_row][current_col] != "X":
        current_direction = traceback_matrix[current_row][current_col]

        if current_direction == "D":
            # Diagonal: pair the characters and move diagonally up-left
            aligned_seq1_reversed.append(sequence_1[current_col - 1])
            aligned_seq2_reversed.append(sequence_2[current_row - 1])
            current_row -= 1
            current_col -= 1

        elif current_direction == "U":
            # Up: seq2 has a character; seq1 gets a gap; move straight up
            aligned_seq1_reversed.append("-")  # gap in seq1
            aligned_seq2_reversed.append(sequence_2[current_row - 1])
            current_row -= 1

        elif current_direction == "L":
            # Left: seq1 has a character; seq2 gets a gap; move straight left
            aligned_seq1_reversed.append(sequence_1[current_col - 1])
            aligned_seq2_reversed.append("-")  # gap in seq2
            current_col -= 1

    #  Reverse both lists to get the correct left->right order
    aligned_seq1 = "".join(reversed(aligned_seq1_reversed))
    aligned_seq2 = "".join(reversed(aligned_seq2_reversed))

    return aligned_seq1, aligned_seq2


# SECTION 5 : PUBLIC INTERFACE


def needleman_wunsch(
    sequence_1: str,
    sequence_2: str,
    gap_penalty: int = -2,
    match: int = 1,
    mismatch: int = -1,
) -> tuple:
    """Run the full Needleman-Wunsch global alignment on two sequences.

    This orchestrator calls the three phases in order:
        1. initialize_score_matrix / initialize_traceback_matrix
        2. fill_score_matrix
        3. traceback_alignment

    and returns the two aligned strings plus the optimal alignment score.

    Args:
        sequence_1:   First sequence  (e.g. 'GATTACA').
        sequence_2:   Second sequence (e.g. 'GCATGCU').
        gap_penalty:  Score per gap character (default -2).
        match:        Score for identical aligned residues (default +1).
        mismatch:     Penalty for differing aligned residues (default -1).

    Returns:
        A tuple (aligned_seq1, aligned_seq2, optimal_score).

    Examples:
        >>> a1, a2, score = needleman_wunsch('GATTACA', 'GCATGCU')
        >>> score
        -1
        >>> len(a1) == len(a2)
        True
        >>> a1.replace('-', '') == 'GATTACA'
        True
        >>> a2.replace('-', '') == 'GCATGCU'
        True

        >>> a1, a2, score = needleman_wunsch('AAA', 'AAA')
        >>> score
        3
        >>> a1
        'AAA'
        >>> a2
        'AAA'

        >>> _, _, score = needleman_wunsch('A', 'T')
        >>> score
        -1
    """
    #  Determine grid dimensions
    # We need one extra row/column for the "empty prefix" border.
    number_of_rows = len(sequence_2) + 1
    number_of_cols = len(sequence_1) + 1

    #  Phase 1: Initialization
    score_matrix = initialize_score_matrix(
        number_of_rows, number_of_cols, gap_penalty=gap_penalty
    )
    traceback_matrix = initialize_traceback_matrix(number_of_rows, number_of_cols)

    #  Phase 2: Matrix Filling
    score_matrix, traceback_matrix = fill_score_matrix(
        score_matrix,
        traceback_matrix,
        sequence_1,
        sequence_2,
        gap_penalty=gap_penalty,
        match=match,
        mismatch=mismatch,
    )

    #  Read the optimal alignment score from the bottom-right cell
    optimal_score = score_matrix[number_of_rows - 1][number_of_cols - 1]

    #  Phase 3: Traceback
    aligned_seq1, aligned_seq2 = traceback_alignment(
        traceback_matrix, sequence_1, sequence_2
    )

    return aligned_seq1, aligned_seq2, optimal_score


# SECTION 6 : PRETTY PRINTERS


def format_alignment(aligned_seq1: str, aligned_seq2: str) -> str:
    """Produce a classic three-line alignment display.

    The middle line uses:
        '|'  -> identical characters (match)
        '.'  -> different characters (mismatch)
        ' '  -> at least one side is a gap

    Args:
        aligned_seq1:  First aligned sequence (may contain '-').
        aligned_seq2:  Second aligned sequence (may contain '-').

    Returns:
        A formatted multi-line string ready for printing.

    Examples:
        >>> print(format_alignment('AC-G', 'ACTG'))
        AC-G
        || |
        ACTG
    """
    annotation_chars = []

    for char_a, char_b in zip(aligned_seq1, aligned_seq2):
        if char_a == "-" or char_b == "-":
            annotation_chars.append(" ")  # gap : no match possible
        elif char_a == char_b:
            annotation_chars.append("|")  # identical
        else:
            annotation_chars.append(".")  # mismatch

    annotation_line = "".join(annotation_chars)
    return f"{aligned_seq1}\n{annotation_line}\n{aligned_seq2}"


def print_score_matrix(score_matrix: list, sequence_1: str, sequence_2: str) -> None:
    """Print the filled scoring matrix in a readable table format.

    Useful for understanding (or teaching) what the DP grid looks like.

    Args:
        score_matrix:  The 2D scoring grid after fill_score_matrix.
        sequence_1:    The first sequence (column headers).
        sequence_2:    The second sequence (row labels).

    Examples:
        >>> sm = initialize_score_matrix(3, 4, -2)
        >>> tm = initialize_traceback_matrix(3, 4)
        >>> sm, _ = fill_score_matrix(sm, tm, 'ACG', 'AC')
        >>> print_score_matrix(sm, 'ACG', 'AC')
            -   A   C   G
           -   0  -2  -4  -6
           A  -2   1  -1  -3
           C  -4  -1   2   0
    """
    col_width = 4

    # Header row: blank corner + sequence_1 characters
    header_labels = ["  -"] + [f"{c:>{col_width}}" for c in sequence_1]
    print("  " + "".join(header_labels))

    # One data row per border label + each character of sequence_2
    row_labels = ["-", *list(sequence_2)]

    for row_index, row_label in enumerate(row_labels):
        row_cells = [f"{cell:>{col_width}}" for cell in score_matrix[row_index]]
        print(f"  {row_label:>2}" + "".join(row_cells))


# SECTION 7 : DEMO


if __name__ == "__main__":
    import doctest

    #  Run all embedded doctests
    print("=" * 60)
    print("Running doctests ...")
    results = doctest.testmod(verbose=False)
    if results.failed == 0:
        print(f"All {results.attempted} doctests passed.\n")
    else:
        print(f"{results.failed} doctest(s) FAILED.\n")

    #  Classic Needleman & Wunsch (1970) example
    print("=" * 60)
    print("Example 1 : Classic NW paper sequences")
    print("  seq1 = GATTACA")
    print("  seq2 = GCATGCU")
    print("-" * 60)

    seq1 = "GATTACA"
    seq2 = "GCATGCU"

    al1, al2, opt_score = needleman_wunsch(seq1, seq2)

    # Rebuild the score matrix for display
    sm = initialize_score_matrix(len(seq2) + 1, len(seq1) + 1)
    tm = initialize_traceback_matrix(len(seq2) + 1, len(seq1) + 1)
    sm, _ = fill_score_matrix(sm, tm, seq1, seq2)

    print("Score Matrix:")
    print_score_matrix(sm, seq1, seq2)
    print(f"\nOptimal alignment score: {opt_score}")
    print("\nAlignment:")
    print(format_alignment(al1, al2))

    #  Second example: identical sequences
    print("\n" + "=" * 60)
    print("Example 2 : Identical sequences (perfect match)")
    print("  seq1 = seq2 = ACGT")
    al1, al2, opt_score = needleman_wunsch("ACGT", "ACGT")
    print(f"Optimal score: {opt_score}")
    print(format_alignment(al1, al2))

    #  Third example: sequences requiring a gap
    print("\n" + "=" * 60)
    print("Example 3 : Gap required")
    print("  seq1 = AGCT")
    print("  seq2 = AGT")
    al1, al2, opt_score = needleman_wunsch("AGCT", "AGT")
    print(f"Optimal score: {opt_score}")
    print(format_alignment(al1, al2))
