"""
Advanced Trie (Prefix Tree) implementation.

A Trie is a tree-like data structure that stores strings in a way that
allows for efficient prefix-based operations. This implementation includes:
- Basic insert, search, and delete operations
- Prefix search and autocomplete
- Longest common prefix
- Pattern matching with wildcards

Time Complexity:
    - Insert: O(m) where m is the length of the string
    - Search: O(m) where m is the length of the string
    - Delete: O(m) where m is the length of the string
    - Prefix search: O(m + k) where m is prefix length, k is number of results
Space Complexity: O(ALPHABET_SIZE * N * M) where N is number of strings, M is average length

Reference: https://en.wikipedia.org/wiki/Trie
"""

from typing import List, Set, Optional, Dict, Any
import re


class TrieNode:
    """Node in the Trie data structure."""

    def __init__(self):
        self.children: Dict[str, "TrieNode"] = {}
        self.is_end_of_word: bool = False
        self.word_count: int = 0  # Number of words ending at this node
        self.prefix_count: int = 0  # Number of words with this prefix
        self.data: Any = None  # Additional data associated with the word


class Trie:
    """
    Advanced Trie implementation with comprehensive functionality.

    Attributes:
        root: Root node of the trie
        size: Number of words in the trie
    """

    def __init__(self):
        """Initialize an empty Trie."""
        self.root = TrieNode()
        self.size = 0

    def insert(self, word: str, data: Any = None) -> None:
        """
        Insert a word into the trie.

        Args:
            word: Word to insert
            data: Additional data to associate with the word

        Examples:
            >>> trie = Trie()
            >>> trie.insert("hello")
            >>> trie.search("hello")
            True
        """
        if not word:
            return

        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.prefix_count += 1

        if not node.is_end_of_word:
            self.size += 1
            node.is_end_of_word = True

        node.word_count += 1
        node.data = data

    def search(self, word: str) -> bool:
        """
        Search for a word in the trie.

        Args:
            word: Word to search for

        Returns:
            True if word exists, False otherwise

        Examples:
            >>> trie = Trie()
            >>> trie.insert("hello")
            >>> trie.search("hello")
            True
            >>> trie.search("world")
            False
        """
        node = self._find_node(word)
        return node is not None and node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """
        Check if any word in the trie starts with the given prefix.

        Args:
            prefix: Prefix to check

        Returns:
            True if any word starts with prefix, False otherwise

        Examples:
            >>> trie = Trie()
            >>> trie.insert("hello")
            >>> trie.starts_with("hel")
            True
            >>> trie.starts_with("xyz")
            False
        """
        node = self._find_node(prefix)
        return node is not None

    def delete(self, word: str) -> bool:
        """
        Delete a word from the trie.

        Args:
            word: Word to delete

        Returns:
            True if word was deleted, False if word didn't exist

        Examples:
            >>> trie = Trie()
            >>> trie.insert("hello")
            >>> trie.delete("hello")
            True
            >>> trie.search("hello")
            False
        """
        if not word:
            return False

        # First check if word exists
        if not self.search(word):
            return False

        # Delete the word
        self._delete_helper(self.root, word, 0)
        self.size -= 1
        return True

    def _delete_helper(self, node: TrieNode, word: str, index: int) -> bool:
        """Helper method for deletion."""
        if index == len(word):
            if node.is_end_of_word:
                node.is_end_of_word = False
                node.word_count -= 1
                return node.word_count == 0
            return False

        char = word[index]
        if char not in node.children:
            return False

        should_delete_child = self._delete_helper(node.children[char], word, index + 1)

        if should_delete_child:
            del node.children[char]

        node.prefix_count -= 1
        return len(node.children) == 0 and not node.is_end_of_word

    def _find_node(self, word: str) -> Optional[TrieNode]:
        """
        Find the node corresponding to the given word.

        Args:
            word: Word to find node for

        Returns:
            TrieNode if found, None otherwise

        Examples:
            >>> trie = Trie()
            >>> trie.insert("hello")
            >>> node = trie._find_node("hello")
            >>> node is not None
            True
            >>> node.is_end_of_word
            True
            >>> trie._find_node("world") is None
            True
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def get_all_words_with_prefix(self, prefix: str) -> List[str]:
        """
        Get all words that start with the given prefix.

        Args:
            prefix: Prefix to search for

        Returns:
            List of words starting with the prefix

        Examples:
            >>> trie = Trie()
            >>> trie.insert("hello")
            >>> trie.insert("help")
            >>> trie.insert("world")
            >>> trie.get_all_words_with_prefix("hel")
            ['hello', 'help']
        """
        node = self._find_node(prefix)
        if node is None:
            return []

        words = []
        self._collect_words(node, prefix, words)
        return words

    def _collect_words(
        self, node: TrieNode, current_word: str, words: List[str]
    ) -> None:
        """
        Collect all words from a given node.

        Args:
            node: Current trie node
            current_word: Current word being built
            words: List to collect words into

        Examples:
            >>> trie = Trie()
            >>> trie.insert("hello")
            >>> trie.insert("help")
            >>> words = []
            >>> trie._collect_words(trie._find_node("hel"), "hel", words)
            >>> sorted(words)
            ['hello', 'help']
        """
        if node.is_end_of_word:
            words.append(current_word)

        for char, child_node in node.children.items():
            self._collect_words(child_node, current_word + char, words)

    def autocomplete(self, prefix: str, max_results: int = 10) -> List[str]:
        """
        Get autocomplete suggestions for the given prefix.

        Args:
            prefix: Prefix to autocomplete
            max_results: Maximum number of results to return

        Returns:
            List of autocomplete suggestions

        Examples:
            >>> trie = Trie()
            >>> trie.insert("hello")
            >>> trie.insert("help")
            >>> trie.insert("world")
            >>> trie.autocomplete("hel", 5)
            ['hello', 'help']
        """
        words = self.get_all_words_with_prefix(prefix)
        return words[:max_results]

    def longest_common_prefix(self) -> str:
        """
        Find the longest common prefix of all words in the trie.

        Returns:
            Longest common prefix

        Examples:
            >>> trie = Trie()
            >>> trie.insert("hello")
            >>> trie.insert("help")
            >>> trie.insert("helicopter")
            >>> trie.longest_common_prefix()
            'hel'
        """
        if self.size == 0:
            return ""

        prefix = ""
        node = self.root

        while len(node.children) == 1 and not node.is_end_of_word:
            char = next(iter(node.children.keys()))
            prefix += char
            node = node.children[char]

        return prefix

    def get_word_count(self, word: str) -> int:
        """
        Get the count of how many times a word was inserted.

        Args:
            word: Word to get count for

        Returns:
            Number of times the word was inserted

        Examples:
            >>> trie = Trie()
            >>> trie.insert("hello")
            >>> trie.insert("hello")
            >>> trie.get_word_count("hello")
            2
        """
        node = self._find_node(word)
        return node.word_count if node and node.is_end_of_word else 0

    def get_prefix_count(self, prefix: str) -> int:
        """
        Get the count of words that start with the given prefix.

        Args:
            prefix: Prefix to count

        Returns:
            Number of words starting with the prefix

        Examples:
            >>> trie = Trie()
            >>> trie.insert("hello")
            >>> trie.insert("help")
            >>> trie.get_prefix_count("hel")
            2
        """
        node = self._find_node(prefix)
        return node.prefix_count if node else 0

    def pattern_search(self, pattern: str) -> List[str]:
        """
        Search for words matching a pattern with wildcards.
        Supports '*' for any character and '?' for single character.

        Args:
            pattern: Pattern to match (supports * and ? wildcards)

        Returns:
            List of words matching the pattern

        Examples:
            >>> trie = Trie()
            >>> trie.insert("hello")
            >>> trie.insert("help")
            >>> trie.insert("world")
            >>> trie.pattern_search("hel*")
            ['hello', 'help']
        """
        words = []
        self._pattern_search_helper(self.root, "", pattern, words)
        return words

    def _pattern_search_helper(
        self, node: TrieNode, current_word: str, pattern: str, words: List[str]
    ) -> None:
        """Helper method for pattern search."""
        if not pattern:
            if node.is_end_of_word:
                words.append(current_word)
            return

        char = pattern[0]
        remaining_pattern = pattern[1:]

        if char == "*":
            # Match zero or more characters
            self._pattern_search_helper(node, current_word, remaining_pattern, words)
            for child_char, child_node in node.children.items():
                self._pattern_search_helper(
                    child_node, current_word + child_char, pattern, words
                )
        elif char == "?":
            # Match any single character
            for child_char, child_node in node.children.items():
                self._pattern_search_helper(
                    child_node, current_word + child_char, remaining_pattern, words
                )
        else:
            # Match exact character
            if char in node.children:
                self._pattern_search_helper(
                    node.children[char], current_word + char, remaining_pattern, words
                )

    def get_all_words(self) -> List[str]:
        """
        Get all words in the trie.

        Returns:
            List of all words

        Examples:
            >>> trie = Trie()
            >>> trie.insert("hello")
            >>> trie.insert("world")
            >>> trie.get_all_words()
            ['hello', 'world']
        """
        return self.get_all_words_with_prefix("")

    def clear(self) -> None:
        """Clear all words from the trie."""
        self.root = TrieNode()
        self.size = 0

    def __len__(self) -> int:
        """Return the number of words in the trie."""
        return self.size

    def __contains__(self, word: str) -> bool:
        """Support 'in' operator."""
        return self.search(word)

    def __repr__(self) -> str:
        """String representation of the trie."""
        return f"Trie(size={self.size})"


class CompressedTrie(Trie):
    """
    Compressed Trie implementation for memory efficiency.

    Reduces memory usage by compressing chains of single-child nodes.
    """

    def __init__(self):
        super().__init__()
        self.compressed = True

    def _compress(self) -> None:
        """Compress the trie by merging single-child chains."""
        self._compress_helper(self.root)

    def _compress_helper(self, node: TrieNode) -> None:
        """Helper method for compression."""
        if len(node.children) == 1 and not node.is_end_of_word:
            child_char, child_node = next(iter(node.children.items()))
            # Merge single child
            node.children = child_node.children
            node.is_end_of_word = child_node.is_end_of_word
            node.word_count = child_node.word_count
            node.prefix_count = child_node.prefix_count
            node.data = child_node.data

        for child_node in node.children.values():
            self._compress_helper(child_node)


if __name__ == "__main__":
    # Example usage
    print("Trie Example")
    print("=" * 50)

    # Create Trie
    trie = Trie()

    # Insert words
    words = ["hello", "help", "world", "word", "helicopter", "hero", "her"]
    for word in words:
        trie.insert(word)
        print(f"Inserted: {word}")

    print(f"\nTrie size: {len(trie)}")

    # Search operations
    print(f"\nSearch operations:")
    search_words = ["hello", "help", "xyz", "world"]
    for word in search_words:
        result = trie.search(word)
        print(f"'{word}': {'Found' if result else 'Not found'}")

    # Prefix operations
    print(f"\nPrefix operations:")
    prefixes = ["hel", "wor", "xyz"]
    for prefix in prefixes:
        has_prefix = trie.starts_with(prefix)
        words_with_prefix = trie.get_all_words_with_prefix(prefix)
        print(f"Prefix '{prefix}': {has_prefix}, Words: {words_with_prefix}")

    # Autocomplete
    print(f"\nAutocomplete:")
    autocomplete_prefixes = ["hel", "wor"]
    for prefix in autocomplete_prefixes:
        suggestions = trie.autocomplete(prefix, 3)
        print(f"'{prefix}' -> {suggestions}")

    # Longest common prefix
    print(f"\nLongest common prefix: '{trie.longest_common_prefix()}'")

    # Pattern search
    print(f"\nPattern search:")
    patterns = ["hel*", "wor?", "h*"]
    for pattern in patterns:
        matches = trie.pattern_search(pattern)
        print(f"Pattern '{pattern}': {matches}")

    # Word counts
    print(f"\nWord counts:")
    trie.insert("hello")  # Insert again
    print(f"'hello' count: {trie.get_word_count('hello')}")
    print(f"'hel' prefix count: {trie.get_prefix_count('hel')}")

    # Delete operation
    print(f"\nDelete operation:")
    print(f"Before delete - 'help' exists: {trie.search('help')}")
    trie.delete("help")
    print(f"After delete - 'help' exists: {trie.search('help')}")
    print(f"After delete - 'hel' prefix count: {trie.get_prefix_count('hel')}")

    # All words
    print(f"\nAll words in trie: {trie.get_all_words()}")

    print(f"\nTrie implementation completed successfully!")
