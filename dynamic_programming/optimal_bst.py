#!/usr/bin/env python3

# This Python program provides O(n^2) dynamic programming solution
# to an optimal binary search tree (abbreviated BST) problem.
#
# The goal of the optimal BST problem is to build a low-cost BST for a
# given set of nodes, each with its own key and frequency. The frequency
# of the node is defined as how many time the node is being searched.
# The search cost of BST is given by this formula:
#
# cost(1, n) = sum{i = 1 to n}((depth(node_i) + 1) * node_i_freq)
#
# where n is number of nodes in the BST. The characteristic of low-cost
# BSTs is having a faster overall search time than other BSTs. The reason
# for their fast search time is that the nodes with high frequencies will
# be placed near the root of the tree while the nodes with low frequencies
# will be placed near the tree leaves thus reducing the search time.

import sys

from random import randint


class Node:
    """Binary Search Tree Node"""

    def __init__(self, key, freq):
        self.key = key
        self.freq = freq

    def __str__(self):
        return f"Node(key={self.key}, freq={self.freq})"


def print_binary_search_tree(root, key, i, j, parent, is_left):
    """
    Recursive function to print a BST from a root table.
    
    >>> key = [3, 8, 9, 10, 17, 21]
    >>> root = [[0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 3], [0, 0, 2, 3, 3, 3], \
                [0, 0, 0, 3, 3, 3], [0, 0, 0, 0, 4, 5], [0, 0, 0, 0, 0, 5]]
    >>> print_binary_search_tree(root, key, 0, 5, -1, False)
    8 is the root of the BST.
    3 is the left child of key 8.
    10 is the right child of key 8.
    9 is the left child of key 10.
    21 is the right child of key 10.
    17 is the left child of key 21.
    """
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

    print_binary_search_tree(root, key, i, root[i][j] - 1, key[root[i][j]], True)
    print_binary_search_tree(root, key, root[i][j] + 1, j, key[root[i][j]], False)


def find_optimal_binary_search_tree(nodes):
    """
    This function calculates and prints the optimal BST.
    The dynamic programming algorithm below runs in O(n^2) time.
    Implemented from CLRS (Introduction to Algorithms) book.
    
    >>> find_optimal_binary_search_tree([Node(12, 8), Node(10, 34), Node(20, 50), \
                                         Node(42, 3), Node(25, 40), Node(37, 30)])
    BST Nodes:
    Node(key=10, freq=34)
    Node(key=12, freq=8)
    Node(key=20, freq=50)
    Node(key=25, freq=40)
    Node(key=37, freq=30)
    Node(key=42, freq=3)
    <BLANKLINE>
    The cost of optimal BST for given tree nodes is 324.
    20 is the root of the BST.
    10 is the left child of key 20.
    12 is the right child of key 10.
    25 is the right child of key 20.
    37 is the right child of key 25.
    42 is the right child of key 37.
    """
    # Tree nodes must be sorted first, the code below sorts the keys in
    # increasing order and rearrange its frequencies accordingly.
    nodes.sort(key=lambda node: node.key)

    n = len(nodes)

    key = [nodes[i].key for i in range(n)]
    freq = [nodes[i].freq for i in range(n)]

    # This 2D array stores the overall tree cost (which's as minimized as possible);
    # for a single key, cost is equal to frequency of the key.
    dp = [[freq[i] if i == j else 0 for j in range(n)] for i in range(n)]
    # sum[i][j] stores the sum of key frequencies between i and j inclusive in nodes array
    sum = [[freq[i] if i == j else 0 for j in range(n)] for i in range(n)]
    # stores tree roots used for constructing BST later
    root = [[i if i == j else 0 for j in range(n)] for i in range(n)]

    for l in range(2, n + 1):  # l is an interval length
        for i in range(n - l + 1):
            j = i + l - 1

            dp[i][j] = sys.maxsize  # set the value to "infinity"
            sum[i][j] = sum[i][j - 1] + freq[j]

            # Apply Knuth's optimization
            # Loop without optimization: for r in range(i, j + 1):
            for r in range(root[i][j - 1], root[i + 1][j] + 1):  # r is a temporal root
                left = dp[i][r - 1] if r != i else 0  # optimal cost for left subtree
                right = dp[r + 1][j] if r != j else 0  # optimal cost for right subtree
                cost = left + sum[i][j] + right

                if dp[i][j] > cost:
                    dp[i][j] = cost
                    root[i][j] = r

    print("BST Nodes:")
    for node in nodes:
        print(node)

    print(f"\nThe cost of optimal BST for given tree nodes is {dp[0][n - 1]}.")
    print_binary_search_tree(root, key, 0, n - 1, -1, False)


def main():
    # A sample BST
    nodes = [Node(i, randint(1, 50)) for i in range(10, 0, -1)]
    find_optimal_binary_search_tree(nodes)


if __name__ == "__main__":
    main()
