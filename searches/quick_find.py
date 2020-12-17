"""
Algorithm to find and output linked joints.
Explanation found here https://ducmanhphan.github.io/2019-03-20-Quick-Union/
"""
import random

from typing import List, Tuple


class QuickUnion:
    """Class with methods to perform a quick union on a 2D list. Uses N array access."""

    def __init__(self, *, connections_len: int = 0, connections: List[Tuple[int, int]] = None) -> None:
        """
        Accepts either a 2D list of connections or an int connections_len.

        connections_len: optional argument for generating an example list

        connections: optional argument to be used instead of connections_len.
        It should be a 2d list that represents the relationships of joints
        where nested values should represent two connected values.
        example: [(1, 2), (2, 3)] indicates 1 is connected to 2 and 2 is connected to 3.
        """
        if connections:
            # if connections_len was passed with connections
            if connections_len:
                raise ValueError(
                    "argument connections_len should not be passed if connections are used"
                )

            self.sequence = [x for x in range(0, len(connections))]
            self.connections = connections
        else:
            self.sequence = [x for x in range(0, connections_len)]
            self.connections = self.create_sample_connections()

    def __str__(self) -> str:
        """
        >>> print(str(QuickUnion(connections_len=3)))
        '[0, 1, 2]'
        """
        return str(self.sequence)

    def create_sample_connections(self) -> list:
        """
        Generates a sample 2D list based on the connections_len value passed to the instance.
        >>> print(type(QuickUnion(connections_len=2).connections) == list
        >>> and len(QuickUnion(connections_len=2).connections) == 2)
        True
        """
        connections = []
        data_set = self.sequence
        for _ in data_set:
            connections.append((random.choice(data_set), random.choice(data_set)))
        return connections

    def root(self, i: int) -> int:
        """Reduce i to a common connection."""
        while i != self.sequence[i]:
            self.sequence[i] = self.sequence[self.sequence[i]]
            i = self.sequence[i]
        return i

    def is_connected(self, first: int, second: int) -> bool:
        """Checks if two values are connected."""
        return self.root(first) == self.root(second)

    def union(self, first: int, second: int) -> None:
        """Form/find the union between two values."""
        first_int = self.root(first)
        sec_int = self.root(second)

        if first_int == sec_int:  # weighted to join smaller trees to larger
            return
        else:
            self.sequence[first_int] = sec_int


def run_test(connection_len: int = None, connections: List[Tuple[int, int]] = None):
    """
    >>> run_test(connections=[(1, 1), (3, 4), (0, 1), (4, 2), (4, 3)])
    '[1, 1, 2, 2, 2]'
    """
    test = QuickUnion(connections_len=connection_len, connections=connections)
    for connection in test.connections:
        test.union(connection[0], connection[1])
    return str(test)


if __name__ == "__main__":
    """
    Example of how this algorithm can be used.
    """
    print(run_test(connections=[(1, 1), (3, 4), (0, 1), (4, 2), (4, 3)]))
