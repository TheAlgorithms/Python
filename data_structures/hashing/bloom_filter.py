"""
See https://en.wikipedia.org/wiki/Bloom_filter

The use of this data structure is to test membership in a set.
Compared to Python's built-in set() it is more space-efficient.
In the following example, only 8 bits of memory will be used:
>>> bloom = Bloom(size=8)

Initially, the filter contains all zeros:
>>> bloom.bitstring
'00000000'

When an element is added, two bits are set to 1
since there are 2 hash functions in this implementation:
>>> "Titanic" in bloom
False
>>> bloom.add("Titanic")
>>> bloom.bitstring
'01100000'
>>> "Titanic" in bloom
True

However, sometimes only one bit is added
because both hash functions return the same value
>>> bloom.add("Avatar")
>>> bloom.format_hash("Avatar")
'00000100'
>>> bloom.bitstring
'01100100'

Not added elements should return False ...
>>> not_present_films = ("The Goodfather", "Interstellar", "Parasite", "Pulp Fiction")
>>> {film: bloom.format_hash(film) for film in not_present_films}
{'The Goodfather': '00011000', 'Interstellar': '00000011', 'Parasite': '00010010', 'Pulp Fiction': '10000100'}
>>> any(film in bloom for film in not_present_films)
False

but sometimes there are false positives:
>>> "Ratatouille" in bloom
True
>>> bloom.format_hash("Ratatouille")
'01100000'

The probability increases with the number of added elements
>>> bloom.estimated_error_rate()
0.140625
>>> bloom.add("The Goodfather")
>>> bloom.estimated_error_rate()
0.390625
>>> bloom.bitstring
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

    def __contains__(self, other: str) -> bool:
        return self.exists(other)

    def format_bin(self, bitarray: int) -> str:
        res = bin(bitarray)[2:]
        return res.zfill(self.size)

    @property
    def bitstring(self) -> str:
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

    def estimated_error_rate(self) -> float:
        n_ones = bin(self.bitarray).count("1")
        k = len(HASH_FUNCTIONS)
        return (n_ones / self.size) ** k
