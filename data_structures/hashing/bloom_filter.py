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
since there are 2 hash functions:
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
>>> "Parasite" in b
False
>>> "Pulp Fiction" in b
False

but sometimes there are false positives:
>>> "Ratatouille" in b
True
>>> b.format_hash("Ratatouille")
'01100000'

>>> b.estimated_error_rate()
0.140625
"""
from hashlib import md5, sha256
from random import choices
from string import ascii_lowercase

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


def random_string(size: int) -> str:
    return "".join(choices(ascii_lowercase + " ", k=size))


def test_probability(filter_bits: int = 64, added_elements: int = 20) -> None:
    b = Bloom(size=filter_bits)

    k = len(HASH_FUNCTIONS)
    estimated_error_rate_beforehand = (
        1 - (1 - 1 / filter_bits) ** (k * added_elements)
    ) ** k

    not_added = {random_string(10) for i in range(1000)}
    for _ in range(added_elements):
        b.add(not_added.pop())

    n_ones = bin(b.bitarray).count("1")
    estimated_error_rate = (n_ones / filter_bits) ** k

    errors = 0
    for string in not_added:
        if b.exists(string):
            errors += 1
    error_rate = errors / len(not_added)

    print(f"error_rate = {errors}/{len(not_added)} = {error_rate}")
    print(f"{estimated_error_rate=}")
    print(f"{estimated_error_rate_beforehand=}")

    assert (
        abs(estimated_error_rate - error_rate) <= 0.05
    )  # 5% absolute margin calculated experiementally


if __name__ == "__main__":
    test_probability()
