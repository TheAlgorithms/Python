import math


class FibonacciHeapNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.degree = 0
        self.parent = None
        self.child = None
        self.mark = False
        self.next = self
        self.prev = self

    def add_child(self, node):
        if not self.child:
            self.child = node
        else:
            node.prev = self.child
            node.next = self.child.next
            self.child.next.prev = node
            self.child.next = node
        node.parent = self
        self.degree += 1

    def remove_child(self, node):
        if node.next == node:  # Single child
            self.child = None
        elif self.child == node:
            self.child = node.next
        node.prev.next = node.next
        node.next.prev = node.prev
        node.parent = None
        self.degree -= 1


class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.total_nodes = 0

    def is_empty(self):
        return self.min_node is None

    def insert(self, key, value=None):
        node = FibonacciHeapNode(key, value)
        self._merge_with_root_list(node)
        if not self.min_node or node.key < self.min_node.key:
            self.min_node = node
        self.total_nodes += 1
        return node

    def find_min(self):
        return self.min_node

    def union(self, other_heap):
        if not other_heap.min_node:
            return self
        if not self.min_node:
            self.min_node = other_heap.min_node
        else:
            self._merge_with_root_list(other_heap.min_node)
            if other_heap.min_node.key < self.min_node.key:
                self.min_node = other_heap.min_node
        self.total_nodes += other_heap.total_nodes

    def extract_min(self):
        z = self.min_node
        if z:
            if z.child:
                children = list(self._iterate(z.child))
                for child in children:
                    self._merge_with_root_list(child)
                    child.parent = None
            self._remove_from_root_list(z)
            if z == z.next:
                self.min_node = None
            else:
                self.min_node = z.next
                self._consolidate()
            self.total_nodes -= 1
        return z

    def decrease_key(self, x, new_key):
        if new_key > x.key:
            raise ValueError("New key is greater than current key")
        x.key = new_key
        y = x.parent
        if y and x.key < y.key:
            self._cut(x, y)
            self._cascading_cut(y)
        if x.key < self.min_node.key:
            self.min_node = x

    def delete(self, x):
        self.decrease_key(x, -math.inf)
        self.extract_min()

    def _cut(self, x, y):
        y.remove_child(x)
        self._merge_with_root_list(x)
        x.mark = False

    def _cascading_cut(self, y):
        if z := y.parent:
            if not y.mark:
                y.mark = True
            else:
                self._cut(y, z)
                self._cascading_cut(z)

    def _merge_with_root_list(self, node):
        if not self.min_node:
            self.min_node = node
        else:
            node.prev = self.min_node
            node.next = self.min_node.next
            self.min_node.next.prev = node
            self.min_node.next = node

    def _remove_from_root_list(self, node):
        if node.next == node:
            self.min_node = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    def _consolidate(self):
        array_size = int(math.log(self.total_nodes) * 2) + 1
        array = [None] * array_size
        nodes = list(self._iterate(self.min_node))
        for w in nodes:
            x = w
            d = x.degree
            while array[d]:
                y = array[d]
                if x.key > y.key:
                    x, y = y, x
                self._link(y, x)
                array[d] = None
                d += 1
            array[d] = x
        self.min_node = None
        for i in range(array_size):
            if array[i]:
                if not self.min_node:
                    self.min_node = array[i]
                else:
                    self._merge_with_root_list(array[i])
                    if array[i].key < self.min_node.key:
                        self.min_node = array[i]

    def _link(self, y, x):
        self._remove_from_root_list(y)
        x.add_child(y)
        y.mark = False

    def _iterate(self, start):
        node = start
        while True:
            yield node
            node = node.next
            if node == start:
                break


# Example usage
if __name__ == "__main__":
    fh = FibonacciHeap()
    n1 = fh.insert(10, "value1")
    n2 = fh.insert(2, "value2")
    n3 = fh.insert(15, "value3")

    print("Min:", fh.find_min().key)  # Output: 2
    fh.decrease_key(n3, 1)
    print("Min after decrease key:", fh.find_min().key)  # Output: 1
    fh.extract_min()
    print("Min after extract:", fh.find_min().key)  # Output: 2
