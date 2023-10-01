"""
Meta Binary Search, also known as One-Sided Binary Search, is a variation of the binary search algorithm used to search ordered lists. It reduces the
number of comparisons needed by performing controlled jumps across the list. It starts with a large interval, compares the middle element to the target,
and adjusts the interval based on the comparison. While it may perform fewer comparisons for targets near the beginning, it can require more for targets
near the end. It works best when the list order aligns with target distribution.

Refer this link for more details : https://www.geeksforgeeks.org/meta-binary-search-one-sided-binary-search/

Time Complexity : O(log N)
Space Complexity : O(1)


For doctests run following command:
python3 -m doctest -v meta_binary_search.py

For manual testing run:
python3 meta_binary_search.py
"""

import math


def meta_binary_search(_Array: list, key_to_search: int) -> int:
    # Initial Interval of size n that includes the entire array
    n = len(_Array)

    # Set number of bits to represent
    lg = int(math.log2(n - 1)) + 1

    # largest array index
    # while ((1 << lg) < n - 1):
    # lg += 1

    pos = 0
    for i in range(lg - 1, -1, -1):
        if _Array[pos] == key_to_search:
            return pos

        # Incrementally construct the
        # index of the target value
        new_pos = pos | (1 << i)

        # find the element in one
        # direction and update position
        if (new_pos < n) and (_Array[new_pos] <= key_to_search):
            pos = new_pos

    # if element found return
    # pos otherwise -1
    return pos if (_Array[pos] == key_to_search) else -1


# Driver code
if __name__ == "__main__":
    user_input = input("Enter numbers separated by comma: ").strip()
    collection = [int(item.strip()) for item in user_input.split(",")]
    assert collection == sorted(collection), f"List must be ordered.\n{collection}."

    target = int(input("Enter the number to be found in the list: ").strip())

    result = meta_binary_search(collection, target)

    if result != -1:
        print(f"{target} found at position: {result}")
