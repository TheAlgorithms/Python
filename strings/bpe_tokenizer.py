"""Byte-Pair Encoding: Subword-based tokenization algorithm used
by state-of-the-art language models.

Wikipedia: https://en.wikipedia.org/wiki/Byte_pair_encoding"""

import itertools
from collections import OrderedDict


def get_byte_pair_counts(ids: list[int]) -> dict:
    """Count consecutive byte-pairs of an encoded string.

    >>> ids = [73, 32, 97, 109, 32, 74, 111, 110, 83, 110, 111, 119, 46]
    >>> get_byte_pair_counts(ids)
    {(73, 32): 1, (32, 97): 1, (97, 109): 1, (109, 32): 1, (32, 74): 1, (74, 111): 1, (111, 110): 1, (110, 83): 1, (83, 110): 1, (110, 111): 1, (111, 119): 1, (119, 46): 1}
    >>> ids = [2, 3, 6, 2, 3, 6, 2, 5]
    >>> get_byte_pair_counts(ids)
    {(2, 3): 2, (3, 6): 2, (6, 2): 2, (2, 5): 1}
    """  # noqa: E501
    counts: dict = {}
    for pair in itertools.pairwise(ids):
        counts[pair] = counts.get(pair, 0) + 1
    return counts


def merge(ids: list[int], pair: tuple, idx: int) -> list[int]:
    """Replace most occurring byte pair with new byte that is not used
    in the data. For utf-8 encoding, we start with 256 as the new byte

    >>> ids = [2, 3, 6, 2, 3, 6, 2, 5]
    >>> pair = (2, 3)
    >>> idx = 256
    >>> merge(ids, pair, idx)
    [256, 6, 256, 6, 2, 5]
    """
    new_ids = []
    i = 0
    while i < len(ids):
        if i < len(ids) - 1 and (ids[i] == pair[0] and ids[i + 1] == pair[1]):
            new_ids.append(idx)
            i += 2
        else:
            new_ids.append(ids[i])
            i += 1
    return new_ids


class Tokenizer:
    """Tokenize a string using the byte-pair encoding algorithm"""

    def __init__(self, num_merges: int = 20, verbose: bool = False) -> None:
        self.num_merges = num_merges
        self.merges: dict = {}
        self.verbose = verbose

    def encode(self, text: str) -> list[int]:
        """Convert a string to tokens (bytes)

        >>> t = Tokenizer()
        >>> text = "I am JonSnow."
        >>> t.encode(text)
        [73, 32, 97, 109, 32, 74, 111, 110, 83, 110, 111, 119, 46]

        >>> t = Tokenizer()
        >>> text = ""
        >>> t.encode(text)
        []
        """
        text_b = text.encode("utf-8")  # raw bytes
        tokens = list(map(int, text_b))  # convert to list of integers

        if self.verbose:
            print(f"Input text: {text}")
            print(f"Tokens: {tokens}")

        ids = list(tokens)  # create a copy of tokens
        self.merges = OrderedDict()  # store a mapping of merges (int, int) -> int
        max_merges = len(tokens) - 1
        num_merges = min(self.num_merges, max_merges)
        # start merging most frequently occurring byte pairs
        for i in range(num_merges):
            counts = get_byte_pair_counts(ids)
            pair = max(counts, key=counts.__getitem__)

            if counts[pair] == 1:
                continue

            idx = 256 + i  # create new token for every merge step
            if self.verbose:
                print(f"Merging {pair} into a new token {idx}")
            ids = merge(ids, pair, idx)
            self.merges[pair] = idx

        return ids

    def decode(self, ids: list[int]) -> str:
        """Convert a list of tokens to the original string

        >>> t = Tokenizer()
        >>> ids = [73, 32, 97, 109, 32, 74, 111, 110, 83, 110, 111, 119, 46]
        >>> t.decode(ids)
        'I am JonSnow.'

        >>> t = Tokenizer()
        >>> ids = []
        >>> t.decode(ids)
        ''
        """
        vocab = {idx: bytes([idx]) for idx in range(256)}  # original vocabulary
        # The iteration of items should be in the order of
        # their insertion. This is the default behavior in Python 3
        # but we use an OrderedDict explicitly here
        for (p0, p1), idx in self.merges.items():
            vocab[idx] = vocab[p0] + vocab[p1]

        if self.verbose:
            print("Vocabulary (after merging): {vocab}")

        tokens = b"".join(vocab[idx] for idx in ids)
        # handle UnicodeDecodeError by replacing the invalid
        # start byte to conform to utf-8 format
        text = tokens.decode("utf-8", errors="replace")
        return text


if __name__ == "__main__":
    import doctest

    doctest.testmod()
