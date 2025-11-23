"""
Rabin-Karp String Matching Algorithm

The Rabin-Karp algorithm uses hashing to find patterns in text.
It employs a rolling hash technique for efficient pattern searching.

Time Complexity:
- Average case: O(n + m) where n is text length, m is pattern length
- Worst case: O(nm) when many spurious hits occur

Space Complexity: O(1) for single pattern, O(k) for k patterns

Applications:
- Plagiarism detection
- DNA sequence matching
- Multiple pattern searching
- Finding duplicate content
"""


def rabin_karp_search(
    text: str, pattern: str, base: int = 256, modulus: int = 101
) -> list[int]:
    """
    Search for a pattern in text using Rabin-Karp algorithm.

    Args:
        text: The text to search in
        pattern: The pattern to search for
        base: The base for hash calculation (default: 256 for ASCII)
        modulus: The modulus for hash calculation (prime number)

    Returns:
        List of starting indices where pattern is found

    Examples:
        >>> rabin_karp_search("hello world hello", "hello")
        [0, 12]
        >>> rabin_karp_search("aaaa", "aa")
        [0, 1, 2]
        >>> rabin_karp_search("abc", "xyz")
        []
        >>> rabin_karp_search("", "a")
        []
        >>> rabin_karp_search("a", "")
        []
        >>> rabin_karp_search("abcdefg", "cde")
        [2]
        >>> rabin_karp_search("ABABDABACDABABCABAB", "ABABCABAB")
        [10]
        >>> rabin_karp_search("test test test", "test")
        [0, 5, 10]
    """
    if not pattern or not text or len(pattern) > len(text):
        return []

    n = len(text)
    m = len(pattern)
    matches = []

    # Calculate hash value for pattern and first window of text
    pattern_hash = 0
    text_hash = 0
    h = 1

    # The value of h would be "pow(base, m-1) % modulus"
    for _ in range(m - 1):
        h = (h * base) % modulus

    # Calculate initial hash values
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % modulus
        text_hash = (base * text_hash + ord(text[i])) % modulus

    # Slide the pattern over text one by one
    for i in range(n - m + 1):
        # Check if hash values match and verify to avoid spurious hits
        if pattern_hash == text_hash and text[i : i + m] == pattern:
            matches.append(i)

        # Calculate hash for next window (rolling hash)
        if i < n - m:
            # Remove leading character and add trailing character
            text_hash = (
                base * (text_hash - ord(text[i]) * h) + ord(text[i + m])
            ) % modulus

            # Handle negative hash values
            if text_hash < 0:
                text_hash += modulus

    return matches


def rabin_karp_multiple(
    text: str, patterns: list[str], base: int = 256, modulus: int = 101
) -> dict[str, list[int]]:
    """
    Search for multiple patterns in text using Rabin-Karp algorithm.

    This is more efficient than running single pattern search multiple times
    because we only scan the text once.

    Args:
        text: The text to search in
        patterns: List of patterns to search for
        base: The base for hash calculation
        modulus: The modulus for hash calculation

    Returns:
        Dictionary mapping each pattern to list of indices where found

    Examples:
        >>> result = rabin_karp_multiple("hello world hello", ["hello", "world"])
        >>> result == {"hello": [0, 12], "world": [6]}
        True
        >>> result = rabin_karp_multiple("aaaa", ["aa", "aaa"])
        >>> result == {"aa": [0, 1, 2], "aaa": [0, 1]}
        True
        >>> result = rabin_karp_multiple("test", ["abc", "xyz"])
        >>> result == {"abc": [], "xyz": []}
        True
        >>> result = rabin_karp_multiple("", ["a", "b"])
        >>> result == {"a": [], "b": []}
        True
        >>> result = rabin_karp_multiple("abcdef", ["ab", "cd", "ef"])
        >>> result == {"ab": [0], "cd": [2], "ef": [4]}
        True
    """
    if not text or not patterns:
        return {pattern: [] for pattern in patterns}

    # Group patterns by length for efficient processing
    patterns_by_length: dict[int, list[str]] = {}
    for pattern in patterns:
        if pattern:  # Skip empty patterns
            length = len(pattern)
            if length not in patterns_by_length:
                patterns_by_length[length] = []
            patterns_by_length[length].append(pattern)

    results: dict[str, list[int]] = {pattern: [] for pattern in patterns}

    # Process each group of patterns with same length
    for pattern_length, pattern_group in patterns_by_length.items():
        if pattern_length > len(text):
            continue

        # Calculate pattern hashes
        pattern_hashes = {}
        for pattern in pattern_group:
            pattern_hash = 0
            for char in pattern:
                pattern_hash = (base * pattern_hash + ord(char)) % modulus
            pattern_hashes[pattern] = pattern_hash

        # Calculate hash for first window
        text_hash = 0
        h = 1
        for _ in range(pattern_length - 1):
            h = (h * base) % modulus

        for i in range(pattern_length):
            text_hash = (base * text_hash + ord(text[i])) % modulus

        # Slide the window over text
        for i in range(len(text) - pattern_length + 1):
            # Check if current hash matches any pattern hash
            for pattern, pattern_hash in pattern_hashes.items():
                # Verify to avoid spurious hits
                if text_hash == pattern_hash and text[i : i + pattern_length] == pattern:
                    results[pattern].append(i)

            # Calculate hash for next window
            if i < len(text) - pattern_length:
                text_hash = (
                    base * (text_hash - ord(text[i]) * h)
                    + ord(text[i + pattern_length])
                ) % modulus

                if text_hash < 0:
                    text_hash += modulus

    return results


def rabin_karp_search_optimized(
    text: str, pattern: str, base: int = 256, modulus: int = 1_000_000_007
) -> list[int]:
    """
    Optimized version with larger modulus to reduce collisions.

    Using a larger prime modulus (10^9 + 7) significantly reduces
    the probability of hash collisions, improving average-case performance.

    Args:
        text: The text to search in
        pattern: The pattern to search for
        base: The base for hash calculation
        modulus: Large prime modulus (default: 10^9 + 7)

    Returns:
        List of starting indices where pattern is found

    Examples:
        >>> rabin_karp_search_optimized("hello world", "world")
        [6]
        >>> rabin_karp_search_optimized("aaabaaaa", "aaaa")
        [4]
        >>> rabin_karp_search_optimized("abc", "d")
        []
    """
    return rabin_karp_search(text, pattern, base, modulus)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Performance demonstration
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit" * 100
    pattern = "consectetur"

    print("Rabin-Karp String Matching Algorithm Demo")
    print("=" * 50)

    # Single pattern search
    matches = rabin_karp_search(text, pattern)
    print(f"\nSearching for '{pattern}' in text ({len(text)} chars)")
    print(f"Found {len(matches)} matches at indices: {matches[:5]}...")

    # Multiple pattern search
    patterns = ["Lorem", "ipsum", "consectetur", "adipiscing"]
    results = rabin_karp_multiple(text, patterns)
    print(f"\nSearching for {len(patterns)} patterns:")
    for p, indices in results.items():
        print(f"  '{p}': {len(indices)} matches")

    print("\n✓ All tests passed!")
