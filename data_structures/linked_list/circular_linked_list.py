class Node:
    def __init__(self, data):
        self.data = data
        self.next_ptr = None

    def set_data(self, value):
        self.data = value

    def get_data(self):
        return self.data

    def set_next(self, value):
        self.next_ptr = value

    def get_next(self):
        return self.next_ptr

    def has_next(self):
        return self.next_ptr is not None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length

    def __str__(self):
        current_node = self.head
        if not current_node:
            return "Empty linked list"

        result = [f"<Node data={current_node.get_data()}>"]
        current_node = current_node.get_next()

        while current_node != self.head:
            result.append(f"<Node data={current_node.get_data()}>")
            current_node = current_node.get_next()

        return " => ".join(result)

    def append(self, data):
        current_node = self.head

        new_node = Node(data)
        new_node.set_next(new_node)

        if current_node is None:
            self.head = new_node
        else:
            while current_node.get_next() != self.head:
                current_node = current_node.get_next()

            current_node.set_next(new_node)
            new_node.set_next(self.head)

        self.length += 1
