"""
    This algorithm was created for sdbm (a public-domain reimplementation of ndbm)
    database library.
    It was found to do well in scrambling bits, causing better distribution of the keys
    and fewer splits.
    It also happens to be a good general hashing function with good distribution.
    The actual function (pseudo code) is:
        for i in i..len(str):
            hash(i) = hash(i - 1) * 65599 + str[i];

    What is included below is the faster version used in gawk. [there is even a faster,
    duff-device version]
    The magic constant 65599 was picked out of thin air while experimenting with
    different constants.
    It turns out to be a prime.
    This is one of the algorithms used in berkeley db (see sleepycat) and elsewhere.

    source: http://www.cse.yorku.ca/~oz/hash.html
"""


def sdbm(plain_text: str) -> int:
    """
    Function implements sdbm hash, easy to use, great for bits scrambling.
    iterates over each character in the given string and applies function to each of
    them.

    >>> sdbm('Algorithms')
    1462174910723540325254304520539387479031000036

    >>> sdbm('scramble bits')
    730247649148944819640658295400555317318720608290373040936089
    """
    hash_value = 0
    for plain_chr in plain_text:
        hash_value = (
            ord(plain_chr) + (hash_value << 6) + (hash_value << 16) - hash_value
        )
    return hash_value
