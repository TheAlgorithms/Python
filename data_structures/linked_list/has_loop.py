import timeit
from typing import Any


class ContainsLoopError(Exception):
    pass


class ListWithAdd(list):
    def add(self, *args, **kwargs):
        return self.append(*args, **kwargs)


SETORLIST = set


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next_node = None

    def __iter__(self):
        node = self
        visited = SETORLIST()
        while node:
            if node in visited:  # set().__contains__ is O(1)
                raise ContainsLoopError
            visited.add(node)
            yield node.data
            node = node.next_node

    @property
    def has_loop(self) -> bool:
        """
        A loop is when the exact same Node appears more than once in a linked list.
        >>> root = Node(1)
        >>> root.next_node = Node(2)
        >>> root.next_node.next_node = Node(3)
        >>> root.next_node.next_node.next_node = Node(4)
        >>> root.has_loop
        False
        >>> root.next_node.next_node.next_node = root.next_node
        >>> root.has_loop
        True
        """
        try:
            list(self)
            return False
        except ContainsLoopError:
            return True


if __name__ == "__main__":
    root = Node(1)
    root.next_node = Node(2)
    root.next_node.next_node = Node(3)
    root.next_node.next_node.next_node = Node(4)
    print(root.has_loop)  # False
    root.next_node.next_node.next_node = root.next_node
    print(root.has_loop)  # True

    root = Node(5)
    root.next_node = Node(6)
    root.next_node.next_node = Node(5)
    root.next_node.next_node.next_node = Node(6)
    print(root.has_loop)  # False

    root = Node(1)
    print(root.has_loop)  # False


    # Performance comparison between using a set or a list
    def bench_f() -> bool:
        return root.has_loop


    for exp in range(1, 4 + 1):
        root = Node(1)
        for i in range(10 ** exp):
            new_node = Node(i)
            new_node.next_node = root
            root = new_node

        SETORLIST = set
        time_set: float = timeit.timeit(bench_f, number=5)
        SETORLIST = ListWithAdd
        time_list: float = timeit.timeit(bench_f, number=5)

        print(f'{time_set=}, {time_list=}, {time_set<time_list=}')
        # time_set = 2.269999999993111e-05, time_list = 3.430000000004263e-05, time_set < time_list = True
        # time_set = 0.00012579999999995373, time_list = 0.0004275000000000251, time_set < time_list = True
        # time_set = 0.0008853999999999251, time_list = 0.033791399999999916, time_set < time_list = True
        # time_set = 0.014864699999999953, time_list = 2.8534654, time_set < time_list = True
