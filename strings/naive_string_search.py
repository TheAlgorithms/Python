"""
https://en.wikipedia.org/wiki/String-searching_algorithm#Na%C3%AFve_string_search

this algorithm tries to find the pattern from every position of
the mainString if pattern is found from position i it add it to
the answer and does the same for position i+1

Complexity : O(n*m)
    n=length of main string
    m=length of pattern string
"""


def naive_pattern_search(main_string: str, pattern: str) -> list:
    """
    >>> naive_pattern_search("ABAAABCDBBABCDDEBCABC", "ABC")
    [4, 10, 18]

    >>> naive_pattern_search("", "ABC")
    []

    >>> naive_pattern_search("TEST", "TEST")
    [0]

    >>> naive_pattern_search("ABCDEGFTEST", "TEST")
    [7]
    """
    pat_len, str_len = len(pattern), len(main_string)
    positions = []
    for i in range(str_len - pat_len + 1):
        found = True
        for j in range(pat_len):
            if main_string[i + j] != pattern[j]:
                found = False
                break

        if found:
            positions.append(i)

    return positions


if __name__ == "__main__":
    assert naive_pattern_search("ABCDEFG", "DE") == [3]
