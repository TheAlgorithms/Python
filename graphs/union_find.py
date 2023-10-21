"""
Implementation of a union-find!
If you want to do doctest:
python3 -m doctest -v union_find.py
"""


class UnionFind:
    def __init__(self, n: int) -> None:
        """
        Initialize a unionfind
        n is the numbers of the initial trees
        """
        self.pa = list(range(n))
        self.size = [1] * n  # size of the current

    def find(self, x: int) -> int:
        """
        Returns the parent of the element x (root element).
        >>> uf = UnionFind(3)
        >>> uf.find(2)
        2
        >>> uf.find(1)
        1
        """
        if self.pa[x] != x:
            self.pa[x] = self.find(self.pa[x])
        return self.pa[x]

    def union(self, x: int, y: int) -> None:
        """
        x and y are trees.
        Returns the union of tree x and tree y.
        we connect a tree with fewer nodes to another tree.
        >>> uf = UnionFind(9)
        >>> uf.union(2,3)
        >>> uf.find(3)
        2
        >>> uf.union(3,4)
        >>> uf.find(4)
        2
        """
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.pa[y] = x
        self.size[x] += self.size[y]

    def get_size(self, x: int) -> int:
        """
        Returns the size of tree x that contains its children
        x is the tree that you want to get its size
        >>> uf = UnionFind(4)
        >>> uf.get_size(1)
        1
        >>> uf.union(1,2)
        >>> uf.get_size(1)
        2
        """
        return self.size[x]


if __name__ == "__main__":
    # test
    uf = UnionFind(6)
    uf.union(1, 2)
    uf.union(2, 4)
    assert uf.get_size(1) == 3
