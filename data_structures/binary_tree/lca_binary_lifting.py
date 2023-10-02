"""
Let G be a tree. For every query of the form (u, v) we want to find the lowest common ancestor of the nodes u and v, i.e. we want to find a node w that lies on the path from u to the root node, that lies on the path from v to the root node, and if there are multiple nodes we pick the one that is farthest away from the root node. In other words the desired node w is the lowest ancestor of u and v. In particular if u is an ancestor of v, then u is their lowest common ancestor.

This algorithm will need O(Nlog N) for preprocessing the tree, and then O(log N) for each LCA query.
"""

import math

n = 0
l = 0
adj = []

timer = 0
tin = []
tout = []
up = []


def dfs(v, p):
    global timer
    tin[v] = timer
    up[v][0] = p
    for i in range(1, l + 1):
        up[v][i] = up[up[v][i - 1]][i - 1]

    for u in adj[v]:
        if u != p:
            dfs(u, v)

    timer += 1
    tout[v] = timer


def is_ancestor(u, v):
    return tin[u] <= tin[v] and tout[u] >= tout[v]


def lca(u, v):
    if is_ancestor(u, v):
        return u
    if is_ancestor(v, u):
        return v
    for i in range(l, -1, -1):
        if not is_ancestor(up[u][i], v):
            u = up[u][i]
    return up[u][0]


def preprocess(root):
    global tin, tout, timer, l
    tin = [0] * n
    tout = [0] * n
    timer = 0
    l = math.ceil(math.log2(n))
    for _ in range(n):
        up.append([0] * (l + 1))
    dfs(root, root)


# Test code
if __name__ == "__main__":
    # Number of nodes in the graph
    n = 9
    adj = [[] for _ in range(n + 1)]
    edges = [(0, 1), (0, 2), (0, 3), (1, 4), (2, 5), (2, 6), (2, 7), (3, 8)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    root = 0  # Root of the tree
    preprocess(root)

    # Test queries
    print("LCA(5, 8):", lca(5, 8))
    print("LCA(4, 8):", lca(4, 8))
    print("LCA(5, 7):", lca(5, 7))
    print("LCA(5, 0):", lca(5, 0))

# # Time Complexity: O(NlogN) i.e. O(logN) for each query.
# # Space Complexity: O(NlogN).
