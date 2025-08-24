from __future__ import annotations

import collections
import pprint
from pathlib import Path


def signature(word: str) -> tuple[int, ...]:
    """Return a word's character frequency signature (26-length tuple).
    Faster than sorting (O(m) instead of O(m log m)).

    >>> signature("test")
    (0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0)
    >>> signature("final")
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0)
    """
    counts = [0] * 26
    for ch in word:
        if ch.isalpha():  # ignore spaces, punctuation
            counts[ord(ch) - ord("a")] += 1
    return tuple(counts)


def anagram(my_word: str) -> list[str]:
    """Return every anagram of the given word"""
    return word_by_signature[signature(my_word)]


# --- Load words from file ---
data: str = Path(__file__).parent.joinpath("words.txt").read_text(encoding="utf-8")
word_list = sorted({word.strip().lower() for word in data.splitlines()})

# --- Build dictionary: signature -> words ---
word_by_signature = collections.defaultdict(list)
for word in word_list:
    word_by_signature[signature(word)].append(word)

# --- Main ---
if __name__ == "__main__":
    all_anagrams = {word: anagram(word) for word in word_list if len(anagram(word)) > 1}

    with open("anagrams.txt", "w") as file:
        file.write("all_anagrams = \n ")
        file.write(pprint.pformat(all_anagrams))
