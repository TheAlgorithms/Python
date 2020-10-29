#!/usr/bin/python3


class Heap:
    """
    >>> unsorted = [103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5]
    >>> h = Heap()
    >>> h.build_heap(unsorted)
    >>> h.display()
    [209, 201, 25, 103, 107, 15, 1, 9, 7, 11, 5]
    >>>
    >>> h.get_max()
    209
    >>> h.display()
    [201, 107, 25, 103, 11, 15, 1, 9, 7, 5]
    >>>
    >>> h.insert(100)
    >>> h.display()
    [201, 107, 25, 103, 100, 15, 1, 9, 7, 5, 11]
    >>>
    >>> h.heap_sort()
    >>> h.display()
    [1, 5, 7, 9, 11, 15, 25, 100, 103, 107, 201]
    >>>
    """

    def __init__(self):
        self.h = []
        self.curr_size = 0

    def get_left_child_index(self, i):
        left_child_index = 2 * i + 1
        if left_child_index < self.curr_size:
            return left_child_index
        return None

    def get_right_child(self, i):
        right_child_index = 2 * i + 2
        if right_child_index < self.curr_size:
            return right_child_index
        return None

    def max_heapify(self, index):
        if index < self.curr_size:
            largest = index
            lc = self.get_left_child_index(index)
            rc = self.get_right_child(index)
            if lc is not None and self.h[lc] > self.h[largest]:
                largest = lc
            if rc is not None and self.h[rc] > self.h[largest]:
                largest = rc
            if largest != index:
                self.h[largest], self.h[index] = self.h[index], self.h[largest]
                self.max_heapify(largest)

    def build_heap(self, collection):
        self.curr_size = len(collection)
        self.h = list(collection)
        if self.curr_size <= 1:
            return
        for i in range(self.curr_size // 2 - 1, -1, -1):
            self.max_heapify(i)

    def get_max(self):
        if self.curr_size >= 2:
            me = self.h[0]
            self.h[0] = self.h.pop(-1)
            self.curr_size -= 1
            self.max_heapify(0)
            return me
        elif self.curr_size == 1:
            self.curr_size -= 1
            return self.h.pop(-1)
        return None

    def heap_sort(self):
        size = self.curr_size
        for j in range(size - 1, 0, -1):
            self.h[0], self.h[j] = self.h[j], self.h[0]
            self.curr_size -= 1
            self.max_heapify(0)
        self.curr_size = size

    def insert(self, data):
        self.h.append(data)
        curr = (self.curr_size - 1) // 2
        self.curr_size += 1
        while curr >= 0:
            self.max_heapify(curr)
            curr = (curr - 1) // 2

    def display(self):
        print(self.h)


def main():
    for unsorted in [
        [],
        [0],
        [2],
        [3, 5],
        [5, 3],
        [5, 5],
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [2, 2, 3, 5],
        [0, 2, 2, 3, 5],
        [2, 5, 3, 0, 2, 3, 0, 3],
        [6, 1, 2, 7, 9, 3, 4, 5, 10, 8],
        [103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5],
        [-45, -2, -5],
    ]:
        print("source unsorted list: %s" % unsorted)

        h = Heap()
        h.build_heap(unsorted)
        print("after build heap: ", end=" ")
        h.display()

        print("max value: %s" % h.get_max())
        print("delete max value: ", end=" ")
        h.display()

        h.insert(100)
        print("after insert new value 100: ", end=" ")
        h.display()

        h.heap_sort()
        print("heap sort: ", end=" ")
        h.display()
        print()


if __name__ == "__main__":
    main()
