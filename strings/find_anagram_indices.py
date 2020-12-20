from collections import Counter, defaultdict

def find_anagram_indices(word: str, letters: str) -> list:
    """
    Given a word `word`, and a string `letters`,
    find all indices in `letters` which are the starting locations of anagrams of `word`.
    For example, given `word` is `te` and `letters` is `textet`, return `[0, 3, 4, 5]`.

    1. Brute force solution

    This algorithm would take O(w x s) time
    - x is the length of the word
    - y is the length of the input string

    :param word: word to be analyzed
    :param letters: complete word to be scanned
    :return: Array

    >>> find_anagram_indices("te", "texetet")
    [0, 3, 4, 5]
    """
    output = []
    for i in range(len(letters) - len(word) + 1):
        window = letters[i:i + len(word)]
        if Counter(window) == Counter(word):
            output.append(i)
    return output

def find_anagram_indices_2(word: str, letters: str) -> list:
    """
    Given a word `word`, and a string `letters`,
    find all indices in `letters` which are the starting locations of anagrams of `word`.
    For example, given `word` is `te` and `letters` is `textet`, return `[0, 3, 4, 5]`.

    2. Better scenario

    This algorithm would run in O(s) time and space.

    :param word: word to be analyzed
    :param letters: complete word to be scanned
    :return: Array

    >>> print(find_anagram_indices_2("te", "texetet"))
    [0, 3, 4, 5]
    """

    output = []
    freq = defaultdict(int)

    for char in word:
        freq[char] += 1

    for char in letters[:len(word)]:
        freq[char] -= 1
        if freq[char] == 0:
            del freq[char]

    if not freq:
        output.append(0)

    for i in range(len(word), len(letters)):
        start_char, end_char = letters[i - len(word)], letters[i]
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
