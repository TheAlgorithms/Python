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


def page_rank(nodes, limit=3, d=0.85):
    """
    Calculate PageRank for a directed graph.

    >>> nodes = [Node('A'), Node('B'), Node('C')]
    >>> nodes[0].add_outbound('B')
    >>> nodes[0].add_outbound('C')
    >>> nodes[1].add_outbound('C')
    >>> nodes[2].add_outbound('A')
    >>> ranks = page_rank(nodes, limit=100)
    >>> round(ranks['A'], 4)
    0.15
    >>> round(ranks['B'], 4)
    0.15
    >>> round(ranks['C'], 4)
    0.15
    """
    n = len(nodes)
    ranks = {}
    for node in nodes:
        ranks[node.name] = 1 / n  # Initialize to 1/n, not 1

    outbounds = {}
    for node in nodes:
        outbounds[node.name] = len(node.outbound)

    for i in range(limit):
        # Handle dangling nodes (nodes with no outbound links)
        for node in nodes:
            outbound_count = outbounds[node.name]
            if outbound_count == 0:
                ranks[node.name] = (1 - d) + d * sum(ranks[ib] for ib in node.inbound) / n
            else:
                ranks[node.name] = (1 - d) + d * sum(
                    ranks[ib] / outbounds[ib] for ib in node.inbound
                )

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

    page_rank(nodes)


if __name__ == "__main__":
    main()