"""
Jacobson's rank on a static bit vector.

rank(i) tells how many 1s there are in bit_vector[0:i], and n is the length of
bit_vector. The naive way is to count them at every query (O(n) time) or to save the
answer for every position (O(n log n) bits). Jacobson showed how to answer in O(1)
using only o(n) extra bits.

The vector is divided into superblocks of about log^2(n) bits, and every superblock into
blocks of about log(n) / 2 bits. For every superblock we save how many 1s come
before it, and for every block how many 1s there are from the start of its
superblock up to the block. What is left is the rank inside a single block, and this
is where the four Russians trick comes in. A block is short, so there are only
2 ** (log(n) / 2) = sqrt(n) possible blocks, so we can precompute the answer for
all of them.

So rank(i) = superblock count + block count + table[block][i inside the block].


Construction: O(n) time
Query: O(1) time
Extra space: o(n) bits

https://en.wikipedia.org/wiki/Succinct_data_structure
G. Jacobson, "Space-efficient static trees and graphs", FOCS 1989
"""

from collections.abc import Sequence
from math import ceil, log2


def is_bit_sequence(sequence: Sequence[int]) -> bool:
    """
    True if the sequence only contains 0s and 1s.

    >>> is_bit_sequence([0, 1, 1, 0])
    True
    >>> is_bit_sequence([0, 2, 1])
    False
    >>> is_bit_sequence([])
    True
    """
    return all(element in (0, 1) for element in sequence)


def bit_vector_to_int(bits: list[int]) -> int:
    """
    Read a list of bits as a binary number (the first bit is the most significant).

    >>> bit_vector_to_int([1, 1, 0])
    6
    >>> bit_vector_to_int([0, 1, 1])
    3
    >>> bit_vector_to_int([])
    0
    """
    number = 0
    for bit in bits:
        number = number * 2 + bit
    return number


def int_to_bit_vector(number: int, num_bits: int) -> list[int]:
    """
    Write number in binary on exactly num_bits bits, with 0s in front if needed.

    >>> int_to_bit_vector(6, 3)
    [1, 1, 0]
    >>> int_to_bit_vector(3, 5)
    [0, 0, 0, 1, 1]
    >>> int_to_bit_vector(8, 3)
    Traceback (most recent call last):
        ...
    ValueError: Number cannot be represented with num_bits bits
    >>> int_to_bit_vector(-1, 3)
    Traceback (most recent call last):
        ...
    ValueError: Number cannot be represented with num_bits bits
    """
    if number < 0 or num_bits < 0 or number >= 2**num_bits:
        raise ValueError("Number cannot be represented with num_bits bits")

    binary = format(number, f"0{num_bits}b")
    return [int(bit) for bit in binary]


