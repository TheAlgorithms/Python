def is_isomorphic(s: str, t: str) -> bool:
    """
    LeetCode No. 205 Isomorphic Strings
    Given two strings s and t, determine if they are isomorphic.
    https://leetcode.com/problems/isomorphic-strings/description/

    Two strings s and t are isomorphic if the characters in s can be
    replaced to get t.

    All occurrences of a character must be replaced with another character
    while preserving the order of characters. No two characters may map to
    the same character, but a character may map to itself.


    >>> is_isomorphic("egg", "add")
    True
    >>> is_isomorphic("foo", "bar")
    False
    >>> is_isomorphic("paper", "title")
    True
    >>> is_isomorphic("ab", "aa")
    False
    """
    if len(s) != len(t):
        return False

    mapping: dict[str, str] = {}
    mapped = set()

    for char_s, char_t in zip(s, t):
        if char_s in mapping:
            if mapping[char_s] != char_t:
                return False
        else:
            if char_t in mapped:
                return False
            mapping[char_s] = char_t
            mapped.add(char_t)

    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(is_isomorphic("egg", "add"))  # True
