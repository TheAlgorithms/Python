"""
Heap's (iterative) algorithm returns the list of all permutations possible from a list.
It minimizes movement by generating each permutation from the previous one
by swapping only two elements.
More information:
https://en.wikipedia.org/wiki/Heap%27s_algorithm.
"""

def heaps(arr: list) -> list:
    """
    Pure python implementation of the Heap's algorithm (recursive version),
    returning all permutations of a list.
     >>> heaps([])
    [()]
    >>> heaps([0])
    [(0,)]
    >>> heaps([-1, 1])
    [(-1, 1), (1, -1)]
    >>> heaps([1, 2, 3])
    [(1, 2, 3), (2, 1, 3), (3, 1, 2), (1, 3, 2), (2, 3, 1), (3, 2, 1)]
    >>> from itertools import permutations
    >>> sorted(heaps([1,2,3])) == sorted(permutations([1,2,3]))
    True
    >>> all(sorted(heaps(x)) == sorted(permutations(x))
    ...     for x in ([], [0], [-1, 1], [1, 2, 3]))
    True
    """

    def generate(k: int, arr: list, res: list):
        if k == 1:
            res.append(tuple(arr))
            return

        generate(k - 1, arr, res)

        for i in range(k - 1):
            if k % 2 == 0:  # k is even
                arr[i], arr[k - 1] = arr[k - 1], arr[i]
            else:  # k is odd
                arr[0], arr[k - 1] = arr[k - 1], arr[0]
            generate(k - 1, arr, res)

    if len(arr) <= 1:
        return [tuple(arr)]

    res = []
    generate(len(arr), arr, res)
    return res


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    arr = [int(item) for item in user_input.split(",")]
    print(heaps(arr))

# Changes made:
# 1. Removed unnecessary slicing `arr[:]`:
#    - Original code was creating a new copy of the array each time which was not necessary.
#    - Directly used `arr` for appending to the result list.
# 2. Removed the global list `res`:
#    - Original function relied on a global variable which isn't always clear in purpose.
#    - Refactored the function to pass `res` as an argument, making the recursion's intent clearer.
