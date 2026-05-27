def min_window(search_str: str, target_letters: str) -> str:
    """
    Given a string to search, and another string of target char_dict,
    return the smallest substring of the search string that contains
    all target char_dict.

    This is somewhat modified from my solution to the problem
    "Minimum Window Substring" on leetcode.
    https://leetcode.com/problems/minimum-window-substring/description/

    >>> min_window("Hello World", "lWl")
    'llo W'
    >>> min_window("Hello World", "f")
    ''

    This solution uses a sliding window, alternating between shifting
    the end of the window right until all target char_dict are contained
    in the window, and shifting the start of the window right until the
    window no longer contains every target character.

    Time complexity: O(target_count + search_len) ->
        The algorithm checks a dictionary at most twice for each character
        in search_str.

    Space complexity: O(search_len) ->
        The primary contributor to additional space is the building of a
        dictionary using the search string.
    """

    target_count = len(target_letters)
    search_len = len(search_str)

    # Return if not possible due to string lengths.
    if search_len < target_count:
        return ""

    # Build dictionary with counts for each letter in target_letters
    char_dict = {}
    for ch in target_letters:
        if ch not in char_dict:
            char_dict[ch] = 1
        else:
            char_dict[ch] += 1

    # Initialize window
    window_start = 0
    window_end = 0

    exists = False
    min_window_len = search_len + 1

    # Start sliding window algorithm
    while window_end < search_len:
        # Slide window end right until all search characters are contained
        while target_count > 0 and window_end < search_len:
            cur = search_str[window_end]
            if cur in char_dict:
                char_dict[cur] -= 1
                if char_dict[cur] >= 0:
                    target_count -= 1
            window_end += 1
        temp = window_end - window_start

        # Check if window is the smallest found so far
        if target_count == 0 and temp < min_window_len:
            min_window = [window_start, window_end]
            exists = True
            min_window_len = temp

        # Slide window start right until a search character exits the window
        while target_count == 0 and window_start < window_end:
            cur = search_str[window_start]
            window_start += 1
            if cur in char_dict:
                char_dict[cur] += 1
                if char_dict[cur] > 0:
                    break
        temp = window_end - window_start + 1

        # Check if window is the smallest found so far
        if temp < min_window_len and target_count == 0:
            min_window = [window_start - 1, window_end]
            min_window_len = temp
        target_count = 1

    if exists:
        return search_str[min_window[0] : min_window[1]]
    else:
        return ""
