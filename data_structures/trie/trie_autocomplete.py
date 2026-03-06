"""
Trie-based Autocomplete System

This module implements an efficient autocomplete system using a Trie data structure.
It supports prefix-based word suggestions with O(p + n) time complexity where p is
the prefix length and n is the number of matching words.

Reference: https://en.wikipedia.org/wiki/Trie
"""

from __future__ import annotations


class TrieNode:
    """
    A node in the Trie data structure.

    Attributes:
        children: Dictionary mapping characters to child nodes
        is_end_of_word: Boolean indicating if this node marks the end of a word
        frequency: Number of times this word has been inserted (for ranking)
    """

    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False
        self.frequency: int = 0


class TrieAutocomplete:
    """
    Trie-based autocomplete system supporting word insertion and prefix search.

    Examples:
    >>> autocomplete = TrieAutocomplete()
    >>> autocomplete.insert("hello")
    >>> autocomplete.insert("help")
    >>> autocomplete.insert("hero")
    >>> autocomplete.insert("hello")
    >>> sorted(autocomplete.search("hel"))
    ['hello', 'help']
    >>> sorted(autocomplete.search("her"))
    ['hero']
    >>> autocomplete.search("hey")
    []
    >>> autocomplete.get_suggestions("hel", max_results=1)
    ['hello']
    >>> autocomplete.contains("hello")
    True
    >>> autocomplete.contains("hel")
    False
    >>> autocomplete.delete("hello")
    True
    >>> autocomplete.contains("hello")
    False
    >>> autocomplete.delete("nonexistent")
    False
    """

    def __init__(self) -> None:
        """Initialize an empty Trie."""
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Insert a word into the Trie.

        Args:
            word: The word to insert

        Time Complexity: O(m) where m is the length of the word

        >>> trie = TrieAutocomplete()
        >>> trie.insert("apple")
        >>> trie.contains("apple")
        True
        """
        if not word:
            return

        node = self.root
        for char in word.lower():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end_of_word = True
        node.frequency += 1

    def contains(self, word: str) -> bool:
        """
        Check if a word exists in the Trie.

        Args:
            word: The word to search for

        Returns:
            True if the word exists, False otherwise

        Time Complexity: O(m) where m is the length of the word

        >>> trie = TrieAutocomplete()
        >>> trie.insert("test")
        >>> trie.contains("test")
        True
        >>> trie.contains("tes")
        False
        """
        node = self._find_node(word)
        return node is not None and node.is_end_of_word

    def _find_node(self, prefix: str) -> TrieNode | None:
        """
        Find the node corresponding to a prefix.

        Args:
            prefix: The prefix to search for

        Returns:
            The node if found, None otherwise
        """
        node = self.root
        for char in prefix.lower():
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def search(self, prefix: str) -> list[str]:
        """
        Find all words with the given prefix.

        Args:
            prefix: The prefix to search for

        Returns:
            List of all words starting with the prefix

        Time Complexity: O(p + n) where p is prefix length and n is number of results

        >>> trie = TrieAutocomplete()
        >>> trie.insert("cat")
        >>> trie.insert("car")
        >>> trie.insert("card")
        >>> sorted(trie.search("car"))
        ['car', 'card']
        """
        node = self._find_node(prefix)
        if node is None:
            return []

        results: list[str] = []
        self._collect_words(node, prefix.lower(), results)
        return results

    def _collect_words(
        self, node: TrieNode, current_word: str, results: list[str]
    ) -> None:
        """
        Recursively collect all words from a given node.

        Args:
            node: The current node
            current_word: The word formed so far
            results: List to store the results
        """
        if node.is_end_of_word:
            results.append(current_word)

        for char, child_node in sorted(node.children.items()):
            self._collect_words(child_node, current_word + char, results)

    def get_suggestions(self, prefix: str, max_results: int = 10) -> list[str]:
        """
        Get autocomplete suggestions sorted by frequency.

        Args:
            prefix: The prefix to search for
            max_results: Maximum number of suggestions to return

        Returns:
            List of suggested words sorted by frequency (most frequent first)

        >>> trie = TrieAutocomplete()
        >>> for _ in range(3):
        ...     trie.insert("popular")
        >>> trie.insert("pop")
        >>> trie.insert("pope")
        >>> suggestions = trie.get_suggestions("pop", max_results=2)
        >>> suggestions[0]
        'popular'
        """
        node = self._find_node(prefix)
        if node is None:
            return []

        words_with_freq: list[tuple[str, int]] = []
        self._collect_words_with_frequency(node, prefix.lower(), words_with_freq)

        words_with_freq.sort(key=lambda x: (-x[1], x[0]))
        return [word for word, _ in words_with_freq[:max_results]]

    def _collect_words_with_frequency(
        self, node: TrieNode, current_word: str, results: list[tuple[str, int]]
    ) -> None:
        """
        Recursively collect words with their frequencies.

        Args:
            node: The current node
            current_word: The word formed so far
            results: List to store (word, frequency) tuples
        """
        if node.is_end_of_word:
            results.append((current_word, node.frequency))

        for char, child_node in node.children.items():
            self._collect_words_with_frequency(
                child_node, current_word + char, results
            )

    def delete(self, word: str) -> bool:
        """
        Delete a word from the Trie.

        Args:
            word: The word to delete

        Returns:
            True if the word was deleted, False if it didn't exist

        >>> trie = TrieAutocomplete()
        >>> trie.insert("test")
        >>> trie.delete("test")
        True
        >>> trie.contains("test")
        False
        >>> trie.delete("test")
        False
        """

        def _delete_helper(node: TrieNode, word: str, index: int) -> bool:
            if index == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                node.frequency = 0
                return len(node.children) == 0

            char = word[index]
            if char not in node.children:
                return False

            child_node = node.children[char]
            should_delete_child = _delete_helper(child_node, word, index + 1)

            if should_delete_child:
                del node.children[char]
                return len(node.children) == 0 and not node.is_end_of_word

            return False

        if not word:
            return False

        node = self._find_node(word.lower())
        if node is None or not node.is_end_of_word:
            return False
        
        _delete_helper(self.root, word.lower(), 0)
        return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    autocomplete = TrieAutocomplete()
    words = ["hello", "help", "hero", "heroic", "hell", "helmet"]
    for word in words:
        autocomplete.insert(word)

    print("Words starting with 'hel':", autocomplete.search("hel"))
    print("Words starting with 'hero':", autocomplete.search("hero"))
    print("Top 3 suggestions for 'he':", autocomplete.get_suggestions("he", 3))
