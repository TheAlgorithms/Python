def length_of_longest_substring_two_distinct(string: str) -> int:
    """
    Finds the length of the longest substring with at most two distinct characters.[https://www.geeksforgeeks.org/window-sliding-technique/]


    Args:
    s (str): The input string.

    Returns:
    int: The length of the longest substring with at most two distinct characters.

    Examples:
    >>> length_of_longest_substring_two_distinct("eceba")
    3
    >>> length_of_longest_substring_two_distinct("ccaabbb")
    5
    >>> length_of_longest_substring_two_distinct("abcabcabc")
    2
    >>> length_of_longest_substring_two_distinct("")
    0
    """
    n = len(s)
    if n == 0:
        return 0

    # Dictionary to store the last occurrence of each character
    char_map = {}
    left = 0
    max_length = 0

    # Sliding window approach
    for right in range(n):
        char_map[s[right]] = right

        # If we have more than two distinct characters
        if len(char_map) > 2:
            # Remove the leftmost character
            del_idx = min(char_map.values())
            del char_map[s[del_idx]]
            left = del_idx + 1

        max_length = max(max_length, right - left + 1)

    return max_length


if __name__ == "__main__":
    import doctest

    doctest.testmod()
