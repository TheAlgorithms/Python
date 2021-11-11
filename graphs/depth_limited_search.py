"""
    Depth Limited Search

    This file contains a function in which the DLS algorithm is implemented.
    In this algorithm we used recursive approach to visit nodes.
    This algorithm is DFS with a limit on maximum depth it can search.

    author: Mahdi Rezaie
    github: mahdirezaie336
    email: mahdi.rezaie.336@gmail.com
"""


class Node:

    instances = {}
    
    def __init__(self, identity=None) -> None:
        # If no args are set in this method
        if identity is None:
            identity = len(Node.instances)
        
        if identity in Node.instances:
            raise NameError("A node with this ID already exists.")

        self.id = identity
        self.neighbours = []

        Node.instances[identity] = self

    def __hash__(self) -> int:
        return hash(self.id)
    
    def __eq__(self, o: object) -> bool:
        return self.id == o.id

    def __ne__(self, o: object) -> bool:
        return self.id != o.id

    def __str__(self) -> str:
        return 'Node<' + str(self.id) + '>'

    def __repr__(self) -> str:
        return str(self)


def dls_search(limit: int, depth: int, node: Node, explored: set):
    """ This DLS implementation is used in IDS search.
        :param limit: Maximum depth
        :param depth: The explored depth until now
        :param node: The node the expand next
        :param explored: The final explored list
        :returns Node of goal if Goal state is found"""

    print('Visited:', node)
    explored.add(node)
    if limit > depth:
        for neighbour_node in node.neighbours:
            if neighbour_node not in explored:
                dls_search(limit, depth+1, neighbour_node, explored)
    explored.remove(node)


if __name__ == '__main__':
    explored = set()
    nodes = []
    for _ in range(7):
        nodes.append(Node())

    """
        n[0]----n[1]----n[2]
            \   |       |
             \  |       |
              n[3]------n[4]----n[6]
              |
              |
              n[5]
    """
    nodes[0].neighbours.append(nodes[1])
    nodes[0].neighbours.append(nodes[3])
    nodes[1].neighbours.append(nodes[0])
    nodes[1].neighbours.append(nodes[2])
    nodes[1].neighbours.append(nodes[3])
    nodes[2].neighbours.append(nodes[1])
    nodes[2].neighbours.append(nodes[4])
    nodes[3].neighbours.append(nodes[0])
    nodes[3].neighbours.append(nodes[1])
    nodes[3].neighbours.append(nodes[4])
    nodes[3].neighbours.append(nodes[5])
    nodes[4].neighbours.append(nodes[2])
    nodes[4].neighbours.append(nodes[3])
    nodes[4].neighbours.append(nodes[6])
    nodes[5].neighbours.append(nodes[3])
    nodes[6].neighbours.append(nodes[4])

    dls_search(1, 0, nodes[0], explored)
