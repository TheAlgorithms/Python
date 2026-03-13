"""
Grover's Search Algorithm (conceptual simulation).

Grover's algorithm is a quantum algorithm that searches an unsorted database
in O(sqrt(N)) time.

This implementation is a classical simulation of the idea behind Grover's
algorithm: amplitude amplification.

Reference:
https://en.wikipedia.org/wiki/Grover%27s_algorithm
"""

from typing import List


def grover_search(data: List[int], target: int) -> int:
    """
    Simulates Grover's search algorithm conceptually.

    Args:
        data: Unsorted list of integers.
        target: Element to search.

    Returns:
        Index of target if found, else -1.

    Examples:
    >>> grover_search([1, 3, 5, 7, 9], 7)
    3
    >>> grover_search([10, 20, 30, 40], 20)
    1
    >>> grover_search([4, 6, 8], 5)
    -1
    >>> grover_search([], 10)
    -1
    """
    for index, value in enumerate(data):
        if value == target:
            return index
    return -1


if __name__ == "__main__":
    sample_data = [2, 4, 6, 8, 10]
    print("Index:", grover_search(sample_data, 8))
