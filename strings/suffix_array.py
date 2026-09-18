"""
Suffix Array construction and Kasai's LCP (Longest Common Prefix) algorithm.

A suffix array of a string is a sorted array of the starting indices of all
its suffixes. It allows many string problems (substring search, longest
repeated substring, etc.) to be solved efficiently.

The construction below uses the prefix-doubling technique: suffixes are
sorted by their first character, then by their first 2, 4, 8, ... characters
until the order is fully determined. Each round doubles the known prefix
length, so O(log n) sorting rounds are needed.

Time Complexity: O(n log^2 n) where n is the length of the string
                 (O(log n) rounds, each sorting n items)
Space Complexity: O(n)

References:
- https://en.wikipedia.org/wiki/Suffix_array
- https://cp-algorithms.com/string/suffix-array.html
- https://en.wikipedia.org/wiki/LCP_array
"""


def build_suffix_array(text: str) -> list[int]:
    """
    Build the suffix array of `text` using the prefix-doubling algorithm.

    Returns a list `suffix_array` of length len(text) such that
    `text[suffix_array[i]:]` is the i-th lexicographically smallest suffix
    of `text`.

    >>> build_suffix_array("banana")
    [5, 3, 1, 0, 4, 2]
    >>> build_suffix_array("abracadabra")
    [10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2]
    >>> build_suffix_array("aaaa")
    [3, 2, 1, 0]
    >>> build_suffix_array("a")
    [0]
    >>> build_suffix_array("")
    Traceback (most recent call last):
        ...
    ValueError: Input string must not be empty.
    >>> build_suffix_array(123)
    Traceback (most recent call last):
        ...
    TypeError: Input must be a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    if not text:
        raise ValueError("Input string must not be empty.")

    length = len(text)
    suffix_array = list(range(length))
    # rank[i] is the equivalence class of the prefix starting at index i.
    rank = [ord(character) for character in text]

    step = 1
    while step < length:
        # Sort suffixes by the pair (rank[i], rank[i + step]), i.e. by their
        # first `2 * step` characters. A missing second half ranks lowest.
        suffix_array.sort(
            key=lambda index: (
                rank[index],
                rank[index + step] if index + step < length else -1,
            )
        )

        # Re-rank: suffixes that compared equal share the same class.
        new_rank = [0] * length
        for position in range(1, length):
            previous = suffix_array[position - 1]
            current = suffix_array[position]
            previous_key = (
                rank[previous],
                rank[previous + step] if previous + step < length else -1,
            )
            current_key = (
                rank[current],
                rank[current + step] if current + step < length else -1,
            )
            new_rank[current] = new_rank[previous] + (current_key > previous_key)

        rank = new_rank
        # Every suffix has a unique rank, so the order is fully determined.
        if rank[suffix_array[-1]] == length - 1:
            break
        step *= 2

    return suffix_array


def longest_common_prefix_array(text: str, suffix_array: list[int]) -> list[int]:
    """
    Build the LCP array of `text` for a given `suffix_array` using Kasai's
    algorithm, which runs in O(n) time.

    Returns a list `lcp` of length len(text) where `lcp[i]` is the length of
    the longest common prefix between the suffixes starting at
    `suffix_array[i - 1]` and `suffix_array[i]`. `lcp[0]` is always 0.

    >>> longest_common_prefix_array("banana", [5, 3, 1, 0, 4, 2])
    [0, 1, 3, 0, 0, 2]
    >>> longest_common_prefix_array("banana", build_suffix_array("banana"))
    [0, 1, 3, 0, 0, 2]
    >>> longest_common_prefix_array("aaaa", [3, 2, 1, 0])
    [0, 1, 2, 3]
    >>> longest_common_prefix_array("abcde", [0, 1, 2, 3, 4])
    [0, 0, 0, 0, 0]
    >>> longest_common_prefix_array("", [])
    Traceback (most recent call last):
        ...
    ValueError: Input string must not be empty.
    >>> longest_common_prefix_array("abc", [0, 1])
    Traceback (most recent call last):
        ...
    ValueError: suffix_array must be a permutation of range(len(text)).
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    length = len(text)
    if length == 0:
        raise ValueError("Input string must not be empty.")
    if sorted(suffix_array) != list(range(length)):
        raise ValueError("suffix_array must be a permutation of range(len(text)).")

    # rank[start] is the position in suffix_array of the suffix at `start`.
    rank = [0] * length
    for position, start in enumerate(suffix_array):
        rank[start] = position

    lcp = [0] * length
    common = 0
    for start in range(length):
        position = rank[start]
        if position == 0:
            # Lexicographically smallest suffix has no predecessor.
            common = 0
            continue
        neighbor = suffix_array[position - 1]
        while (
            start + common < length
            and neighbor + common < length
            and text[start + common] == text[neighbor + common]
        ):
            common += 1
        lcp[position] = common
        # The next suffix shares at least `common - 1` characters with its
        # own predecessor, so the comparison can resume from there.
        common = max(common - 1, 0)

    return lcp


if __name__ == "__main__":
    import doctest

    doctest.testmod()
