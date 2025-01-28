# https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm


def knuth_morris_pratt(text: str, pattern: str) -> list[int]:
    """
    Knuth-Morris-Pratt (KMP) string search algorithm in Python.

    :param text: The text in which to search for the pattern.
    :param pattern: The pattern to search for in the text.
    :return: A list of starting positions where the pattern is found in the text.

    Examples:
    >>> knuth_morris_pratt("ABABDABACDABABCABAB", "ABABCABAB")
    [10]
    >>> knuth_morris_pratt("ABCABCABCABCABC", "ABC")
    [0, 3, 6, 9, 12]
    >>> knuth_morris_pratt("AAAAAA", "AA")
    [0, 1, 2, 3, 4]
    >>> knuth_morris_pratt("ABCDEF", "XYZ")
    []

    """

    def build_prefix_table(pattern: str) -> list[int]:
        """
        Build the prefix table for the given pattern.

        :param pattern: The pattern for which to build the prefix table.
        :return: The prefix table, which is a list of integers.

        Examples:
        >>> build_prefix_table("ABABCA")
        [0, 0, 1, 2, 3, 0]
        >>> build_prefix_table("ABCABC")
        [0, 0, 0, 1, 2, 3]
        >>> build_prefix_table("AAAAAA")
        [0, 1, 2, 3, 4, 5]
        >>> build_prefix_table("XYZ")
        [0, 0, 0]

        """
        prefix_table = [0] * len(pattern)
        j = 0
        for i in range(1, len(pattern)):
            while j > 0 and pattern[i] != pattern[j]:
                j = prefix_table[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
            prefix_table[i] = j
        return prefix_table

    prefix_table = build_prefix_table(pattern)
    positions = []
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = prefix_table[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            positions.append(i - j + 1)
            j = prefix_table[j - 1]
    return positions


if __name__ == "__main__":
    text = input("Enter the text: ")
    pattern = input("Enter the pattern to search for: ")
    positions = knuth_morris_pratt(text, pattern)
    if positions:
        print(f"Pattern found at positions: {positions}")
    else:
        print("Pattern not found in the text.")