class JacobsonRank:
    """
    Bit vector that answers rank queries in O(1) after a linear preprocessing.

    >>> bits = [1, 0, 1, 1, 0, 0, 1, 0, 1, 1]
    >>> jacobson_rank = JacobsonRank(bits)
    >>> [jacobson_rank.rank(position) for position in range(len(bits) + 1)]
    [0, 1, 1, 2, 3, 3, 3, 4, 4, 5, 6]
    >>> JacobsonRank([0, 1, 2])
    Traceback (most recent call last):
        ...
    ValueError: bit_vector must contain only 0s and 1s
    """

    def __init__(self, bit_vector: Sequence[int]) -> None:
        if not is_bit_sequence(bit_vector):
            message = "bit_vector must contain only 0s and 1s"
            raise ValueError(message)
        self._n_bits = len(bit_vector)
        # log2(self._n_bits) gives the size of blocks and superblocks. with 0 or 1
        # bits log2 fails or gives 0, so max(self._n_bits, 2) makes the minimum size 1
        log_n = log2(max(self._n_bits, 2))
        self._total_ones = sum(bit_vector)
        self._superblocks_size = ceil(log_n**2)
        self._blocks_size = ceil(log_n / 2)

        # superblocks must contain a whole number of blocks, otherwise a block could
        # start in one superblock and end in the next
        while self._superblocks_size % self._blocks_size != 0:
            self._superblocks_size += 1

        self._n_superblocks = ceil(self._n_bits / self._superblocks_size)
        self._n_blocks = ceil(self._n_bits / self._blocks_size)

        self._compute_values_for_blocks(bit_vector)
        self._compute_superblocks_blocks_table()
        self._compute_four_russians_trick()

    def _compute_values_for_blocks(self, bit_vector: Sequence[int]) -> None:
        """
        Turn every block into the number its bits make in binary.

        >>> JacobsonRank([1, 0, 1, 1, 0, 0, 1, 0, 1, 1])._blocks_values
        [2, 3, 0, 2, 3]
        >>> JacobsonRank([1, 0, 1, 1, 1])._blocks_values  # [1] -> [1, 0]
        [2, 3, 2]
        >>> JacobsonRank([])._blocks_values
        []
        """
        self._blocks_values = [0] * self._n_blocks
        for index in range(self._n_blocks):
            start = self._blocks_size * index
            end = self._blocks_size * (index + 1)
            block = list(bit_vector[start:end])

            # the last block can be shorter than the others. the lookup table only
            # knows blocks of exactly blocks_size bits, so we fill it with 0s on the
            # right (0s on the left would shift the bits and give the wrong rank)
            if len(block) < self._blocks_size:
                block += [0] * (self._blocks_size - len(block))
            self._blocks_values[index] = bit_vector_to_int(block)

    def _compute_superblocks_blocks_table(self) -> None:
        """
        Fill both counting tables: for every superblock the 1s that come before it,
        and for every block the 1s from the start of its superblock up to the block.

        >>> jacobson_rank = JacobsonRank([1] * 64)
        >>> jacobson_rank._superblocks_table
        [0, 36]
        >>> jacobson_rank._blocks_table[10:14]  # second superblock starts at 12
        [30, 33, 0, 3]
        """
        ones_so_far = 0
        self._superblocks_table = [0] * self._n_superblocks
        self._blocks_table = [0] * self._n_blocks

        for block_index in range(self._n_blocks):
            start = block_index * self._blocks_size
            if start % self._superblocks_size == 0:
                ones_before_superblock = ones_so_far
                self._superblocks_table[start // self._superblocks_size] = ones_so_far
            self._blocks_table[block_index] = ones_so_far - ones_before_superblock
            ones_so_far += self._blocks_values[block_index].bit_count()

    def _compute_four_russians_trick(self) -> None:
        """
        For every possible block, that is every number with blocks_size bits, save
        the rank of each position inside it: tables[number][i] is the number of 1s in
        the first i bits of number.

        >>> JacobsonRank([1, 0, 1, 1, 0, 0, 1, 0, 1, 1])._four_russians_tables
        [[0, 0], [0, 0], [0, 1], [0, 1]]
        """

        def trivial_rank(bit_vector: Sequence[int], index: int) -> int:
            return sum(bit_vector[0:index])

        number_of_tables = 2 ** (self._blocks_size)
        self._four_russians_tables = [[]] * number_of_tables
        for number in range(number_of_tables):
            bit_vector = int_to_bit_vector(number, self._blocks_size)
            rank_table = [
                trivial_rank(bit_vector, index) for index in range(len(bit_vector))
            ]
            self._four_russians_tables[number] = rank_table

    def rank(self, position: int) -> int:
        """
        Number of 1s in bit_vector[0:position]. position goes from 0 to the length
        of the bit vector, both included.

        >>> JacobsonRank([1, 0, 1]).rank(2)
        1
        >>> JacobsonRank([1, 0, 1]).rank(3)
        2
        >>> JacobsonRank([1] * 29).rank(28)  # last block is shorter
        28
        >>> JacobsonRank([1] * 24).rank(23)  # superblock size goes 22 -> 24
        23
        >>> JacobsonRank([]).rank(0)
        0
        >>> JacobsonRank([1]).rank(1)
        1
        >>> import random
        >>> bits = [random.randint(0, 1) for _ in range(1000)]
        >>> jacobson_rank = JacobsonRank(bits)
        >>> all(
        ...     jacobson_rank.rank(position) == sum(bits[:position])
        ...     for position in range(len(bits) + 1)
        ... )
        True
        >>> JacobsonRank([1, 0, 1]).rank(4)
        Traceback (most recent call last):
            ...
        ValueError: position must be between 0 and 3, got 4
        >>> JacobsonRank([1, 0, 1]).rank(-1)
        Traceback (most recent call last):
            ...
        ValueError: position must be between 0 and 3, got -1
        """
        if position < 0 or position > self._n_bits:
            message = f"position must be between 0 and {self._n_bits}, got {position}"
            raise ValueError(message)
        if position == self._n_bits:
            return self._total_ones

        superblock_index = position // self._superblocks_size
        block_index = position // self._blocks_size
        index_in_block = position % self._blocks_size

        number = self._blocks_values[block_index]
        return (
            self._superblocks_table[superblock_index]
            + self._blocks_table[block_index]
            + self._four_russians_tables[number][index_in_block]
        )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
