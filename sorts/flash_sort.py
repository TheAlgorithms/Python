"""
Implementation of Flash Sort in Python
Author: Yash Kiradoo

For doctests, run the following command:
python3 -m doctest -v flash_sort.py

For manual testing, run:
python3 flash_sort.py
"""

from __future__ import annotations
from collections.abc import Callable


class FlashSort:
    def __init__(self, arr: list[int], n_classes: int, sort_key: Callable[[int], int] = lambda x: x):
        self.arr = arr
        self.n = len(arr)
        self.n_classes = n_classes
        self.sort_key = sort_key

    def flash_sort(self) -> None:
        """
        Performs flash sort on the array in-place.

        >>> arr = [5, 3, 8, 6, 2, 7, 4, 1]
        >>> sorter = FlashSort(arr, n_classes=5)
        >>> sorter.flash_sort()
        >>> arr
        [1, 2, 3, 4, 5, 6, 7, 8]

        >>> arr = [1]
        >>> sorter = FlashSort(arr, n_classes=1)
        >>> sorter.flash_sort()
        >>> arr
        [1]

        >>> arr = [2, 2, 2]
        >>> sorter = FlashSort(arr, n_classes=2)
        >>> sorter.flash_sort()
        >>> arr
        [2, 2, 2]
        """
        if self.n <= 1:
            return

        min_val = min(self.arr, key=self.sort_key)
        max_val = max(self.arr, key=self.sort_key)

        if self.sort_key(min_val) == self.sort_key(max_val):
            return

        l = [0] * self.n_classes  # renamed L to l
        c1 = (self.n_classes - 1) / (self.sort_key(max_val) - self.sort_key(min_val))

        # Classification step
        for i in range(self.n):
            k = int(c1 * (self.sort_key(self.arr[i]) - self.sort_key(min_val)))
            l[k] += 1

        # Cumulative step
        for i in range(1, self.n_classes):
            l[i] += l[i - 1]

        # Permutation step
        i, nmove, flash = 0, 0, self.arr[0]
        while nmove < self.n:
            while i >= l[int(c1 * (self.sort_key(flash) - self.sort_key(min_val)))]:
                i += 1
                flash = self.arr[i]
            k = int(c1 * (self.sort_key(flash) - self.sort_key(min_val)))

            while i != l[k]:
                k = int(c1 * (self.sort_key(flash) - self.sort_key(min_val)))
                hold = self.arr[l[k] - 1]
                self.arr[l[k] - 1] = flash
                flash = hold
                l[k] -= 1
                nmove += 1

        # Final step: Insertion sort to finish
        for i in range(1, self.n):
            key_item = self.arr[i]
            j = i - 1
            while j >= 0 and self.arr[j] > key_item:
                self.arr[j + 1] = self.arr[j]
                j -= 1
            self.arr[j + 1] = key_item


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    if user_input == "":
        unsorted = []
    else:
        unsorted = [int(item.strip()) for item in user_input.split(",")]
    sorter = FlashSort(unsorted, n_classes=5)
    sorter.flash_sort()
    print(unsorted)
