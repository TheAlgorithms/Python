"""
Given a word `x`, and a string `y`, find all indices in `y` which are the starting locations of anagrams of `x`.

For example, given `x` is `te` and `y` is `textet`, return `[0, 3, 4, 5]`.
"""

"""
1. Brute force solution

This algorithm would take O(w x s) time
- w is the length of the word
- s is the length of the input string
"""

from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)

def find_anagram_indices(word, s):
    result = []
    for i in range(len(s) - len(word) + 1):
        window = s[i:i + len(word)]
        if is_anagram(window, word):
            result.append(i)
    return result

print(find_anagram_indices("te", "texetet"))

"""
2. Better scenario

This algorithm would run in O(s) time and space.
"""

from collections import defaultdict

def delete_if_zero(dict, char):
    if dict[char] == 0:
        del dict[char]

def find_anagram_indices(word, s):
    result = []
    freq = defaultdict(int)

    for char in word:
        freq[char] += 1

    for char in s[:len(word)]:
        freq[char] -= 1
        delete_if_zero(freq, char)

    if not freq:
        result.append(0)

    for i in range(len(word), len(s)):
        start_char, end_char = s[i - len(word)], s[i]
        freq[start_char] += 1
        delete_if_zero(freq, start_char)

        freq[end_char] -= 1
        delete_if_zero(freq, end_char)

        if not freq:
            beginning_index = i - len(word) + 1
            result.append(beginning_index)

    return result

print(find_anagram_indices("te", "texetet"))
