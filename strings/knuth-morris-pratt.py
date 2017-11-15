def kmp(pattern, text, len_p=None, len_t=None):
    """
    The Knuth-Morris-Pratt Algorithm for finding a pattern within a piece of text
    with complexity O(n + m)

    1) Preprocess pattern to identify any suffixes that are identical to prefixes

        This tells us where to continue from if we get a mismatch between a character in our pattern
        and the text.

    2) Step through the text one character at a time and compare it to a character in the pattern
        updating our location within the pattern if necessary

    """

    # 1) Construct the failure array
    failure = [0]
    i = 0
    for index, char in enumerate(pattern[1:]):
        if pattern[i] == char:
            i += 1
        else:
            i = 0
        failure.append(i)

    # 2) Step through text searching for pattern
    i, j = 0, 0  # index into text, pattern
    while i < len(text):
        if pattern[j] == text[i]:
            if j == (len(pattern) - 1):
                return True
            i += 1
            j += 1

        # if this is a prefix in our pattern
        # just go back far enough to continue
        elif failure[j] > 0:
            j = failure[j] - 1
        else:
            i += 1
    return False


if __name__ == '__main__':

    # Test 1)
    pattern = "abc1abc12"
    text1 = "alskfjaldsabc1abc1abc12k23adsfabcabc"
    text2 = "alskfjaldsk23adsfabcabc"
    assert kmp(pattern, text1) and not kmp(pattern, text2)

    # Test 2)
    pattern = "ABABX"
    text = "ABABZABABYABABX"
    assert kmp(pattern, text)


