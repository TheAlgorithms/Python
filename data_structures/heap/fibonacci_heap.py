# Reference: https://en.wikipedia.org/wiki/Fibonacci_heap

import math


class FibonacciTree:
    """
    FibonacciTree represents a node in a Fibonacci heap.

    Attributes:
        key (int): The key value associated with the node.
        children (list): A list of child nodes.
        order (int): The number of children the node has.
    """

    def __init__(self, key: int) -> None:
        self.key = key
        self.children: list["FibonacciTree"] = []
        self.order = 0

    def add_at_end(self, child_node: "FibonacciTree") -> None:
        """
        Adds a child node 'child_node' to the end of the children list.

        Args:
            child_node (FibonacciTree): The child node to add.
        """
        self.children.append(child_node)
        self.order = self.order + 1


class FibonacciHeap:
    """
    FibonacciHeap represents a priority queue data structure with efficient
    amortized time complexities for various operations.

    Usage:
    >>> heap = FibonacciHeap()
    >>> heap.insert(5)
    >>> heap.insert(3)
    >>> heap.insert(7)
    >>> heap.get_min()
    3
    >>> heap.extract_min()
    3
    >>> heap.get_min()
    5

    Attributes:
        trees (list): A list of FibonacciTree objects.
        least (FibonacciTree | None): A reference to the node with the minimum key.
        count (int): The total number of nodes in the heap.
    """

    def __init__(self) -> None:
        self.trees: list["FibonacciTree"] = []
        self.least = None
        self.count = 0

    def insert(self, key: int) -> None:
        """
        Inserts a new node with the given key into the Fibonacci heap.

        Args:
            key (int): The key to insert.
        """
        new_tree = FibonacciTree(key)
        self.trees.append(new_tree)
        if self.least is None or key < self.least.key:
            self.least = new_tree
        self.count = self.count + 1

    def get_min(self) -> int | None:
        """
        Returns the minimum key in the Fibonacci heap.

        Returns:
            int: The minimum key.
        """
        if self.least is None:
            return None
        return self.least.key

    def extract_min(self) -> int | None:
        """
        Removes and returns the node with the minimum key from the Fibonacci heap.

        Returns:
            int: The minimum key.
        """
        if (smallest := self.least) is not None:
            for child in smallest.children:
                if child is not None:
                    self.trees.append(child)
            self.trees.remove(smallest)
            if self.trees:
                self.least = self.trees[0]
                self.consolidate()
            else:
                self.least = None
            self.count = self.count - 1
            return smallest.key
        return None

    def consolidate(self) -> None:
        """
        Consolidates trees in the Fibonacci heap to maintain the heap's structure.
        """
        max_degree = floor_log2(self.count) + 1  # Maximum possible degree
        aux = [None] * max_degree

        # Filter out None values from self.trees
        valid_trees = [tree for tree in self.trees if tree is not None]

        while valid_trees:
            x = valid_trees[0]
            order = x.order
            valid_trees.remove(x)
            while aux[order] is not None:
                y = aux[order]
                if x.key > y.key:
                    x, y = y, x
                x.add_at_end(y)
                aux[order] = None
                order = order + 1
            aux[order] = x

        self.least = None
        for k in aux:
            if k is not None:
                self.trees.append(k)
                if self.least is None:
                    self.least = k
                    continue
                if self.least.key > k.key:
                    self.least = k
                    continue


def floor_log2(x: int) -> int:
    """
    Computes the floor of the base-2 logarithm of 'x'.

    Args:
        x (int): The input number.

    Returns:
        int: The floor of the base-2 logarithm of 'x'.
    """
    return math.floor(math.log2(x)) if x > 0 else 0


# Doctest for floor_log2
if __name__ == "__main__":
    import doctest

    doctest.testmod()

if __name__ == "__main__":
    import doctest

    doctest.testmod()
