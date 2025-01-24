from __future__ import annotations

import collections
import pprint
from pathlib import Path


def signature(word: str) -> str:
    """Return a word sorted
    >>> signature("test")
    'estt'
    >>> signature("this is a test")
    '   aehiisssttt'
    >>> signature("finaltest")
    'aefilnstt'
    """
    return "".join(sorted(word))


def anagram(my_word: str) -> list[str]:
    """Return every anagram of the given word
    >>> anagram('test')
    ['sett', 'stet', 'test']
    >>> anagram('this is a test')
    []
    >>> anagram('final')
    ['final']
    """
    return word_by_signature[signature(my_word)]


data: str = Path(__file__).parent.joinpath("words.txt").read_text(encoding="utf-8")
word_list = sorted({word.strip().lower() for word in data.splitlines()})

word_by_signature = collections.defaultdict(list)
for word in word_list:
    word_by_signature[signature(word)].append(word)

if __name__ == "__main__":
    all_anagrams = {word: anagram(word) for word in word_list if len(anagram(word)) > 1}

    with open("anagrams.txt", "w") as file:
        file.write("all_anagrams = \n ")
        file.write(pprint.pformat(all_anagrams))
