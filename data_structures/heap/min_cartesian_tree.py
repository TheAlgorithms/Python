class min_cartesian_tree:
    """
    Implementation of the Cartesian tree, a detailed description can be found in:
    https://en.wikipedia.org/wiki/Cartesian_tree

    In short, the tree is a min heap (so that the root always the smallest), and
    the in order traversal of the tree is the same as the input order.

    The insert operation is amortized O(1), the can be seen by observing a
    node enter and leave the right most spine at most once. Once it leaves the
    rightmost spine, it will never be processed by insert again.

    Turn your head right 90 degree to visualize the tree.

    >>> m = min_cartesian_tree()
    >>> for i in [3, 0, 6, 2, 4, 7, 0, 0]:
    ...     m.insert(i)
    >>> print(m)
    [3, 0, 6, 2, 4, 7, 0, 0]
            null
          3
            null
        0
              null
            6
              null
          2
              null
            4
                null
              7
                null
      0
        null
    0
      null
    """

    def __init__(self):
        self.__storage = []
        self.__parent = []
        self.__left = []
        self.__right = []
        self.__root = -1

    def insert(self, v):
        n = len(self.__storage)
        self.__storage.append(v)
        self.__left.append(-1)
        self.__right.append(-1)
        self.__parent.append(n - 1)
        if n > 0:
            self.__right[n - 1] = n
        else:
            self.__root = 0
        c = self.__parent[n]
        while c != -1:
            if self.__storage[c] < self.__storage[n]:
                break
            else:
                nc = self.__parent[c]
                left = self.__left[n]
                self.__right[c] = -1
                self.__parent[n] = -1
                if nc != -1:
                    self.__right[nc] = n
                self.__parent[n] = nc
                self.__left[n] = c
                self.__parent[c] = n
                self.__right[c] = left
                if left != -1:
                    self.__parent[left] = n
                c = nc
        if c == -1:
            self.__root = n

    def __to_string(self, root, indent):
        spaces = ""
        for i in range(0, indent):
            spaces = spaces + " "
        result = ""
        if root == -1:
            result = result + spaces + "null\n"
        else:
            result = result + self.__to_string(self.__left[root], indent + 2)
            result = result + spaces + str(self.__storage[root]) + "\n"
            result = result + self.__to_string(self.__right[root], indent + 2)
        return result

    def __str__(self):
        return (str(self.__storage) + "\n" + self.__to_string(self.__root, 0)).strip()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
