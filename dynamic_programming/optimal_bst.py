#!/usr/bin/python3

# This Python program provides O(n^2) dynamic programming solution
# to an optimal BST problem.
#
# The goal of the optimal BST problem is to build a low-cost BST for a
# given set of nodes, each with its own key and frequency. The frequency
# of the node is defined as how many time the node is being searched.
# The characteristic of low-cost BSTs is having a faster overall search
# time than other BSTs. The reason for their fast search time is that
# the nodes with high frequencies will be placed near the root of the
# tree while the nodes with low frequencies will be placed near the tree
# leaves thus reducing the search time.

import sys

from random import randint


class Node:
    """BST Node"""

    def __init__(self, key, freq):
        self.key = key
        self.freq = freq


def print_BST(root, key, i, j, parent, is_left):
    """Recursive function to print a BST from a root table."""
    if i > j or i < 0 or j > len(root) - 1:
        return

    if parent == -1:
        print(
            f"{key[root[i][j]]} is the root of the BST."
        )  # root does not have a parent
    elif is_left:
        print(f"{key[root[i][j]]} is the left child of key {parent}.")
    else:
        print(f"{key[root[i][j]]} is the right child of key {parent}.")

    print_BST(
        root, key, i, root[i][j] - 1, key[root[i][j]], True
    )  # recur to left child
    print_BST(
        root, key, root[i][j] + 1, j, key[root[i][j]], False
    )  # recur to right child


def find_optimal_BST(nodes):
    """
    This function calculates and prints the optimal BST.
    The dynamic programming algorithm below runs in O(n^2) time
    """
    n = len(nodes)

    key = [nodes[i].key for i in range(n)]
    freq = [nodes[i].freq for i in range(n)]

    # This 2D array stores the overall tree cost (which's as minimized as possible); for a single key, cost is equal to frequency of the key.
    dp = [[freq[i] if i == j else 0 for j in range(n)] for i in range(n)]
    # sum[i][j] stores the sum of key frequencies between i and j inclusive in nodes array
    sum = [[freq[i] if i == j else 0 for j in range(n)] for i in range(n)]
    # stores tree roots used for constructing BST later
    root = [[i if i == j else 0 for j in range(n)] for i in range(n)]

    for l in range(2, n + 1):  # l is an interval length
        for i in range(n - l + 1):
            j = i + l - 1

            dp[i][j] = sys.maxsize  # set the value to "infinity"
            sum[i][j] = (
                sum[i][j - 1] + freq[j]
            )  # (sum in range [i...j]) = (sum in range [i...j - 1]) + freq[j]

            # Apply Knuth's optimization
            # Loop without optimization: for r in range(i, j + 1):
            for r in range(root[i][j - 1], root[i + 1][j] + 1):  # r is a temporal root
                left = dp[i][r - 1] if r != i else 0  # optimal cost for left subtree
                right = dp[r + 1][j] if r != j else 0  # optimal cost for right subtree
                cost = left + sum[i][j] + right

                if dp[i][j] > cost:
                    dp[i][j] = cost
                    root[i][j] = r

    print_BST(root, key, 0, n - 1, -1, False)


def main():
    # A sample BST
    nodes = [Node(i, randint(1, 50)) for i in range(10, 0, -1)]

    # Tree nodes must be sorted first, the code below sorts the keys in
    # increasing order and rearrange its frequencies accordingly.
    nodes.sort(key=lambda node: node.key)

    find_optimal_BST(nodes)


if __name__ == "__main__":
    main()
