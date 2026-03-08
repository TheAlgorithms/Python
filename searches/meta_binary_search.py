"""
Meta Binary Search (One-Sided Binary Search)

Meta Binary Search is a variation of binary search that uses
bit manipulation to determine the index of the target element
in a sorted array. Instead of repeatedly dividing the search
space like traditional binary search, it constructs the index
bit by bit from the most significant bit to the least.

Time Complexity: O(log n)
Space Complexity: O(1)

Reference:
https://www.geeksforgeeks.org/meta-binary-search-one-sided-binary-search/
"""


def meta_binary_search(arr: list[int], target: int) -> int:
    """
    Perform Meta Binary Search on a sorted list.

    The algorithm determines the index by checking bits from
    the most significant bit down to the least significant bit.

    Parameters
    ----------
    arr : list[int]
        A sorted list of integers where the search will be performed.
    target : int
        The element to search for.

    Returns
    -------
    int
        Index of the target element if found, otherwise -1.

    Examples
    --------
    >>> meta_binary_search([2, 4, 6, 8, 10], 6)
    2
    >>> meta_binary_search([2, 4, 6, 8, 10], 7)
    -1
    >>> meta_binary_search([], 5)
    -1
    """

    n = len(arr)
    if n == 0:
        return -1

    # Step 1: Find the Most Significant Bit position
    max_idx = n - 1
    msb_pos = 0 if max_idx == 0 else max_idx.bit_length() - 1

    idx = 0  # Initialize index before using it!

    # Step 2: Iterate from MSB down to LSB
    for i in range(msb_pos, -1, -1):
        new_idx = idx | (1 << i)

        if new_idx < n and arr[new_idx] <= target:
            idx = new_idx

    # Step 3: Final verification
    if idx < n and arr[idx] == target:
        return idx
    return -1


if __name__ == "__main__":
    example_array = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

    print(meta_binary_search(example_array, 14))  # Expected output: 6
    print(meta_binary_search(example_array, 5))  # Expected output: -1
