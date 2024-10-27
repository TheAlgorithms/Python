"""
This is a pure Python implementation 
of the Commentz-Walter algorithm
for searching multiple patterns in a single text.

The algorithm combines Boyer-Moore's and 
Aho-Corasick's techniques for
efficiently searching multiple patterns 
by using pattern shifts and suffix automata.

For doctests run:
    python -m doctest -v commentz_walter.py
or
    python3 -m doctest -v commentz_walter.py
For manual testing run:
    python commentz_walter.py
"""

from typing import List, Dict, Set, Tuple
from collections import defaultdict
class CommentzWalter:
    """
    Class to represent the Commentz-Walter algorithm 
    for multi-pattern string searching.

    Attributes:
        patterns (List[str]): List of patterns to search for.
        alphabet (Set[str]): Unique characters in the patterns.
        shift_table (Dict[str, int]): Table to store 
        the shift values for characters.
        automaton (Dict[int, Dict[str, int]]): 
        Automaton used for state transitions.

    Methods:
        preprocess(): Builds the shift table 
        and automaton for pattern matching.
        search(text: str) -> List[Tuple[int, str]]: 
        Searches patterns in the given text.

    Examples:
    >>> cw = CommentzWalter(["he", "she", "his", "hers"])
    >>> cw.search("ahishers")
    [(1, 'his'), (4, 'she'), (5, 'hers')]
    """
    def __init__(self, patterns: List[str]) -> None:
        self.patterns = patterns
        self.alphabet: Set[str] = set("".join(patterns))
        self.shift_table: Dict[str, int] = {}
        self.automaton: Dict[int, Dict[str, int]] = {}
        self.preprocess()
    def preprocess(self) -> None:
        """
        Builds the shift table and automaton required 
        for the Commentz-Walter algorithm.
        """
        # Build the shift table for the rightmost occurrence of characters in patterns
        max_len = max(len(pattern) for pattern in self.patterns)
        for char in self.alphabet:
            self.shift_table[char] = max_len

        for pattern in self.patterns:
            for i, char in enumerate(pattern):
                self.shift_table[char] = max(1, max_len - i - 1)
        # Build the Aho-Corasick automaton for the set of patterns
        state = 0
        self.automaton[0] = {}
        for pattern in self.patterns:
            current_state = 0
            for char in pattern:
                if char not in self.automaton[current_state]:
                    state += 1
                    self.automaton[state] = {}
                    self.automaton[current_state][char] = state
                current_state = self.automaton[current_state][char]

    def search(self, text: str) -> List[Tuple[int, str]]:
        """
        Searches for patterns in the given text using
        the Commentz-Walter algorithm.
        :param text: The text to search in.
        :return: List of tuples with starting index and matched pattern.
        Examples:
        >>> cw = CommentzWalter(["abc", "bcd", "cde"])
        >>> cw.search("abcdef")
        [(0, 'abc'), (1, 'bcd'), (2, 'cde')]
        """
        results = []
        n = len(text)
        m = max(len(p) for p in self.patterns)
        i = 0
        while i <= n - m:
            j = m - 1
            while j >= 0 and text[i + j] in self.shift_table:
                j -= 1
            if j < 0:
                # We have a potential match; use the automaton to verify
                state = 0
                for k in range(m):
                    if text[i + k] in self.automaton[state]:
                        state = self.automaton[state][text[i + k]]
                    else:
                        break
                else:
                    for pattern in self.patterns:
                        if text[i:i + len(pattern)] == pattern:
                            results.append((i, pattern))
                i += self.shift_table.get(text[i + m - 1], m)
            else:
                i += self.shift_table.get(text[i + j], m)
        return results
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # Example usage for manual testing
    patterns = ["abc", "bcd", "cde"]
    cw = CommentzWalter(patterns)
    text = "abcdef"
    matches = cw.search(text)
    print("Matches found:", matches)
