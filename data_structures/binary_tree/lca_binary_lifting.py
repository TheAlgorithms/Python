"""

Let G be a tree. For every query of the form (u, v) we want to find the lowest common ancestor of the nodes u and v, i.e. we want to find a node w that lies on the path from u to the root node, that lies on the path from v to the root node, and if there are multiple nodes we pick the one that is farthest away from the root node. In other words the desired node w is the lowest ancestor of u and v. In particular if u is an ancestor of v, then u is their lowest common ancestor.

This algorithm will need O(Nlog N) for preprocessing the tree, and then O(log N) for each LCA query.

"""

import math


#  Abbrevations:

#  n: number of nodes in the graph
#  adj: adjacency list for the graph
#  timer: keeps track of the current time
#  tin: entry time for the node (time of first visit)
#  tout: exit time for the node (time of last visit)
#  l: logarithmic depth
#  up: ancestors list


class TreeLCA:
    # Constructor

    def __init__(self, n: int):
        self.n = n
        self.adj = [[] for _ in range(n)]
        self.timer = 0
        self.tin = [0] * n
        self.tout = [0] * n
        self.l = 0
        self.up = []

    # Constructing graph by adding edges (Creating Adjacency list)

    def add_edge(self, node_1: int, node_2: int) -> None:
        self.adj[node_1].append(node_2)
        self.adj[node_2].append(node_1)

    def dfs(self, node: int, parent: int) -> None:
        """
        Perform a depth-first search (DFS) traversal of the tree to compute important information for LCA.

        Args:
            node (int): The current node being processed.
            parent (int): The parent of the current node.

        Returns:
            None

        This method calculates entry and exit times, stores parent-child relationships, and prepares the 'up' list
        to efficiently find the Lowest Common Ancestor (LCA) of nodes in the tree using a binary lifting technique.
        """

        self.tin[node] = self.timer
        self.up[node][0] = parent
        for i in range(1, self.l + 1):
            self.up[node][i] = self.up[self.up[node][i - 1]][i - 1]
        # The following for loop is used to recursively traverse the adjacent nodes of the current node (node). It iterates through each adjacent node u in self.adj[node]. If u is not the same as the parent node (parent), it means that the traversal is moving to a child node (not going back to the parent), so it recursively calls the dfs method for node u.
        for u in self.adj[node]:
            if u != parent:
                self.dfs(u, node)
        # Incrementing the timer to mark the exit time (time of the last visit) for the current node.
        self.timer += 1

        # recording the exit time for the current node in the tout list.
        self.tout[node] = self.timer

    def is_ancestor(self, parent: int, node: int) -> bool:
        """
        Check if 'parent' is an ancestor of 'node' in the tree based on entry and exit times.

        Args:
            parent (int): The potential ancestor node.
            node (int): The potential descendant node.

        Returns:
            bool: True if 'parent' is an ancestor of 'node', False otherwise.

        This method uses entry and exit times stored during preprocessing to determine if 'parent' is an ancestor of 'node'
        in the tree. It returns True if 'parent' is an ancestor of 'node', and False otherwise.

        """
        return (
            self.tin[parent] <= self.tin[node] and self.tout[parent] >= self.tout[node]
        )

    def lca(self, u: int, v: int) -> int:
        """
        Find the Lowest Common Ancestor (LCA) of two nodes 'u' and 'v' in the tree.

        Args:
            u (int): The first node.
            v (int): The second node.

        Return:
            int: The LCA node of 'u' and 'v'.

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

        >>> tree.lca(5, 8)
        0
        >>> tree.lca(4, 8)
        0
        >>> tree.lca(5, 7)
        2
        >>> tree.lca(5, 0)
        0

        This method calculates the LCA of two nodes 'u' and 'v' in the tree. It uses the 'is_ancestor' method to
        determine if 'u' is an ancestor of 'v' or vice versa. Then, it performs binary lifting to find the LCA.
        """
        # Check if 'u' is an ancestor of 'v'
        if self.is_ancestor(u, v):
            return u
        # Check if 'v' is an ancestor of 'u'
        if self.is_ancestor(v, u):
            return v
        # Perform binary lifting to find the LCA
        for i in range(self.l, -1, -1):
            # Check if the ancestor of 'u' at depth 'i' is not an ancestor of 'v'
            if not self.is_ancestor(self.up[u][i], v):
                u = self.up[u][i]
        # The LCA is the parent of the final 'u' node after binary lifting
        return self.up[u][0]

    def preprocess(self, root: int) -> None:
        """
        Preprocess the tree to calculate entry and exit times, store parent-child relationships, and prepare for LCA queries.

        Args:
            root (int): The root node of the tree.

        Returns:
            None

        This method initializes and populates the necessary data structures for efficient LCA queries. It calculates
        entry and exit times for all nodes in the tree, determines the logarithmic depth, and prepares the 'up' list
        using a depth-first search (DFS) starting from the 'root' node.

        """
        # Initialize entry and exit times, timer, and logarithmic depth
        self.tin = [0] * self.n
        self.tout = [0] * self.n
        self.timer = 0
        self.l = math.ceil(math.log2(self.n))

        # Initialize 'up' list for binary lifting
        for _ in range(self.n):
            self.up.append([0] * (self.l + 1))
        # Perform DFS traversal starting from the 'root' node
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
# Time Complexity: O(NlogN) i.e. O(logN) for each query.
# Space Complexity: O(NlogN).
