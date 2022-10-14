"""
This algorithm (k=33) was first reported by Dan Bernstein many years ago in comp.lang.c
Another version of this algorithm (now favored by Bernstein) uses xor:
    hash(i) = hash(i - 1) * 33 ^ str[i];

    First Magic constant 33:
    It has never been adequately explained.
    It's magic because it works better than many other constants, prime or not.

    Second Magic Constant 5381:

    1. odd number
    2. prime number
    3. deficient number
    4. 001/010/100/000/101 b

    source: http://www.cse.yorku.ca/~oz/hash.html
"""


def djb2(s: str) -> int:
    """
    Implementation of djb2 hash algorithm that
    is popular because of it's magic constants.

    >>> djb2('Algorithms')
    3782405311

    >>> djb2('scramble bits')
    1609059040
    """
    hash_value = 5381
    for x in s:
        hash_value = ((hash_value << 5) + hash_value) + ord(x)
    return hash_value & 0xFFFFFFFF
