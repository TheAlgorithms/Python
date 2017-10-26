class UnionFind():
    """
    https://en.wikipedia.org/wiki/Disjoint-set_data_structure

    The union-find is a disjoint-set data structure

    You can merge two sets and tell if one set belongs to
    another one.

    It's used on the Kruskal Algorithm
    (https://en.wikipedia.org/wiki/Kruskal%27s_algorithm)

    The elements are in range [0, size]
    """
    def __init__(self, size):
        if size <= 0:
            raise ValueError("size should be greater than 0")

        self.size = size

        # The below plus 1 is because we are using elements
        # in range [0, size]. It makes more sense.

        # Every set begins with only itself
        self.root = [i for i in range(size+1)]

        # This is used for heuristic union by rank
        self.weight = [0 for i in range(size+1)]

    def union(self, u, v):
        """
        Union of the sets u and v.
        Complexity: log(n).
        Amortized complexity: < 5 (it's very fast).
        """

        self._validate_element_range(u, "u")
        self._validate_element_range(v, "v")

        if u == v:
            return

        # Using union by rank will guarantee the
        # log(n) complexity
        rootu = self._root(u)
        rootv = self._root(v)
        weight_u = self.weight[rootu]
        weight_v = self.weight[rootv]
        if weight_u >= weight_v:
            self.root[rootv] = rootu
            if weight_u == weight_v:
                self.weight[rootu] += 1
        else:
            self.root[rootu] = rootv

    def same_set(self, u, v):
        """
        Return true if the elements u and v belongs to
        the same set
        """

        self._validate_element_range(u, "u")
        self._validate_element_range(v, "v")

        return self._root(u) == self._root(v)

    def _root(self, u):
        """
        Get the element set root.
        This uses the heuristic path compression
        See wikipedia article for more details.
        """

        if u != self.root[u]:
            self.root[u] = self._root(self.root[u])

        return self.root[u]

    def _validate_element_range(self, u, element_name):
        """
        Raises ValueError if element is not in range
        """
        if u < 0 or u > self.size:
            msg = ("element {0} with value {1} "
                   "should be in range [0~{2}]")\
                  .format(element_name, u, self.size)
            raise ValueError(msg)
