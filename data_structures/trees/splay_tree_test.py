# the_algorithms/trees/splay_tree_test.py

import unittest
from splay_tree import SplayTree

class TestSplayTree(unittest.TestCase):
    def test_insert_and_root(self):
        """Test basic insertion and verify the splayed node becomes the root."""
        tree = SplayTree()
        keys = [50, 30, 70, 20, 40]
        for key in keys:
            tree.insert(key)
            self.assertEqual(tree.root.key, key, f"Expected {key} to be the root after insertion.")

    def test_search_and_splay(self):
        """Test searching for an existing key and verify it is splayed to the root."""
        tree = SplayTree()
        keys = [50, 30, 70, 20, 40, 60, 80]
        for key in keys:
            tree.insert(key)

        # Search for 20. It should become the new root.
        found_node = tree.search(20)
        self.assertIsNotNone(found_node)
        self.assertEqual(found_node.key, 20)
        self.assertEqual(tree.root.key, 20, "20 should be the root after search.")

        # Search for a key that doesn't exist (99). The last accessed node (e.g., 80) should be splayed.
        _ = tree.search(99)
        # The exact last accessed node depends on the tree structure, but it should not be the original root (50)
        self.assertNotEqual(tree.root.key, 50, "Root should change after unsuccessful search.")

    def test_empty_tree(self):
        """Test operations on an empty tree."""
        tree = SplayTree()
        self.assertIsNone(tree.search(10))
        self.assertIsNone(tree.root)
        
        tree.insert(10)
        self.assertEqual(tree.root.key, 10)

if __name__ == '__main__':
    unittest.main()
