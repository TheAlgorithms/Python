"""
Author: https://github.com/bhushan-borole
"""

"""
The input graph for the algorithm is:

  A B C
A 0 1 1
B 0 0 1
C 1 0 0

"""

graph = [[0, 1, 1], [0, 0, 1], [1, 0, 0]]


class Node:
    def __init__(self, name):
        self.name = name
        self.inbound = []
        self.outbound = []

    def add_inbound(self, node):
        self.inbound.append(node)

    def add_outbound(self, node):
        self.outbound.append(node)

    def __repr__(self):
        return f"<node={self.name} inbound={self.inbound} outbound={self.outbound}>"


def page_rank(nodes, limit=100, d=0.85, tol=1e-6):
    """Compute PageRank for ``nodes`` and return the final rank mapping.

    The implementation follows the standard formulation: ranks are
    initialised to ``1 / len(nodes)`` so they form a probability
    distribution summing to 1.0, dangling nodes (nodes with no
    outbound edges) have their rank redistributed evenly across every
    node at each step, and the iteration stops as soon as the L1
    difference between successive rank vectors falls below ``tol``
    (default ``1e-6``) — so ``limit`` is an upper bound, not a fixed
    iteration count.
    """
    n = len(nodes)
    if n == 0:
        return {}

    ranks = {node.name: 1.0 / n for node in nodes}
    outbounds = {node.name: len(node.outbound) for node in nodes}

    for _ in range(limit):
        dangling_sum = sum(
            ranks[node.name] for node in nodes if outbounds[node.name] == 0
        )
        new_ranks = {}
        for node in nodes:
            inbound_share = sum(
                ranks[ib] / outbounds[ib]
                for ib in node.inbound
                if outbounds[ib] > 0
            )
            new_ranks[node.name] = (1 - d) / n + d * (
                inbound_share + dangling_sum / n
            )
        if sum(abs(new_ranks[k] - ranks[k]) for k in ranks) < tol:
            ranks = new_ranks
            break
        ranks = new_ranks

    return ranks


def main():
    names = list(input("Enter Names of the Nodes: ").split())

    nodes = [Node(name) for name in names]

    for ri, row in enumerate(graph):
        for ci, col in enumerate(row):
            if col == 1:
                nodes[ci].add_inbound(names[ri])
                nodes[ri].add_outbound(names[ci])

    print("======= Nodes =======")
    for node in nodes:
        print(node)

    print("======= PageRank =======")
    print(page_rank(nodes))


if __name__ == "__main__":
    main()
