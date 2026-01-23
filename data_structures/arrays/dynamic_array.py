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
        >>> arr.append(4)
        >>> arr.array[:arr.size]
        [1, 2, 3, 4]
        >>> arr.append(5)
        >>> arr.array[:arr.size]
        [1, 2, 3, 4, 5]
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
        >>> arr._resize(10)
        >>> arr.capacity
        10
        >>> arr.array[:arr.size]
        [1, 2]
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
        >>> arr.get(-1)
        Traceback (most recent call last):
        ...
        IndexError: index out of range
        """
        if index < 0 or index >= self.size:
            raise IndexError("index out of range")
        return self.array[index]

    def __setitem__(self, index: int, value: int) -> None:
        if index < 0 or index >= self.size:
            raise IndexError("index out of range")
        self.array[index] = value

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
        >>> arr.append(3)
        >>> len(arr)
        3
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
        >>> arr.append(4)
        >>> str(arr)
        '[1, 2, 3, 4]'
        """
        return "[" + ", ".join(str(self.array[i]) for i in range(self.size)) + "]"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
