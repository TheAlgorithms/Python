"""
Given a string and a positive number k, find the longest substring of the string containing k distinct characters.
If k is more than the total number of distinct characters in the string, return the whole string.
//https://medium.com/techie-delight/top-problems-on-sliding-window-technique-8e63f1e2b1fa
"""


def find_longest_substring(input_str: str, max_distinct: int) -> str:
    """
    Find the longest substring of a given string containing at most k distinct characters.

    Args:
        input_str (str): The input string to search in.
        max_distinct (int): The maximum number of distinct characters allowed in the substring.

    Returns:
        str: The longest substring containing at most k distinct characters.

    Example:
        >>> find_longest_substring("abcbdbdbbdcdabd", 2)
        'bdbdbbd'
    """
    if input_str is None or len(input_str) == 0:
        return input_str

    start, end = 0, 0
    distinct_chars = set()
    char_frequency = [0] * 128

    for left in range(len(input_str)):
        for right in range(len(input_str)):
            distinct_chars.add(input_str[right])
            char_frequency[ord(input_str[right])] += 1

            while len(distinct_chars) > max_distinct:
                if char_frequency[ord(input_str[left])] == 1:
                    distinct_chars.remove(input_str[left])
                char_frequency[ord(input_str[left])] -= 1
                left += 1

            if end - start < right - left:
                end = right
                start = left

    return input_str[start : end + 1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
