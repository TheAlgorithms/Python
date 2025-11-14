"""Trie (prefix tree) implementation."""

from dataclasses import dataclass, field
from typing import Dict


@dataclass
class _TrieNode:
    children: Dict[str, "_TrieNode"] = field(default_factory=dict)
    end_of_word: bool = False


class Trie:
    def __init__(self) -> None:
        self._root = _TrieNode()

    def insert(self, word: str) -> None:
        node = self._root
        for char in word:
            node = node.children.setdefault(char, _TrieNode())
        node.end_of_word = True

    def search(self, word: str) -> bool:
        node = self._find_node(word)
        return bool(node and node.end_of_word)

    def starts_with(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None

    def _find_node(self, key: str) -> _TrieNode | None:
        node = self._root
        for char in key:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
