"""
See https://en.wikipedia.org/wiki/Bloom_filter
"""
from hashlib import md5, sha256
from random import choices
from string import ascii_lowercase


class Bloom:
    # number of hash functions is fixed
    HASH_FUNCTIONS = (sha256, md5)

    def __init__(self, size=8):
        self.bitstring = 0b0
        self.size = size

    def add(self, value: str):
        h = self.hash_(value)
        self.bitstring |= h
        print(
            f"""\
[add] value =      {value}
      hash =       {self.format_bin(h)}
      filter =     {self.format_bin(self.bitstring)}
"""
        )

    def exists(self, value: str) -> bool:
        h = self.hash_(value)
        res = (h & self.bitstring) == h

        print(
            f"""\
[exists] value =   {value}
         hash =    {self.format_bin(h)}
         filter =  {self.format_bin(self.bitstring)}
         res =     {res}
"""
        )
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


def test_movies():
    b = Bloom()
    b.add("titanic")
    b.add("avatar")

    assert b.exists("titanic")
    assert b.exists("avatar")

    assert b.exists("the goodfather") in (True, False)
    assert b.exists("interstellar") in (True, False)
    assert b.exists("Parasite") in (True, False)
    assert b.exists("Pulp fiction") in (True, False)


def random_string(size):
    return "".join(choices(ascii_lowercase + " ", k=size))


def test_probability(m=64, n=20):
    b = Bloom(size=m)

    added = {random_string(10) for i in range(n)}
    for a in added:
        b.add(a)

    k = len(b.HASH_FUNCTIONS)

    n_ones = bin(b.bitstring).count("1")
    expected_probability = (n_ones / m) ** k

    expected_probability_wikipedia = (1 - (1 - 1 / m) ** (k * n)) ** k

    not_added = {random_string(10) for i in range(1000)}
    fails = 0
    for string in not_added:
        if b.exists(string):
            fails += 1
    fail_rate = fails / len(not_added)

    print(f"total = {len(not_added)}, fails = {fails}, fail_rate = {fail_rate}")
    print(f"{expected_probability=}")
    print(f"{expected_probability_wikipedia=}")

    assert (
        abs(expected_probability - fail_rate) <= 0.05
    )  # 5% absolute margin calculated experiementally


if __name__ == "__main__":
    test_movies()
    test_probability()
