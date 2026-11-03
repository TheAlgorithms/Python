"""
https://en.wikipedia.org/wiki/Suffix_array
https://cp-algorithms.com/string/suffix-array.html

A suffix array lists the starting positions of every suffix of a string in
lexicographic order. It needs one integer per suffix, where a suffix tree
needs a node per character, so it is the compact structure used for pattern
search and for the LCP-based algorithms built on top of it.

Construction here uses prefix doubling (Manber-Myers).

Time Complexity: O(n log² n) - where n is the length of the text
Space Complexity: O(n)
"""


def suffix_array(text: str) -> list[int]:
    """
    Return the starting indices of all suffixes of `text`, in lexicographic
    order.

    >>> suffix_array("banana")
    [5, 3, 1, 0, 4, 2]
    >>> suffix_array("mississippi")
    [10, 7, 4, 1, 0, 9, 8, 6, 3, 5, 2]
    >>> suffix_array("abababab")
    [6, 4, 2, 0, 7, 5, 3, 1]
    >>> suffix_array("aaaa")
    [3, 2, 1, 0]
    >>> suffix_array("aça")
    [2, 0, 1]
    >>> suffix_array("a")
    [0]
    >>> suffix_array("")
    []
    """
    n = len(text)
    if n == 0:
        return []

    suffixes = list(range(n))
    # Ranking by code point is enough to start: Python orders strings by code
    # point too, so one comparison of the first character is already right.
    rank = list(map(ord, text))
    k = 1

    while k < n:
        # Sort by the first 2k characters of each suffix, which are exactly the
        # pair (rank of the first k, rank of the next k). A second half that
        # runs past the end gets -1: ranks are never negative, so a shorter
        # suffix sorts before a longer one that shares its prefix.
        keys = [(rank[i], rank[i + k] if i + k < n else -1, i) for i in range(n)]
        keys.sort()
        suffixes = [i for _, _, i in keys]

        # Renumber so that equal 2k-prefixes share a rank and every distinct
        # prefix gets the next one. This keeps ranks dense in range(n).
        new_rank = [0] * n
        for position in range(1, n):
            previous, current = suffixes[position - 1], suffixes[position]
            previous_key = (
                rank[previous],
                rank[previous + k] if previous + k < n else -1,
            )
            current_key = (
                rank[current],
                rank[current + k] if current + k < n else -1,
            )
            new_rank[current] = new_rank[previous] + int(previous_key != current_key)

        rank = new_rank
        # Dense ranks ending at n - 1 means every suffix has a unique rank, so
        # the 2k-prefixes already order them completely; doubling cannot change
        # the order, and the next round always breaks too, since 2k >= n.
        if rank[suffixes[-1]] == n - 1:
            break
        k *= 2

    return suffixes
