"""Algorithm to find and output linked joints."""
import random


class QuickUnion:
    """Class with methods to perform a quick union on a 2D list. Uses N array access."""

    def __init__(self, *, n: int = 0, connections: list = None):
        """
        Accepts either a 2D list of connections or an int n.

        n: optional argument for generating an example list

        connections: optional argument to be used instead of n.
        It should be a 2d list that represents the relationships of joints
        where nested vaules should represent two connected values.
        example: [(1, 2), (2, 3)] indicates 1 is connected to 2 and 2 is connected to 3.
        """
        if connections:
            # if n was passed with connections
            if n:
                raise ValueError(
                    "argument n should not be passed if connections are used"
                )

            self.id = [x for x in range(0, len(connections))]
            self.connections = connections
        else:
            self.id = [x for x in range(0, n)]
            self.connections = self.create_sample_connections()

    def __str__(self):
        return str(self.id)

    def create_sample_connections(self):
        """Generates a sample 2D list based on the n value passed to the instance."""
        connections = []
        data_set = self.id
        for _ in data_set:
            connections.append((random.choice(data_set), random.choice(data_set)))
        return connections

    def root(self, i):
        """Reduce i to a common connection."""
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]  # one-pass path compression improvement
            i = self.id[i]
        return i

    def is_connected(self, p, q):
        """Checks if two values are connected."""
        return self.root(p) == self.root(q)

    def union(self, p, q):
        """Form/find the union between two values."""
        i = self.root(p)
        j = self.root(q)

        if i == j:  # weighted to join smaller trees to larger
            return
        else:
            self.id[i] = j


if __name__ == "__main__":
    """Example of how this algorithm can be used."""
    test = QuickUnion(connections=[(1, 1), (3, 4), (0, 1), (4, 2), (4, 3)])
    for connection in test.connections:
        test.union(connection[0], connection[1])
    print(test)
