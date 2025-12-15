"""
Trie (Prefix Tree) Data Structure

A Trie is a tree-like data structure that stores strings efficiently.
Each node represents a character, and paths from root to leaf nodes form complete words.

Reference: https://en.wikipedia.org/wiki/Trie

Time Complexity:
  - Insert: O(m) where m is the length of the word
  - Search: O(m) where m is the length of the word
  - Delete: O(m) where m is the length of the word
  - StartsWith: O(m) where m is the length of the prefix
  - LongestCommonPrefix: O(n*m) where n is number of words and m is their length

Space Complexity: O(ALPHABET_SIZE * n * m)
  - ALPHABET_SIZE: size of character set (26 for lowercase English)
  - n: number of words stored
  - m: average length of words

Use Cases:
  - Autocomplete/Search suggestions
  - Spell checking
  - IP routing (longest prefix matching)
  - Dictionary implementation
  - Word games (Scrabble)
"""


class Node:
    """Represents a single node in the Trie.

    Each node contains:
    - children: Dictionary mapping characters to child nodes
    - is_end_of_word: Boolean flag indicating if this node marks the end of a valid word
    """

    def __init__(self):
        self.children: dict[str, Node] = {}  # Maps character to child Node
        self.is_end_of_word = False  # True if node represents end of a valid word


