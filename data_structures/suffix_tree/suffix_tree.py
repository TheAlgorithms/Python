#  Created by: Ramy-Badr-Ahmed (https://github.com/Ramy-Badr-Ahmed)
#  in Pull Request: #11554
#  https://github.com/TheAlgorithms/Python/pull/11554
#
#  Please mention me (@Ramy-Badr-Ahmed) in any issue or pull request
#  addressing bugs/corrections to this file.
#  Thank you!

from data_structures.suffix_tree.suffix_tree_node import SuffixTreeNode


class SuffixTree:
    def __init__(self, text: str) -> None:
        """
        Initializes the suffix tree with the given text.

        Args:
            text (str): The text for which the suffix tree is to be built.
        """
        self.text: str = text
        self.root: SuffixTreeNode = SuffixTreeNode()
        self.build_suffix_tree()

    def build_suffix_tree(self) -> None:
        """
        Builds the suffix tree for the given text by adding all suffixes.
        """
        text = self.text
        n = len(text)
        for i in range(n):
            suffix = text[i:]
            self._add_suffix(suffix, i)

    def _add_suffix(self, suffix: str, index: int) -> None:
        """
        Adds a suffix to the suffix tree.

        Args:
            suffix (str): The suffix to add.
            index (int): The starting index of the suffix in the original text.
        """
        node = self.root
        for char in suffix:
            if char not in node.children:
                node.children[char] = SuffixTreeNode()
            node = node.children[char]
        node.is_end_of_string = True
        node.start = index
        node.end = index + len(suffix) - 1

    def search(self, pattern: str) -> bool:
        """
        Searches for a pattern in the suffix tree.

        Args:
            pattern (str): The pattern to search for.

        Returns:
            bool: True if the pattern is found, False otherwise.
        """
        node = self.root
        for char in pattern:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
