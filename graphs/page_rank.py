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


def page_rank(nodes, limit=None, d=0.85, tol=1e-8, max_iter=100):
    if not nodes:
        return {}

    if limit is not None:
        max_iter = limit

    n = len(nodes)
    ranks = {node.name: 1.0 / n for node in nodes}
    outbounds = {node.name: len(node.outbound) for node in nodes}

    for _ in range(max_iter):
        new_ranks = {}
        dangling_sum = sum(
            ranks[node.name] for node in nodes if outbounds[node.name] == 0
        )

        for node in nodes:
            inbound_rank = sum(
                ranks[inbound_node] / outbounds[inbound_node]
                for inbound_node in node.inbound
            )
            new_ranks[node.name] = (1 - d) / n + d * (
                inbound_rank + dangling_sum / n
            )

        if sum(abs(new_ranks[name] - ranks[name]) for name in ranks) < tol:
            return new_ranks
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

    print("======= Page Rank =======")
    print(page_rank(nodes))


if __name__ == "__main__":
    main()
