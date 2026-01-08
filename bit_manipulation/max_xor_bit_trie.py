"""
Author  : Abhiraj Mandal
Date    : October 3, 2025

This is a pure Python implementation of Bitwise Trie (Binary Trie) to compute
the maximum XOR of any two numbers in an array.

The problem is:
Given an array of integers, find the maximum XOR value obtainable by XOR-ing
any two numbers in the array. The implementation uses a bitwise Trie to efficiently
compute the maximum XOR.
"""

from __future__ import annotations


class TrieNode:
    """Node of the Bitwise Trie."""

    def __init__(self) -> None:
        self.child: list[TrieNode | None] = [
            None,
            None,
        ]  # child[0] for bit 0, child[1] for bit 1


class BitwiseTrieMaxXOR:
    """
    Use:
        solver = BitwiseTrieMaxXOR()
        result = solver.find_maximum_xor(nums)
    """

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, num: int) -> None:
        """
        Insert a number into the trie.

        >>> trie = BitwiseTrieMaxXOR()
        >>> trie.insert(5)
        >>> trie.insert(10)
        """
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if node.child[bit] is None:
                node.child[bit] = TrieNode()
            node = node.child[bit]  # type: ignore[misc]

    def query_max_xor(self, num: int) -> int:
        """
        Query the maximum XOR achievable with `num` using the trie.

        Args:
            num (int): The number to XOR against numbers in the trie.

        Returns:
            int: Maximum XOR value achievable with `num`.

        >>> trie = BitwiseTrieMaxXOR()
        >>> trie.insert(5)
        >>> trie.insert(10)
        >>> trie.query_max_xor(5)
        15
        >>> trie.query_max_xor(10)
        15
        """
        node = self.root
        max_xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            toggle = 1 - bit
            if node.child[toggle] is not None:
                max_xor |= 1 << i
                node = node.child[toggle]
            else:
                assert node.child[bit] is not None
                node = node.child[bit]
        return max_xor

    def find_maximum_xor(self, nums: list[int]) -> int:
        """
        Compute maximum XOR of any two numbers in `nums`.

        >>> BitwiseTrieMaxXOR().find_maximum_xor([3, 10, 5, 25, 2, 8])
        28
        >>> BitwiseTrieMaxXOR().find_maximum_xor([42])
        0
        >>> BitwiseTrieMaxXOR().find_maximum_xor([0xFFFFFFFF, 0])
        4294967295
        >>> BitwiseTrieMaxXOR().find_maximum_xor([7, 7, 7])
        0
        >>> BitwiseTrieMaxXOR().find_maximum_xor([1, 2, 3, 4, 5])
        7
        >>> BitwiseTrieMaxXOR().find_maximum_xor([16, 8, 4, 2, 1])
        24
        >>> BitwiseTrieMaxXOR().find_maximum_xor([1, 2, 4, 8, 16, 32])
        48
        >>> BitwiseTrieMaxXOR().find_maximum_xor([9, 14, 3, 6, 12])
        15
        """
        if not nums:
            return 0
        for num in nums:
            self.insert(num)
        return max(self.query_max_xor(num) for num in nums)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print("All doctests passed!")

    # Manual test suite
    print(
        "\n************ Manual Testing Bitwise Trie Maximum XOR Algorithm "
        "************\n"
    )

    test_cases = [
        ([3, 10, 5, 25, 2, 8], 28),
        ([42], 0),
        ([8, 1], 9),
        ([0, 0, 0], 0),
        ([7, 7, 7], 0),
        ([1, 2, 3, 4, 5], 7),
        ([16, 8, 4, 2, 1], 24),
        ([1, 2, 4, 8, 16, 32], 48),
        ([9, 14, 3, 6, 12], 15),
    ]

    for idx, (nums, expected) in enumerate(test_cases, 1):
        solver = BitwiseTrieMaxXOR()
        result = solver.find_maximum_xor(nums)
        print(f"Testcase {idx}: Expected={expected}, Got={result}")
        assert result == expected, f"Testcase {idx} failed!"

    print("\nAll manual test cases successfully passed!")
