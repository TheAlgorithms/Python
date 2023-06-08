"""
A number container system that uses binary search to delete and insert values into
arrays with O(n logn) write times and O(1) read times.

This container system holds integers at indexes.

Further explained in this leetcode problem
> https://leetcode.com/problems/minimum-cost-tree-from-leaf-values
"""


class NumberContainer:
    def __init__(self) -> None:
        # numbermap keys are the number and its values are lists of indexes sorted
        # in ascending order
        self.numbermap: dict[int, list[int]] = {}
        # indexmap keys are an index and it's values are the number at that index
        self.indexmap: dict[int, int] = {}

    def binary_search_delete(self, array: list[int], item: int) -> list[int]:
        """
        Removes the item from the array and returns
        the new array.

        >>> NumberContainer().binary_search_delete([1,2,3], 2)
        [1, 3]
        >>> NumberContainer().binary_search_delete([], 0)
        Traceback (most recent call last):
            ...
        ValueError: The item is not in the array, and therefore cannot be deleted
        """
        low = 0
        high = len(array) - 1

        while low <= high:
            mid = (low + high) // 2
            if array[mid] == item:
                array.pop(mid)
                return array
            elif array[mid] < item:
                low = mid + 1
            else:
                high = mid - 1
        raise ValueError(
            "The item is not in the array, and therefore cannot be deleted"
        )

    def binary_search_insert(self, array: list[int], index: int) -> list[int]:
        """
        Inserts the index into the sorted array
        at the correct position

        >>> NumberContainer().binary_search_insert([1,2,3], 2)
        [1, 2, 2, 3]
        >>> NumberContainer().binary_search_insert([0,1,3], 2)
        [0, 1, 2, 3]
        """
        low = 0
        high = len(array) - 1

        while low <= high:
            mid = (low + high) // 2
            if array[mid] == index:
                # If the item already exists in the array,
                # insert it after the existing item
                array.insert(mid + 1, index)
                return array
            elif array[mid] < index:
                low = mid + 1
            else:
                high = mid - 1

        # If the item doesn't exist in the array, insert it at the appropriate position
        array.insert(low, index)
        return array

    def change(self, index: int, number: int) -> None:
        """
        Changes (sets) the index as number

        >>> cont = NumberContainer()
        >>> cont.change(0, 10)
        >>> cont.change(0, 20)
        >>> cont.change(-1, 20)
        """
        # Remove previous index
        if index in self.indexmap:
            n = self.indexmap[index]
            if len(self.numbermap[n]) == 1:
                del self.numbermap[n]
            else:
                self.numbermap[n] = self.binary_search_delete(self.numbermap[n], index)

        # Set new index
        self.indexmap[index] = number

        # Number not seen before or empty so insert number value
        if number not in self.numbermap:
            self.numbermap[number] = [index]

        # Here we need to perform a binary search insertion in order to insert
        # The item in the correct place
        else:
            self.numbermap[number] = self.binary_search_insert(
                self.numbermap[number], index
            )

    def find(self, number: int) -> int:
        """
        Returns the smallest index where the number is.

        >>> cont = NumberContainer()
        >>> cont.find(10)
        -1
        >>> cont.change(0, 10)
        >>> cont.find(10)
        0
        >>> cont.change(0, 20)
        >>> cont.find(10)
        -1
        >>> cont.find(20)
        0
        """
        # Simply return the 0th index (smallest) of the indexes found (or -1)
        return self.numbermap.get(number, [-1])[0]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
