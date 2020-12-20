from collections import Counter

def find_anagram_indices(word, string):
    """
    Given a word `x`, and a string `y`, find all indices in `y` which are the starting locations of anagrams of `x`.
    For example, given `x` is `te` and `y` is `textet`, return `[0, 3, 4, 5]`.
    1. Brute force solution

    This algorithm would take O(w x s) time
    - x is the length of the word
    - y is the length of the input string

    >>> find_anagram_indices("te", "texetet")
    [0, 3, 4, 5]
    """
    result = []
    for i in range(len(string) - len(word) + 1):
        window = string[i:i + len(word)]
        if Counter(window) == Counter(word):
            result.append(i)
    return result

from collections import defaultdict

def find_anagram_indices_2(word, s):
    """
    Given a word `x`, and a string `y`, find all indices in `y` which are the starting locations of anagrams of `x`.
    For example, given `x` is `te` and `y` is `textet`, return `[0, 3, 4, 5]`.

    2. Better scenario

    This algorithm would run in O(s) time and space.

    >>> print(find_anagram_indices_2("te", "texetet"))
    [0, 3, 4, 5]
    """

    result = []
    freq = defaultdict(int)

    for char in word:
        freq[char] += 1

    for char in s[:len(word)]:
        freq[char] -= 1
        if freq[char] == 0:
            del freq[char]

    if not freq:
        result.append(0)

    for i in range(len(word), len(s)):
        start_char, end_char = s[i - len(word)], s[i]
        freq[start_char] += 1
        if freq[start_char] == 0:
            del freq[start_char]

        freq[end_char] -= 1
        if freq[end_char] == 0:
            del freq[end_char]

        if not freq:
            beginning_index = i - len(word) + 1
            result.append(beginning_index)

    return result
