"""
A Trie-based Spell Checker that suggests corrections for misspelled words.

This module uses a Trie data structure to store a dictionary of valid words
and provides spell-checking functionality with edit-distance-based suggestions.

The spell checker can:
- Load a dictionary of valid words into a Trie
- Check if a word is spelled correctly
- Suggest corrections for misspelled words based on edit distance
"""


class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Insert a word into the Trie.

        >>> trie = Trie()
        >>> trie.insert("hello")
        >>> trie.search("hello")
        True
        >>> trie.search("hell")
        False
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Search for a word in the Trie.

        >>> trie = Trie()
        >>> trie.insert("world")
        >>> trie.search("world")
        True
        >>> trie.search("wor")  # codespell:ignore
        False
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def _collect_words(self, node: TrieNode, prefix: str) -> list[str]:
        """Collect all words from a given node with the given prefix."""
        words: list[str] = []
        if node.is_end_of_word:
            words.append(prefix)
        for char, child in node.children.items():
            words.extend(self._collect_words(child, prefix + char))
        return words

    def get_all_words(self) -> list[str]:
        """
        Return all words stored in the Trie.

        >>> trie = Trie()
        >>> trie.insert("apple")
        >>> trie.insert("app")
        >>> sorted(trie.get_all_words())
        ['app', 'apple']
        """
        return self._collect_words(self.root, "")


class SpellChecker:
    """
    A spell checker that uses a Trie to store a dictionary and provides
    suggestions for misspelled words based on edit distance.

    >>> sc = SpellChecker(["hello", "world", "help", "held", "helm"])
    >>> sc.is_correct("hello")
    True
    >>> sc.is_correct("helo")
    False
    >>> "hello" in sc.suggest("helo")
    True
    >>> sc.is_correct("world")
    True
    """

    def __init__(self, dictionary: list[str] | None = None) -> None:
        self.trie = Trie()
        if dictionary:
            for word in dictionary:
                self.trie.insert(word.lower())

    def add_word(self, word: str) -> None:
        """
        Add a word to the dictionary.

        >>> sc = SpellChecker()
        >>> sc.add_word("python")
        >>> sc.is_correct("python")
        True
        """
        self.trie.insert(word.lower())

    def is_correct(self, word: str) -> bool:
        """
        Check if a word is spelled correctly (exists in dictionary).

        >>> sc = SpellChecker(["test"])
        >>> sc.is_correct("test")
        True
        >>> sc.is_correct("tst")
        False
        """
        return self.trie.search(word.lower())

    @staticmethod
    def _edit_distance(word1: str, word2: str) -> int:
        """
        Calculate the Levenshtein edit distance between two words.

        >>> SpellChecker._edit_distance("kitten", "sitting")
        3
        >>> SpellChecker._edit_distance("hello", "hello")
        0
        >>> SpellChecker._edit_distance("", "abc")
        3
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],  # deletion
                        dp[i][j - 1],  # insertion
                        dp[i - 1][j - 1],  # substitution
                    )
        return dp[m][n]

    def suggest(self, word: str, max_suggestions: int = 5) -> list[str]:
        """
        Suggest corrections for a misspelled word.

        Returns up to max_suggestions words from the dictionary sorted
        by edit distance (closest first).

        >>> sc = SpellChecker(["hello", "help", "held", "helm", "world"])
        >>> suggestions = sc.suggest("helo")
        >>> "hello" in suggestions
        True
        >>> "help" in suggestions
        True
        """
        word = word.lower()
        if self.is_correct(word):
            return [word]

        all_words = self.trie.get_all_words()
        distances = [(w, self._edit_distance(word, w)) for w in all_words]
        distances.sort(key=lambda x: x[1])

        return [w for w, _ in distances[:max_suggestions]]


def test_spell_checker() -> None:
    """Test the SpellChecker functionality."""
    dictionary = [
        "apple",
        "application",
        "apply",
        "banana",
        "band",
        "bandana",
        "hello",
        "help",
        "held",
        "helm",
        "world",
        "word",
        "work",
    ]
    sc = SpellChecker(dictionary)

    # Test correct words
    assert sc.is_correct("apple")
    assert sc.is_correct("hello")
    assert sc.is_correct("world")
    assert sc.is_correct("banana")

    # Test incorrect words
    assert not sc.is_correct("aple")
    assert not sc.is_correct("helo")
    assert not sc.is_correct("wrld")

    # Test suggestions
    suggestions = sc.suggest("aple")
    assert "apple" in suggestions

    suggestions = sc.suggest("helo")
    assert "hello" in suggestions
    assert "help" in suggestions

    suggestions = sc.suggest("wrld")
    assert "world" in suggestions

    # Test add_word
    sc.add_word("python")
    assert sc.is_correct("python")
    assert sc.is_correct("Python")  # case-insensitive search

    # Test edit distance
    assert SpellChecker._edit_distance("hello", "hello") == 0
    assert SpellChecker._edit_distance("hello", "helo") == 1
    assert SpellChecker._edit_distance("kitten", "sitting") == 3

    print("All spell checker tests passed!")


if __name__ == "__main__":
    test_spell_checker()
