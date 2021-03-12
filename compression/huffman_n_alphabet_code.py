"""
Python implementation of n-ary Huffman coding algorithm
https://en.wikipedia.org/wiki/Huffman_coding#Variations
"""
from __future__ import annotations

import heapq
import itertools
from collections import Counter, defaultdict
from collections.abc import Hashable, Iterable, Iterator, Mapping, Sequence
from dataclasses import dataclass
from typing import TypeVar

T = TypeVar("T")
H = TypeVar("H", bound=Hashable)


@dataclass(order=True, frozen=True)
class Node:
    """
    Node of priority queue. Has sum of probabilities of containing elements.
    """

    frequency: float
    elements: tuple[Hashable, ...]

    def __add__(self, other: Node) -> Node:
        """
        Add two nodes and returns new one

        Examples:
        >>> Node(3, (2, 3, 1)) + Node(1, (6, 4))
        Node(frequency=4, elements=(2, 3, 1, 6, 4))
        """
        return Node(self.frequency + other.frequency, self.elements + other.elements)


def huffman(frequencies: Mapping[H, int], alphabet_size: int = 2) -> dict[H, list[int]]:
    """
    N-ary Huffman algorithm that uses priority queue

    Encodes each element with prefix code according to frequencies table.
    Produced codes is lists of integers because it can be easily converted to bits
    (if alphabet size == 2), strings of decimals (alphabet_size == 10), hexadecimal
    string (alphabet_size == 16) or anything else on demand.

    :param frequencies: table of frequency for each element
    :param alphabet_size: size of alphabet of code (default creates binary alphabet)
    :return: table of codes for each element

    Examples:
    >>> sorted(huffman({"a": 4, "b": 1, "c": 3, "d": 1}, 3).items())
    [('a', [0]), ('b', [1, 0]), ('c', [1, 2]), ('d', [1, 1])]
    >>> huffman({})
    {}
    >>> huffman({"a": 1})
    {'a': [0]}
    >>> huffman({"a": 4, "b": 1, "c": 3, "d": 1}, 1)
    Traceback (most recent call last):
    ...
    ValueError: Alphabet size cannot be less 2
    """
    if alphabet_size < 2:
        raise ValueError("Alphabet size cannot be less 2")
    if len(frequencies) == 1:
        return {next(iter(frequencies)): [0]}
    codes = defaultdict(list)
    node_heap = [Node(freq, (elem,)) for elem, freq in frequencies.items()]
    heapq.heapify(node_heap)
    while len(node_heap) > 1:
        nodes = [
            heapq.heappop(node_heap) for _ in range(min(alphabet_size, len(node_heap)))
        ]
        for i, node in enumerate(nodes):
            for e in node.elements:
                codes[e].append(i)
        heapq.heappush(node_heap, sum(nodes, Node(0, ())))
    for code in codes.values():
        code.reverse()
    return dict(codes)


def encode(elements: Iterable[H], coding_table: Mapping[H, Sequence[T]]) -> Iterator[T]:
    """
    Encode sequence of elements with given encoding table

    :param elements: elements to be encoded
    :param coding_table: map containing codes for each element
    :return: iterator over encoded sequence

    Examples:
    >>> list(encode("abcc", {"a": (0,), "b": (1, 0), "c": (1, 1)}))
    [0, 1, 0, 1, 1, 1, 1]
    >>> "".join(encode("abc", {"a": "0", "b": "10", "c": "11"}))
    '01011'
    """
    return itertools.chain.from_iterable(coding_table[elem] for elem in elements)


if __name__ == "__main__":
    text = "abcccdefffffaaabcddddcccaaab"
    code_alphabet_size = 10
    frequencies_table = Counter(text)
    huffman_coding_table = huffman(frequencies_table, code_alphabet_size)
    encoded_text = "".join(map(str, encode(text, huffman_coding_table)))
    print(encoded_text)
