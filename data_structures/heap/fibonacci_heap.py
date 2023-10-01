class FibonacciNode:
    def __init__(self, key):
        self.key = key
        self.children = []
        self.marked = False
        self.degree = 0
        self.parent = None

class FibonacciHeap:
    def __init__(self):
        self.trees = []
        self.least = None
        self.count = 0

    def insert(self, key):
        new_node = FibonacciNode(key)
        self.trees.append(new_node)
        self.count += 1
        if self.least is None or key < self.least.key:
            self.least = new_node

    def extract_min(self):
        if self.count == 0:
            raise ValueError("Heap is empty")

        min_node = self.least
        self.trees.remove(min_node)

        for child in min_node.children:
            child.parent = None
            self.trees.append(child)

        self.count -= 1

        if self.least is min_node:
            self.least = None
            for node in self.trees:
                if self.least is None or node.key < self.least.key:
                    self.least = node

        self.consolidate()
        return min_node.key

    def consolidate(self):
        degree_counts = [None] * (2 * len(self.trees))

        for node in self.trees[:]:
            degree = node.degree
            while degree_counts[degree] is not None:
                other_node = degree_counts[degree]
                if node.key > other_node.key:
                    node, other_node = other_node, node  # Swap nodes
                self.link(other_node, node)
                degree_counts[degree] = None
                degree += 1
            degree_counts[degree] = node

        self.trees = [node for node in degree_counts if node is not None]

    def link(self, node1, node2):
        self.trees.remove(node2)
        node1.children.append(node2)
        node2.parent = node1
        node1.degree += 1
        node2.marked = False

    def decrease_key(self, node, new_key):
        if new_key > node.key:
            raise ValueError("New key must be less than or equal to old key")

        node.key = new_key

        if node == self.least:
            self.update_least()

        parent = node.parent
        if parent is not None and node.key < parent.key:
            self.cut(node, parent)
            self.cascading_cut(parent)

    def cut(self, node, parent):
        parent.children.remove(node)
        parent.degree -= 1
        self.trees.append(node)
        node.parent = None
        node.marked = False

    def cascading_cut(self, node):
        parent = node.parent
        if parent is not None:
            if not node.marked:
                node.marked = True
            else:
                self.cut(node, parent)
                self.cascading_cut(parent)

    def update_least(self):
        self.least = None
        for node in self.trees:
            if self.least is None or node.key < self.least.key:
                self.least = node
