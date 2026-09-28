"""Find a longest common subsequence with Hirschberg's algorithm.

https://en.wikipedia.org/wiki/Hirschberg%27s_algorithm
"""


def _lcs_lengths(
    first: str, first_indices: range, second: str, second_indices: range
) -> list[int]:
    """Return LCS lengths for every prefix of the second sequence.

    >>> _lcs_lengths("ABC", range(3), "AC", range(2))
    [0, 1, 2]
    """
    previous = [0] * (len(second_indices) + 1)
    for first_index in first_indices:
        current = [0]
        for column, second_index in enumerate(second_indices, start=1):
            if first[first_index] == second[second_index]:
                current.append(previous[column - 1] + 1)
            else:
                current.append(max(current[-1], previous[column]))
        previous = current
    return previous


def _hirschberg(
    first: str,
    first_indices: range,
    second: str,
    second_indices: range,
    result: list[str],
) -> None:
    """Append a longest common subsequence of the indexed ranges to result.

    >>> result: list[str] = []
    >>> _hirschberg("ABC", range(3), "AC", range(2), result)
    >>> "".join(result)
    'AC'
    """
    if not first_indices or not second_indices:
        return
    if len(first_indices) == 1:
        character = first[first_indices[0]]
        if any(character == second[index] for index in second_indices):
            result.append(character)
        return
    if len(second_indices) == 1:
        character = second[second_indices[0]]
        if any(character == first[index] for index in first_indices):
            result.append(character)
        return

    midpoint = len(first_indices) // 2
    left_indices = first_indices[:midpoint]
    right_indices = first_indices[midpoint:]
    # Forward and backward rows score every place to split the second string.
    left_lengths = _lcs_lengths(first, left_indices, second, second_indices)
    right_lengths = _lcs_lengths(
        first, right_indices[::-1], second, second_indices[::-1]
    )

    split = 0
    best_length = -1
    for candidate_split in range(len(second_indices) + 1):
        candidate_length = (
            left_lengths[candidate_split]
            + right_lengths[len(second_indices) - candidate_split]
        )
        if candidate_length > best_length:
            best_length = candidate_length
            split = candidate_split
    del left_lengths, right_lengths

    _hirschberg(first, left_indices, second, second_indices[:split], result)
    _hirschberg(first, right_indices, second, second_indices[split:], result)


def hirschberg(first: str, second: str) -> str:
    """Return a longest common subsequence using linear-size DP rows.

    The result is not necessarily unique. Aside from the result, the algorithm
    uses O(min(m, n) + log(max(m, n))) space and O(mn) time.

    >>> hirschberg("ABCDEF", "ACE")
    'ACE'
    >>> hirschberg("AGGTAB", "GXTXAYB")
    'GTAB'
    >>> hirschberg("", "ABC")
    ''
    >>> hirschberg("ABC", "XYZ")
    ''
    >>> hirschberg(123, "ABC")
    Traceback (most recent call last):
    ...
    TypeError: both inputs must be strings
    """
    if not isinstance(first, str) or not isinstance(second, str):
        raise TypeError("both inputs must be strings")

    if len(first) < len(second):
        first, second = second, first

    result: list[str] = []
    _hirschberg(first, range(len(first)), second, range(len(second)), result)
    return "".join(result)
