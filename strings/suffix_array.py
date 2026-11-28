"""
Suffix array and longest common prefix (LCP) array.

The suffix array of a string is the list of the starting indices of all of its
suffixes, sorted in lexicographical order. Together with the LCP array it answers
many substring questions (pattern search, longest repeated substring, number of
distinct substrings) without the memory cost of a suffix tree.

- Suffix array: prefix doubling, O(n * log^2 n) time, O(n) space
- LCP array: Kasai's algorithm, O(n) time, O(n) space

https://en.wikipedia.org/wiki/Suffix_array
https://en.wikipedia.org/wiki/LCP_array
https://cp-algorithms.com/string/suffix-array.html
"""

from functools import partial


def rank_pair(ranks: list[int], index: int, half: int) -> tuple[int, int]:
    """
    Return the sort key of the suffix starting at ``index`` for one round of
    prefix doubling: the rank of its first ``half`` characters and the rank of
    the next ``half`` characters.

    A suffix shorter than ``half`` has an empty second half, ranked -1 so that it
    sorts before every non-empty one.

    >>> rank_pair([1, 0, 2, 0, 2, 0], 0, 1)
    (1, 0)
    >>> rank_pair([1, 0, 2, 0, 2, 0], 5, 1)
    (0, -1)
    >>> rank_pair([3, 2, 1, 0], 2, 2)
    (1, -1)
    """
    second_half = index + half
    if second_half >= len(ranks):
        return ranks[index], -1
    return ranks[index], ranks[second_half]


