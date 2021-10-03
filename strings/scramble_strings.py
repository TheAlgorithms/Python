def is_scramble(s1: str, s2: str) -> bool:
    """
    Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.
    >>> is_scramble("great", "rgeat")
    True
    """
    def split(l1, r1, l2, r2):
        if r1 - l1 == 1:
            return s1[l1] == s2[l2]
        if sorted(s1[l1:r1]) != sorted(s2[l2:r2]):
            return False
        for i in range(1, r1-l1):
            if split(l1, l1+i, l2, l2+i) and \
                    split(l1+i, r1, l2+i, r2) or \
                    split(l1, l1+i, r2-i, r2) and \
                    split(l1+i, r1, l2, r2-i):
                return True
    return split(0, len(s1), 0, len(s2))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    
