"""
Bitap exact string matching
https://en.wikipedia.org/wiki/Bitap_algorithm

Searches for a pattern inside text, and returns the index of the first occurrence
of the pattern. Both text and pattern consist of lowercase alphabetical characters only.

Complexity: O(m*n)
    n = length of text
    m = length of pattern

Python doctests can be run using this command:
python3 -m doctest -v bitap_string_match.py
"""


def bitap_string_match(text: str, pattern: str) -> int:
    """
    Retrieves the index of the first occurrence of pattern in text.

    Args:
        text: A string consisting only of lowercase alphabetical characters.
        pattern: A string consisting only of lowercase alphabetical characters.

    Returns:
        int: The index where pattern first occurs. Return -1  if not found.

    >>> bitap_string_match('abdabababc', 'ababc')
    5
    >>> bitap_string_match('aaaaaaaaaaaaaaaaaa', 'a')
    0
    >>> bitap_string_match('zxywsijdfosdfnso', 'zxywsijdfosdfnso')
    0
    >>> bitap_string_match('abdabababc', '')
    0
    >>> bitap_string_match('abdabababc', 'c')
    9
    >>> bitap_string_match('abdabababc', 'fofosdfo')
    -1
    >>> bitap_string_match('abdab', 'fofosdfo')
    -1
    """
    if not pattern:
        return 0
    m = len(pattern)
    if m > len(text):
        return -1

    # Initial state of bit string 1110
    state = ~1
    # Bit = 0 if character appears at index, and 1 otherwise
    pattern_mask: list[int] = [~0] * 27  # 1111

    for i, char in enumerate(pattern):
        # For the pattern mask for this character, set the bit to 0 for each i
        # the character appears.
        pattern_index: int = ord(char) - ord("a")
        pattern_mask[pattern_index] &= ~(1 << i)

    for i, char in enumerate(text):
        text_index = ord(char) - ord("a")
        # If this character does not appear in pattern, it's pattern mask is 1111.
        # Performing a bitwise OR between state and 1111 will reset the state to 1111
        # and start searching the start of pattern again.
        state |= pattern_mask[text_index]
        state <<= 1

        # If the mth bit (counting right to left) of the state is 0, then we have
        # found pattern in text
        if (state & (1 << m)) == 0:
            return i - m + 1

    return -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
