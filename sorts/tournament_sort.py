"""
Tournament Sort algorithm implementation.

Tournament sort works by creating a tournament tree (a min-heap style
binary tree) where elements compete against each other. The smallest
element wins each round and is extracted, similar to a sports tournament.

Time Complexity:
    Best Case:    O(n log n)
    Average Case: O(n log n)
    Worst Case:   O(n log n)

Space Complexity: O(n)

Reference: https://en.wikipedia.org/wiki/Tournament_sort
"""


def tournament_sort(sequence: list[int]) -> list[int]:
    """
    Sort a list using the tournament sort algorithm.

    :param sequence: list of integers to sort
    :return: sorted list in ascending order

    >>> tournament_sort([0, 5, 3, 1, 2])
    [0, 1, 2, 3, 5]
    >>> tournament_sort([])
    []
    >>> tournament_sort([1])
    [1]
    >>> tournament_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> tournament_sort([1, 1, 1])
    [1, 1, 1]
    >>> tournament_sort([-3, -1, -2])
    [-3, -2, -1]
    >>> tournament_sort([3, -1, 0, -5, 2])
    [-5, -1, 0, 2, 3]
    """
    if len(sequence) <= 1:
        return list(sequence)

    def build_tree(arr: list[int]) -> list[int | None]:
        """Build a tournament tree from the array."""
        n = len(arr)
        # Tree size: leaves start at index n (1-indexed internal nodes)
        tree: list[int | None] = [None] * (2 * n)
        # Fill leaves
        for i in range(n):
            tree[n + i] = arr[i]
        # Build internal nodes (winners)
        for i in range(n - 1, 0, -1):
            left = tree[2 * i]
            right = tree[2 * i + 1]
            if left is None:
                tree[i] = right
            elif right is None:
                tree[i] = left
            else:
                tree[i] = min(left, right)
        return tree

    def extract_min(tree: list[int | None], n: int) -> int:
        """Extract minimum value and remove it from tree."""
        min_val = tree[1]
        # Find the leaf holding min_val and remove it
        i = 1
        while i < n:
            left = tree[2 * i]
            right = tree[2 * i + 1]
            i = 2 * i if left == min_val else 2 * i + 1
        tree[i] = None
        # Update internal nodes on path back to root
        i //= 2
        while i >= 1:
            left = tree[2 * i]
            right = tree[2 * i + 1]
            if left is None:
                tree[i] = right
            elif right is None:
                tree[i] = left
            else:
                tree[i] = min(left, right)
            i //= 2
        return min_val  # type: ignore[return-value]

    n = len(sequence)
    tree = build_tree(sequence)
    return [extract_min(tree, n) for _ in range(n)]


if __name__ == "__main__":
    user_input = input("Enter numbers separated by comma:\n").strip()
    sequence = [int(item.strip()) for item in user_input.split(",")]
    sorted_sequence = tournament_sort(sequence)
    print(f"tournament_sort({sequence}) = {sorted_sequence}")
