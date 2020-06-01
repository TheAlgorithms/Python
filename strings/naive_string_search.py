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
    patLen = len(pattern)
    strLen = len(main_string)
    position = []
    for i in range(strLen - patLen + 1):
        match_found = True
        for j in range(patLen):
            if main_string[i + j] != pattern[j]:
                match_found = False
                break
        if match_found:
            position.append(i)
    return position


if __name__ == "__main__":
    assert naive_pattern_search("ABCDEFG", "DE") == [3]
