"""Rabin-Karp string search returning all match indices."""

from typing import List


def rabin_karp_search(text: str, pattern: str, base: int = 256, modulus: int = 1_000_000_007) -> List[int]:
    if not pattern:
        return list(range(len(text) + 1))
    if len(pattern) > len(text):
        return []
    h = pow(base, len(pattern) - 1, modulus)
    pattern_hash = 0
    window_hash = 0
    for char_p, char_t in zip(pattern, text):
        pattern_hash = (pattern_hash * base + ord(char_p)) % modulus
        window_hash = (window_hash * base + ord(char_t)) % modulus
    matches: List[int] = []
    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash == window_hash and text[i : i + len(pattern)] == pattern:
            matches.append(i)
        if i + len(pattern) < len(text):
            window_hash = (
                (window_hash - ord(text[i]) * h) * base + ord(text[i + len(pattern)])
            ) % modulus
            if window_hash < 0:
                window_hash += modulus
    return matches
