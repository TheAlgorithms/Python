def sliding_window(input_string: str) -> int:
    """
    This function takes a string and returns the length of the longest substring
    without repeating characters using the sliding window algorithm.

    Args:
        input_string: A string input.

    Returns:
        max_len: Length of the longest substring without repeating characters.

    Examples:
    >>> sliding_window("abcabcbb")
    3
    >>> sliding_window("bbbbb")
    1
    >>> sliding_window("pwwkew")
    3
    >>> sliding_window("")
    0
    >>> sliding_window("abcdefg")
    7
    >>> sliding_window("abccba")
    3
    """
    char_index_map: dict[str, int] = {}
    left = 0
    max_len = 0

    # Traverse the string with a right pointer
    for right, char in enumerate(input_string):
        if char in char_index_map and char_index_map[char] >= left:
            # Move the left pointer to avoid repeating characters
            left = char_index_map[char] + 1
        # Update the latest index of the character
        char_index_map[char] = right
        # Calculate the current length of the window
        max_len = max(max_len, right - left + 1)
    return max_len


if __name__ == "__main__":
    import doctest

    doctest.testmod()
