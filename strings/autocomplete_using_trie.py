from __future__ import annotations
from typing import Dict, List, Tuple, Union

END = "#"


class Trie:
    def __init__(self) -> None:
        self._trie: Dict[str, Union[Dict, bool]] = {}

    def insert_word(self, word: str) -> None:
        """Inserts a word into the trie, case insensitive."""
        node = self._trie
        word = word.lower()
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[END] = True

    def find_word(self, prefix: str) -> Union[List[str], Tuple[str, ...]]:
        """Finds all suffixes in the trie that match the given prefix, case insensitive."""
        node = self._trie
        prefix = prefix.lower()
        for char in prefix:
            if char in node:
                node = node[char]
            else:
                return []
        return self._elements(node)

    def delete_word(self, word: str) -> None:
        """Deletes a word from the trie if it exists, case insensitive."""

        def _delete(node: Dict[str, Union[Dict, bool]], word: str, depth: int) -> bool:
            if depth == len(word):
                if END in node:
                    del node[END]
                    return len(node) == 0
                return False
            char = word[depth]
            if char in node and _delete(node[char], word, depth + 1):
                del node[char]
                return len(node) == 0
            return False

        _delete(self._trie, word.lower(), 0)

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


# Example usage of the enhanced Trie class
def autocomplete_using_trie(prefix: str, trie: Trie) -> Tuple[str, ...]:
    """
    Autocompletes the given prefix using the trie.

    >>> trie = Trie()
    >>> words = ("depart", "detergent", "daring", "dog", "deer", "deal")
    >>> for word in words:
    ...     trie.insert_word(word)
    ...
    >>> matches = autocomplete_using_trie("de", trie)
    >>> "detergent" in matches
    True
    >>> "dog" in matches
    False
    """
    suffixes = trie.find_word(prefix)
    return tuple(prefix + suffix for suffix in suffixes)


def main() -> None:
    trie = Trie()
    words = ("depart", "detergent", "daring", "dog", "deer", "deal")
    for word in words:
        trie.insert_word(word)
    print(autocomplete_using_trie("de", trie))
    trie.delete_word("detergent")
    print(autocomplete_using_trie("de", trie))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
