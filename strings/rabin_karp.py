"""
Rabin–Karp String Matching Algorithm
https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm
"""

from typing import Dict, Iterable, List, Tuple

MOD: int = 1_000_000_007
BASE: int = 257


def rabin_karp(text: str, pattern: str) -> List[int]:
    """
    Return all starting indices where `pattern` appears in `text`.

    >>> rabin_karp("abracadabra", "abra")
    [0, 7]
    >>> rabin_karp("aaaaa", "aa")  # overlapping matches
    [0, 1, 2, 3]
    >>> rabin_karp("hello", "")  # empty pattern matches everywhere
    [0, 1, 2, 3, 4, 5]
    >>> rabin_karp("", "abc")
    []
    """
    n, m = len(text), len(pattern)
    if m == 0:
        return list(range(n + 1))
    if n < m:
        return []

    # Precompute BASE^(m-1) % MOD
    power = pow(BASE, m - 1, MOD)

    # Hashes for pattern and first window of text
    hp = ht = 0
    for i in range(m):
        hp = (hp * BASE + ord(pattern[i])) % MOD
        ht = (ht * BASE + ord(text[i])) % MOD

    results: List[int] = []

    for i in range(n - m + 1):
        if hp == ht and text[i : i + m] == pattern:
            results.append(i)

        if i < n - m:
            # sliding window: remove left char, add right char
            left = (ord(text[i]) * power) % MOD
            ht = (ht - left) % MOD
            ht = (ht * BASE + ord(text[i + m])) % MOD

    return results


def rabin_karp_multi(text: str, patterns: Iterable[str]) -> Dict[str, List[int]]:
    """
    Multiple-pattern Rabin–Karp.
    Groups patterns by length and scans text once.

    >>> rabin_karp_multi("abracadabra", ["abra", "bra", "cad"])
    {'abra': [0, 7], 'bra': [1, 8], 'cad': [4]}
    >>> rabin_karp_multi("aaaaa", ["aa", "aaa"])
    {'aa': [0, 1, 2, 3], 'aaa': [0, 1, 2]}
    """
    patterns = list(patterns)
    result: Dict[str, List[int]] = {p: [] for p in patterns}

    # Group patterns by length
    groups: Dict[int, List[str]] = {}
    for p in patterns:
        groups.setdefault(len(p), []).append(p)

    for length, group in groups.items():
        if length == 0:
            for p in group:
                result[p] = list(range(len(text) + 1))
            continue

        # Precompute pattern hashes
        p_hash: Dict[int, List[str]] = {}
        for p in group:
            h = 0
            for c in p:
                h = (h * BASE + ord(c)) % MOD
            p_hash.setdefault(h, []).append(p)

        # Scan text using sliding window hashing
        if len(text) < length:
            continue

        power = pow(BASE, length - 1, MOD)
        h = 0
        for i in range(length):
            h = (h * BASE + ord(text[i])) % MOD

        for i in range(len(text) - length + 1):
            if h in p_hash:
                window = text[i : i + length]
                for p in p_hash[h]:
                    if window == p:
                        result[p].append(i)

            if i < len(text) - length:
                left = (ord(text[i]) * power) % MOD
                h = (h - left) % MOD
                h = (h * BASE + ord(text[i + length])) % MOD

    return result
