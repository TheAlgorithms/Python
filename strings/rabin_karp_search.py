"""
Rabin-Karp String Searching Algorithm

An efficient string searching algorithm that uses hashing to find patterns in text.
It's particularly useful for searching multiple patterns simultaneously.

Reference: https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm

Time Complexity:
    - Average: O(n + m) where n is text length and m is pattern length
    - Worst: O(n * m) with many hash collisions
Space Complexity: O(1)
"""


def rabin_karp_search(text: str, pattern: str, prime: int = 101) -> list[int]:
    """
    Find all occurrences of pattern in text using Rabin-Karp algorithm.

    Args:
        text: The text to search in
        pattern: The pattern to search for
        prime: A prime number for hash calculation (default: 101)

    Returns:
        List of starting indices where pattern is found

    Examples:
    >>> rabin_karp_search("AABAACAADAABAABA", "AABA")
    [0, 9, 12]
    >>> rabin_karp_search("hello world", "world")
    [6]
    >>> rabin_karp_search("abcabcabc", "abc")
    [0, 3, 6]
    >>> rabin_karp_search("test", "xyz")
    []
    >>> rabin_karp_search("", "pattern")
    []
    >>> rabin_karp_search("text", "")
    []
    >>> rabin_karp_search("aaaa", "aa")
    [0, 1, 2]
    >>> rabin_karp_search("The quick brown fox", "quick")
    [4]
    """
    if not text or not pattern or len(pattern) > len(text):
        return []

    n = len(text)
    m = len(pattern)
    d = 256
    pattern_hash = 0
    text_hash = 0
    h = 1
    results: list[int] = []

    for i in range(m - 1):
        h = (h * d) % prime

    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % prime
        text_hash = (d * text_hash + ord(text[i])) % prime

    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            if text[i : i + m] == pattern:
                results.append(i)

        if i < n - m:
            text_hash = (d * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if text_hash < 0:
                text_hash += prime

    return results


def rabin_karp_multiple_patterns(
    text: str, patterns: list[str], prime: int = 101
) -> dict[str, list[int]]:
    """
    Find all occurrences of multiple patterns in text using Rabin-Karp.

    This is more efficient than running single pattern search multiple times
    when searching for many patterns.

    Args:
        text: The text to search in
        patterns: List of patterns to search for
        prime: A prime number for hash calculation

    Returns:
        Dictionary mapping each pattern to list of indices where it's found

    Examples:
    >>> result = rabin_karp_multiple_patterns("abcabcabc", ["abc", "cab", "bca"])
    >>> result["abc"]
    [0, 3, 6]
    >>> result["cab"]
    [2, 5]
    >>> result["bca"]
    [1, 4]
    >>> rabin_karp_multiple_patterns("hello", ["hi", "bye"])
    {'hi': [], 'bye': []}
    """
    if not text or not patterns:
        return {pattern: [] for pattern in patterns}

    results: dict[str, list[int]] = {pattern: [] for pattern in patterns}

    for pattern in patterns:
        results[pattern] = rabin_karp_search(text, pattern, prime)

    return results


def rabin_karp_with_wildcard(text: str, pattern: str, wildcard: str = "?") -> list[int]:
    """
    Rabin-Karp variant that supports a single wildcard character.

    The wildcard character matches any single character.

    Args:
        text: The text to search in
        pattern: The pattern with optional wildcard characters
        wildcard: The wildcard character (default: '?')

    Returns:
        List of starting indices where pattern matches

    Examples:
    >>> rabin_karp_with_wildcard("abcdefgh", "c?e")
    [2]
    >>> rabin_karp_with_wildcard("hello world", "w?rld")
    [6]
    >>> rabin_karp_with_wildcard("test", "t?st")
    [0]
    >>> rabin_karp_with_wildcard("aaaa", "a?a")
    [0, 1]
    """
    if not text or not pattern or len(pattern) > len(text):
        return []

    n = len(text)
    m = len(pattern)
    results: list[int] = []

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if pattern[j] != wildcard and text[i + j] != pattern[j]:
                match = False
                break
        if match:
            results.append(i)

    return results


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    text = "AABAACAADAABAABA"
    pattern = "AABA"
    print(f"Text: {text}")
    print(f"Pattern: {pattern}")
    print(f"Pattern found at indices: {rabin_karp_search(text, pattern)}")

    print("\nMultiple pattern search:")
    patterns = ["AAB", "AAC", "AAD"]
    results = rabin_karp_multiple_patterns(text, patterns)
    for pat, indices in results.items():
        print(f"  '{pat}' found at: {indices}")

    print("\nWildcard search:")
    print(f"Pattern 'A?BA' found at: {rabin_karp_with_wildcard(text, 'A?BA')}")
