"""
See https://en.wikipedia.org/wiki/Bloom_filter

The use of this data structure is to test membership in a set.
Compared to python built-in set() it is more space-efficent.
In the following example, only 8 bits of memory will be used:
>>> b = Bloom(size=8)
>>> "Titanic" in b
False

Initially the filter contains all zeros:
>>> b.bitstring
'00000000'

When an element is added, two bits are set to 1
since there are 2 hash functions in this implementation:
>>> b.add("Titanic")
>>> b.bitstring
'01100000'
>>> "Titanic" in b
True

However, sometimes only one bit is added
because both hash functions return the same value
>>> b.add("Avatar")
>>> b.format_hash("Avatar")
'00000100'
>>> b.bitstring
'01100100'

Not added elements should return False ...
>>> "The Goodfather" in b
False
>>> b.format_hash("The Goodfather")
'00011000'
>>> "Interstellar" in b
False
>>> b.format_hash("Interstellar")
'00000011'
>>> "Parasite" in b
False
>>> b.format_hash("Parasite")
'00010010'
>>> "Pulp Fiction" in b
False
>>> b.format_hash("Pulp Fiction")
'10000100'

but sometimes there are false positives:
>>> "Ratatouille" in b
True
>>> b.format_hash("Ratatouille")
'01100000'

The probability increases with the number of added elements
>>> b.estimated_error_rate()
0.140625
>>> b.add("The Goodfather")
>>> b.estimated_error_rate()
0.390625
>>> b.bitstring
'01111100'
"""
from hashlib import md5, sha256

HASH_FUNCTIONS = (sha256, md5)


class Bloom:
    def __init__(self, size: int = 8) -> None:
        self.bitarray = 0b0
        self.size = size

    def add(self, value: str) -> None:
        h = self.hash_(value)
        self.bitarray |= h

    def exists(self, value: str) -> bool:
        h = self.hash_(value)
        return (h & self.bitarray) == h

    def __contains__(self, other):
        return self.exists(other)

    def format_bin(self, bitarray: int) -> str:
        res = bin(bitarray)[2:]
        return res.zfill(self.size)

    @property
    def bitstring(self):
        return self.format_bin(self.bitarray)

    def hash_(self, value: str) -> int:
        res = 0b0
        for func in HASH_FUNCTIONS:
            b = func(value.encode()).digest()
            position = int.from_bytes(b, "little") % self.size
            res |= 2**position
        return res

    def format_hash(self, value: str) -> str:
        return self.format_bin(self.hash_(value))

    def estimated_error_rate(self):
        n_ones = bin(self.bitarray).count("1")
        k = len(HASH_FUNCTIONS)
        return (n_ones / self.size) ** k
