def build_suffix_array(s: str) -> list[int]:
    # Append a sentinel that is lexicographically smaller than all other characters
    s += "\0"
    n = len(s)
    # Initial ranking by character code
    ranks = [ord(c) for c in s]
    sa = list(range(n))
    tmp = [0] * n
    k = 1
    # Doubling loop
    while k < n:
        # Sort by (rank[i], rank[i+k]) pairs
        sa.sort(key=lambda i: (ranks[i], ranks[i + k] if i + k < n else -1))
        # Temporary array for new ranks
        tmp[sa[0]] = 0
        for i in range(1, n):
            prev, curr = sa[i - 1], sa[i]
            # Compare pair (rank, next rank)
            r_prev = (ranks[prev], ranks[prev + k] if prev + k < n else -1)
            r_curr = (ranks[curr], ranks[curr + k] if curr + k < n else -1)
            tmp[curr] = tmp[prev] + (1 if r_curr != r_prev else 0)
        ranks, tmp = tmp, ranks  # reuse lists to save memory
        k <<= 1
        if ranks[sa[-1]] == n - 1:
            break
    # Drop the sentinel index
    return sa[1:]


def build_lcp_array(s: str, sa: list[int]) -> list[int]:
    n = len(sa)
    # Inverse of suffix array: pos[i] gives rank of suffix at i
    pos = [0] * n
    for i, suf in enumerate(sa):
        pos[suf] = i
    lcp = [0] * n
    k = 0
    for i in range(len(s)):
        if pos[i] == 0:
            k = 0
            continue
        j = sa[pos[i] - 1]
        # Compare characters starting from k
        while i + k < len(s) and j + k < len(s) and s[i + k] == s[j + k]:
            k += 1
        lcp[pos[i]] = k
        if k:
            k -= 1
    return lcp[1:]


if __name__ == "__main__":
    # Example usage and simple tests
    test_strings = ["banana", "abracadabra", "mississippi"]
    for s in test_strings:
        sa = build_suffix_array(s)
        lcp = build_lcp_array(s, sa)
        print(f"String: {s}")
        print(f"Suffix Array: {sa}")
        print(f"LCP Array   : {lcp}\n")

    # Assertions for correctness
    s = "banana"
    expected_sa = [5, 3, 1, 0, 4, 2]  # indices of sorted suffixes
    assert build_suffix_array(s) == expected_sa, "SA test failed"
    print("All tests passed!")
