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

    def prepend(self, data):
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

            self.head = new_node

        self.length += 1

    def delete_front(self):
        if self.head is None:
            raise IndexError()

        current_node = self.head

        if current_node.get_next() == current_node:
            self.head, self.length = None, 0
        else:
            while current_node.get_next() != self.head:
                current_node = current_node.get_next()

            current_node.set_next(self.head.get_next())
            self.head = self.head.get_next()

        self.length -= 1

    def delete_rear(self):
        if self.head is None:
            raise IndexError()

        temp_node, current_node = self.head, self.head

        if current_node.get_next() == current_node:
            self.head, self.length = None, 0
        else:
            while current_node.get_next() != self.head:
                temp_node = current_node
                current_node = current_node.get_next()

            temp_node.set_next(current_node.get_next())

        self.length -= 1


if __name__ == "__main__":
    temp = CircularLinkedList()
    for i in range(10):
        temp.prepend(i)
    print(temp)

    temp.delete_rear()
    print(temp)
