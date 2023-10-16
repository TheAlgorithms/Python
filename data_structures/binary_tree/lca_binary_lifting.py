"""

Let G be a tree.

For every query of the form (u, v)
we want to find the LCA of the nodes
u and v, i.e. we want to find a node w that lies
on the path from u to the root node, that
lies on the path from v to the root node,
and if there are multiple nodes we pick the
one that is farthest away from the root node.

In other words the desired node w is the
lowest ancestor of u and v.
In particular if u is an ancestor of v,
then u is their lowest common ancestor.

This algorithm will need O(Nlog N) for
preprocessing the tree,
and then O(log N) for each LCA query.

"""

import math

#  Abbreviations:
#  n: number of nodes in the graph
#  adj: adjacency list for the graph
#  timer: keeps track of the current time
#  tin: entry time for the node (time of first visit)
#  tout: exit time for the node (time of last visit)
#  l: logarithmic depth
#  up: ancestors list


class TreeLCA:
    # Constructor
    def __init__(self, nodes: int) -> None:
        """
        Initialize a TreeLCA instance with
        the specified number of nodes.

        Args:
            nodes (int): The number of nodes in the tree.

        Returns:
            None

        This constructor initializes the TreeLCA instance
        with the given number of nodes
        and sets up data structures
        for storing tree information.

        >>> tree = TreeLCA(7)
        >>> tree.n
        7
        >>> tree.adj
        [[], [], [], [], [], [], []]
        >>> tree.timer
        0
        >>> tree.tin
        [0, 0, 0, 0, 0, 0, 0]
        >>> tree.tout
        [0, 0, 0, 0, 0, 0, 0]
        >>> tree.l
        0
        >>> tree.up
        []
        """

        # Initialize the number of nodes,
        # adjacency list, timer,
        # entry and exit times,
        # logarithmic depth, and 'up' list
        self.n: int = nodes
        self.adj: list[list[int]] = [[] for _ in range(nodes)]
        self.timer: int = 0
        self.tin: list[int] = [0] * nodes
        self.tout: list[int] = [0] * nodes
        self.l: int = 0
        self.up: list[list[int]] = []

    # Constructing graph by adding edges
    def add_edge(self, node_1: int, node_2: int) -> None:
        """
        Add an edge between two nodes in the tree.

        Args:
            node_1 (int): The first node.
            node_2 (int): The second node.

        Returns:
            None

        This method adds an edge between 'node_1' and 'node_2'
        by updating the adjacency list for both nodes.

        >>> tree = TreeLCA(5)
        >>> tree.add_edge(0, 1)
        >>> tree.add_edge(0, 2)
        >>> tree.add_edge(1, 3)
        >>> tree.add_edge(1, 4)
        >>> tree.adj
        [[1, 2], [0, 3, 4], [0], [1], [1]]

        """
        self.adj[node_1].append(node_2)
        self.adj[node_2].append(node_1)

    def dfs(self, node: int, parent: int) -> None:
        """
        Perform a depth-first search (DFS) traversal of the tree to
        compute important information for LCA.

        Args:
            node (int): The current node being processed.
            parent (int): The parent of the current node.

        Returns:
            None

        This method calculates entry and exit times,
        stores parent-child relationships,
        and prepares the 'up' list
        to efficiently find the Lowest Common Ancestor (LCA)
        of nodes in the tree using a binary lifting technique.

        >>> n = 9
        >>> tree = TreeLCA(n)
        >>> edges = [
        ...     [0, 1],
        ...     [0, 2],
        ...     [0, 3],
        ...     [1, 4],
        ...     [2, 5],
        ...     [2, 6],
        ...     [2, 7],
        ...     [3, 8],
        ... ]
        >>> for u, v in edges:
        ...     tree.add_edge(u, v)
        >>> root = 0
        >>> tree.preprocess(root)  # Preprocess the tree
        >>> tree.dfs(root, root)  # Start DFS traversal from the root
        >>> tree.tin
        [9, 9, 11, 15, 9, 11, 12, 13, 15]
        >>> tree.tout
        [18, 11, 15, 17, 10, 12, 13, 14, 16]
        """

        self.tin[node] = self.timer
        self.up[node][0] = parent

        # Calculate ancestors for binary lifting
        for i in range(1, self.l + 1):
            self.up[node][i] = self.up[self.up[node][i - 1]][i - 1]
        # Traverse adjacent nodes
        for u in self.adj[node]:
            if u != parent:
                self.dfs(u, node)
        self.timer += 1  # Increment timer for exit time
        self.tout[node] = self.timer

    def is_ancestor(self, parent: int, node: int) -> bool:
        """
        Check if 'parent' is an ancestor of 'node' in the tree
        based on entry and exit times.

        Args:
            parent (int): The potential ancestor node.
            node (int): The potential descendant node.

        Returns:
            bool: True if 'parent' is ancestor of 'node'
            False otherwise.

        This method uses entry and exit times stored
        during preprocessing to determine
        if 'parent' is an ancestor of 'node'
        in the tree.
        It returns True if 'parent' is an
        ancestor of 'node', and False otherwise.

        >>> n = 9
        >>> tree = TreeLCA(n)
        >>> edges = [
        ...     [0, 1],
        ...     [0, 2],
        ...     [0, 3],
        ...     [1, 4],
        ...     [2, 5],
        ...     [2, 6],
        ...     [2, 7],
        ...     [3, 8],
        ... ]
        >>> for u, v in edges:
        ...     tree.add_edge(u, v)
        >>> root = 0
        >>> tree.preprocess(root)
        >>> tree.is_ancestor(0, 4)
        True
        >>> tree.is_ancestor(4, 0)
        False
        >>> tree.is_ancestor(2, 7)
        True
        >>> tree.is_ancestor(8, 3)
        False
        >>> tree.is_ancestor(5, 1)
        False
        >>> tree.is_ancestor(0, 8)
        True

        """

        return (
            self.tin[parent] <= self.tin[node] and self.tout[parent] >= self.tout[node]
        )

    def lca(self, node_1: int, node_2: int) -> int:
        """
        Find the Lowest Common Ancestor (LCA) of
        two nodes 'node_1' and 'node_2' in the tree.

        Args:
            node_1 (int): The first node.
            node_2 (int): The second node.

        Return:
            int: The LCA node of 'node_1' and 'node_2'.

        >>> n = 9
        >>> tree = TreeLCA(n)
        >>> edges = [
        ...     [0, 1],
        ...     [0, 2],
        ...     [0, 3],
        ...     [1, 4],
        ...     [2, 5],
        ...     [2, 6],
        ...     [2, 7],
        ...     [3, 8],
        ... ]
        >>> for node_1, node_2 in edges:
        ...     tree.add_edge(node_1, node_2)
        >>> root = 0
        >>> tree.preprocess(root)

        >>> tree.lca(5, 8)
        0
        >>> tree.lca(4, 8)
        0
        >>> tree.lca(5, 7)
        2
        >>> tree.lca(5, 0)
        0

        This method calculates the LCA of two nodes
        'node_1' and 'node_2' in the tree.
        It uses the 'is_ancestor' method to
        determine if 'node_1' is an ancestor of 'node_2'
        or vice versa.
        Then, it performs binary lifting to find the LCA.

        """
        # Check if 'node_1' is an ancestor of 'node_2'
        if self.is_ancestor(node_1, node_2):
            return node_1
        # Check if 'node_2' is an ancestor of 'node_1'
        if self.is_ancestor(node_1, node_2):
            return node_2
        # Perform binary lifting to find the LCA
        for i in range(self.l, -1, -1):
            # Check if the ancestor of 'node_1' at depth 'i'
            # is not an ancestor of 'node_2'
            if not self.is_ancestor(self.up[node_1][i], node_2):
                node_1 = self.up[node_1][i]
        # The LCA is the parent of the final 'node_1'
        # node after binary lifting
        return self.up[node_1][0]

    def preprocess(self, root: int) -> None:
        """
        Preprocess the tree to calculate entry and exit times,
        store parent-child relationships, and prepare for LCA queries.

        Args:
            root (int): The root node of the tree.

        Returns:
            None

        This method initializes and populates the necessary
        data structures for efficient LCA queries.
        It calculates entry and exit times for all nodes in the tree,
        determines the logarithmic depth, and prepares the 'up' list
        using a depth-first search (DFS) starting from the 'root' node.

        >>> n = 9
        >>> tree = TreeLCA(n)
        >>> edges = [
        ...     [0, 1],
        ...     [0, 2],
        ...     [0, 3],
        ...     [1, 4],
        ...     [2, 5],
        ...     [2, 6],
        ...     [2, 7],
        ...     [3, 8],
        ... ]
        >>> for u, v in edges:
        ...     tree.add_edge(u, v)
        >>> root = 0
        >>> tree.preprocess(root)
        >>> tree.tin
        [0, 0, 2, 6, 0, 2, 3, 4, 6]
        >>> tree.tout
        [9, 2, 6, 8, 1, 3, 4, 5, 7]
        >>> tree.l
        4
        """

        # Initialize entry and exit times,
        # timer, and logarithmic depth
        self.tin = [0] * self.n
        self.tout = [0] * self.n
        self.timer = 0
        self.l = math.ceil(math.log2(self.n))

        # Initialize 'up' list for binary lifting
        for _ in range(self.n):
            self.up.append([0] * (self.l + 1))
        # Perform DFS traversal starting
        # from the 'root' node
        self.dfs(root, root)


# Test code
if __name__ == "__main__":
    # Number of nodes in the graph
    n = 9
    tree = TreeLCA(n)
    edges = [
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 4),
        (2, 5),
        (2, 6),
        (2, 7),
        (3, 8),
    ]
    for u, v in edges:
        tree.add_edge(u, v)
    # Root of the tree
    root = 0
    tree.preprocess(root)

    # Test queries
    print("LCA(5, 8):", tree.lca(5, 8))
    print("LCA(4, 8):", tree.lca(4, 8))
    print("LCA(5, 7):", tree.lca(5, 7))
    print("LCA(5, 0):", tree.lca(5, 0))

    import doctest

    doctest.testmod()
# Time Complexity: O(NlogN)
# i.e. O(logN) for each query.


# Space Complexity: O(NlogN).
