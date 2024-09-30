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
    return "".join(sorted(word.replace(" ", "").lower()))


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


def load_word_list(file_path: Path) -> list[str]:
    """Load a list of words from a file"""
    return sorted(
        {
            word.strip().lower()
            for word in file_path.read_text(encoding="utf-8").splitlines()
        }
    )


def create_word_by_signature(word_list: list[str]) -> dict[str, list[str]]:
    """Create a dictionary mapping word signatures to lists of words"""
    word_by_signature = collections.defaultdict(list)
    for word in word_list:
        word_by_signature[signature(word)].append(word)
    return word_by_signature


def find_all_anagrams(word_list: list[str]) -> dict[str, list[str]]:
    """Find all anagrams in a list of words"""
    word_by_signature = create_word_by_signature(word_list)
    return {word: anagram(word) for word in word_list if len(anagram(word)) > 1}


def main():
    data_file = Path(__file__).parent.joinpath("words.txt")
    word_list = load_word_list(data_file)
    all_anagrams = find_all_anagrams(word_list)

    with open("anagrams.txt", "w") as file:
        file.write("all_anagrams = \n ")
        file.write(pprint.pformat(all_anagrams))


if __name__ == "__main__":
    main()
