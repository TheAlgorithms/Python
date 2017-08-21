'''
A Trie/Prefix Tree is a kind of search tree used to provide quick lookup
of words/patterns in a set of words. A basic Trie however has O(n^2) space complexity
making it impractical in practice. It however provides O(max(search_string, length of longest word)) lookup
time making it an optimal approach when space is not an issue.
'''


class TrieNode:
    def __init__(self):
        self.nodes = dict() # Mapping from char to TrieNode

    def insert_many(self, words: [str]):
        for word in words:
            self.insert(word)

    def insert(self, word: str):
        pass

    def find(self, word: str) -> bool:
        pass