class FenwickTree:
    def __init__(self, arg):
        """
        Creates a Fenwick Tree

        args: arg(two ways)
            1. If arg is an integer, it creates a Fenwick tree
               of size arg
            2. If arg is of type (list, tuple, set), it creates
               a Fenwick tree with the contents in the list
        """
        if isinstance(arg, int):
            self.size = arg
        else:
            self.size = len(arg) + 1
        self.tree = [0 for i in range(self.size)]

        if not isinstance(arg, int):
            for i, val in enumerate(arg):
                self.update(i + 1, val)

    def add(self, i, val):
        """
        Increases (/decreases) the value at index i with <val>

        While updating a list consider 1-indexing (add 1 to 0-indexing)
        """
        while i < self.size:
            self.tree[i] += val
            i += i & (-i)

    def update(self, i, val):
        """
        Updates the value at index i with <val>

        While updating a list consider 1-indexing (add 1 to 0-indexing)
        """
        orig = self.range_query(i, i)  # value at i-index
        self.add(i, val - orig)

    def query(self, i):
        """
        Queries the cumulative sum from index 1 to i (inclusive) 
        (indices in 1-indexing)
        """
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & (-i)

        return res

    def range_query(self, i, j):
        """
        Queries the total sum from i-index to j-index (inclusive)

        (indices in 1-indexing)
        """
        return self.query(j) - self.query(i - 1)


if __name__ == "__main__":
    f = FenwickTree(100)
    f.add(1, 20)
    f.add(4, 4)
    print(f.query(1))
    print(f.query(3))
    print(f.query(4))
    f.add(2, -5)
    print(f.query(1))
    print(f.query(3))
    f.update(2, 10)
    print(f.query(1))
    print(f.query(2))

    # List arguments
    fen = FenwickTree([1, 2, 3, 4, 5])
    fen.add(1, 1)
    print(fen.query(1))
    print(fen.query(5))
    fen.update(1, 10)
    print(fen.query(1))
    print(fen.query(3))
    print(fen.range_query(3, 5))
