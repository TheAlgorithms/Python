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
        degree_counts = [0] * len(self.trees)

        for node in self.trees:
            degree_counts[node.degree] += 1

        new_trees = []
        for i in range(len(degree_counts)):
            while degree_counts[i] > 1:
                degree_counts[i] -= 1

                node1 = self.trees.pop()
                node2 = self.trees.pop()

                if node1.key < node2.key:
                    new_node = node1
                    new_node.children.append(node2)
                else:
                    new_node = node2
                    new_node.children.append(node1)

                new_node.degree += 1
                new_trees.append(new_node)

        self.trees = new_trees

    def decrease_key(self, node, new_key):
        if new_key > node.key:
            raise ValueError("New key must be less than or equal to old key")

        node.key = new_key

        if node == self.least:
            self.least = node

        while node.parent is not None and node.key < node.parent.key:
            self.cut(node)
            self.cascading_cut(node.parent)

    def cut(self, node):
        node.parent.children.remove(node)
        node.parent = None
        self.trees.append(node)

        node.degree = 0
        node.marked = False

    def cascading_cut(self, node):
        if node.marked:
            self.cut(node)

            if node.parent is not None:
                node.parent.marked = True
