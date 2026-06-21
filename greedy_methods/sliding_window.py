def sliding_window(input_string: str) -> int:
    """
    This function takes a string and returns the length of the longest substring
    without repeating characters using the sliding window algorithm.

    It runs in O(n) time, where n is the length of the string. The sliding window
    approach ensures that each character is processed at most twice.

    Args:
        input_string: A string input.

    Returns:
        int: Length of the longest substring without repeating characters.

    Raises:
        TypeError: If the input is not a string.

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
    >>> sliding_window("a"*10000)
    1
    """
    # Error handling for non-string inputs
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")

    # Handle empty string case immediately
    if len(input_string) == 0:
        return 0

    # Dictionary to store the most recent index of each character
    char_index_map: dict[str, int] = {}

    # Initialize the sliding window pointers
    left: int = 0
    max_len: int = 0
    # Traverse the string with a right pointer
    for right, char in enumerate(input_string):
        if char in char_index_map and char_index_map[char] >= left:
            # Move the left pointer to avoid repeating characters
            left = char_index_map[char] + 1
        # Update the latest index of the character
        char_index_map[char] = right
        # Calculate the current length of the window
        current_len = right - left + 1
        max_len = max(max_len, current_len)
    return max_len


if __name__ == "__main__":
    import doctest

    doctest.testmod()
