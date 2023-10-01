class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("The Linked List is empty ")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def add_begin(self, data: int) -> None:
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data: int) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self, data: int, target_value: int) -> None:
        n = self.head
        while n is not None:
            if target_value == n.data:
                break
            n = n.ref
        new_node = Node(data)
        new_node.ref = n.ref
        n.ref = new_node


if __name__ == "__main__":
    import doctest

    doctest.testmod()
