from __future__ import annotations

import collections
import pprint
from pathlib import Path
from typing import List


def signature(word: str) -> str:
    """
    Return a frequency-based signature for a word.

    >>> signature("test")
    'e1s1t2'
    >>> signature("this is a test")
    ' 3a1e1h1i2s3t3'
    >>> signature("finaltest")
    'a1e1f1i1l1n1s1t2'
    """
    freq = collections.Counter(word)
    return "".join(f"{ch}{freq[ch]}" for ch in sorted(freq))


def anagram(my_word: str) -> List[str]:
    """
    Return every anagram of the given word from the dictionary.

    >>> anagram('test')
    ['sett', 'stet', 'test']
    >>> anagram('this is a test')
    []
    >>> anagram('final')
    ['final']
    """
    return word_by_signature.get(signature(my_word), [])


# Load word list
data: str = Path(__file__).parent.joinpath("words.txt").read_text(encoding="utf-8")
word_list = sorted({word.strip().lower() for word in data.splitlines()})

# Map signatures to word list
word_by_signature = collections.defaultdict(list)
for word in word_list:
    word_by_signature[signature(word)].append(word)

if __name__ == "__main__":
    all_anagrams = {word: anagram(word) for word in word_list if len(anagram(word)) > 1}

    with open("anagrams.txt", "w", encoding="utf-8") as file:
        file.write("all_anagrams = \n")
        file.write(pprint.pformat(all_anagrams))
