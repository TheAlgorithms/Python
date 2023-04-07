"""
See https://en.wikipedia.org/wiki/Bloom_filter

>>> b = Bloom()
>>> b.add("Titanic")
>>> b.add("Avatar")
>>> b.exists("Titanic")
True
>>> b.exists("Avatar")
True
>>> b.exists("The Goodfather")
False
>>> b.exists("Interstellar")
False
>>> b.exists("Parasite")
False
>>> b.exists("Pulp Fiction")
False
"""
from hashlib import md5, sha256
from random import choices
from string import ascii_lowercase


class Bloom:
    # number of hash functions is fixed
    HASH_FUNCTIONS = (sha256, md5)

    def __init__(self, size: int = 8) -> None:
        self.bitstring = 0b0
        self.size = size

    def add(self, value: str) -> None:
        h = self.hash_(value)
        self.bitstring |= h

    #        print(
    #            f"""\
    # [add] value =      {value}
    #      hash =       {self.format_bin(h)}
    #      filter =     {self.format_bin(self.bitstring)}
    # """
    #        )

    def exists(self, value: str) -> bool:
        h = self.hash_(value)
        res = (h & self.bitstring) == h

        #        print(
        #            f"""\
        # [exists] value =   {value}
        #         hash =    {self.format_bin(h)}
        #         filter =  {self.format_bin(self.bitstring)}
        #         res =     {res}
        # """
        #        )
        return res

    def format_bin(self, value: int) -> str:
        res = bin(value)[2:]
        return res.zfill(self.size)

    def hash_(self, value: str) -> int:
        res = 0b0
        for func in self.HASH_FUNCTIONS:
            b = func(value.encode()).digest()
            position = int.from_bytes(b, "little") % self.size
            res |= 2**position
        return res


def random_string(size: int) -> str:
    return "".join(choices(ascii_lowercase + " ", k=size))


def test_probability(filter_bits: int = 64, added_elements: int = 20) -> None:
    b = Bloom(size=filter_bits)

    k = len(b.HASH_FUNCTIONS)
    estimated_error_rate_beforehand = (
        1 - (1 - 1 / filter_bits) ** (k * added_elements)
    ) ** k

    not_added = {random_string(10) for i in range(1000)}
    for _ in range(added_elements):
        b.add(not_added.pop())

    n_ones = bin(b.bitstring).count("1")
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
