import unittest
from data_structures.suffix_tree.build_suffix_tree import SuffixTree


class TestSuffixTree(unittest.TestCase):
    def setUp(self) -> None:
        """Set up the initial conditions for each test."""
        self.text = "banana"
        self.suffix_tree = SuffixTree(self.text)

    def test_search_existing_patterns(self):
        """Test searching for patterns that exist in the suffix tree."""
        patterns = ["ana", "ban", "na"]
        for pattern in patterns:
            with self.subTest(pattern = pattern):
                self.assertTrue(self.suffix_tree.search(pattern), f"Pattern '{pattern}' should be found.")

    def test_search_non_existing_patterns(self):
        """Test searching for patterns that do not exist in the suffix tree."""
        patterns = ["xyz", "apple", "cat"]
        for pattern in patterns:
            with self.subTest(pattern = pattern):
                self.assertFalse(self.suffix_tree.search(pattern), f"Pattern '{pattern}' should not be found.")

    def test_search_empty_pattern(self):
        """Test searching for an empty pattern."""
        self.assertTrue(self.suffix_tree.search(""), "An empty pattern should be found.")

    def test_search_full_text(self):
        """Test searching for the full text."""
        self.assertTrue(self.suffix_tree.search(self.text), "The full text should be found in the suffix tree.")

    def test_search_substrings(self):
        """Test searching for substrings of the full text."""
        substrings = ["ban", "ana", "a", "na"]
        for substring in substrings:
            with self.subTest(substring = substring):
                self.assertTrue(self.suffix_tree.search(substring), f"Substring '{substring}' should be found.")


if __name__ == "__main__":
    unittest.main()
