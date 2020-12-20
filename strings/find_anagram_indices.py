from collections import Counter, defaultdict

def find_anagram_indices(word: string, string: string) -> Array:
    """
    Given a word `x`, and a string `y`, find all indices in `y` which are the starting locations of anagrams of `x`.
    For example, given `x` is `te` and `y` is `textet`, return `[0, 3, 4, 5]`.
    1. Brute force solution

    This algorithm would take O(w x s) time
    - x is the length of the word
    - y is the length of the input string

    :param word: word to be analyzed
    :param string: complete word to be scanned
    :return: Array

    >>> find_anagram_indices("te", "texetet")
    [0, 3, 4, 5]
    """
    output = []
    for i in range(len(string) - len(word) + 1):
        window = string[i:i + len(word)]
        if Counter(window) == Counter(word):
            output.append(i)
    return output

def find_anagram_indices_2(word: string, string: string) -> Array:
    """
    Given a word `x`, and a string `y`, find all indices in `y` which are the starting locations of anagrams of `x`.
    For example, given `x` is `te` and `y` is `textet`, return `[0, 3, 4, 5]`.

    2. Better scenario

    This algorithm would run in O(s) time and space.

    :param word: word to be analyzed
    :param string: complete word to be scanned
    :return: Array

    >>> print(find_anagram_indices_2("te", "texetet"))
    [0, 3, 4, 5]
    """

    output = []
    freq = defaultdict(int)

    for char in word:
        freq[char] += 1

    for char in string[:len(word)]:
        freq[char] -= 1
        if freq[char] == 0:
            del freq[char]

    if not freq:
        output.append(0)

    for i in range(len(word), len(string)):
        start_char, end_char = string[i - len(word)], string[i]
        freq[start_char] += 1
        if freq[start_char] == 0:
            del freq[start_char]

        freq[end_char] -= 1
        if freq[end_char] == 0:
            del freq[end_char]

        if not freq:
            beginning_index = i - len(word) + 1
            output.append(beginning_index)

    return output
