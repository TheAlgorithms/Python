"""Rabin-Karp rolling hash algorithm for substring search.

Implements the classic Rabin-Karp algorithm using a rolling hash to find
all occurrences of a pattern in a text in O(n) average time.

The algorithm uses a simple polynomial rolling hash with modulo prime to
avoid overflow. It works well for ASCII/Unicode strings.

References:
- Rabin, M. O., & Karp, R. M. (1987). Algorithms for pattern matching.
"""
from typing import List


def rabin_karp(text: str, pattern: str) -> List[int]:
    """Return starting indices of pattern in text using rolling hash.

    Args:
        text: The text to search within.
        pattern: The pattern to find.

    Returns:
        List of starting indices (0-based) where pattern occurs.

    Example:
        >>> rabin_karp("abracadabra", "abra")
        [0, 7]
    """
    # Edge cases
    if pattern == "":
        # By convention, empty pattern matches at each position plus one
        return list(range(len(text) + 1))
    if len(pattern) > len(text):
        return []

    # Rolling hash parameters
    base = 256  # number of possible character values (ASCII/extended)
    prime = 101  # a small prime for modulus
    m, n = len(pattern), len(text)

    # Precompute base^(m-1) mod prime for rolling removal
    h = 1
    for _ in range(m - 1):
        h = (h * base) % prime

    # Compute initial hash values
    pattern_hash = 0
    window_hash = 0
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        window_hash = (base * window_hash + ord(text[i])) % prime

    matches: List[int] = []
    # Slide the window over text
    for i in range(n - m + 1):
        if pattern_hash == window_hash:
            # Double-check to avoid hash collisions
            if text[i:i + m] == pattern:
                matches.append(i)
        if i < n - m:
            # Roll: remove leading char, add trailing char
            window_hash = (base * (window_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if window_hash < 0:
                window_hash += prime
    return matches


def demo() -> None:
    """Run a simple demonstration."""
    text = "abracadabra"
    pattern = "abra"
    indices = rabin_karp(text, pattern)
    print(f"Pattern '{pattern}' found at positions: {indices}")


if __name__ == "__main__":
    demo()
