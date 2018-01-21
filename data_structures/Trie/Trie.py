"""
A Trie/Prefix Tree is a kind of search tree used to provide quick lookup
of words/patterns in a set of words. A basic Trie however has O(n^2) space complexity
making it impractical in practice. It however provides O(max(search_string, length of longest word)) lookup
time making it an optimal approach when space is not an issue.

"""


class TrieNode:
    def __init__(self):
        self.nodes = dict()  # Mapping from char to TrieNode
        self.is_leaf = False

    def insert_many(self, words: [str]):  # noqa: F821 This syntax is Python 3 only
        """
        Inserts a list of words into the Trie
        :param words: list of string words
        :return: None
        """
        for word in words:
            self.insert(word)

    def insert(self, word: str):  # noqa: F821 This syntax is Python 3 only
        """
        Inserts a word into the Trie
        :param word: word to be inserted
        :return: None
        """
        curr = self
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = TrieNode()
            curr = curr.nodes[char]
        curr.is_leaf = True

    def find(self, word: str) -> bool:  # noqa: F821 This syntax is Python 3 only
        """
        Tries to find word in a Trie
        :param word: word to look for
        :return: Returns True if word is found, False otherwise
        """
        curr = self
        for char in word:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        return curr.is_leaf


def print_words(node: TrieNode, word: str):  # noqa: F821 This syntax is Python 3 only
    """
    Prints all the words in a Trie
    :param node: root node of Trie
    :param word: Word variable should be empty at start
    :return: None
    """
    if node.is_leaf:
        print(word, end=' ')

    for key, value in node.nodes.items():
        print_words(value, word + key)


def test():
    words = ['banana', 'bananas', 'bandana', 'band', 'apple', 'all', 'beast']
    root = TrieNode()
    root.insert_many(words)
    # print_words(root, '')
    assert root.find('banana')
    assert not root.find('bandanas')
    assert not root.find('apps')
    assert root.find('apple')

test()
