"""
Author  : Yashwanth Adimulam
Date    : October 22, 2024

Implement the class of DynamicArray with useful functions based on it.
References: https://en.wikipedia.org/wiki/Dynamic_array
            https://www.geeksforgeeks.org/how-do-dynamic-arrays-work/

"""


class DynamicArray:
    def __init__(self) -> None:
        self.size = 0  # Number of elements in the array
        self.capacity = 1  # Initial capacity of the array
        self.array = [None] * self.capacity  # Create an array with initial capacity

    def append(self, item: int) -> None:
        """
        The function adds an item to the end of the dynamic array.

        Runtime : O(1) amortized
        Space: O(1) amortized

        >>> arr = DynamicArray()
        >>> arr.append(1)
        >>> arr.append(2)
        >>> arr.append(3)
        >>> arr.array[:arr.size]  # Display only the filled part of the array
        [1, 2, 3]
        """
        if self.size == self.capacity:
            self._resize(2 * self.capacity)  # Double the capacity

        self.array[self.size] = item
        self.size += 1

    def _resize(self, new_capacity: int) -> None:
        """
        Resizes the array to the new capacity.

        Runtime : O(n)
        Space: O(n)

        >>> arr = DynamicArray()
        >>> arr.append(1)
        >>> arr.append(2)
        >>> arr.append(3)
        >>> arr._resize(10)
        >>> arr.capacity
        10
        """
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def get(self, index: int) -> int:
        """
        The function returns the item at the specified index.

        Runtime : O(1)
        Space: O(1)

        >>> arr = DynamicArray()
        >>> arr.append(1)
        >>> arr.append(2)
        >>> arr.get(0)
        1
        >>> arr.get(1)
        2
        >>> arr.get(2)
        Traceback (most recent call last):
        ...
        IndexError: index out of range
        """
        if index < 0 or index >= self.size:
            raise IndexError("index out of range")
        return self.array[index]

    def __len__(self) -> int:
        """
        Returns the number of elements in the dynamic array.

        Runtime : O(1)
        Space: O(1)

        >>> arr = DynamicArray()
        >>> arr.append(1)
        >>> len(arr)
        1
        >>> arr.append(2)
        >>> len(arr)
        2
        """
        return self.size

    def __str__(self) -> str:
        """
        Returns a string representation of the dynamic array.

        >>> arr = DynamicArray()
        >>> arr.append(1)
        >>> arr.append(2)
        >>> arr.append(3)
        >>> str(arr)
        '[1, 2, 3]'
        """
        return "[" + ", ".join(str(self.array[i]) for i in range(self.size)) + "]"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
