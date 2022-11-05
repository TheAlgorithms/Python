"""
A Trie/Prefix Tree is a kind of search tree used to provide quick lookup
of words/patterns in a set of words. A basic Trie however has O(n^2) space complexity
making it impractical in practice. It however provides O(max(search_string, length of
longest word)) lookup time making it an optimal approach when space is not an issue.
"""
from __future__ import annotations


class TrieNode:
    def __init__(self) -> None:
        self.nodes: dict[str, TrieNode] = {}  # Mapping from char to TrieNode
        self.is_leaf = False

    def insert_many(self, words: list[str]) -> None:
        """
        Inserts a list of words into the Trie
        :param words: list of string words
        :return: None
        """
        for word in words:
            self.insert(word)

    def insert(self, word: str) -> None:
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

    def merge(self, trie_node: TrieNode) -> None:
        """
        Merge the current instance of TrieNode with the passed instance.
        :param trie_node: the source to be merged.
        """

        for source_node in trie_node.nodes:
            if source_node not in self.nodes:
                self.nodes[source_node] = TrieNode()

            self.nodes[source_node].merge(trie_node.nodes[source_node])

        if trie_node.is_leaf:
            self.is_leaf = True

    def find(self, word: str) -> bool:
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

    def delete(self, word: str) -> None:
        """
        Deletes a word in a Trie
        :param word: word to delete
        :return: None
        """

        def _delete(curr: TrieNode, word: str, index: int) -> bool:
            if index == len(word):
                # If word does not exist
                if not curr.is_leaf:
                    return False
                curr.is_leaf = False
                return len(curr.nodes) == 0
            char = word[index]
            char_node = curr.nodes.get(char)
            # If char not in current trie node
            if not char_node:
                return False
            # Flag to check if node can be deleted
            delete_curr = _delete(char_node, word, index + 1)
            if delete_curr:
                del curr.nodes[char]
                return len(curr.nodes) == 0
            return delete_curr

        _delete(self, word, 0)


def print_words(node: TrieNode, word: str) -> None:
    """
    Prints all the words in a Trie
    :param node: root node of Trie
    :param word: Word variable should be empty at start
    :return: None
    """
    if node.is_leaf:
        print(word, end=" ")

    for key, value in node.nodes.items():
        print_words(value, word + key)


def test_trie() -> bool:
    words = "banana bananas bandana band apple all beast".split()
    root = TrieNode()
    root.insert_many(words)
    # print_words(root, "")
    assert all(root.find(word) for word in words)
    assert root.find("banana")
    assert not root.find("bandanas")
    assert not root.find("apps")
    assert root.find("apple")
    assert root.find("all")
    root.delete("all")
    assert not root.find("all")
    root.delete("banana")
    assert not root.find("banana")
    assert root.find("bananas")

    assert not root.find("new_merged_word")
    assert not root.find("new_merged_word2")
    nodeToMerge = TrieNode()
    nodeToMerge.insert_many(["new_merged_word", "new_merged_word2"])
    root.merge(nodeToMerge)
    assert root.find("new_merged_word")
    assert root.find("new_merged_word2")
    assert root.find("bananas")

    return True


def print_results(msg: str, passes: bool) -> None:
    print(str(msg), "works!" if passes else "doesn't work :(")


def pytests() -> None:
    assert test_trie()


def main() -> None:
    """
    >>> pytests()
    """
    print_results("Testing trie functionality", test_trie())


if __name__ == "__main__":
    main()
