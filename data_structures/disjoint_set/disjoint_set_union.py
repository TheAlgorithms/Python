"""
Disjoint Set Union (Union-Find) data structure with path compression
and union by rank optimizations.

Reference: https://en.wikipedia.org/wiki/Disjoint-set_data_structure

Time Complexity:
    - find: O(alpha(n)) amortized, where alpha is the inverse Ackermann function
    - union: O(alpha(n)) amortized
    - connected: O(alpha(n)) amortized

Space Complexity: O(n)
"""


class DisjointSetUnion:
    """
    A Disjoint Set Union (Union-Find) data structure supporting efficient
    union and find operations with path compression and union by rank.

    >>> dsu = DisjointSetUnion(5)
    >>> dsu.find(0)
    0
    >>> dsu.union(0, 1)
    >>> dsu.connected(0, 1)
    True
    >>> dsu.connected(0, 2)
    False
    >>> dsu.union(1, 2)
    >>> dsu.connected(0, 2)
    True
    """

    def __init__(self, size: int) -> None:
        """
        Initialize a Disjoint Set Union with `size` elements (0 to size-1).

        Args:
            size: The number of elements in the disjoint set.

        Raises:
            ValueError: If size is not a positive integer.

        >>> dsu = DisjointSetUnion(5)
        >>> len(dsu.parent)
        5
        >>> dsu = DisjointSetUnion(0)
        Traceback (most recent call last):
            ...
        ValueError: size must be a positive integer
        >>> dsu = DisjointSetUnion(-1)
        Traceback (most recent call last):
            ...
        ValueError: size must be a positive integer
        """
        if size <= 0:
            raise ValueError("size must be a positive integer")
        self.size = size
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, element: int) -> int:
        """
        Find the representative (root) of the set containing `element`.
        Uses path compression for optimization.

        Args:
            element: The element to find the representative of.

        Returns:
            The representative of the set containing element.

        Raises:
            IndexError: If element is out of bounds.

        >>> dsu = DisjointSetUnion(5)
        >>> dsu.find(0)
        0
        >>> dsu.union(0, 1)
        >>> dsu.find(1) == dsu.find(0)
        True
        >>> dsu.find(5)
        Traceback (most recent call last):
            ...
        IndexError: element 5 is out of bounds for size 5
        >>> dsu.find(-1)
        Traceback (most recent call last):
            ...
        IndexError: element -1 is out of bounds for size 5
        """
        if element < 0 or element >= self.size:
            msg = f"element {element} is out of bounds for size {self.size}"
            raise IndexError(msg)

        if self.parent[element] != element:
            self.parent[element] = self.find(self.parent[element])
        return self.parent[element]

    def union(self, element1: int, element2: int) -> None:
        """
        Merge the sets containing `element1` and `element2`.
        Uses union by rank for optimization.

        Args:
            element1: An element in the first set.
            element2: An element in the second set.

        Raises:
            IndexError: If either element is out of bounds.

        >>> dsu = DisjointSetUnion(5)
        >>> dsu.union(0, 1)
        >>> dsu.connected(0, 1)
        True
        >>> dsu.union(2, 3)
        >>> dsu.union(0, 3)
        >>> dsu.connected(1, 2)
        True
        >>> dsu.union(4, 4)  # Self-union should not corrupt the structure
        >>> dsu.find(4)
        4
        >>> dsu.union(5, 0)
        Traceback (most recent call last):
            ...
        IndexError: element 5 is out of bounds for size 5
        """
        root1 = self.find(element1)
        root2 = self.find(element2)

        if root1 == root2:
            return

        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1

    def connected(self, element1: int, element2: int) -> bool:
        """
        Check if `element1` and `element2` belong to the same set.

        Args:
            element1: The first element.
            element2: The second element.

        Returns:
            True if both elements are in the same set, False otherwise.

        Raises:
            IndexError: If either element is out of bounds.

        >>> dsu = DisjointSetUnion(5)
        >>> dsu.connected(0, 1)
        False
        >>> dsu.union(0, 1)
        >>> dsu.connected(0, 1)
        True
        >>> dsu.connected(1, 0)
        True
        >>> dsu.connected(0, 0)
        True
        >>> dsu.connected(0, 5)
        Traceback (most recent call last):
            ...
        IndexError: element 5 is out of bounds for size 5
        """
        return self.find(element1) == self.find(element2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
