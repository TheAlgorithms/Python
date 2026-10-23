"""
https://en.wikipedia.org/wiki/Lyndon_word
https://cp-algorithms.com/string/lyndon_factorization.html

Lyndon factorization (Duval's algorithm)

A Lyndon word is a non-empty string that is strictly smaller than all of its
proper rotations. Every string can be written uniquely as a concatenation of
Lyndon words w1 >= w2 >= ... >= wk. Duval's algorithm finds this factorization.

Time Complexity: O(n) - where n is the length of the string
Space Complexity: O(1) extra, apart from the output
"""


def lyndon_factorization(input_str: str) -> list[str]:
    """
    Return the Lyndon factorization of the given string.

    >>> lyndon_factorization("abab")
    ['ab', 'ab']
    >>> lyndon_factorization("banana")
    ['b', 'an', 'an', 'a']
    >>> lyndon_factorization("aaa")
    ['a', 'a', 'a']
    >>> lyndon_factorization("abc")
    ['abc']
    >>> lyndon_factorization("cba")
    ['c', 'b', 'a']
    >>> lyndon_factorization("a")
    ['a']
    >>> lyndon_factorization("")
    []
    >>> lyndon_factorization(123)
    Traceback (most recent call last):
        ...
    TypeError: object of type 'int' has no len()
    """
    length = len(input_str)
    factors: list[str] = []
    start = 0

    while start < length:
        # `compare` scans ahead while the text keeps repeating the current word
        compare = start + 1
        candidate = start
        while compare < length and input_str[candidate] <= input_str[compare]:
            if input_str[candidate] < input_str[compare]:
                candidate = start
            else:
                candidate += 1
            compare += 1

        # The repeated Lyndon word has length (compare - candidate)
        word_length = compare - candidate
        while start <= candidate:
            factors.append(input_str[start : start + word_length])
            start += word_length

    return factors


if __name__ == "__main__":
    import doctest

    doctest.testmod()