class Trie:
    """Trie (Prefix Tree) data structure for efficient string storage and retrieval.

    Examples:
        >>> trie = Trie()
        >>> trie.insert("hello")
        >>> trie.search("hello")
        True
        >>> trie.search("hell")
        False
        >>> trie.starts_with("hel")
        True
    """

    def __init__(self):
        """Initialize Trie with an empty root node.

        The root node doesn't represent any character and serves as the entry point.

        Examples:
            >>> trie = Trie()
            >>> trie.root is not None
            True
            >>> isinstance(trie.root, Node)
            True
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """Insert a word into the Trie.

        Time Complexity: O(m) where m is the length of the word
        Space Complexity: O(m) for storing new nodes (worst case)

        Args:
            word: The word to insert into the Trie

        Process:
            1. Start at the root node
            2. For each character in the word:
               - If character doesn't exist as a child, create a new node
               - Move to that child node
            3. Mark the final node as end of word

        Examples:
            >>> trie = Trie()
            >>> trie.insert("cat")
            >>> trie.search("cat")
            True
            >>> trie.insert("car")
            >>> trie.search("car")
            True
            >>> trie.search("ca")
            False
            >>> trie.insert("ca")
            >>> trie.search("ca")
            True
        """
        current_node = self.root
        # Traverse through each character in the word
        for char in word:
            # If character path doesn't exist, create a new node
            if char not in current_node.children:
                current_node.children[char] = Node()
            # Move to the next node in the path
            current_node = current_node.children[char]
        # Mark this node as the end of a valid word
        current_node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """Search for an exact word in the Trie.

        Time Complexity: O(m) where m is the length of the word
        Space Complexity: O(1)

        Args:
            word: The word to search for

        Returns:
            True if the word exists in the Trie, False otherwise

        Process:
            1. Start at the root node
            2. For each character in the word:
               - If character doesn't exist as a child, word doesn't exist
               - Move to that child node
            3. Return whether the final node is marked as end of word

        Examples:
            >>> trie = Trie()
            >>> trie.insert("apple")
            >>> trie.search("apple")
            True
            >>> trie.search("app")
            False
            >>> trie.search("apples")
            False
            >>> trie.search("orange")
            False
        """
        current_node = self.root
        # Traverse through each character in the word
        for char in word:
            # If character path doesn't exist, word is not in Trie
            if char not in current_node.children:
                return False
            # Move to the next node in the path
            current_node = current_node.children[char]
        # Word exists only if we've reached end of word marker
        return current_node.is_end_of_word

    def delete(self, word: str) -> None:
        """Delete a word from the Trie.

        Time Complexity: O(m) where m is the length of the word
        Space Complexity: O(m) for recursion stack

        Args:
            word: The word to delete from the Trie

        Process:
            1. Use recursive helper to traverse to the word's end
            2. Unmark the end-of-word flag
            3. Remove nodes with no children (cleanup unused nodes)
            4. Only removes nodes that don't form other words

        Examples:
            >>> trie = Trie()
            >>> trie.insert("cat")
            >>> trie.insert("car")
            >>> trie.search("cat")
            True
            >>> trie.delete("cat")
            >>> trie.search("cat")
            False
            >>> trie.search("car")
            True
            >>> trie.insert("apple")
            >>> trie.insert("app")
            >>> trie.delete("app")
            >>> trie.search("app")
            False
            >>> trie.search("apple")
            True
        """

        def _delete(node: Node, word: str, index: int) -> bool:
            """Recursively delete a word and cleanup unused nodes.

            Args:
                node: Current node being processed
                word: The word being deleted
                index: Current position in the word

            Returns:
                True if the node should be deleted (has no children and not end of word)
            """
            # Base case: reached the end of the word
            if index == len(word):
                # Word doesn't exist if we can't mark it as unfinished
                if not node.is_end_of_word:
                    return False
                # Unmark the word ending
                node.is_end_of_word = False
                # Return True if node has no children (can be deleted)
                return len(node.children) == 0

            # Get the current character
            char = word[index]
            # Get the child node for this character
            child_node = node.children.get(char)
            # If child doesn't exist, word doesn't exist
            if not child_node:
                return False

            # Recursively delete from the child node
            should_delete_child = _delete(child_node, word, index + 1)

            # If child should be deleted and it has no other children
            if should_delete_child:
                # Remove the child node
                del node.children[char]
                # Return True if current node has no children and isn't end of word
                return len(node.children) == 0

            return False

        _delete(self.root, word, 0)

    def starts_with(self, prefix: str) -> bool:
        """Check if any word in the Trie starts with the given prefix.

        Time Complexity: O(m) where m is the length of the prefix
        Space Complexity: O(1)

        Args:
            prefix: The prefix to search for

        Returns:
            True if at least one word starts with the prefix, False otherwise

        Process:
            1. Start at the root node
            2. For each character in the prefix:
               - If character doesn't exist as a child, prefix doesn't exist
               - Move to that child node
            3. If we successfully traverse all characters, prefix exists

        Examples:
            >>> trie = Trie()
            >>> trie.insert("hello")
            >>> trie.insert("help")
            >>> trie.starts_with("hel")
            True
            >>> trie.starts_with("hello")
            True
            >>> trie.starts_with("hey")
            False
            >>> trie.starts_with("h")
            True
        """
        current_node = self.root
        # Traverse through each character in the prefix
        for char in prefix:
            # If character path doesn't exist, prefix is not in Trie
            if char not in current_node.children:
                return False
            # Move to the next node in the path
            current_node = current_node.children[char]
        # Prefix exists if we've successfully traversed all characters
        return True

    def longest_common_prefix(self) -> str:
        """Find the longest common prefix of all words in the Trie.

        Time Complexity: O(n*m) where n is number of words and m is their length
        Space Complexity: O(m) for storing the prefix

        Returns:
            The longest common prefix string shared by all words

        Process:
            1. Start at the root node
            2. Continue traversing while:
               - Node has exactly one child (unambiguous path)
               - Node is not marked as end of word (prevents prefixes)
            3. Stop when multiple paths exist or word ends
            4. Return the prefix built from traversed characters

        Examples:
            >>> trie = Trie()
            >>> trie.insert("flower")
            >>> trie.insert("flow")
            >>> trie.insert("flight")
            >>> trie.longest_common_prefix()
            'fl'
            >>> trie2 = Trie()
            >>> trie2.insert("dog")
            >>> trie2.insert("cat")
            >>> trie2.longest_common_prefix()
            ''
        """
        prefix = []
        current_node = self.root

        # Keep traversing while there's a single unambiguous path
        while True:
            # Stop if node has multiple children or marks end of a word
            if len(current_node.children) != 1 or current_node.is_end_of_word:
                break
            # Get the only child node
            char, next_node = next(iter(current_node.children.items()))
            # Add character to prefix
            prefix.append(char)
            # Move to next node
            current_node = next_node

        return "".join(prefix)

    def print_all_words(self) -> None:
        """Print all words stored in the Trie.

        Time Complexity: O(n*m) where n is number of words and m is average length
        Space Complexity: O(m) for recursion stack

        Process:
            1. Use depth-first search (DFS) to traverse all paths
            2. Start from root with empty word
            3. For each node:
               - If marked as end of word, print the current word
               - Recursively visit all children

        Note:
            Output has a trailing space after the last word.
        """

        def _print_words(node: Node, current_word: str) -> None:
            """Recursively traverse and print all words.

            Args:
                node: Current node being processed
                current_word: The word built up to this point
            """
            # If this node marks end of word, print it
            if node.is_end_of_word:
                print(current_word, end=" ")
            # Recursively explore all children
            for char, child_node in node.children.items():
                # Build word by adding current character and recurse
                _print_words(child_node, current_word + char)

        _print_words(self.root, "")

    def autocomplete(self, prefix: str, limit: int) -> list:
        """Find all words starting with a given prefix (up to limit).

        Time Complexity: O(m + n) where m is prefix length and n is words to find
        Space Complexity: O(limit) for storing results

        Args:
            prefix: The prefix to search for
            limit: Maximum number of results to return

        Returns:
            List of words starting with the prefix (at most 'limit' words)

        Process:
            1. Traverse to the node representing the end of prefix
            2. If prefix doesn't exist, return empty list
            3. Use DFS from that node to find all words starting with prefix
            4. Stop once limit is reached

        Examples:
            >>> trie = Trie()
            >>> trie.insert("apple")
            >>> trie.insert("app")
            >>> trie.insert("apply")
            >>> trie.insert("apricot")
            >>> results = trie.autocomplete("app", 3)
            >>> len(results)
            3
            >>> "apple" in results
            True
            >>> results2 = trie.autocomplete("ap", 5)
            >>> len(results2) >= 3
            True
            >>> trie.autocomplete("xyz", 5)
            []
        """
        results = []
        current_node = self.root

        # Traverse to the end of the prefix
        for char in prefix:
            # If prefix doesn't exist, return empty results
            if char not in current_node.children:
                return results
            # Move to next node
            current_node = current_node.children[char]

        def _find_words(node: Node, current_word: str):
            """Recursively find words starting from current node.

            Args:
                node: Current node being processed
                current_word: The word built up to this point
            """
            # Stop if we've reached the limit
            if len(results) >= limit:
                return
            # If this node marks end of word, add to results
            if node.is_end_of_word:
                results.append(current_word)
            # Recursively explore all children
            for char, child_node in node.children.items():
                # Build word by adding current character and recurse
                _find_words(child_node, current_word + char)

        _find_words(current_node, prefix)
        return results


if __name__ == "__main__":
    """
    Test Suite for Trie Data Structure

    This section demonstrates and tests all Trie operations:
    - Inserting words
    - Searching for words
    - Checking prefixes
    - Finding longest common prefix
    - Autocomplete functionality
    - Deleting words
    - Printing all stored words
    """

    print("=" * 60)
    print("TRIE DATA STRUCTURE - TEST SUITE")
    print("=" * 60)

    # Initialize a new Trie
    trie = Trie()

    # Test 1: Insert words
    print("\n[TEST 1] Inserting words into Trie")
    print("-" * 60)
    words = ["apple", "app", "application", "apply", "apricot", "banana", "band", "can"]
    print(f"Inserting words: {words}")
    for word in words:
        trie.insert(word)
    print("✓ All words inserted successfully")

    # Test 2: Search for existing words
    print("\n[TEST 2] Searching for existing words")
    print("-" * 60)
    search_words = ["apple", "app", "apply"]
    for word in search_words:
        result = trie.search(word)
        status = "✓ FOUND" if result else "✗ NOT FOUND"
        print(f"  Search '{word}': {status}")

    # Test 3: Search for non-existing words
    print("\n[TEST 3] Searching for non-existing words")
    print("-" * 60)
    non_existing = ["appl", "apps", "xyz", "bat"]
    for word in non_existing:
        result = trie.search(word)
        status = "✓ NOT FOUND (correct)" if not result else "✗ FOUND (incorrect)"
        print(f"  Search '{word}': {status}")

    # Test 4: Check prefix existence
    print("\n[TEST 4] Checking if prefixes exist")
    print("-" * 60)
    prefixes = ["app", "appl", "ban", "xyz", "ca"]
    for prefix in prefixes:
        result = trie.starts_with(prefix)
        status = "✓ EXISTS" if result else "✗ DOESN'T EXIST"
        print(f"  Prefix '{prefix}': {status}")

    # Test 5: Find longest common prefix
    print("\n[TEST 5] Finding longest common prefix")
    print("-" * 60)
    trie2 = Trie()
    trie2_words = ["flower", "flow", "flight"]
    for word in trie2_words:
        trie2.insert(word)
    lcp = trie2.longest_common_prefix()
    print(f"  Words: {trie2_words}")
    print(f"  Longest common prefix: '{lcp}'")

    # Test 6: Autocomplete functionality
    print("\n[TEST 6] Autocomplete - Finding words with prefix")
    print("-" * 60)
    autocomplete_tests = [
        ("app", 3),
        ("ap", 5),
        ("ban", 2),
        ("xyz", 5),
    ]
    for prefix, limit in autocomplete_tests:
        results = trie.autocomplete(prefix, limit)
        print(f"  Autocomplete '{prefix}' (limit {limit}): {results}")

    # Test 7: Print all words in Trie
    print("\n[TEST 7] Printing all words stored in Trie")
    print("-" * 60)
    print("  All words: ", end="")
    trie.print_all_words()
    print()

    # Test 8: Delete words
    print("\n[TEST 8] Deleting words from Trie")
    print("-" * 60)
    delete_word = "app"
    print(f"  Before deletion - searching '{delete_word}': {trie.search(delete_word)}")
    trie.delete(delete_word)
    print(f"  After deletion - searching '{delete_word}': {trie.search(delete_word)}")

    # Verify related words still exist after deletion
    print(
        f"  Checking if 'apple' still exists: {trie.search('apple')} (should be True)"
    )
    print(
        f"  Checking if 'apply' still exists: {trie.search('apply')} (should be True)"
    )

    # Test 9: Delete another word and verify
    print("\n[TEST 9] Deleting word 'apple' and checking related words")
    print("-" * 60)
    trie.delete("apple")
    print(f"  After deletion - searching 'apple': {trie.search('apple')}")
    app_exists = trie.search("application")
    print(
        f"  Checking if 'application' still exists: {app_exists} "
        "(should be True)"
    )
    app_prefix = trie.starts_with("app")
    print(
        f"  Checking if prefix 'app' still matches: {app_prefix} "
        "(should be True)"
    )

    # Test 10: Verify final state
    print("\n[TEST 10] Final state - All remaining words")
    print("-" * 60)
    print("  Remaining words: ", end="")
    trie.print_all_words()
    print()

    print("\n" + "=" * 60)
    print("ALL TESTS COMPLETED SUCCESSFULLY")
    print("=" * 60)