def build_suffix_array(text: str) -> list[int]:
    """
    Return the starting indices of the suffixes of ``text`` in sorted order.

    Suffixes are first ranked by their first character. Each round then sorts them
    by their first ``2 * length`` characters, using the pair of ranks of the two
    halves as the key, so only O(log n) rounds are needed.

    >>> build_suffix_array("banana")
    [5, 3, 1, 0, 4, 2]
    >>> build_suffix_array("abracadabra")
    [10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2]
    >>> build_suffix_array("aaaa")
    [3, 2, 1, 0]
    >>> build_suffix_array("a")
    [0]
    >>> build_suffix_array("")
    []
    >>> text = "mississippi"
    >>> build_suffix_array(text) == sorted(range(len(text)), key=lambda i: text[i:])
    True
    >>> build_suffix_array(123)
    Traceback (most recent call last):
        ...
    TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text_length = len(text)
    suffix_array = list(range(text_length))
    ranks = [ord(character) for character in text]
    length = 1

    while length < text_length:
        suffix_array.sort(key=partial(rank_pair, ranks, half=length))

        new_ranks = [0] * text_length
        for position in range(1, text_length):
            current, previous = suffix_array[position], suffix_array[position - 1]
            new_ranks[current] = new_ranks[previous] + (
                rank_pair(ranks, current, length) != rank_pair(ranks, previous, length)
            )
        ranks = new_ranks

        # Every suffix already has a distinct rank, so the order is final
        if ranks[suffix_array[-1]] == text_length - 1:
            break
        length *= 2

    return suffix_array


def build_lcp_array(text: str, suffix_array: list[int] | None = None) -> list[int]:
    """
    Return the LCP array of ``text`` using Kasai's algorithm.

    ``lcp[i]`` is the length of the longest common prefix of the suffixes starting
    at ``suffix_array[i - 1]`` and ``suffix_array[i]``; ``lcp[0]`` is always 0.

    Suffixes are visited in text order. Dropping the first character of a suffix
    shortens its common prefix with its sorted neighbour by at most one, so the
    comparison never has to restart from scratch.

    >>> build_lcp_array("banana")
    [0, 1, 3, 0, 0, 2]
    >>> build_lcp_array("abracadabra")
    [0, 1, 4, 1, 1, 0, 3, 0, 0, 0, 2]
    >>> build_lcp_array("aaaa")
    [0, 1, 2, 3]
    >>> build_lcp_array("abc", [0, 1, 2])
    [0, 0, 0]
    >>> build_lcp_array("")
    []
    >>> build_lcp_array("abc", [0, 1])
    Traceback (most recent call last):
        ...
    ValueError: suffix_array must have one entry per character of text
    """
    if suffix_array is None:
        suffix_array = build_suffix_array(text)
    text_length = len(text)
    if len(suffix_array) != text_length:
        raise ValueError("suffix_array must have one entry per character of text")

    rank_of_suffix = [0] * text_length
    for rank, suffix_start in enumerate(suffix_array):
        rank_of_suffix[suffix_start] = rank

    lcp_array = [0] * text_length
    common_length = 0
    for suffix_start in range(text_length):
        rank = rank_of_suffix[suffix_start]
        if rank == 0:
            common_length = 0
            continue
        neighbour_start = suffix_array[rank - 1]
        while (
            suffix_start + common_length < text_length
            and neighbour_start + common_length < text_length
            and text[suffix_start + common_length]
            == text[neighbour_start + common_length]
        ):
            common_length += 1
        lcp_array[rank] = common_length
        if common_length:
            common_length -= 1

    return lcp_array


def find_pattern(
    text: str, pattern: str, suffix_array: list[int] | None = None
) -> list[int]:
    """
    Return the sorted starting indices of every occurrence of ``pattern`` in
    ``text``.

    All suffixes that start with ``pattern`` are contiguous in the suffix array, so
    two binary searches find the block in O(m * log n) time, where m is the pattern
    length.

    >>> find_pattern("banana", "ana")
    [1, 3]
    >>> find_pattern("banana", "a")
    [1, 3, 5]
    >>> find_pattern("banana", "banana")
    [0]
    >>> find_pattern("banana", "nab")
    []
    >>> find_pattern("banana", "bananas")
    []
    >>> find_pattern("abc", "")
    [0, 1, 2]
    >>> find_pattern("", "a")
    []
    """
    if suffix_array is None:
        suffix_array = build_suffix_array(text)
    block_start = first_suffix_position(
        text, suffix_array, pattern, strictly_greater=False
    )
    block_end = first_suffix_position(
        text, suffix_array, pattern, strictly_greater=True
    )
    return sorted(suffix_array[block_start:block_end])


def first_suffix_position(
    text: str, suffix_array: list[int], pattern: str, *, strictly_greater: bool
) -> int:
    """
    Binary search the suffix array for the first position whose suffix, cut to
    the pattern length, is >= ``pattern`` (or > ``pattern`` when
    ``strictly_greater`` is True).

    >>> suffix_array = build_suffix_array("banana")
    >>> suffix_array
    [5, 3, 1, 0, 4, 2]
    >>> first_suffix_position("banana", suffix_array, "ana", strictly_greater=False)
    1
    >>> first_suffix_position("banana", suffix_array, "ana", strictly_greater=True)
    3
    >>> first_suffix_position("banana", suffix_array, "z", strictly_greater=False)
    6
    >>> first_suffix_position("", [], "a", strictly_greater=False)
    0
    """
    pattern_length = len(pattern)
    low, high = 0, len(suffix_array)
    while low < high:
        middle = (low + high) // 2
        start = suffix_array[middle]
        prefix = text[start : start + pattern_length]
        if prefix < pattern or (strictly_greater and prefix == pattern):
            low = middle + 1
        else:
            high = middle
    return low


def longest_repeated_substring(text: str) -> str:
    """
    Return the longest substring that occurs at least twice in ``text``
    (occurrences may overlap). Ties are resolved in favour of the
    lexicographically smallest substring.

    The answer is the longest common prefix of two neighbouring suffixes in sorted
    order, i.e. the maximum of the LCP array.

    >>> longest_repeated_substring("banana")
    'ana'
    >>> longest_repeated_substring("abracadabra")
    'abra'
    >>> longest_repeated_substring("aaaa")
    'aaa'
    >>> longest_repeated_substring("abcd")
    ''
    >>> longest_repeated_substring("")
    ''
    """
    suffix_array = build_suffix_array(text)
    lcp_array = build_lcp_array(text, suffix_array)
    if not lcp_array:
        return ""
    best_position = max(range(len(lcp_array)), key=lcp_array.__getitem__)
    start = suffix_array[best_position]
    return text[start : start + lcp_array[best_position]]


def count_distinct_substrings(text: str) -> int:
    """
    Return the number of distinct non-empty substrings of ``text``.

    Every suffix contributes one new substring per prefix, except for the prefixes
    it shares with the previous suffix in sorted order.

    >>> count_distinct_substrings("banana")
    15
    >>> count_distinct_substrings("aaaa")
    4
    >>> count_distinct_substrings("abc")
    6
    >>> count_distinct_substrings("")
    0
    >>> text = "mississippi"
    >>> count_distinct_substrings(text) == len(
    ...     {text[i:j] for i in range(len(text)) for j in range(i + 1, len(text) + 1)}
    ... )
    True
    """
    text_length = len(text)
    total_substrings = text_length * (text_length + 1) // 2
    return total_substrings - sum(build_lcp_array(text))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
