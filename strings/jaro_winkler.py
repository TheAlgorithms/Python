"""https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance"""


def jaro_winkler(str1: str, str2: str) -> float:
    """
    Jaro–Winkler distance is a string metric measuring an edit distance between two
    sequences.
    Output value is between 0.0 and 1.0.

    >>> jaro_winkler("martha", "marhta")
    0.9611111111111111
    >>> jaro_winkler("CRATE", "TRACE")
    0.7333333333333334
    >>> jaro_winkler("test", "dbdbdbdb")
    0.0
    >>> jaro_winkler("test", "test")
    1.0
    >>> jaro_winkler("hello world", "HeLLo W0rlD")
    0.6363636363636364
    >>> jaro_winkler("test", "")
    0.0
    >>> jaro_winkler("hello", "world")
    0.4666666666666666
    >>> jaro_winkler("hell**o", "*world")
    0.4365079365079365
    """

    def get_matched_characters(_str1: str, _str2: str) -> str:
        matched = []
        limit = min(len(_str1), len(_str2)) // 2
        for i, l in enumerate(_str1):
            left = int(max(0, i - limit))
            right = int(min(i + limit + 1, len(_str2)))
            if l in _str2[left:right]:
                matched.append(l)
                _str2 = f"{_str2[0:_str2.index(l)]} {_str2[_str2.index(l) + 1:]}"

        return "".join(matched)

    # matching characters
    matching_1 = get_matched_characters(str1, str2)
    matching_2 = get_matched_characters(str2, str1)
    match_count = len(matching_1)

    # transposition
    transpositions = (
        len([(c1, c2) for c1, c2 in zip(matching_1, matching_2) if c1 != c2]) // 2
    )

    if not match_count:
        jaro = 0.0
    else:
        jaro = (
            1
            / 3
            * (
                match_count / len(str1)
                + match_count / len(str2)
                + (match_count - transpositions) / match_count
            )
        )

    # common prefix up to 4 characters
    prefix_len = 0
    for c1, c2 in zip(str1[:4], str2[:4]):
        if c1 == c2:
            prefix_len += 1
        else:
            break

    return jaro + 0.1 * prefix_len * (1 - jaro)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(jaro_winkler("hello", "world"))
