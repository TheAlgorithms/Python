#  Created by: Ramy-Badr-Ahmed (https://github.com/Ramy-Badr-Ahmed)
#  in Pull Request: #11554
#  https://github.com/TheAlgorithms/Python/pull/11554
#
#  Please mention me (@Ramy-Badr-Ahmed) in any issue or pull request
#  addressing bugs/corrections to this file.
#  Thank you!

import unittest

from data_structures.suffix_tree.suffix_tree import SuffixTree


class TestSuffixTree(unittest.TestCase):
    def setUp(self) -> None:
        """Set up the initial conditions for each test."""
        self.text = "banana"
        self.suffix_tree = SuffixTree(self.text)

    def test_search_existing_patterns(self) -> None:
        """Test searching for patterns that exist in the suffix tree."""
        patterns = ["ana", "ban", "na"]
        for pattern in patterns:
            with self.subTest(pattern=pattern):
                assert self.suffix_tree.search(
                    pattern
                ), f"Pattern '{pattern}' should be found."

    def test_search_non_existing_patterns(self) -> None:
        """Test searching for patterns that do not exist in the suffix tree."""
        patterns = ["xyz", "apple", "cat"]
        for pattern in patterns:
            with self.subTest(pattern=pattern):
                assert not self.suffix_tree.search(
                    pattern
                ), f"Pattern '{pattern}' should not be found."

    def test_search_empty_pattern(self) -> None:
        """Test searching for an empty pattern."""
        assert self.suffix_tree.search(""), "An empty pattern should be found."

    def test_search_full_text(self) -> None:
        """Test searching for the full text."""
        assert self.suffix_tree.search(
            self.text
        ), "The full text should be found in the suffix tree."

    def test_search_substrings(self) -> None:
        """Test searching for substrings of the full text."""
        substrings = ["ban", "ana", "a", "na"]
        for substring in substrings:
            with self.subTest(substring=substring):
                assert self.suffix_tree.search(
                    substring
                ), f"Substring '{substring}' should be found."


if __name__ == "__main__":
    unittest.main()
