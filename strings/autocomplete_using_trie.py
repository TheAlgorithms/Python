from __future__ import annotations
from typing import Dict, List, Tuple, Union

END = "#"

class Trie:
    def __init__(self) -> None:
        self._trie: Dict[str, Union[Dict, bool]] = {}

    def insert_word(self, word: str) -> None:
        """Inserts a word into the trie."""
        node = self._trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[END] = True

    def find_word(self, prefix: str) -> Union[List[str], Tuple[str]]:
        """Finds all suffixes in the trie that match the given prefix."""
        node = self._trie
        for char in prefix:
            if char in node:
                node = node[char]
            else:
                return []
        return self._elements(node)

    def _elements(self, node: Dict[str, Union[Dict, bool]]) -> Tuple[str, ...]:
        """Recursively collects all words from the current node."""
        result = []
        for char, next_node in node.items():
            if char == END:
                result.append("")
            else:
                sub_result = [char + suffix for suffix in self._elements(next_node)]
                result.extend(sub_result)
        return tuple(result)

trie = Trie()
words = ("depart", "detergent", "daring", "dog", "deer", "deal")
for word in words:
    trie.insert_word(word)

def autocomplete_using_trie(prefix: str) -> Tuple[str, ...]:
    """
    Autocompletes the given prefix using the trie.

    >>> trie = Trie()
    >>> for word in words:
    ...     trie.insert_word(word)
    ...
    >>> matches = autocomplete_using_trie("de")
    >>> "detergent" in matches
    True
    >>> "dog" in matches
    False
    """
    suffixes = trie.find_word(prefix)
    return tuple(prefix + suffix for suffix in suffixes)

def main() -> None:
    print(autocomplete_using_trie("de"))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
