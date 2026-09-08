"""
Finds the top K most frequent words from the provided word list.

This implementation aims to show how to solve the problem using the Heap class
already present in this repository.
Computing order statistics is, in fact, a typical usage of heaps.

This is mostly shown for educational purposes, since the problem can be solved
in a few lines using collections.Counter from the Python standard library:

from collections import Counter
def top_k_frequent_words(words, k_value):
    return [x[0] for x in Counter(words).most_common(k_value)]
"""

from collections import Counter
from functools import total_ordering

from data_structures.heap.heap import Heap


@total_ordering
class WordCount:
    def __init__(self, word: str, count: int) -> None:
        self.word = word
        self.count = count

    def __eq__(self, other: object) -> bool:
        """
        >>> WordCount('a', 1).__eq__(WordCount('b', 1))
        True
        >>> WordCount('a', 1).__eq__(WordCount('a', 1))
        True
        >>> WordCount('a', 1).__eq__(WordCount('a', 2))
        False
        >>> WordCount('a', 1).__eq__(WordCount('b', 2))
        False
        >>> WordCount('a', 1).__eq__(1)
        NotImplemented
        """
        if not isinstance(other, WordCount):
            return NotImplemented
        return self.count == other.count

    def __lt__(self, other: object) -> bool:
        """
        >>> WordCount('a', 1).__lt__(WordCount('b', 1))
        False
        >>> WordCount('a', 1).__lt__(WordCount('a', 1))
        False
        >>> WordCount('a', 1).__lt__(WordCount('a', 2))
        True
        >>> WordCount('a', 1).__lt__(WordCount('b', 2))
        True
        >>> WordCount('a', 2).__lt__(WordCount('a', 1))
        False
        >>> WordCount('a', 2).__lt__(WordCount('b', 1))
        False
        >>> WordCount('a', 1).__lt__(1)
        NotImplemented
        """
        if not isinstance(other, WordCount):
            return NotImplemented
        return self.count < other.count


def top_k_frequent_words(words: list[str], k_value: int) -> list[str]:
    """
    Returns the `k_value` most frequently occurring words,
    in non-increasing order of occurrence.
    In this context, a word is defined as an element in the provided list.

    In case `k_value` is greater than the number of distinct words, a value of k equal
    to the number of distinct words will be considered, instead.

    >>> top_k_frequent_words(['a', 'b', 'c', 'a', 'c', 'c'], 3)
    ['c', 'a', 'b']
    >>> top_k_frequent_words(['a', 'b', 'c', 'a', 'c', 'c'], 2)
    ['c', 'a']
    >>> top_k_frequent_words(['a', 'b', 'c', 'a', 'c', 'c'], 1)
    ['c']
    >>> top_k_frequent_words(['a', 'b', 'c', 'a', 'c', 'c'], 0)
    []
    >>> top_k_frequent_words([], 1)
    []
    >>> top_k_frequent_words(['a', 'a'], 2)
    ['a']
    """
    heap: Heap[WordCount] = Heap()
    count_by_word = Counter(words)
    heap.build_max_heap(
        [WordCount(word, count) for word, count in count_by_word.items()]
    )
    return [heap.extract_max().word for _ in range(min(k_value, len(count_by_word)))]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
