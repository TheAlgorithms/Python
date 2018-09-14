def rabin_karp(pattern, text, base=128, mod=997):
    """

    The Rabin-Karp Algorithm for finding a pattern within a piece of text
    with average complexity O(n+m), most efficient when it is used with multiple patterns
    because you can put all hashed patterns in, e.g. a Bloom filter to see if hash of current window
    matches any pattern in O(1).

    This will be the simple version which only assumes one pattern is being searched for but it's not hard to modify

    1) Calculate pattern hash

    2) Step through the text one character at a time as a sliding window, and update the
       hash (rolling hash) in O(1) time. Hash function used is:
              hash(a_1 ... a_k) = a_k * b^(k-1) + a_(k-1) * b^(k-2)) + ... a_1 modulo m

              Where b is a multiplicative base,
              and m is a number to keep hash size reasonable (use prime for best performance)

    3) Compare if rolled text hash matches pre-computed pattern hash. If so, do actual string comparison
       in case this is just a hash collision. The check against entire string means the worst-case
       running-time is O(nm) if every hash collides.

    """
    p_len = len(pattern)
    p_hash = 0
    text_hash = 0
    highest_multiplier = base ** (p_len - 1) % mod

    # Compute initial hash values for pattern and text
    multiplier = 1
    for i in range(p_len):
        p_hash = (p_hash * base + ord(pattern[i])) % mod
        text_hash = (text_hash * base + ord(text[i])) % mod
        multiplier *= base

    for i in range(0, len(text) - p_len + 1):
        if text_hash == p_hash and \
                text[i:i + p_len] == pattern:
            return True

        # Last iteration should only compare pattern and not compute next hash (out of range)
        if i < len(text) - p_len:
            # Remove leftmost character from hash
            text_hash -= ord(text[i]) * highest_multiplier
            # Shift all characters left by 1
            text_hash *= base
            # Add new character to hash
            text_hash = (text_hash + ord(text[i + p_len])) % mod
    return False


if __name__ == '__main__':
    # Test 1)
    pattern = "abc1abc12"
    text1 = "alskfjaldsabc1abc1abc12k23adsfabcabc"
    text2 = "alskfjaldsk23adsfabcabc"
    assert rabin_karp(pattern, text1) and not rabin_karp(pattern, text2)

    # Test 2)
    pattern = "ABABX"
    text = "ABABZABABYABABX"
    assert rabin_karp(pattern, text)

    # Test 3)
    pattern = "AAAB"
    text = "ABAAAAAB"
    assert rabin_karp(pattern, text)

    # Test 4)
    pattern = "abcdabcy"
    text = "abcxabcdabxabcdabcdabcy"
    assert rabin_karp(pattern, text)

    # Test 5)
    pattern = "blah"
    text = "blahgobbledigook"
    assert rabin_karp(pattern, text)
