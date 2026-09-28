"""Factor a string into Lyndon words using Duval's linear-time algorithm.

https://cp-algorithms.com/string/lyndon_factorization.html
"""


def lyndon_factorization(text: str) -> list[str]:
    """Return the unique non-increasing sequence of Lyndon words in ``text``.

    A Lyndon word is strictly smaller than each of its nontrivial rotations.
    The empty string has an empty factorization.

    >>> lyndon_factorization("banana")
    ['b', 'an', 'an', 'a']
    >>> lyndon_factorization("abab")
    ['ab', 'ab']
    >>> lyndon_factorization("aaaa")
    ['a', 'a', 'a', 'a']
    >>> lyndon_factorization("")
    []
    >>> lyndon_factorization(123)
    Traceback (most recent call last):
    ...
    TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    factors: list[str] = []
    start = 0
    length = len(text)

    while start < length:
        candidate = start
        end = start + 1

        while end < length and text[candidate] <= text[end]:
            if text[candidate] < text[end]:
                candidate = start
            else:
                candidate += 1
            end += 1

        factor_length = end - candidate
        while start <= candidate:
            factors.append(text[start : start + factor_length])
            start += factor_length

    return factors
